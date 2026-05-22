# Flight Yatra — Airline Data Analysis

Hi! This is my data analysis project on airline flights in India.
I made this project to learn Python and data analysis tools.
I collected flight data, cleaned it, analysed it, and made charts and maps from it.

---

## Why I Made This Project

I wanted to learn how to work with real data using Python.
I chose airline data because it has many interesting things to analyse
like ticket prices, popular routes, and departure times.

---

## What I Did in This Project

First I collected flight data of 20 flights across India.
Then I cleaned the data to remove errors and fix formats.
After that I analysed the data to find patterns and insights.
Then I created charts and graphs to show my findings visually.
Finally I built an interactive dashboard and a flight route map.

---

## Tools and Libraries I Used

- Python — main programming language I used for everything
- Pandas — I used this to load and clean my data like Excel but in code
- NumPy — I used this for calculations like average and sum
- Matplotlib — I used this to make basic bar charts and line graphs
- Seaborn — I used this to make better looking charts like heatmaps and box plots
- Plotly — I used this to make interactive charts that you can hover and zoom
- Folium — I used this to show flight routes on a real map of India
- VS Code — this is the editor I used to write all my code

---

## Project Files I Created

| File Name | What I Did In This File |
|-----------|------------------------|
| 01_data_cleaning.py | I loaded the raw CSV file and cleaned the data |
| 02_analysis.py | I analysed the data and found key insights |
| 03_visualizations.py | I created 7 charts using Matplotlib Seaborn and Plotly |
| 04_maps.py | I built a flight route map of India using Folium |
| 05_dashboard.py | I made a basic dashboard with 4 charts |
| 06_full_dashboard.py | I made a full dashboard with 12 charts combined |
| data/flight_data.csv | This is my raw dataset with 20 flight records |
| data/cleaned_flight_data.csv | This is the cleaned version of my dataset |
| requirements.txt | This file has all the libraries needed to run my project |

---

## My Dataset

I used a dataset of 20 flights with these columns:

| Column | What It Means |
|--------|--------------|
| airline | Name of the airline like IndiGo or Vistara |
| source | City where the flight starts |
| destination | City where the flight lands |
| stops | How many stops the flight has 0 or 1 |
| departure_time | When the flight leaves like Morning or Evening |
| duration | How long the flight takes |
| price | How much the ticket costs in Rupees |
| date | The date of the flight |
| class | Economy or Business class |

---

## What I Found After Analysis

- IndiGo has the most flights with 7 out of 20 total flights
- Vistara is the most expensive airline with average price of Rs 6325
- SpiceJet is the cheapest airline with average price of Rs 2850
- Delhi to Mumbai is the most popular and busiest route
- Business class ticket costs almost double compared to Economy class
- Most flights in my data depart in the morning time slot
- January had more bookings compared to February

---

## Charts I Created

- Bar chart showing how many flights each airline has
- Box plot showing price range of each airline
- Heatmap showing average price by airline and class
- Bar chart comparing non stop and 1 stop flight prices
- Bar chart comparing Economy and Business class prices
- Interactive bar chart for average price per airline
- Interactive pie chart showing airline market share
- Full interactive dashboard with 12 charts combined
- Interactive map of India showing all flight routes

