import pandas as pd
import folium
import os

os.makedirs('outputs/maps', exist_ok=True)

df = pd.read_csv('data/cleaned_flight_data.csv')
print("Data loaded!\n")

# Airport coordinates
airports = {
    'Delhi':     [28.6139, 77.2090],
    'Mumbai':    [19.0760, 72.8777],
    'Bangalore': [12.9716, 77.5946],
    'Chennai':   [13.0827, 80.2707],
    'Kolkata':   [22.5726, 88.3639],
    'Hyderabad': [17.3850, 78.4867],
}

# Base map of India
flight_map = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5,
    tiles='CartoDB positron'
)

# Add airport markers
for city, coords in airports.items():
    folium.CircleMarker(
        location=coords,
        radius=9,
        color='darkblue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.8,
        tooltip=city,
        popup=city
    ).add_to(flight_map)

    folium.Marker(
        location=[coords[0] + 0.5, coords[1]],
        icon=folium.DivIcon(
            html=f'<div style="font-size:11px;font-weight:bold;color:black">{city}</div>'
        )
    ).add_to(flight_map)

# Draw flight routes
routes = df.groupby(['source', 'destination']).size().reset_index(name='count')

for _, row in routes.iterrows():
    src = row['source']
    dst = row['destination']
    if src in airports and dst in airports:
        folium.PolyLine(
            locations=[airports[src], airports[dst]],
            color='red',
            weight=row['count'] * 1.5,
            opacity=0.6,
            tooltip=f"{src} to {dst} | {row['count']} flights"
        ).add_to(flight_map)

# Save map
flight_map.save('outputs/maps/india_flight_routes.html')
print("Map saved!")
print("Go to outputs/maps/india_flight_routes.html")
print("Right click that file and open in your browser!")