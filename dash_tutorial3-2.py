import pandas_datareader.data as web
import quandl
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html

quandl.ApiConfig.api_key = 'naV6nybsUYU66Sppp2xP'
stock = 'HKEX/00005'
df=quandl.get(stock, start_date='2018-06-15', end_date='2018-09-30')

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Nominal Price", axis=1)

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Stock tricker'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Bid, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
