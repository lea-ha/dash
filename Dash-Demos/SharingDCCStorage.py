from io import StringIO
import time
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

app = Dash(__name__)



df = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
    dcc.Graph(figure={}, id='graph'),
    html.Table(id='table'),
    dcc.Dropdown(list(range(1, 6)), 1,id='dropdown'),

    # dcc.Store stores the intermediate value
    dcc.Store(id='intermediate-value')
])

@callback(Output('intermediate-value', 'data'), Input('dropdown', 'value'))
def clean_data(value):
     # Assume this is expensive data processing step
     time.sleep(4) # Simulate a long callback
     cleaned_df = df[df['score'] == value]

     return cleaned_df.to_json(date_format='iso', orient='split')

@callback(Output('graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(jsonified_cleaned_data):

    # more generally, this line would be
    # json.loads(jsonified_cleaned_data)
    json_file = StringIO(jsonified_cleaned_data)
    dff = pd.read_json(json_file, orient='split')
    figure = px.histogram(dff, x='student_id', y='score', nbins=10)
    return figure

@callback(Output('table', 'children'), Input('intermediate-value', 'data'))
def update_table(jsonified_cleaned_data):
    json_file = StringIO(jsonified_cleaned_data)
    dff = pd.read_json(json_file, orient='split')
    table = dash_table.DataTable(data=dff.to_dict('records'), page_size=10)
    return table

if __name__ == '__main__':
    app.run(debug=True)
