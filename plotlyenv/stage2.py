# Import relevant libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from datetime import datetime, date, timedelta
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
                       html.H1('Stock Ticker Dashboard'),
                       html.H3('Enter a stock symbol:'),
                       dcc.Input(
                        # Add ID to input box
                        id= 'my_ticker_symbol',
                        value='TSLA' # == Tesla
                                 ),
                       dcc.Graph(
                        # Add ID to graph
                        id= 'my_graph',
                        figure={
                            'data': [
                                     {'x': [1, 2], 'y': [3, 1]}
                                     ],
                                 }
                                  )
                      ])
# Callback Function
@app.callback( 
               Output('my_graph', 'figure'),
               [Input('my_ticker_symbol', 'value')]
              )
def update_graph(stock_ticker):
    start = datetime.today()-timedelta(days=90)
    end = datetime.today()
    df = web.DataReader(stock_ticker, 'iex', start, end)
    fig = {
           'data': [
                     {'x': df.index, 'y': df['close']}
                    ],
           'layout': {'title': stock_ticker}
            }
    return fig


if __name__ == '__main__':
    app.run_server()