from dash import Dash, dcc, html, Input, Output, callback

external_stylesheet = ["https://cdn.jsdelivr.net/npm/water.css@2/out/dark.css"]
app = Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    html.H1("Input X and Y"),
    dcc.Input(id="input-x", type="number", value=1),
    dcc.Input(id="input-y", type="number", value=1),
    html.Table([
        html.Tr([html.Td("X+Y"), html.Td(id="sum")]),
        html.Tr([html.Td("X-Y"), html.Td(id="difference")]),
        html.Tr([html.Td("X*Y"), html.Td(id="product")]),
        html.Tr([html.Td("X/Y"), html.Td(id="quotient")]),
    ])
])
@callback(
    Output(component_id="sum", component_property="children"),
    Output(component_id="difference", component_property="children"),
    Output(component_id="product", component_property="children"),
    Output(component_id="quotient", component_property="children"),
    [Input(component_id="input-x", component_property="value"),
     Input(component_id="input-y", component_property="value")]
)
def update_table(x, y):
    return x + y, x - y, x * y, x / y


if __name__ == '__main__':
    app.run_server(debug=True)