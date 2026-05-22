import pandas as pd
import numpy as np

df = pd.read_csv('data/cleaned_flight_data.csv')
print("Data loaded!\n")

# 1. Flights per airline
print("=" * 40)
print("FLIGHTS PER AIRLINE")
print("=" * 40)
print(df['airline'].value_counts())

# 2. Average price per airline
print("\n" + "=" * 40)
print("AVERAGE PRICE PER AIRLINE")
print("=" * 40)
avg_price = df.groupby('airline')['price'].mean().round(0).sort_values(ascending=False)
print(avg_price)

# 3. Most popular routes
print("\n" + "=" * 40)
print("TOP 5 POPULAR ROUTES")
print("=" * 40)
routes = df.groupby(['source','destination']).size().reset_index(name='count')
print(routes.sort_values('count', ascending=False).head())

# 4. Economy vs Business
print("\n" + "=" * 40)
print("PRICE BY CLASS")
print("=" * 40)
print(df.groupby('class')['price'].agg(['mean','min','max']).round(0))

# 5. Non-stop vs connecting
print("\n" + "=" * 40)
print("PRICE BY STOPS")
print("=" * 40)
print(df.groupby('stops')['price'].mean().round(0))

# 6. Cheapest ticket
print("\n" + "=" * 40)
print("CHEAPEST TICKET")
print("=" * 40)
print(df.loc[df['price'].idxmin(), ['airline','source','destination','price']])

# 7. Most expensive ticket
print("\n" + "=" * 40)
print("MOST EXPENSIVE TICKET")
print("=" * 40)
print(df.loc[df['price'].idxmax(), ['airline','source','destination','price']])

# 8. Busiest month
print("\n" + "=" * 40)
print("BOOKINGS PER MONTH")
print("=" * 40)
print(df['month'].value_counts())