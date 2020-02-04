import pandas as pd
import numpy as np
import os
import csv
import math
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

file = 'TP1.xls'

fileDF = pd.ExcelFile(file)

fileDF = pd.ExcelFile(file).parse('Données')


fileDF = fileDF.dropna()

coutJournalier = fileDF.iloc[:, [10]].astype('float64', errors='raise')
coutPrévu = fileDF.iloc[:, [11]].astype('float64', errors='raise')
coutRéel = fileDF.iloc[:, [12]].astype('float64', errors='raise')
diffCout = fileDF.iloc[:, [11, 12]]['Coût\nréel'].sub(
    fileDF.iloc[:, [11, 12]]['Coût\nprévu'], axis=0).astype('float64', errors='raise')

diffCoutPourcentage = (fileDF.iloc[:, [14]].astype(
    'float64', errors='raise')*100).round(1)



couts_layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
