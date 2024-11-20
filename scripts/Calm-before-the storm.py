# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed dataset
df = pd.read_csv("master_data.csv")

# Filter data for the years 1995-2007 and select relevant countries
countries_to_plot = ["United States", "China", "Germany", "India", "United Kingdom"]
filtered_df = df[(df['Year'] >= 1995) & (df['Year'] <= 2007) & (df["Country"].isin(countries_to_plot))]

# 1. Combined GDP Analysis Plot
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('GDP Analysis (1995-2007)', fontsize=16)

# Plot Total GDP
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    axes[0].plot(country_data["Year"], country_data["GDP (current BillUS$)"], label=country)

axes[0].set_title('Total GDP (1995-2007)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('GDP (Billion USD)')
axes[0].legend()
axes[0].grid(True)

# Plot GDP per Capita Growth
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    axes[1].plot(country_data["Year"], country_data["GDP per capita growth (annual %)"], label=country)

axes[1].set_title('GDP per Capita Growth (1995-2007)')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('GDP per Capita Growth (%)')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("gdp_analysis_combined01.png", dpi=150)
plt.show()

# 2. Combined Population Analysis Plot
fig, axes = plt.subplots(2, 1, figsize=(10, 10))
fig.suptitle('Population Analysis (1995-2007)', fontsize=16)

# Plot Population Growth Rate
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    axes[0].plot(country_data["Year"], country_data["Population Growth Rate (Percentage)"], label=country)

axes[0].set_title('Population Growth Rate (1995-2007)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Population')
axes[0].legend()
axes[0].grid(True)

# Plot Population Sex Ratio
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    axes[1].plot(country_data["Year"], country_data["Population Sex Ratio, as of 1 July (males per 100 females)"], label=country)

axes[1].set_title('Population Sex Ratio (1995-2007)')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Population Sex Ratio')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("population_analysis_combined01.png", dpi=150)
plt.show()

# Create a new figure for Total Fertility Rate
fig, ax = plt.subplots(figsize=(10, 6))
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    ax.plot(country_data["Year"], country_data["Total Fertility Rate (live births per woman)"], label=country)

ax.set_title('Total Fertility Rate (1995-2007)')
ax.set_xlabel('Year')
ax.set_ylabel('Fertility Rate (live births per woman)')
ax.legend()
ax.grid(True)


# Save the fertility rate figure separately
plt.savefig("fertility_rate_analysis01.png", dpi=150)
plt.show()

# 3. Unemployment and Trade Analysis Plot
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('Unemployment and Trade Analysis (1995-2007)', fontsize=16)

# Plot Unemployment Rate
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    axes[0].plot(country_data["Year"], country_data["Unemployment"], label=country)

axes[0].set_title('Unemployment Rate (1995-2007)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Unemployment (%)')
axes[0].legend()
axes[0].grid(True)

# Plot Net Trade in Goods and Services
for country in countries_to_plot:
    country_data = filtered_df[filtered_df["Country"] == country]
    axes[1].plot(country_data["Year"], country_data["Net trade in goods and services (BoP, current USB$)"], label=country)

axes[1].set_title('Net Trade in Goods and Services (1995-2007)')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Net Trade (USD)')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("unemployment_trade_analysis01.png", dpi=150)
plt.show()

