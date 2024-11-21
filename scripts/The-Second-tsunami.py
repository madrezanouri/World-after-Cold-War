# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

# Load the processed dataset
df = pd.read_csv("master_data.csv")

# Filter data for the years 2016-2024 and select relevant countries
countries_to_plot = ["United States", "China", "Germany", "India", "United Kingdom", "France", "Japan", "Brazil", "South Africa", "Australia"]
filtered_df = df[(df['Year'] >= 2016) & (df['Year'] <= 2019) & (df["Country"].isin(countries_to_plot))]

# 1. Line Chart for Exports of Goods and Services (China vs. Others) to Highlight Trade Tensions Impact
plt.figure(figsize=(12, 8))
for country in ["China", "United States", "Germany", "India"]:
    country_data = filtered_df[filtered_df['Country'] == country]
    plt.plot(country_data['Year'], country_data['Net trade in goods and services (BoP, current USB$)'], label=country)

plt.title('Exports and Net Trade in Goods and Services (2016-2024)')
plt.xlabel('Year')
plt.ylabel('Net Trade (USD Billion)')
plt.legend()
plt.tight_layout()
plt.savefig("net_trade_exports_line_chart_2016_2024.png", dpi=150)
plt.show()

# 2. Stacked Area Chart for Net Trade in Goods and Services (2016-2024)
fig, ax = plt.subplots(figsize=(12, 8))
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    ax.fill_between(country_data["Year"], country_data["Net trade in goods and services (BoP, current USB$)"], label=country, alpha=0.5)

ax.set_title('Stacked Area Chart for Net Trade in Goods and Services (2016-2024)')
ax.set_xlabel('Year')
ax.set_ylabel('Net Trade (USD Billion)')
ax.legend()
plt.tight_layout()
plt.savefig("net_trade_stacked_area_2016_2024.png", dpi=150)
plt.show()

# 3. Bar Plot for Unemployment Rate During Pandemic (2018-2022)
pandemic_df = filtered_df[(filtered_df['Year'] >= 2018) & (filtered_df['Year'] <= 2022)]
plt.figure(figsize=(12, 8))
sns.barplot(x='Year', y='Unemployment', hue='Country', data=pandemic_df, palette='viridis')
plt.title('Bar Plot of Unemployment Rate During Pandemic (2018-2022)')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("unemployment_barplot_pandemic_2019_2021.png", dpi=150)
plt.show()

# 4. Line Plot: Population Growth Rate Decline (2016-2024)
plt.figure(figsize=(12, 8))
global_population_growth = filtered_df.groupby('Year')['Population Growth Rate (Percentage)'].mean()
plt.plot(global_population_growth.index, global_population_growth.values, marker='o', linestyle='-', color='b')
plt.axhline(y=1, color='r', linestyle='--', label='1% Threshold')
plt.title('Global Population Growth Rate Decline (2016-2024)')
plt.xlabel('Year')
plt.ylabel('Population Growth Rate (%)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("population_growth_decline_line_2016_2024.png", dpi=150)
plt.show()
