import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

os.makedirs('outputs/charts', exist_ok=True)

df = pd.read_csv('data/cleaned_flight_data.csv')
print("Data loaded!\n")

# Chart 1: Flights per airline
plt.figure(figsize=(8, 5))
counts = df['airline'].value_counts()
plt.bar(counts.index, counts.values, color='steelblue', edgecolor='white')
plt.title('Number of Flights per Airline')
plt.xlabel('Airline')
plt.ylabel('Count')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('outputs/charts/01_flights_per_airline.png')
plt.show()
print("Chart 1 done")

# Chart 2: Price distribution boxplot
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='airline', y='price', palette='pastel')
plt.title('Ticket Price Distribution by Airline')
plt.xlabel('Airline')
plt.ylabel('Price (Rs)')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('outputs/charts/02_price_distribution.png')
plt.show()
print("Chart 2 done")

# Chart 3: Heatmap
pivot = df.pivot_table(values='price', index='airline', columns='class', aggfunc='mean')
plt.figure(figsize=(7, 5))
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Average Price: Airline vs Class')
plt.tight_layout()
plt.savefig('outputs/charts/03_price_heatmap.png')
plt.show()
print("Chart 3 done")

# Chart 4: Price by stops
plt.figure(figsize=(6, 4))
stops_price = df.groupby('stops')['price'].mean().round(0)
plt.bar(['Non-Stop', '1 Stop'], stops_price.values, color=['green', 'orange'])
plt.title('Average Price: Non-Stop vs 1 Stop')
plt.ylabel('Average Price (Rs)')
plt.tight_layout()
plt.savefig('outputs/charts/04_price_by_stops.png')
plt.show()
print("Chart 4 done")

# Chart 5: Economy vs Business
plt.figure(figsize=(6, 4))
class_price = df.groupby('class')['price'].mean().round(0)
plt.bar(class_price.index, class_price.values, color=['skyblue', 'coral'])
plt.title('Average Price: Economy vs Business')
plt.ylabel('Average Price (Rs)')
plt.tight_layout()
plt.savefig('outputs/charts/05_price_by_class.png')
plt.show()
print("Chart 5 done")

# Chart 6: Interactive bar chart
avg = df.groupby('airline')['price'].mean().round(0).reset_index()
fig = px.bar(
    avg,
    x='airline',
    y='price',
    color='airline',
    title='Average Ticket Price per Airline',
    labels={'price': 'Avg Price (Rs)', 'airline': 'Airline'}
)
fig.write_html('outputs/charts/06_interactive_bar.html')
fig.show()
print("Chart 6 done")

# Chart 7: Pie chart
fig2 = px.pie(
    df,
    names='airline',
    title='Airline Market Share',
    hole=0.3
)
fig2.write_html('outputs/charts/07_market_share.html')
fig2.show()
print("Chart 7 done")

print("\nAll charts saved in outputs/charts/")