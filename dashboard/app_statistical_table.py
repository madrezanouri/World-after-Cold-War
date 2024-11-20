
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the processed dataset
df = pd.read_csv("master_data.csv")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Statistical Summary Dashboard"

# App layout
app.layout = html.Div([
    html.Div(
        html.H1("Statistical Summary Dashboard", style={"text-align": "center", "color": "#2c3e50", "font-family": "Arial"}),
        style={"background-color": "#ecf0f1", "padding": "10px"}
    ),

    # Country selector
    html.Div([
        html.Label("Select Country:", style={"font-size": "16px", "font-weight": "bold"}),
        dcc.Dropdown(
            id="country_selector",
            options=[{"label": country, "value": country} for country in sorted(df["Country"].unique())],
            value="United States",  # Default value
            multi=False,
            style={"font-size": "14px"}
        )
    ], style={"width": "50%", "margin": "20px auto"}),

    # Indicator selector
    html.Div([
        html.Label("Select Indicator:", style={"font-size": "16px", "font-weight": "bold"}),
        dcc.Dropdown(
            id="indicator_selector",
            options=[{"label": col, "value": col} for col in df.columns if col not in ["Country", "Year"]],
            value="gdp_growth_rate",  # Default value
            multi=False,
            style={"font-size": "14px"}
        )
    ], style={"width": "50%", "margin": "20px auto"}),

    # Data table for .describe() output
    html.Div([
        html.Label("Statistical Summary Table:", style={"font-size": "18px", "font-weight": "bold", "text-align": "center"}),
        dash_table.DataTable(
            id="describe_table",
            columns=[{"name": "Statistic", "id": "Statistic"}, {"name": "Value", "id": "Value"}],
            style_table={"overflowX": "auto", "margin": "20px auto"},
            style_cell={"textAlign": "center", "fontFamily": "Arial", "font-size": "14px"},
            style_header={"fontWeight": "bold", "backgroundColor": "#bdc3c7", "color": "#2c3e50"},
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#ecf0f1"}
            ]
        )
    ], style={"width": "80%", "margin": "auto"}),

    # Visualization of the statistical data
    html.Div([
        dcc.Graph(id="describe_chart")
    ], style={"width": "80%", "margin": "20px auto"})
])

# Callback to update the .describe() table and visualization
@app.callback(
    [Output("describe_table", "data"),
     Output("describe_chart", "figure")],
    [Input("country_selector", "value"),
     Input("indicator_selector", "value")]
)
def update_dashboard(selected_country, selected_indicator):
    # Filter the dataset for the selected country
    filtered_df = df[df["Country"] == selected_country]

    # Apply .describe() to the selected indicator
    describe_data = filtered_df[selected_indicator].describe()

    # Convert .describe() output to a table format
    describe_table = describe_data.reset_index()
    describe_table.columns = ["Statistic", "Value"]

    # Remove the "count" statistic for visualization
    describe_table_no_count = describe_table[describe_table["Statistic"] != "count"]

    # Create a bar chart for .describe() statistics (excluding "count")
    fig = px.bar(
        describe_table_no_count,
        x="Statistic",
        y="Value",
        title=f"Statistical Summary for {selected_indicator} in {selected_country}",
        labels={"Value": "Value", "Statistic": "Statistic"},
        template="plotly_white"
    )
    fig.update_layout(title_font_size=18, xaxis_title=None, yaxis_title=None)

    # Return both the table data and chart figure
    return describe_table.to_dict("records"), fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

