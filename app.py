import dash
import dash_core_components as dcc
import dash_html_components as html
from FirebaseManager import getData
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

days = 1
data = getData(days)
print("Get initial data")
datapoints = len(data['Humidity'])

figHum = px.line(data, x="Timestamp", y="Humidity", title="Luftfeuchtigkeit über die letzten 3 Tage")
figTemp = px.line(data, x="Timestamp", y="Temperature", title="Temperatur über die letzten 3 Tage")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Raspi Home - Temperatur und Luftfeuchtigkeit',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(
        id="currentDescription"
    ),
    dcc.Graph(
        id='hum-graph',
        figure=figHum,
        style={
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='temp-graph',
        figure=figTemp,
        style={
            'color': colors['text']
        }
    ),
    dcc.Interval(
        id='interval-component',
        interval=600*1000, # in milliseconds
        n_intervals=0
    )
])

@app.callback(Output('currentDescription', 'children'),
              [Input('interval-component', 'n_intervals')])
def updateTempText(n):
    data = getData(days)
    print("Get data")
    datapoints = len(data['Humidity'])

    return(
        [
            html.H6(
                children='Letzte Messung: ' + str(data['Timestamp'][datapoints - 1]),
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
            html.H3(
                children='Luftfeuchtigkeit: ' + str(data['Humidity'][datapoints - 1]) + "%",
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
            html.H3(
                children='Temperatur: ' + str(data['Temperature'][datapoints - 1]) + "°C",
                id="text-temp",
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
        ]
    )

@app.callback(Output('temp-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def updateTempGraph(n):
    print(len(data))
    print(datapoints)
    figTemp = px.line(data, x="Timestamp", y="Temperature", title="Temperatur über die letzten " + str(days) + " Tage")
    return figTemp

@app.callback(Output('hum-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def updateTempGraph(n):
    figHum = px.line(data, x="Timestamp", y="Humidity", title="Luftfeuchtigkeit über die letzten " + str(days) + " Tage")
    return figHum


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=False)
