import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import os

os.makedirs('outputs/charts', exist_ok=True)

df = pd.read_csv('data/cleaned_flight_data.csv')

# ── Summary numbers ────────────────────────────────────
total_flights   = len(df)
avg_price       = int(df['price'].mean())
cheapest        = int(df['price'].min())
expensive       = int(df['price'].max())
total_routes    = df.groupby(['source','destination']).ngroups
economy_avg     = int(df[df['class']=='Economy']['price'].mean())
business_avg    = int(df[df['class']=='Business']['price'].mean())
nonstop_avg     = int(df[df['stops']==0]['price'].mean())
stop1_avg       = int(df[df['stops']==1]['price'].mean())

# ── Data prep ──────────────────────────────────────────
airline_counts  = df['airline'].value_counts().reset_index()
airline_counts.columns = ['airline','count']

airline_price   = df.groupby('airline')['price'].mean().round(0).reset_index()
airline_price.columns = ['airline','avg_price']

route_counts    = df.groupby(['source','destination']).size().reset_index(name='count')
route_counts['route'] = route_counts['source'] + ' → ' + route_counts['destination']
route_counts    = route_counts.sort_values('count', ascending=True).tail(8)

time_counts     = df['departure_time'].value_counts().reset_index()
time_counts.columns = ['time','count']

month_counts    = df['month'].value_counts().reset_index()
month_counts.columns = ['month','count']

class_price     = df.groupby('class')['price'].mean().round(0).reset_index()

stops_price     = df.groupby('stops')['price'].mean().round(0).reset_index()
stops_price['stops'] = stops_price['stops'].map({0:'Non-Stop', 1:'1 Stop'})

# ── Build dashboard ────────────────────────────────────
fig = make_subplots(
    rows=4, cols=3,
    subplot_titles=(
        'Flights per Airline',
        'Average Price per Airline (Rs)',
        'Market Share by Airline',
        'Top Routes by Bookings',
        'Departure Time Distribution',
        'Bookings per Month',
        'Economy vs Business Price',
        'Non-Stop vs 1 Stop Price',
        'Price Distribution by Airline',
        'Cheapest vs Most Expensive',
        'Flights by Class',
        'Price Range per Airline'
    ),
    specs=[
        [{"type":"xy"},     {"type":"xy"},     {"type":"domain"}],
        [{"type":"xy"},     {"type":"domain"}, {"type":"xy"}],
        [{"type":"xy"},     {"type":"xy"},     {"type":"xy"}],
        [{"type":"xy"},     {"type":"domain"}, {"type":"xy"}],
    ],
    vertical_spacing=0.1,
    horizontal_spacing=0.08
)

colors = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd']

# Row 1 ────────────────────────────────────────────────

# 1. Flights per airline
fig.add_trace(go.Bar(
    x=airline_counts['airline'],
    y=airline_counts['count'],
    marker_color=colors[:len(airline_counts)],
    text=airline_counts['count'],
    textposition='outside',
    name='Flights'
), row=1, col=1)

# 2. Avg price per airline
fig.add_trace(go.Bar(
    x=airline_price['airline'],
    y=airline_price['avg_price'],
    marker_color='coral',
    text=airline_price['avg_price'].astype(int),
    textposition='outside',
    name='Avg Price'
), row=1, col=2)

# 3. Market share pie
fig.add_trace(go.Pie(
    labels=airline_counts['airline'],
    values=airline_counts['count'],
    hole=0.4,
    name='Market Share'
), row=1, col=3)

# Row 2 ────────────────────────────────────────────────

# 4. Top routes
fig.add_trace(go.Bar(
    x=route_counts['count'],
    y=route_counts['route'],
    orientation='h',
    marker_color='steelblue',
    name='Routes'
), row=2, col=1)

# 5. Departure time pie
fig.add_trace(go.Pie(
    labels=time_counts['time'],
    values=time_counts['count'],
    hole=0.4,
    name='Departure Time'
), row=2, col=2)

# 6. Bookings per month
fig.add_trace(go.Bar(
    x=month_counts['month'],
    y=month_counts['count'],
    marker_color='mediumseagreen',
    text=month_counts['count'],
    textposition='outside',
    name='Monthly'
), row=2, col=3)

# Row 3 ────────────────────────────────────────────────

# 7. Economy vs Business
fig.add_trace(go.Bar(
    x=class_price['class'],
    y=class_price['price'],
    marker_color=['skyblue','purple'],
    text=class_price['price'].astype(int),
    textposition='outside',
    name='Class Price'
), row=3, col=1)

# 8. Non-stop vs 1 stop
fig.add_trace(go.Bar(
    x=stops_price['stops'],
    y=stops_price['price'],
    marker_color=['green','orange'],
    text=stops_price['price'].astype(int),
    textposition='outside',
    name='Stops Price'
), row=3, col=2)

# 9. Price distribution violin
for i, airline in enumerate(df['airline'].unique()):
    subset = df[df['airline'] == airline]
    fig.add_trace(go.Box(
        y=subset['price'],
        name=airline,
        marker_color=colors[i % len(colors)],
        showlegend=False
    ), row=3, col=3)

# Row 4 ────────────────────────────────────────────────

# 10. Cheapest vs most expensive per airline
airline_min = df.groupby('airline')['price'].min().reset_index()
airline_max = df.groupby('airline')['price'].max().reset_index()

fig.add_trace(go.Bar(
    x=airline_min['airline'],
    y=airline_min['price'],
    name='Cheapest',
    marker_color='lightgreen'
), row=4, col=1)

fig.add_trace(go.Bar(
    x=airline_max['airline'],
    y=airline_max['price'],
    name='Most Expensive',
    marker_color='tomato'
), row=4, col=1)

# 11. Flights by class pie
class_counts = df['class'].value_counts().reset_index()
class_counts.columns = ['class','count']
fig.add_trace(go.Pie(
    labels=class_counts['class'],
    values=class_counts['count'],
    hole=0.4,
    name='Class Split'
), row=4, col=2)

# 12. Price range per airline (scatter)
for i, airline in enumerate(df['airline'].unique()):
    subset = df[df['airline'] == airline]
    fig.add_trace(go.Scatter(
        x=subset['airline'],
        y=subset['price'],
        mode='markers',
        name=airline,
        marker=dict(size=10, color=colors[i % len(colors)]),
        showlegend=False
    ), row=4, col=3)

# ── Layout ─────────────────────────────────────────────
fig.update_layout(
    title=dict(
        text='Flight Yatra — Complete Airline Analytics Dashboard',
        font=dict(size=22)
    ),
    height=1800,
    showlegend=True,
    barmode='group',
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=11),
    legend=dict(
        orientation='h',
        yanchor='top',
        y=-0.02,
        xanchor='center',
        x=0.5
    )
)

# Clean up axes
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=True, gridcolor='#f0f0f0')

# ── Save ───────────────────────────────────────────────
output_path = 'outputs/charts/full_dashboard.html'
fig.write_html(output_path)
fig.show()

print("Full dashboard saved!")
print(f"Open this file in your browser: {output_path}")
print("\nSummary:")
print(f"  Total Flights   : {total_flights}")
print(f"  Average Price   : Rs {avg_price}")
print(f"  Cheapest Ticket : Rs {cheapest}")
print(f"  Most Expensive  : Rs {expensive}")
print(f"  Total Routes    : {total_routes}")
print(f"  Economy Avg     : Rs {economy_avg}")
print(f"  Business Avg    : Rs {business_avg}")
print(f"  Non-Stop Avg    : Rs {nonstop_avg}")
print(f"  1 Stop Avg      : Rs {stop1_avg}")