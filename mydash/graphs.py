from dash import Dash, dcc, html, Input, Output, State, callback

app = Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/water.css@2/out/dark.css'])

app.layout = html.Div([
    dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'A'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'B'},
            ],
            'layout': {
                'title': 'Graph with HoverData Callback'
            }
        }
    ),
    html.Div(id='hover-data'),
])

@callback(
    Output('hover-data', 'children'),
    [Input('graph', 'hoverData')]
)
def display_hover_data(hover_data):
    if hover_data is not None:
        return f"Hovered data:({hover_data['points'][0]['x']},{hover_data['points'][0]['y']})"
    else:
        return ""

if __name__ == '__main__':
    app.run_server(debug=True)