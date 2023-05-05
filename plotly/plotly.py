from sys import displayhook
import pandas as pd, numpy as np, plotly.express as px, js; 
from js import JSON, Plotly;
def add_div(name): 
        displayhook(name, target = name) 
def plot(fig, name): 
    Plotly.react(name, JSON.parse(fig.to_json()))
def test_pyscript(name): 
    df = pd.DataFrame(np.random.rand(10000, 4), columns=['A', 'B', 'C', 'D']) 
    fig = px.scatter_3d(df, x='A', y='B', z = 'C', color='D') 
    plot(fig, name)