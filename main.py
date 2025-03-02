from dash import Dash, html, dcc ,Input, Output, State
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from dash_bootstrap_components._components.Container import Container

app = Dash(__name__, use_pages=True, pages_folder='pages', external_stylesheets=[dbc.themes.BOOTSTRAP])

nav_bar = html.Div(
     style={
    },
    children = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home Page", href='/',)),
            dbc.NavItem(dbc.NavLink("Contact", href='/Contact')),
        ],
        
        # color="#287346",
        color="#000000",
        dark=True,
        
    ), 
    
]))
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="static\logo.png", height="100px",style={"opacity":"0.9"})),
                        dbc.Col(dbc.NavbarBrand("Group 1 Grades Prediction", className="ms-2",style={'margin-right':'100px',"color":"white",
        "opacity":"0.8"})),
                    ],
                    align="center",
                    className="g-0",
                    style={
                        'font-family':'Sans-serif',
                        "margin-left":"270px"
                        
                    }
                ),
                href="http://127.0.0.1:8050/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                
                nav_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
                style={
                    # "position": "absolute",
                    # "top": "8 px",
                    # "right" : "16 px",
                    
                },
            )
        ]
    ),
    style={"background": "rgb(185,0,25)",
           "background": "linear-gradient(90deg, rgba(185,0,25,1) 0%, rgba(0,0,0,1) 25%, rgba(0,0,0,1) 75%, rgba(205,0,49,1) 100%)",
           "margin-bottom":"0"},
    dark=True,
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

app.layout = html.Div(
    [
    navbar,
    dash.page_container, ],
    style={"background": "rgb(185,0,25)",
           "background": "linear-gradient(90deg, rgba(185,0,25,1) 0%, rgba(0,0,0,1) 25%, rgba(0,0,0,1) 75%, rgba(205,0,49,1) 100%)",
           "margin-bottom":"0"})

if __name__ == '__main__':
    app.run_server()