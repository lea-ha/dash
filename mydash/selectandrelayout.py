from dash import Dash, dcc, html, Input, Output, State, callback

app = Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/water.css@2/out/dark.css'])

app.layout = html.Div([
    dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Data 1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Data 2'},
            ],
            'layout': {
                'title': 'Graph',
            }
        }
    ),
    html.Button('Select Data', id='select-button'),
    html.Button('Relayout Data', id='relayout-button'),
    html.Div(id='output')
])
@callback(
    Output('output', 'children'),
    [Input('select-button', 'n_clicks'),
     Input('relayout-button', 'n_clicks')],
    [State('graph', 'selectedData'),
     State('graph', 'relayoutData')]
)
def update_output(select_clicks, relayout_clicks, selected_data, relayout_data):
    if select_clicks is not None:
        # Handle select button click
        # Access selected data using selected_data variable
        return f'Selected Data: {selected_data}'
    elif relayout_clicks is not None:
        # Handle relayout button click
        # Access relayout data using relayout_data variable
        return f'Relayout Data: {relayout_data}'
    else:
        return ''
if __name__ == '__main__':
    app.run_server(debug=True)