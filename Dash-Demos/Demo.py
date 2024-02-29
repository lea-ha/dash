# Import necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import seaborn as sns

# Load the iris dataset
df = sns.load_dataset('iris')

# Initialize the app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Data Exploration Dashboard"),
    dcc.Dropdown(
        id='xaxis-column',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='sepal_length'
    ),
    dcc.Dropdown(
        id='yaxis-column',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='sepal_width'
    ),
    dcc.Graph(id='scatter-plot'),
    dcc.Dropdown(
        id='histogram-column',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='species'
    ),
    dcc.Graph(id='histogram'),
])

# Define callback to update scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value')]
)
def update_scatter_plot(xaxis_column_name, yaxis_column_name):
    fig = px.scatter(df, x=xaxis_column_name, y=yaxis_column_name, color='species')
    return fig

# Define callback to update histogram
@app.callback(
    Output('histogram', 'figure'),
    [Input('histogram-column', 'value')]
)
def update_histogram(histogram_column_name):
    fig = px.histogram(df, x=histogram_column_name, color='species')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)