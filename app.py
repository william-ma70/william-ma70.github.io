import pandas as pd
import numpy as np

import plotly.express as px
import plotly
import plotly.io as pio

df = pd.read_csv('/Users/williamma/downloads/Psych_Research/data/input/suicide-death-rates.csv')
df

# https://plotly.com/python/choropleth-maps/

# fig = px.choropleth(df, locations="Code",
#                     color="Deaths - Self-harm - Sex: Both - Age: Age-standardized (Rate)", # lifeExp is a column of gapminder
#                     hover_name="Entity", # column to add to hover information
#                     color_continuous_scale=px.colors.sequential.Plasma)
# fig.show()

fig = px.choropleth(df, locations="Code",  animation_frame="Year", animation_group="Entity",
          color="Deaths - Self-harm - Sex: Both - Age: Age-standardized (Rate)", hover_name="Entity")

fig["layout"].pop("updatemenus") # optional, drop animation buttons


pio.write_html(fig, file='map.html', auto_open=True)

# fig.show()


df1 = pd.read_csv('/Users/williamma/downloads/Psych_Research/data/input/suicide-rate-vs-income-inequality.csv')
df

fig1 = px.scatter(df1, animation_frame="Year", animation_group="Entity", size="Population (historical estimates)",
          color="Suicide mortality rate (per 100,000 population)", hover_name="Entity")

fig1["layout"].pop("updatemenus") # optional, drop animation buttons

pio.write_html(fig, file='scatter.html', auto_open=True)


#ATTEMPTED DASH IMPLEMENTATION

# import plotly.graph_objects as go # or plotly.express as px
# # fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# # fig.add_trace( ... )
# # fig.update_layout( ... )

# import dash
# from dash import dcc, html, callback, Input, Output
# import graph

# app = dash.Dash()

# server = app.server

# app.layout = html.Div([
#     # represents the browser address bar and doesn't render anything
#     dcc.Location(id='url', refresh=False),

#     dcc.Link('Navigate to "/"', href='/'),
#     html.Br(),
#     dcc.Link('Navigate to "/page-2"', href='/page-2'),

#     # content will be rendered in this element
#     html.Div(id='page-content', children=[])
# ])


# @callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])

# def display_page():
#     return graph.layout

# if __name__ == '__main__':
#     app.run_server(debug=True)