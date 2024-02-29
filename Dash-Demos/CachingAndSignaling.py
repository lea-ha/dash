import time
import math
from flask_caching import Cache
from dash import Dash, dcc, html, State
from dash.dependencies import Input, Output

# Set up the Dash app and Flask-Cache
app = Dash(__name__, serve_locally=False)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': 'redis://localhost:6379'
})

# This is the "expensive computation" that we cache
@cache.memoize()
def expensive_computation(x):
    y = math.factorial(x)
    time.sleep(5)  # Simulate a long computation
    return y # Return the factorial of x

# Set up the layout with an input, output, and a Store
app.layout = html.Div([
    dcc.Input(id='input', type='number', value=0, className='full-width'),
    dcc.Loading(
        id="loading", 
        children=[
            html.Div(id='output'), 
            dcc.Store(id='signal'),
            html.Button('Compute', id='button', n_clicks=0)
        ], 
        type="circle"
    )
], className='container')

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# When the input changes, perform the expensive computation and update the Store
@app.callback(Output('signal', 'data'), [Input('button', 'n_clicks')], [State('input', 'value')])
def update_signal(n_clicks, input_value):
    if n_clicks > 0:
        return expensive_computation(input_value)

# When the Store updates, update the output
@app.callback(Output('output', 'children'), Input('signal', 'data'))
def update_output(x):
    return f'The expensive computation is complete! The result is {x}.'

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_serve_dev_bundles=False)