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

dateFinPrevue = fileDF.iloc[:, [2]]
# print(dateFinPrevue)

dateFinReelle = fileDF.iloc[:, [3]]
dureePrevue = fileDF.iloc[:, [4]]
dureeReelle = fileDF.iloc[:, [7]]
retardJour = fileDF.iloc[:, [8]]
retardPourcent = fileDF.iloc[:, [9]]
coutJournalier = fileDF.iloc[:, [10]]
coutPrévu = fileDF.iloc[:, [11]]
coutRéel = fileDF.iloc[:, [12]]
diffCout = fileDF.iloc[:, [11, 12]]['Coût\nréel'].sub(
    fileDF.iloc[:, [11, 12]]['Coût\nprévu'], axis=0)
#print(fileDF['Prob.\nTech'].astype('float64', errors='raise').apply(np.floor))


delais_layout = html.Div([
    html.H1('Page 1'),
    html.Div([
        dcc.Dropdown(
            id='page-1-dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        dcc.Dropdown(
            id='page-2-dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        )
    ]),
    html.Div(id='page-1-content')
])
