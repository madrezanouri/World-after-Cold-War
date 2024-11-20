import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_gdp_growth(df, countries, start_year, end_year):
    filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
    filtered_df = filtered_df[filtered_df["Country"].isin(countries)]
    fig = px.line(filtered_df, x="year", y="Real GDP growth (Annual percent change)", color="Country",
                  title="GDP Growth Rates (1995-2007): The Calm Before the Storm",
                  labels={"gdp_growth_rate": "Real GDP growth (Annual percent change)", "year": "Year"})
    fig.write_image("../images/calm_before_storm_gdp_growth.png")

# Call the function for specific countries
df = pd.read_csv("../data/processed/master_data.csv")
plot_gdp_growth(df, ["United States", "China", "Germany", "India"], 1995, 2007)

