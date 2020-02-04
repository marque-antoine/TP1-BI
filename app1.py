import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from tabs import delais, couts, rapport, risques, satisfactionClient

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    html.H1('BI TP1'),
    dcc.Tabs(id="tabs-example", value='delais', children=[
        dcc.Tab(label='Délais', value='delais'),
        dcc.Tab(label='Couts', value='couts'),
        dcc.Tab(label='Risques', value='risques'),
        dcc.Tab(label='Satisfaction Client', value='satisfactionClient'),
        dcc.Tab(label='Rapport', value='rapport'),
    ]),
    html.Div(id='tabs-content-example')
])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'delais':
        return delais.delais_layout
    elif tab == 'couts':
        return couts.couts_layout
    elif tab == 'risques':
        return risques.risques_layout
    elif tab == 'satisfactionClient':
        return satisfactionClient.satisfactionClient_layout
    elif tab == 'rapport':
        return rapport.rapport_layout

# Tab 1 callback
@app.callback(Output('page1content', 'children'),
              [Input('page1dropdown', 'value'), Input('page2dropdown', 'value')])
# @app.callback(dash.dependencies.Output('example-graph', 'children'))
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


def page_2_dropdown(value):
    return 'You are amaging "{}"'.format(value)

# Tab 2 callback
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
