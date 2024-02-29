
import time
from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.DataFrame({
    'student_id' : range(1, 11),
    'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})
# Expensive computation upfront
def some_expensive_function():
        time.sleep(7)
        result = []
        for i in range(1, 6):
                result.append(df[df['score'] == i]['student_id'].tolist())
        return result
expensive_computation = some_expensive_function()


app.layout = html.Div([
    dcc.Store(id='store', data=expensive_computation),
    dcc.Dropdown(id='dropdown', options=[{'label': i, 'value': i} for i in range(6)]),  # Select a number to square
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('dropdown', 'value'),
    Input('store', 'data')
)
def update_output(value, data):
    # Use the precomputed data here
    if value is not None:
        return '{} was scored by students ids: {}'.format(value, str(data[value-1]))
        #return 'The square of {} is {}'.format(value, data[str(value)])
    else:
        return 'Please select a value'

if __name__ == '__main__':
    app.run_server(debug=True)