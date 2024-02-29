from dash import Dash, dcc, html, Input, Output, callback
import numpy as np
import pandas as pd
import plotly.express as px

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

data = {
    "Temperature (C)": [12, 10, 8, 14, 6, 18, 9, 11, 13, 7, 16, 20, 5, 15],
    "Humidity (%)": [65, 70, 60, 75, 55, 80, 63, 68, 72, 58, 75, 80, 70, 65],
    "Wind Speed (km/h)": [15, 12, 10, 18, 8, 20, 11, 14, 16, 9, 10, 15, 8, 14],
    "Precipitation (mm)": [0.5, 1.2, 0.0, 2.5, 0.0, 3.0, 0.8, 1.5, 2.0, 0.2, 1.0, 0.5, 0.0, 1.2]
}

df = pd.DataFrame(data)

app.layout = html.Div(
    [
        html.Div(
            dcc.Graph(id="temperature_vs_humidity", config={"displayModeBar": False}),
            className="four columns",
        ),
        html.Div(
            dcc.Graph(id="temperature_vs_wind", config={"displayModeBar": False}),
            className="four columns",
        ),
        html.Div(
            dcc.Graph(id="temperature_vs_precipitation", config={"displayModeBar": False}),
            className="four columns",
        ),
    ],
    className="row",
)


def update_scatter_plot(x_col, y_col, selectedpoints):
    fig = px.scatter(df, x=x_col, y=y_col, text=df.index)

    fig.update_traces(
        selectedpoints=selectedpoints,
        customdata=df.index,
        mode="markers+text",
        marker={"color": "rgba(0, 116, 217, 0.7)", "size": 20},
        unselected={
            "marker": {"opacity": 0.3},
            "textfont": {"color": "rgba(0, 0, 0, 0)"},
        },
    )

    fig.update_layout(
        margin={"l": 20, "r": 0, "b": 15, "t": 5},
        dragmode="select",
        hovermode=False,
        newshape_line_color='darkgrey'
    )

    return fig


@callback(
    [Output("temperature_vs_humidity", "figure"),
     Output("temperature_vs_wind", "figure"),
     Output("temperature_vs_precipitation", "figure")],
    [Input("temperature_vs_humidity", "selectedData"),
     Input("temperature_vs_wind", "selectedData"),
     Input("temperature_vs_precipitation", "selectedData")]
)
def update_selected_data(selection1, selection2, selection3):
    selectedpoints = df.index
    for selected_data in [selection1, selection2, selection3]:
        if selected_data and selected_data["points"]:
            selectedpoints = np.intersect1d(
                selectedpoints, [p["customdata"] for p in selected_data["points"]]
            )

    return [
        update_scatter_plot("Humidity (%)", "Temperature (C)", selectedpoints),
        update_scatter_plot("Wind Speed (km/h)", "Temperature (C)", selectedpoints),
        update_scatter_plot("Precipitation (mm)", "Temperature (C)", selectedpoints),
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
