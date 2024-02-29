from dash import Dash, dcc, html, Input, Output, callback

external_stylesheet = ["https://cdn.jsdelivr.net/npm/water.css@2/out/dark.css"]
app = Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    html.Button("Click me", id="button"),
    html.Div(id="output-div"),
])

@callback(
    Output(component_id="output-div",
           component_property= "children"),
    [Input(component_id="button", 
           component_property="n_clicks")]
)
def update_output(clicks):
    return html.P(f"{clicks} clicks!")

@callback(
    Output(component_id='my-output', 
           component_property='children'),
    Input(component_id='my-input',
           component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)
