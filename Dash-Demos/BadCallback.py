
import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

# Global variable
last_selected = None

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Option 1', 'value': '1'},
            {'label': 'Option 2', 'value': '2'},
        ],
        value='1'
    ),
    html.Div(id='display-selected'),
    html.Div(id='current-selected'),
    dcc.Interval(
        id='interval-component',
        interval=30,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output('display-selected', 'children'),
    Input('my-dropdown', 'value')
)
def update_selected(value):
    global last_selected
    last_selected = value
    return f'Last selected: {last_selected}'

@app.callback(
    Output('current-selected', 'children'),
    Input('interval-component', 'n_intervals')
)
def check_last_selected(n):
    global last_selected
    return f'Actual Value: {last_selected}'

if __name__ == '__main__':
    app.run_server(debug=True)