import plotly
import seaborn as sns
import plotly.graph_objects  as go
import plotly.express as px
from cleaning_data import data_mpg
import json


def dist_mpg():
    df = data_mpg()
    df_group= df['mpg']
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])

    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
  


def dist_horse():
    df = data_mpg()
    df_group= df['horsepower']  
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])

    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json