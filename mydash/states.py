from dash import Dash, dcc, html, Input, Output, State, callback
import pandas as pd

external_stylesheets = ['https://cdn.jsdelivr.net/npm/water.css@2/out/dark.css']

data = {'country': ['Lebanon'], 'city': ['Beirut']} 
df = pd.DataFrame(data)

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='city', type='text', value='Montréal'),
    dcc.Input(id='country', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

@callback(Output('output-state', 'children'),
              [Input('submit-button-state', 'n_clicks')],
              [State('city', 'value'),
               State('country', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        df.loc[len(df)] = [input2, input1]
        return [
            html.Table([
                html.Thead(
                    html.Tr([html.Th('Country'), html.Th('City')])
                ),
                html.Tbody([
                    html.Tr([html.Td(country), html.Td(city)]) for country, 
                    city in zip(df['country'], df['city'])
                ])
            ])
        ]
    else:
        return [
            html.Table([
                html.Thead(
                    html.Tr([html.Th('Country'), html.Th('City')])
                ),
                html.Tbody([
                    html.Tr([html.Td(country), html.Td(city)]) for country, city in zip(df['country'], df['city'])
                ])
            ])
        ]

if __name__ == '__main__':
    app.run_server(debug=True)
