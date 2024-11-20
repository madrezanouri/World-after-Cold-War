import pandas as pd
import plotly.express as px

# Load the processed dataset
df = pd.read_csv("../data/processed/master_data.csv")

# Filter data for the years 1995-2007 and select relevant countries
filtered_df = df[(df['year'] >= 1995) & (df['year'] <= 2007)]
countries_to_plot = ["United States", "China", "Germany", "India"]
filtered_df = filtered_df[filtered_df["Country"].isin(countries_to_plot)]

# Plot GDP Growth Rate for selected countries
fig = px.line(filtered_df, x="Year", y="Real GDP growth (Annual percent change)", color="Country",
              title="GDP Growth Rates (1995-2007): The Calm Before the Storm",
              labels={"gdp_growth_rate": "Real GDP growth (Annual percent change)", "year": "Year"})
fig.update_layout(title_font_size=18, xaxis_title=None, yaxis_title=None, template="plotly_white")

# Save the plot as a PNG image
fig.write_image("../images/calm_before_storm_gdp_growth.png")
