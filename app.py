import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "width": "80%",
        "margin": "auto",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),

        html.P(
            "Select a region to filter sales data:",
            style={"fontWeight": "bold"}
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        ),

        dcc.Graph(id="sales-graph")
    ]
)

# Callback to update graph
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={"Sales": "Total Sales", "Date": "Date"}
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)
