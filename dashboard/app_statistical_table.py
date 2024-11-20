
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd

# Load the processed dataset
df = pd.read_csv("../data/processed/master_data.csv")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Statistical Tables Dashboard"

# App layout
app.layout = html.Div([
    html.H1("Statistical Tables Dashboard", style={"text-align": "center"}),

    # Dropdown for selecting countries
    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id="country_selector",
            options=[{"label": country, "value": country} for country in sorted(df["country"].unique())],
            value="United States",  # Default value
            multi=False
        )
    ], style={"width": "50%", "margin": "auto", "margin-top": "20px"}),

    # Dropdown for selecting indicators
    html.Div([
        html.Label("Select Indicator:"),
        dcc.Dropdown(
            id="indicator_selector",
            options=[{"label": col, "value": col} for col in df.columns if col not in ["country", "year"]],
            value="gdp_growth_rate",  # Default value
            multi=False
        )
    ], style={"width": "50%", "margin": "auto", "margin-top": "20px"}),

    # Range slider for selecting years
    html.Div([
        html.Label("Select Year Range:"),
        dcc.RangeSlider(
            id="year_slider",
            min=df["year"].min(),
            max=df["year"].max(),
            step=1,
            value=[df["year"].min(), df["year"].max()],
            marks={str(year): str(year) for year in range(df["year"].min(), df["year"].max() + 1, 5)}
        )
    ], style={"width": "80%", "margin": "auto", "margin-top": "20px"}),

    # Data table
    html.Div([
        dash_table.DataTable(
            id="stat_table",
            columns=[{"name": col, "id": col} for col in df.columns],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "center", "fontFamily": "Arial"},
            style_header={"fontWeight": "bold", "backgroundColor": "#f4f4f4"},
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#f9f9f9"}
            ]
        )
    ], style={"margin": "20px"})
])

# Callback to update the table
@app.callback(
    Output("stat_table", "data"),
    Input("country_selector", "value"),
    Input("indicator_selector", "value"),
    Input("year_slider", "value")
)
def update_table(selected_country, selected_indicator, year_range):
    # Filter dataset
    filtered_df = df[(df["country"] == selected_country) &
                     (df["year"] >= year_range[0]) &
                     (df["year"] <= year_range[1])]

    # Return only selected indicator columns
    return filtered_df[["year", "country", selected_indicator]].to_dict("records")

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
