import pandas as pd
import numpy as np
import os

# Load data
df = pd.read_csv('data/flight_data.csv')

print("Data loaded!")
print("Shape (rows, columns):", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Clean data
df['airline']     = df['airline'].str.strip()
df['source']      = df['source'].str.strip()
df['destination'] = df['destination'].str.strip()
df['date']        = pd.to_datetime(df['date'])
df['month']       = df['date'].dt.month_name()
df['month_num']   = df['date'].dt.month

print("\nData cleaned!")

# Save cleaned data
df.to_csv('data/cleaned_flight_data.csv', index=False)
print("Saved to data/cleaned_flight_data.csv")