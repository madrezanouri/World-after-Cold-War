# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the processed dataset
df = pd.read_csv("master_data.csv")

# Filter data for the years 2006-2016 and select relevant countries
countries_to_plot = ["United States", "China", "Germany", "India", "United Kingdom", "France", "Japan", "Brazil", "South Africa", "Australia"]
filtered_df = df[(df['Year'] >= 2006) & (df['Year'] <= 2016) & (df["Country"].isin(countries_to_plot))]

# 1. Heatmap for GDP Growth Rates to Highlight Impact of 2008 Financial Crisis
pivot_data_gdp = filtered_df.pivot_table(index='Year', columns='Country', values='Real GDP growth (Annual percent change)')
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_data_gdp, annot=True, cmap='coolwarm', center=0, linewidths=.5)
plt.title('Heatmap of Real GDP Growth Rates (2006-2016): Impact of 2008 Financial Crisis')
plt.xlabel('Country')
plt.ylabel('Year')
plt.tight_layout()
plt.savefig("gdp_growth_heatmap_2006_2016.png", dpi=150)
plt.show()

# 2. Boxplot for Unemployment Rates to Show Variation Before and After the Crisis
plt.figure(figsize=(12, 8))
sns.boxplot(x='Year', y='Unemployment', data=filtered_df, palette='viridis')
plt.title('Boxplot of Unemployment Rates (2006-2016): Financial Crisis Impact')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("unemployment_boxplot_2006_2016.png", dpi=150)
plt.show()

# 3. Stacked Area Chart for Net Trade in Goods and Services
fig, ax = plt.subplots(figsize=(12, 8))
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    ax.fill_between(country_data["Year"], country_data["Net trade in goods and services (BoP, current USB$)"], label=country, alpha=0.5)

ax.set_title('Stacked Area Chart for Net Trade in Goods and Services (2006-2016)')
ax.set_xlabel('Year')
ax.set_ylabel('Net Trade (USD Billion)')
ax.legend()
plt.tight_layout()
plt.savefig("net_trade_stacked_area_2006_2016.png", dpi=150)
plt.show()

# 4. Sunburst Chart for GDP Composition (Regional Contributions to Global GDP)
import plotly.express as px
fig = px.sunburst(filtered_df, path=['Year', 'Country'], values='GDP (current BillUS$)',
                  title='Sunburst Chart: Regional Contributions to Global GDP (2006-2016)',
                  color='GDP (current BillUS$)', hover_data=['Real GDP growth (Annual percent change)'],
                  color_continuous_scale='RdBu')
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.write_image("gdp_sunburst_2006_2016.png")
fig.show()

# 5. Bar Plot for GDP Growth by Year
plt.figure(figsize=(12, 8))
gdp_growth_means = filtered_df.groupby('Year')['Real GDP growth (Annual percent change)'].mean()
gdp_growth_means.plot(kind='bar', color='teal')
plt.title('Average GDP Growth Rate by Year (2006-2016)')
plt.xlabel('Year')
plt.ylabel('Average GDP Growth Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("gdp_growth_barplot_2006_2016.png", dpi=150)
plt.show()
