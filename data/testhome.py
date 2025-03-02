from dash import dash, dcc, html,Input, Output
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas
import plotly.graph_objects as go

dash.register_page(__name__, path='/')
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
 
first_card = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H5("Input 1"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                },
                            ),
                        ],
                        style={"display": "inline-block", "margin-right": "20px","margin-left": "20px"},
                    ),
                    html.Div(
                        [
                            html.H5("Input 2"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                },
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"},
                    ),
                    html.Div(
                        [
                            html.H5("Input 3"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                },
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px","margin-top": "20px"},
                    ),
                    html.Div(
                        [
                            html.H5("Input 4"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"}
                    ),
                    html.Div(
                        [
                            html.H5("Input 5"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"}
                    ),
                    html.Div(
                        [
                            html.H5("Input 6"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px","margin-left": "20px","margin-top": "20px"}
                    ),
                    html.Div(
                        [
                            html.H5("Input 7"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"}
                    ),
                    html.Div(
                        [
                            html.H5("Input 8"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"}
                    ),
                    html.Div(
                        [
                            html.H5("Input 9"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"}
                    ),
                    html.Div(
                        [
                            html.H5("Input 10"),
                            dcc.Dropdown(
                                options=[],
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"}
                    ),
                ],
            ),
                    html.Div([
                        html.Br(),
                            html.Label(style={'marginRight': '20px',"margin-left": "20px"}), 
                            dcc.Input(id="input1", type="text", placeholder="เกรดปี1เทอม1", 
                                    style={'marginRight': '10px','border-radius':'5px',"text-align":"center"}),
                            html.Label(style={'marginRight': '10px'}),
                            dcc.Input(id="input2", type="text", placeholder='เกรดปี1เทอม2', 
                                    style={'marginRight': '10px','border-radius':'5px',"text-align":"center"}),
                            html.Label(style={'marginRight': '10px'}),
                            dcc.Input(id="input3", type="text", placeholder='เกรดปี2เทอม1',  
                                    style={'marginRight': '10px','marginTop': '10px','border-radius':'5px',"text-align":"center"}),
                            html.Label(style={'marginRight': '10px'}),
                            dcc.Input(id="input4", type="text", placeholder='เกรดปี2เทอม2', 
                                    style={'marginRight': '160px','border-radius':'5px',"text-align":"center"}),
                            html.Label(style={'marginRight': '10px'}),
                        html.Br(),
                            dcc.Input(id="input5", type="text", placeholder='เกรดปี3เทอม1', 
                                    style={'marginRight': '10px','marginTop': '10px','border-radius':'5px','marginleft': '320px',"text-align":"center"}),
                            html.Label( 
                                    style={'marginRight': '10px'}),
                            dcc.Input(id="input6", type="text", placeholder='เกรดปี3เทอม2', 
                                    style={'marginRight': '10px','border-radius':'5px',"text-align":"center"}),
                            html.Label( 
                                        style={'marginRight': '10px'}),
                            dcc.Input(id="input7", type="text", placeholder='เกรดปี4เทอม1', 
                                    style={'marginRight': '10px','marginTop': '10px','border-radius':'5px',"border-color":"#ccccc","text-align":"center"}),
                            html.Label( 
                                    style={'marginRight': '10px'}),
                            dcc.Input(id="input8", type="text", placeholder='เกรดปี4เทอม2',style={'marginRight': '10px','marginTop': '10px','border-radius':'5px',"text-align":"center"}, debounce=True),
                            html.Div(id="output"),
                    ]
                ),
                dbc.Button("Predictions", color="success",
                           style={'marginLeft': '300px','marginTop': '18px'}),
        ]
    ),
    style={
        "background-color": "#DCD7C9",
        "margin-bottom": "10px",
        "width": "65vw",
        "height": "65vh",
        "position": "center",
        "display": "flex",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)",
        # "margin-left": "0.25vw",
        "margin-bottom": "20px",
    }
)

second_card = dbc.Card(
    dbc.CardBody(
    
        [
            html.H5("2", className="card-title"),
            html.P(""
            ),
            dbc.Button("Go somewhere", color="success"),
      
        ]
    ),
    style={
        # "margin-bottom": "10px",
        "background-color": "#F7F6CF",
        "width": "30vw",
        "height": "65vh",
        "position": "center",
        "display": "flex",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)",
        "margin-left": "33.5vw",
        "margin-bottom": "20px",
    }
)
third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("3", className="card-title"),
            html.P(""),
            dbc.Button("Go somewhere", color="success"),
        ]
    ),
    style={
        "background-color": "#F7F6CF",
        "margin-bottom": "10px",
        "width": "33vw",
        "height": "65vh",
        "position": "center",
        "display": "flex",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)",
        # "margin-left": "0.25vw",
        "margin-bottom": "20px",
    }
)

fouth_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("4", className="card-title"),
            html.P(""),
            dbc.Button("Go somewhere", color="success"),
        ]
    ),
    style={
        # "margin-bottom": "10px",
        "background-color": "#F7F6CF",
        "width": "62vw",
        "height": "65vh",
        "position": "center",
        "display": "flex",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)",
        "margin-left": "1.5vw",
        "margin-bottom": "20px",
    }
)

cards = dbc.Row(
    [
        dbc.Col(first_card, width=4),
        dbc.Col(second_card, width=6),
        dbc.Col(third_card, width=4),
        dbc.Col(fouth_card, width=6),
    ],
    style={'marginTop': '20px'}
)


layout = html.Div(
     style={
     "background":"#0e361e",
     "margin-bottom": "0",
    },
    children = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home Page", href="#")),
            dbc.NavItem(dbc.NavLink("Archive", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("☎️"+" Telephone", href="#"),
                    dbc.DropdownMenuItem("📱"+" Mobile", href="#"),
                    dbc.DropdownMenuItem("📠"+" Fax", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Group 1 Grades Prediction",
        brand_href="#",
        color="#287346",
        dark=True,
    ),
    html.Div(
        cards,
        style={'margin': '20px'},
    )
]))

@callback(
    Output("output", "children"),
    Input("input1", "value"),
    Input("input2", "value"),
    Input("input3", "value"),
    Input("input4", "value"),
    Input("input5", "value"),
    Input("input6", "value"),
    Input("input7", "value"),
    Input("input8", "value")
)

def update_output(input1, input2, input3, input4, input5, input6, input7, input8):
    return

if __name__ == "__main__":
    app.run_server()
    