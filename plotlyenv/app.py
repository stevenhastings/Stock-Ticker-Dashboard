import dash
import dash_core_components as dcc
import dash_html_components as html

# Launch application
app = dash.Dash()

# Div containing [headers, input box, graph]
app.layout = html.Div([
                        html.H1('Stock Ticker Dashboard'),
                        html.H3('Enter a stock symbol:'),
                        
                        dcc.Input(id= 'my_stock_picker',
                                  value= 'TSLA'),
                        dcc.Graph(
                                  id= 'my_graph',
                                  figure= {
                                            'data': [{
                                            'x': [1,2], 
                                            'y': [3,1]
                                                     }]
                                            }
                                   )
                        ])

# Connect to Server
if __name__ == '__main__':
    app.run_server()