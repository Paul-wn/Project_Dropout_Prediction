import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__ , path='/Contact')

contact = html.Div(children=[
    html.H1(children='Contact Us',style={"text-align": "center","color": "white"}),

    html.Div(children=" "),

])

# Define the cards
card1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("6510110311", className="card-title",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.P("พัทธดนย์ หนุดทอง 6510110311@psu.ac.th", className="card-text",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.Img(src="static\ppic.jpg", style={"width": "21.5vw", "height": "21.5v", "display": "block", "margin": "auto"}),
        ],
            style={"width": "12vw","height": "85vh","margin-bottom": "200px",},
    ),style={"background":"#252525","margin-bottom": "1vh","opacity":"0.9"}
)

card2 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("6510110399", className="card-title",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.P("รักษิต พูลสวัสดิ์ 6510110399@psu.ac.th", className="card-text",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.Img(src="static\ss.png", style={"width": "21.5vw", "height": "21.5v", "display": "block", "margin": "auto"}),
        ],
        style={"width": "12vw","height": "85vh","margin-bottom": "200px",},
    ),style={"background":"#252525","margin-bottom": "1vh","opacity":"0.9"}
)

card3 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("6510110427", className="card-title",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.P("นายวรากร หนูผุด 6510110427@psu.ac.th", className="card-text",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.Img(src="static\paulpic.jpg", style={"width": "21.5vw", "height": "21.5v", "display": "block", "margin": "auto"}),
        ],
        style={"width":"12vw","height": "85vh","margin-bottom": "200px"},
    ),style={"background":"#252525","margin-bottom": "1vh","opacity":"0.9"}
)

card4 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("6510110541", className="card-title",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.P("นายอับดาร์ เอียดวารี 6510110541@psu.ac.th", className="card-text",style={"text-align": "center","width": "21.5vw", "height": "21.5v", "display": "block","color":"white"}),
            html.Img(src="static\qq.png", style={"width": "21.5vw", "height": "21.5v", "display": "block", "margin": "auto"}),
        ],
         style={"width": "12vw","height": "85vh","margin-bottom": "200px",},
    ),style={"background":"#252525","margin-bottom": "0.2vh","opacity":"0.9"}
)

# Add the cards to the layout
card = html.Div(
    [
        dbc.Row(
            [   
                dbc.Col(contact, width=14),
                dbc.Col(card1, width=3),
                dbc.Col(card2, width=3),
                dbc.Col(card3, width=3),
                dbc.Col(card4, width=3),
            ]
        )
    ]
)
layout = html.Div(
    children=
    card,
    style={'margin':'20px'}
)