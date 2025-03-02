from dash import dash, dcc, html,Input, Output ,State,register_page,callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas
import plotly.graph_objects as go
from pycaret.classification import *
import numpy as np 
model = load_model('Dropout_Model')
register_page(__name__, path='/')
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
data = pandas.read_excel('ignore/data_dropout_59-64.xlsx')
data['DEGREE_ID'] = data["DEGREE_ID"].dropna()
data['FUND_NAME_CODE'] = data["FUND_NAME_CODE"].replace({'Y':1,'N':2,'other':3})
# data['FUND_NAME_CODE'] = data["FUND_NAME_CODE"].replace('N',2)
# data['FUND_NAME_CODE'] = data["FUND_NAME_CODE"].replace('other',3)
data['SEX_SHORT_NAME_THAI'] = data['SEX_SHORT_NAME_THAI'].replace({'ช':0,'ญ':1})
# data['SEX_SHORT_NAME_THAI'] = data['SEX_SHORT_NAME_THAI'].replace('ญ',1)
# data['ENT_METHOD'] = data['ENT_METHOD'].replace('B1',103)
# data['ENT_METHOD'] = data['ENT_METHOD'].replace('D0',100)
# data['ENT_METHOD'] = data['ENT_METHOD'].replace('P4',101)
# data['ENT_METHOD'] = data['ENT_METHOD'].replace('E1',102)
data["IN_PROVINCE"] = data["IN_PROVINCE"].replace(["N","Y"],[0,1])
data["IN_PROVINCE_CAMPUS"] = data["IN_PROVINCE_CAMPUS"].replace(["N","Y"],[0,1])

df_dash = pandas.read_excel('ignore\data_dropout_59-64.xlsx')
df_grap1 = df_dash[[  "ADMIT_YEAR", 'STUDY_STATUS' ]]
df_grap1 = df_grap1[df_grap1['STUDY_STATUS']=='R']
df_grap1.columns = ['ปีการศึกษา','จำนวนผู้ตกออก']
grap1 = df_grap1.groupby('ปีการศึกษา').count()
df_grap2 = df_dash[['ADMIT_YEAR', 'MAJOR_NAME_THAI', 'STUDY_STATUS']]
df_grap2 = df_grap2[df_grap2['STUDY_STATUS'] == 'R']
df_grap2 = df_grap2.groupby(['ADMIT_YEAR', 'MAJOR_NAME_THAI']).count().reset_index()
df_grap2.columns = ['ปีการศึกษา', 'สาขา', 'จำนวนผู้ตกออก']
fig = px.pie(grap1, values='จำนวนผู้ตกออก', names=grap1.index, title='จำนวนผู้ตกออกตามปีการศึกษา',hole=0.4 )
fig2 = px.bar(df_grap2, x='ปีการศึกษา', y='จำนวนผู้ตกออก', color='สาขา', title='จำนวนนักศึกษาที่ตกออกต่อปี แยกตามสาขา')
fig.update_layout(
    plot_bgcolor='#E6E6FA',
    paper_bgcolor='#252525',
    title_font_color='white',
    legend_font_color='white',
    
)
fig2.update_layout(
    plot_bgcolor='#E6E6FA',
    paper_bgcolor='#252525',
    title_font_color='white',
    legend_font_color='white'
)
first_card = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H5("สาขาวิชา",style={"font-size": "15px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                                options=[{"label": p.strip(), "value": p.strip()} for p in data["MAJOR_NAME_THAI"].unique()]
                                        ,
                                id='input9',
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "12vw",
                                    "height": "5vh",
                                },
                            ),
                        ],
                        style={"display": "inline-block", "margin-right": "20px","margin-left": "2vw"},
                    ),
                    html.Div(
                        [
                            html.H5("ภาควิชา",style={"font-size": "15px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                               options=[{"label": p.strip(), "value": p.strip()} for p in data["DEPT_NAME_THAI"].unique()],
                                id = 'input10',
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "12vw",
                                    "height": "5vh",
                                },
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px"},
                    ),
                    html.Div(
                        [
                            html.H5("ประเภทการศึกษา",style={"font-size": "15px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                                options=[{"label": p.strip(), "value": p.strip()} for p in data["STUDY_TYPE_NAME"].unique()],
                                id='input11',
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "12vw",
                                    "height": "5vh",
                                },
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px","margin-top": "20px"},
                    ),
                    html.Div(
                        
                            [
                                html.H5("ปริญญาบัตรที่จบ",style={"font-size": "15px","text-align":"center","color":"white"}),
                                dcc.Dropdown(
                                    options=[{"label": p.strip(), "value": p.strip()} for p in data["COURSE_DEGREE"].unique()],
                                    id="input12",
                                    searchable=False,
                                    className="row-1 card",
                                    style={"width": "20vw", "height": "5vh"},
                                ),
                            ],
                            style={"display": "inline-block", "margin-right": "20px"},
                        ),
                    html.Div(
                        [
                            html.H5("เพศ",style={"font-size": "15px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                                options=[
                                    dict(label=p.strip(), value=p.strip())
                                    for p in ['ชาย','หญิง']],
                                id='input13',
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px","margin-top": "30px","margin-left": "2.1vw"}
                    ),
                   
                    html.Div(
                        [
                            html.H5("เกิดในจังหวัดเดียวกับมหาลัย",style={"font-size": "15px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                                options=[dict(label=p.strip(), value=p.strip())
                                    for p in ['ใช่','ไม่ใช่']],
                                id = 'input15',
                                searchable=False,
                                className="row-1 card",
                                style={
                                    "width": "11vw",
                                    "height": "5vh",
                                }
                            ),
                        ],
                        style={"display": "inline-block","margin-right": "20px","font-size": "15px"}
                    ),
                    html.Div(
                        [
                            html.H5("จบจากโรงเรียนที่อยู่จังหวัดเดียวกับมหาลัย",style={"font-size": "13px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                                options=[dict(label=p.strip(), value=p.strip())
                                    for p in ['ใช่','ไม่ใช่']],
                                id='input16',
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
                            html.H5("ได้รับทุน",style={"font-size": "15px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                                options=[dict(label=p.strip(), value=p.strip())
                                    for p in ['ได้รับ','ไม่ได้รับ','อื่นๆ']],
                                id='input17',
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
                            html.H5("สถานะทางครอบครัว",style={"font-size": "15px","text-align":"center","color":"white"}),
                            dcc.Dropdown(
                                options=[{"label": p.strip(), "value": p.strip()} for p in data["PARENTS_MARRIED_NAME"].unique()],
                                id = 'input18',
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
                            dcc.Input(id="input1", type="number", max="4", min="0",placeholder="เกรดปี1เทอม1", 
                                    style={'marginRight': '20px','marginTop': '20px','border-radius':'5px','margin-left': '160px',"text-align":"center"
                                           ,"width": "11vw","height": "4vh","display": "inline-right", "font-size": "23px",}),
                            dcc.Input(id="input2", type="number",  max="4", min="0",placeholder='เกรดปี1เทอม2', 
                                    style={'marginRight': '20px','border-radius':'5px',"text-align":"center","width": "11vw","height": "4vh", "font-size": "23px",}),
                            dcc.Input(id="input3", type="number", max="4", min="0",placeholder='เกรดปี2เทอม1',  
                                    style={'marginRight': '20px','marginTop': '10px','border-radius':'5px',"text-align":"center","width": "11vw","height": "4vh", "font-size": "23px",}),
                            dcc.Input(id="input4", type="number", max="4", min="0",placeholder='เกรดปี2เทอม2', 
                                    style={'marginRight': '20px','border-radius':'5px',"text-align":"center","width": "11vw","height": "4vh", "font-size": "23px",}),
                        html.Br(),
                            dcc.Input(id="input5", type="number", max="4", min="0",placeholder='เกรดปี3เทอม1', 
                                    style={'marginTop': '30px','marginRight': '20px','margin-Top': '30px','border-radius':'5px','margin-left': '160px',"text-align":"center","width": "11vw","height": "4vh", "font-size": "23px",}),
                            dcc.Input(id="input6", type="number", max="4", min="0",placeholder='เกรดปี3เทอม2', 
                                    style={'marginRight': '20px','border-radius':'5px',"text-align":"center","width": "11vw","height": "4vh", "font-size": "23px",}),
                            dcc.Input(id="input7", type="number", max="4", min="0",placeholder='เกรดปี4เทอม1', 
                                    style={'marginbottom': '20px','marginRight': '20px','marginTop': '10px','border-radius':'5px',"border-color":"#ccccc","text-align":"center","width": "11vw","height": "4vh", "font-size": "23px",}),
                            dcc.Input(id="input8", type="number", max="4", min="0",placeholder='เกรดปี4เทอม2',style={'marginRight': '10px','marginTop': '10px','border-radius':'5px',"text-align":"center","width": "11vw","height": "4vh", "font-size": "23px",}, debounce=True),
                            html.Div(id="output"),
                    ]
                ),
                dbc.Button("Predict Here", color="danger",id="compute-button",n_clicks=0,
                           style={"font-size": "24px",'margin-left': '25vw','marginTop': '37px',"hover-color":"white","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.5)","width": "11vw","height": "4.9vh","opacity":"1"}),
        ]
    ),
    style={
        # "background-color": "#F7F6CF",
        "background": "#252525",
        # "background-color": "#FAF7F0",    #card bg
        "margin-bottom": "10px",
        "width": "65vw",
        "height": "65vh",
        "position": "center",
        "opacity":"0.8",
        "display": "flex",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.4)",
        # "margin-left": "0.25vw",
        "margin-bottom": "20px",
    }
)

second_card = dbc.Card(
    dbc.CardBody(
    
        [
            html.H5("Prediction", className="card-title",style={"font-size": "45px",'text-align':'center','color':'danger',"opacity":"1",}),
            html.P(""
            ),
            html.Div(id='prediction'),
            # dbc.Button("Go somewhere", color="danger"),
      
        ]
    ),
    style={
        # "margin-bottom": "10px",
        "background-color": "#252525",
        "width": "30vw",
        "height": "65vh",
        "position": "center",
        "display": "flex",
        "opacity":"0.9",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.5)",
        "margin-left": "33.5vw",
        "margin-bottom": "20px",
        "font-family": "Arial, sans-serif", "font-size": "64px", "color": "#E50914", "text-shadow": "2px 2px #000", "letter-spacing": "2px", "animation": "neon 1.5s ease-in-out infinite alternate"})
    

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Prediction Pie Graph", className="card-title",style={"color":"white"}),
            html.P(""),
            # dbc.Button("Go somewhere", color="success"),
            html.Div(id="piepredict")
        ]
    ),
    style={
        "background-color": "#252525",
        "margin-bottom": "10px",
        "width": "33vw",
        "height": "65vh",
        "opacity":"0.8",
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
            html.H5("Data Statistics", className="card-title",style={"color":"white"}),
            html.P(""),
            # dbc.Button("Update Graph", id="button", color="primary"),
            html.Div(id='info'),
            dbc.Row([
            dbc.Col(dcc.Graph(figure=fig), width=6),
            dbc.Col(dcc.Graph(figure=fig2), width=6)
        ])
        ]
    ),
    style={
        # "margin-bottom": "10px",
        "background-color": "#252525",
        "width": "62vw",
        "height": "65vh",
        "position": "center",
        "display": "flex",
        "opacity":"0.8",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)",
        "margin-left": "1.5vw",
        "margin-bottom": "20px",
    }
)
cards = dbc.Row(
    [
        dbc.Col(first_card, width=4),
        dbc.Col(second_card, width=6,),
        dbc.Col(third_card, width=4),
        dbc.Col(fouth_card, width=6),
    ],
    style={'marginTop': '20px'}
)


layout = html.Div(
    children=
        cards,
        style={'margin': '20px'},
    )


@callback(
    Output("output", "children"),
    Input("compute-button", "n_clicks"),
    State("input1", "value"),
    State("input2", "value"),
    State("input3", "value"),
    State("input4", "value"),
    State("input5", "value"),
    State("input6", "value"),
    State("input7", "value"),
    State("input8", "value"),
    State("input9", "value"),
    State("input10", "value"),
    State("input11", "value"),
    State("input12", "value"),
    State("input13", "value"),
    State("input15", "value"),
    State("input16", "value"),
    State("input17", "value"),
    State("input18", "value"),
)
def update_output(n_clicks, input1, input2, input3, input4, input5, input6, input7, input8, input9,
                  input10, input11, input12, input13,  input15, input16, input17, input18):
    # if any(val is None for val in [input1, input2, input3, input4, input5, input6, input7, input8, input9,
    #               input10, input11, input12, input13,  input15, input16, input17, input18]):
    #     return  
                                                   
    Data_Test = pandas.DataFrame({'MAJOR_ID':input9, 
                        'DEPT_ID':input10,  
                        'STUDY_TYPE_ID':input11,
                        'DEGREE_ID':input12, 
                        'SEX_SHORT_NAME_THAI':input13,
                        # 'ENT_METHOD':input14,  
                        'IN_PROVINCE':input15,
                        'IN_PROVINCE_CAMPUS':input16,
                        'เกรดปี1เทอม1':input1,
                        'เกรดปี1เทอม2':input2,
                        'เกรดปี2เทอม1':input3,
                        'เกรดปี2เทอม2':input4,
                        'เกรดปี3เทอม1':input5,
                        'เกรดปี3เทอม2':input6,                                                
                        'เกรดปี4เทอม1':input7,
                        'เกรดปี4เทอม2':input8,
                        'FUND_NAME_CODE':input17,
                        'PARENTS_MARRIED_NAME_CODE':input18},index=[0])
    
    Data_Test[['เกรดปี1เทอม1','เกรดปี1เทอม2',
                     'เกรดปี2เทอม1','เกรดปี2เทอม2',
                     'เกรดปี3เทอม1','เกรดปี3เทอม2',
                     'เกรดปี4เทอม1','เกรดปี4เทอม2',]]= Data_Test[['เกรดปี1เทอม1','เกรดปี1เทอม2','เกรดปี2เทอม1',
                                                                'เกรดปี2เทอม2','เกรดปี3เทอม1','เกรดปี3เทอม2',
                                                                'เกรดปี4เทอม1','เกรดปี4เทอม2',]].apply(lambda row: row.fillna(row.median()), axis=1)
    Data_Test = Data_Test.astype({
    'MAJOR_ID': str,
    'DEPT_ID': str,
    'STUDY_TYPE_ID': str,
    'DEGREE_ID': str,
    'SEX_SHORT_NAME_THAI':str,
    'IN_PROVINCE':str, 
    'IN_PROVINCE_CAMPUS':str,
    'เกรดปี1เทอม1': float,
    'เกรดปี1เทอม2': float,
    'เกรดปี2เทอม1': float,
    'เกรดปี2เทอม2': float,
    'เกรดปี3เทอม1': float,
    'เกรดปี3เทอม2': float,
    'เกรดปี4เทอม1': float,
    'เกรดปี4เทอม2': float,
    'FUND_NAME_CODE':str,
    'PARENTS_MARRIED_NAME_CODE': str
})
    Data_Test['MAJOR_ID'] = Data_Test['MAJOR_ID'].replace({'ยังไม่แยกสาขาวิชา':200,'วิศวกรรมและการจัดการนวัตกรรม':203,
                                                 'วิศวกรรมปัญญาประดิษฐ์':204,'วิศวกรรมสิ่งแวดล้อม':205,'วิศวกรรมไฟฟ้า':210,
                                                 'วิศวกรรมชีวการแพทย์':214,'วิศวกรรมเครื่องกล':215,'วิศวกรรมเมคาทรอนิกส์':216,
                                                 'วิศวกรรมโยธา':220,'วิศวกรรมอุตสาหการ':225,'วิศวกรรมการผลิต':226,
                                                 'วิศวกรรมเคมี':230,'วิศวกรรมเหมืองแร่':235,'วิศวกรรมคอมพิวเตอร์':240,
                                                 'วิศวกรรมวัสดุ':250,'วิศวกรรมเหมืองแร่และวัสดุ':254})
    Data_Test['DEPT_ID'] = Data_Test['DEPT_ID'].replace({'ภาควิชาวิศวกรรมไฟฟ้า':28,'ภาควิชาวิศวกรรมโยธา':29,'ภาควิชาวิศวกรรมเครื่องกล':30,
                                                         'ภาควิชาวิศวกรรมอุตสาหการ':31,'ภาควิชาวิศวกรรมเคมี':32,'ภาควิชาวิศวกรรมเหมืองแร่และวัสดุ':33,
                                                         'ภาควิชาวิศวกรรมคอมพิวเตอร์':34,'คณะวิศวกรรมศาสตร์':193})
    
    Data_Test['STUDY_TYPE_ID'] = Data_Test['STUDY_TYPE_ID'].replace({'ภาคปกติ':1,'ภาคปกติ (นานาชาติ)':4,'ภาคปกติ (พิเศษ)':7})

    Data_Test['DEGREE_ID'] = Data_Test['DEGREE_ID'].replace({'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมเหมืองแร่และวัสดุ)':149.0,'วิศวกรรมศาสตรบัณฑิต':200.0,
                                                             'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมชีวการแพทย์)':211.0,'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมไฟฟ้า)':213.0,
                                                             'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมเครื่องกล)':218.0,'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมโยธา)':223.0,
                                                             'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมอุตสาหการ)':228.0,'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมเคมี)':233.0,
                                                             'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมวัสดุ)':238.0,'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมการผลิต)':239.0,
                                                             'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมเหมืองแร่)':240.0,'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมเมคาทรอนิกส์)':242.0,
                                                             'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมคอมพิวเตอร์)':243.0,'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมสิ่งแวดล้อม)':245.0,
                                                             'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมปัญญาประดิษฐ์)':252.0,'วิศวกรรมศาสตรบัณฑิต (วิศวกรรมและการจัดการนวัตกรรม)':254.0})
    
    Data_Test['SEX_SHORT_NAME_THAI'] = Data_Test['SEX_SHORT_NAME_THAI'].replace({'ชาย':0,'หญิง':1})

    Data_Test['IN_PROVINCE'] = Data_Test['IN_PROVINCE'].replace({'ไม่ใช่':0,'ใช่':1})
    
    Data_Test['IN_PROVINCE_CAMPUS'] = Data_Test['IN_PROVINCE_CAMPUS'].replace({'ไม่ใช่':0,'ใช่':1})

    Data_Test['FUND_NAME_CODE'] = Data_Test['FUND_NAME_CODE'].replace({'ไม่ได้รับ':2,'ได้รับ':1,'อื่นๆ':3})

    Data_Test['PARENTS_MARRIED_NAME_CODE'] = Data_Test['PARENTS_MARRIED_NAME_CODE'].replace({'อยู่ด้วยกัน':9,'บิดาแต่งงานใหม่':3,'บิดาถึงแก่กรรม':6,'บิดาและมารดาแต่งงานใหม่':4,
                                                                                             'บิดาและมารดาถึงแก่กรรม':5,'มารดาแต่งงานใหม่':7,'มารดาถึงแก่กรรม':8,
                                                                                             'แยกกันอยู่เพราะความจำเป็นเกี่ยวกับอาชีพ':1,'แยกกันอยู่เพราะสาเหตุอื่น':2,'หย่าร้าง':10,
                                                                                             'อื่น ๆ':11})

    
    Dict = {0:"G",1:"R"}
    prediction = model.predict_proba(Data_Test)[0]
    status,percent = Dict[(prediction.tolist()).index(prediction.max())],f"{round(prediction.max()*100,2)}"
    

    # if status == 'G':
    #     status = 'R'
    #     percent = f"{(100 - float(percent)):.2f}"
    #     return status, percent
    # else :
    return status, percent
    
@callback(
    Output("prediction", "children"),
    Input("output", "children")
)
def show_prediction(output_value):
    status, percent = output_value[:2]
    # statusss = status.replace(['R','G'],['Retine','Pass'])
    if float(percent) > 50 and status == 'R':
        # status = 'Retire'/
        return html.Div([
        # html.H4(f"{status}", style={"align": "center","width": "2vw","height": "5vh","font-family": "Arial, sans-serif", "font-size": "64px", "color": "#E50914", "text-shadow": "2px 2px #000", "letter-spacing": "2px","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)","background-color": "#eeeeee",'border-radius':'5px',"padding-left":"100px"}),
        html.H4('Retire', style={"font-family": "Arial, sans-serif", "font-size": "110px", "color": "#E50914", "text-shadow": "2px 2px #000", "letter-spacing": "2px", "animation": "neon 1.5s ease-in-out infinite alternate","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)"}),
        html.H4(f"{percent}%", style={"font-family": "Arial, sans-serif", "font-size": "110px", "color": "#E50914", "text-shadow": "2px 2px #000", "letter-spacing": "2px", "animation": "neon 1.5s ease-in-out infinite alternate","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)"})
    ], style={"text-align": "center","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)",})
    else:
        # status = 'Pass'
        return html.Div([
        # html.H4(f"{status}", style={"align": "center","width": "2vw","height": "5vh","font-family": "Arial, sans-serif", "font-size": "64px", "color": "#E50914", "text-shadow": "2px 2px #000", "letter-spacing": "2px","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)","background-color": "#eeeeee",'border-radius':'5px',"padding-left":"100px"}),
        html.H4('Pass', style={"font-family": "Arial, sans-serif", "font-size": "110px", "color": "#0FD347", "text-shadow": "2px 2px #000", "letter-spacing": "2px", "animation": "neon 1.5s ease-in-out infinite alternate","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)"}),
        html.H4(f"{percent}%", style={"font-family": "Arial, sans-serif", "font-size": "110px", "color": "#0FD347", "text-shadow": "2px 2px #000", "letter-spacing": "2px", "animation": "neon 1.5s ease-in-out infinite alternate","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)"})
    ], style={"text-align": "center","box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)",})
    


@callback(
    Output("piepredict", "children"),
    Input("output", "children")
)
def show_graph(output_value):
    status,percent = output_value[:2]
    
    df = pandas.DataFrame({'labels': ['G', 'R'], 'values': [float(percent), 100-float(percent)]})
    fig3 = px.pie(df, values='values', names='labels')
    fig3.update_layout(
    plot_bgcolor='#E6E6FA',
    paper_bgcolor='#252525',
    title_font_color='white',
    legend_font_color='white',
)
    return dcc.Graph(figure=fig3)
    
# @callback(
#     Output('input1', 'style'),
#     Input('input1', 'value')
# )
# def update_input_style(value):
#     if value is not None and float(value) > 4:
#         return {'backgroundColor': 'red'}
#     else:
#         return {'backgroundColor': 'white'}
   