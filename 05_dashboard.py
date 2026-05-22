import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

os.makedirs('outputs/charts', exist_ok=True)

df = pd.read_csv('data/cleaned_flight_data.csv')
print("Data loaded!\n")

# Dashboard with 4 charts
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Flights per Airline',
        'Avg Price by Airline',
        'Flights by Departure Time',
        'Economy vs Business Price'
    ),
    specs=[
        [{"type": "xy"},   {"type": "xy"}],
        [{"type": "domain"}, {"type": "xy"}]
    ]
)

# Chart 1 - Flights per airline
counts = df['airline'].value_counts().reset_index()
counts.columns = ['airline', 'count']
fig.add_trace(
    go.Bar(x=counts['airline'], y=counts['count'], marker_color='steelblue', name='Flights'),
    row=1, col=1
)

# Chart 2 - Avg price per airline
avg = df.groupby('airline')['price'].mean().round(0).reset_index()
fig.add_trace(
    go.Bar(x=avg['airline'], y=avg['price'], marker_color='coral', name='Avg Price'),
    row=1, col=2
)

# Chart 3 - Departure time pie chart
time_counts = df['departure_time'].value_counts().reset_index()
time_counts.columns = ['time', 'count']
fig.add_trace(
    go.Pie(labels=time_counts['time'], values=time_counts['count'], name='Timing'),
    row=2, col=1
)

# Chart 4 - Economy vs Business
class_price = df.groupby('class')['price'].mean().round(0).reset_index()
fig.add_trace(
    go.Bar(x=class_price['class'], y=class_price['price'], marker_color='purple', name='Class Price'),
    row=2, col=2
)

fig.update_layout(
    title_text='Flight Yatra - Airline Dashboard',
    height=700,
    showlegend=False
)

fig.write_html('outputs/charts/dashboard.html')
fig.show()
print("Dashboard saved to outputs/charts/dashboard.html")