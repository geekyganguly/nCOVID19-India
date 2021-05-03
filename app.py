import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# BootStrap CSS
import dash_bootstrap_components as dbc

# Plotly for Graphs
import plotly
import plotly.graph_objs as go

import assets.colors as clr
import data.data as data


# # external JavaScript files
# external_scripts = [
#     {'src': '/assets/app.js'},
#     {'src': 'https://platform-api.sharethis.com/js/sharethis.js#property=5f19e8bd1bfd970012d81410'},
# ]

external_stylesheets = [
    {
        'href': '/css/all.css',
        'rel': 'stylesheet',
    },
]

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                # external_scripts=external_scripts,
                external_stylesheets = [dbc.themes.BOOTSTRAP, external_stylesheets],
                meta_tags=[
                    {
                        'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1, shrink-to-fit=no',
                        'charset':'utf-8'
                    }
                ]
)

server = app.server
app.title = "nCOVID-19 India"

tab1_content = [
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col(html.Img(src=f'{data.myths_img[i]}', className='img-fluid')),
                        dbc.Col(html.P(f'{data.myths_data[i]}', className="card-text text-muted",), width=9),
                    ], no_gutters=True),
                ]),
            ], style={'backgroundColor' : clr.cardColor['cardBackground']}, className='mt-2')
            for i in range(0,6)
        ],lg=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col(html.Img(src=f'{data.myths_img[i]}', className='img-fluid')),
                        dbc.Col(html.P(f'{data.myths_data[i]}', className="card-text text-muted",), width=9),
                    ], no_gutters=True),
                ]),
            ], style={'backgroundColor' : clr.cardColor['cardBackground']}, className='mt-2')
            for i in range(6,10)
        ],lg=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col(html.Img(src=f'{data.myths_img[i]}', className='img-fluid')),
                        dbc.Col(html.P(f'{data.myths_data[i]}', className="card-text text-muted",), width=9),
                    ], no_gutters=True),
                ]),
            ], style={'backgroundColor' : clr.cardColor['cardBackground']}, className='mt-2')
            for i in range(10,14)
        ],lg=4),
    ]),
]

tab2_content = [
    dbc.Card([
        dbc.CardBody([
            html.ObjectEl("/data/FAQ.pdf", type="application/pdf"),
        ])
    ], style={'backgroundColor' : clr.cardColor['cardBackground']}, className='mt-2')
]

resources_tab1_content = [
    dbc.Table([
        html.Thead(html.Tr([html.Th("States"), html.Th("Helpline Info")])),
        html.Tbody([
            html.Tr([
                html.Td(f"{i['loc']}"), html.Td(f"{i['number']}")
            ])
            for i in data.get_states_contacts_data(data.urls['states_contacts_url'])
        ])
    ], bordered=True, responsive=True, hover=True, striped=True, className='mt-2'),
]

resources_tab2_content = [
    dbc.Table([
        html.Thead(html.Tr([
            html.Th("States"),
            html.Th("Rural Hospitals"),
            html.Th("Rural Beds"),
            html.Th("Urban Hospitals"),
            html.Th("Urban Beds"),
            html.Th("Total Hospitals"),
            html.Th("Total Beds"),
        ])),
        html.Tbody([
            html.Tr([
                html.Td(f"{i['state']}"),
                html.Td(f"{i['ruralHospitals']}"),
                html.Td(f"{i['ruralBeds']}"),
                html.Td(f"{i['urbanHospitals']}"),
                html.Td(f"{i['urbanBeds']}"),
                html.Td(f"{i['totalHospitals']}"),
                html.Td(f"{i['totalBeds']}"),
            ])
            for i in data.get_hosipital_bed_data(data.urls['hospitals_beds_url'])
        ])
    ], bordered=True, responsive=True, hover=True, striped=True, className='mt-2'),
]

resources_tab3_content = [
    dbc.Table([
        html.Thead(html.Tr([
            html.Th("States"),
            html.Th("Colleges"),
            html.Th("City"),
            html.Th("Ownership"),
            html.Th("Admission Capacity"),
            html.Th("Hospital Bed"),
        ])),
        html.Tbody([
            html.Tr([
                html.Td(f"{i['state']}"),
                html.Td(f"{i['name']}"),
                html.Td(f"{i['city']}"),
                html.Td(f"{i['ownership']}"),
                html.Td(f"{i['admissionCapacity']}"),
                html.Td(f"{i['hospitalBeds']}"),
            ])
            for i in data.get_medical_colleges_data(data.urls['medical_colleges_url'])
        ])
    ], bordered=True, responsive=True, hover=True, striped=True, className='mt-2'),
]

#------------------------------ Layout ---------------------#
app.layout = html.Div([
    dcc.Interval(
        id='interval-component',
        interval=5*60*1000, # in milliseconds
        n_intervals=0
    ),

    #---------------------------- NavBar ------------------#
    dbc.NavbarSimple([
        dbc.NavItem(dbc.NavLink("Info", href='#info',external_link=True,style={'color':clr.navColor['linkColor']})),
        dbc.NavItem(dbc.NavLink("Resources", href='#resources',external_link=True,style={'color':clr.navColor['linkColor']})),
        dbc.NavItem(dbc.NavLink("Sources", href="#sources",external_link=True,style={'color':clr.navColor['linkColor']})),
        dbc.NavItem(dbc.NavLink("About", href="#about",external_link=True,style={'color':clr.navColor['linkColor']})),
    ],
        color=clr.navColor['backGround'],
        light=True,
        brand="nCOVID-19 India",
        brand_href="#",
        sticky='top',
        brand_style={'color' : clr.navColor['linkColor']},
        className='border-bottom font-weight-bold',
    ),
    #--------------------------- NavBar End -----------------#

    #--------------------------- Helpline --------------------#
    html.Div([
        html.H6([
            html.I(className="fas fa-phone-alt"),
            ' 1075 ',
            html.Span(' +91-11-23978046', style={'color': clr.textColor['headBlue']}, className='text-muted'),
        ], style={'color': clr.textColor['headColor']}),
        html.H6([
            html.I(className="far fa-envelope"),
            ' ncov2019@gov.in',
        ], style={'color': clr.textColor['headBlue']}),
    ],className='container-sm mt-3 text-center'),
    #--------------------------- Helpline End ----------------#

    #----------------------------Summary --------------------#
    html.Div([
        html.P(['Updated : ', html.Span(id='update-date')], style={'font-size': '14px'}, className='text-center text-muted font-italic'),
        dbc.Row([
            dbc.Col([
                html.H5('WORLD', style={'color': clr.textColor['headColor']}, className='pb-2 font-weight-bold'),
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='world-confirmed', className="card-title text-center font-weight-bold"),
                            html.P("Confirmed", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['confirmed'], "height": "8rem"})),
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='world-active', className="card-title text-center font-weight-bold"),
                            html.P("Active", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['active'], "height": "8rem"})),
                ],className='mb-3'),
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='world-recovered', className="card-title text-center font-weight-bold"),
                            html.P("Recovered", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['recovered'], "height": "8rem"})),
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='world-deaths', className="card-title text-center font-weight-bold"),
                            html.P("Deaths", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ] ,style={'background-color': clr.cardColor['deaths'], "height": "8rem"})),
                ],className='mb-3'),
            ],lg=4),

            dbc.Col([
                html.H5("INDIA'S LATEST", style={'color': clr.textColor['headColor']}, className='pb-2 font-weight-bold'),
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='india-confirmed', className="card-title text-center font-weight-bold"),
                            html.P("Confirmed", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['confirmed'], "height": "8rem"})),
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='india-active', className="card-title text-center font-weight-bold"),
                            html.P("Active", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['active'], "height": "8rem"})),
                ],className='mb-3'),
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='india-recovered', className="card-title text-center font-weight-bold"),
                            html.P("Recovered", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['recovered'], "height": "8rem"})),
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='india-deaths', className="card-title text-center font-weight-bold"),
                            html.P("Deaths", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ] ,style={'background-color': clr.cardColor['deaths'], "height": "8rem"})),
                ],className='mb-3'),
            ],lg=4),

            dbc.Col([
                dbc.Row([
                    dbc.Col(html.H5('STATES', style={'color': clr.textColor['headColor']}, className='font-weight-bold')),
                    dbc.Col(
                        dcc.Dropdown(
                            id='states-dd',
                            value='Bihar',
                            searchable=False,
                            clearable=False,
                            placeholder="Select a State",
                            style={
                                'backgroundColor': '#DFDFEF',
                                'color': '#000000',
                            },
                        ) , width=9
                    ),
                ], className='pb-1'),
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='state-confirmed', className="card-title text-center font-weight-bold"),
                            html.P("Confirmed", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['confirmed'], "height": "8rem"})),
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='state-active', className="card-title text-center font-weight-bold"),
                            html.P("Active", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['active'], "height": "8rem"})),
                ],className='mb-3'),
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='state-recovered', className="card-title text-center font-weight-bold"),
                            html.P("Recovered", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ],style={'background-color': clr.cardColor['recovered'], "height": "8rem"})),
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            html.H4(id='state-deaths', className="card-title text-center font-weight-bold"),
                            html.P("Deaths", className="card-text text-muted font-weight-bold text-center",),
                        ]),
                    ] ,style={'background-color': clr.cardColor['deaths'], "height": "8rem"})),
                ],className='mb-3'),
            ],lg=4),
        ]),
    ],className='container-sm mt-4'),
    #------------------------------- Summary End -------------------------#

    #------------------------------- Graphs -----------------------------#
    html.Div([
        dcc.Graph(
            id='graph-1',
            config={'displayModeBar': False},
        ),
    ],className='container-sm mt-3'),

    html.Div([
        dcc.Graph(
            id='graph-2',
                config={'displayModeBar': False},
            ),

    ],className='container-sm mt-4'),
    #------------------------------- Graphs End -----------------------#

    #------------------------------- Info -----------------------------#
    html.Div([
        dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                            html.H5("CORONA VIRUS (COVID-19)", style={'color': clr.textColor['headColor']}, className="font-weight-bold card-title"),
                            html.P('The World Health Organization (WHO) has dubbed the new corona virus a "global epidemic" and declared it a global epidemic. The corona virus is a respiratory disease. It is transmitted from one person to another through the nasal passages when an infected person coughs or sneezes.',
                                className="card-text text-muted",
                                style={'font-size': '15px'},
                            ),
                            html.P("It is a new species of virus that was not previously identified in humans. The virus infects humans and animals. The virus can cause severe colds to severe acute respiratory syndrome (SARS).",
                                className="card-text text-muted",
                                style={'font-size': '15px'},
                            ),
                    ],lg=6),
                    dbc.Col([
                            html.Iframe(src='https://www.youtube.com/embed/OFFg21KhOV0', className='p-3 embed-responsive-item'),
                    ],lg=6,className='embed-responsive embed-responsive-16by9'),
                ]),

                dbc.Row([
                    dbc.Col(
                        html.Img(src='/assets/images/symptoms.png', className='img-fluid'),
                        lg=6
                    ),
                    dbc.Col(
                        html.Img(src='/assets/images/prevention.png', className='img-fluid'),
                        lg=6
                    ),
                ]),

                dbc.Tabs([
                    dbc.Tab(label="Myth-Busters", tab_id="tab-1"),
                    dbc.Tab(label="FAQ", tab_id="tab-2"),
                ], id="tabs", active_tab="tab-1", className='pt-3 h6 font-weight-bold', style={'color' : clr.textColor['headBlue']}),
                html.Div(id='tab-content'),

            ]),
        ], style={'background-color': clr.cardColor['cardBackground']}),
    ], id='info', className='container-sm'),
    #--------------------------------- Info End --------------------------#

    #--------------------------------- Resources -------------------------#
    html.Div([
        dbc.Card([
            dbc.CardBody([
                html.H5("RESOURCES", style={'color': clr.textColor['headColor']}, className="font-weight-bold card-title"),
                dbc.Tabs([
                    dbc.Tab(label="States Helpline", tab_id="resources_tab1"),
                    dbc.Tab(label="Hospitals & Beds", tab_id="resources_tab2"),
                    dbc.Tab(label="Medical Colleges", tab_id="resources_tab3"),
                ], id="resources-tabs", active_tab="resources_tab1", className='pt-3 h6 font-weight-bold', style={'color' : clr.textColor['headBlue']}),
                html.Div(id='resources-tab-content'),
            ]),
        ], style={'background-color': clr.cardColor['cardBackground']}),
    ], id='resources', className='container-sm mt-3'),
    #--------------------------------- Resources End -------------------------#

    #--------------------------------- Sources ---------------------------#
    html.Div([
        dbc.Card([
            dbc.CardBody([
                html.H5("SOURCES", style={'color': clr.textColor['headColor']}, className="font-weight-bold card-title"),
                html.H6('India government websites/health departments', className='h6 font-weight-bold', style={'color' : clr.textColor['headBlue']}),
                html.A('who.int' , href='https://covid19.who.int/',target="_blank", className='text-muted h6'),
                html.Br(),
                html.A('mohfw.gov.in' , href='https://www.mohfw.gov.in/',target="_blank", className='text-muted h6'),
                html.Br(),
                html.A('mygov.in' , href='https://www.mygov.in/covid-19',target="_blank", className='text-muted h6'),
            ]),
        ], style={'background-color': clr.cardColor['cardBackground']}),
    ], id='sources', className='container-sm mt-3 text-center'),
    #--------------------------------- Sources End ---------------------------#

    #--------------------------------- About ---------------------------------#
    html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5('ABOUT ME', style={'color': clr.textColor['headColor']}, className="font-weight-bold card-title"),
                        html.H6('Who am i?', className='h6 font-weight-bold', style={'color' : clr.textColor['headBlue']}),
                        html.Img(src='assets/images/about.png', height=200, width=250),
                        html.H3('Saurav Ganguly', className='text-muted'),
                        html.H5('FullStack Python Developer', className='text-muted'),
                        html.H5('Find me on', className='text-muted'),
                        html.Div([
                            html.A(html.I(className='fas fa-globe'), href='https://www.sauravganguly.in', target='_blank', className='text-muted pr-4'),
                            html.A(html.I(className='fab fa-github'), href='https://github.com/SauravGanguly', target='_blank', className='text-muted pr-4',),
                            html.A(html.I(className='fab fa-linkedin-in'), href='https://www.linkedin.com/in/gangulysaurav', target='_blank', className='text-muted pr-4',),
                            html.A(html.I(className='fab fa-twitter'), href='https://twitter.com/saurav__ganguly', target='_blank', className='text-muted ',),
                        ],style={'fontSize' : '25px'}),
                    ]),
                ], style={'background-color': clr.cardColor['cardBackground']}),
            ],lg=6, className='text-center mt-3'),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5('FEEDBACK', style={'color': clr.textColor['headColor']}, className="font-weight-bold card-title text-center"),
                        html.H6('Please give your valuable feedback', className='h6 font-weight-bold text-center', style={'color' : clr.textColor['headBlue']}),
                        dbc.Form([
                            dbc.Input(id='name', type="text", placeholder="Enter your name", className="mb-3 mt-3",),
                            dbc.FormGroup([
                                dbc.Input(id='email', type="email", placeholder="Enter your email"),
                                dbc.Checklist(
                                    options=[
                                        {'label': 'Get daily nCOVID-19 updates to your inbox.', 'value': 'Yes'},
                                    ],
                                    id='checklist',
                                    className='text-muted',
                                ),
                            ]),
                            dbc.FormGroup([
                                html.Div(className='sharethis-inline-reaction-buttons'),
                            ], className='text-muted'),
                            dbc.Textarea(
                                id='feedback',
                                placeholder="Please leave your message or suggestion",
                                className='mb-3',
                            ),
                            dbc.Button("Submit", id='submit', color="primary"),
                        ]),
                    ]),
                ], style={'background-color': clr.cardColor['cardBackground']}),
                dbc.Modal([
                    dbc.ModalHeader("Thank you for your valuable feedback."),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close", className="ml-auto"
                        )
                    ),
                ],id="modal", backdrop=True, style={'background-color': clr.cardColor['cardBackground']}),
            ],lg=6, className='mt-3'),
        ]),
    ], id='about', className='container-sm'),
    #---------------------------------- About End ---------------------------#

    #---------------------------------- Footer ------------------------------#
    html.Div([
        html.H6("Made with ❤ in India", style={'color': clr.textColor['headBlue']}, className='text-center mt-3'),
        html.P("Keep calm | Stay @ home | Learn something new", className='text-muted text-center mb-3')
    ]),
    #---------------------------------- Footer End --------------------------#
])
#--------------------------------------- layout End -------------------------------#

#------------------------------- States Dropdown Callbacks ----------------------#
@app.callback([Output('states-dd', "options")],
    [Input('interval-component', 'n_intervals')])
def create_dd(n):
    states_data = data.get_data(data.urls['india_latest_data_url'])
    states = []
    for i in states_data["data"]["regional"]:
        temp_dict = {'label': i['loc'], 'value': i['loc']}
        states.append(temp_dict)
    return states,
#------------------------------- States Dropdown Callbacks End ----------------------#

#------------------------------ Summary Callback -----------------------------#
@app.callback(
    [Output('update-date', 'children'),
     Output('world-confirmed', 'children'),
     Output('world-active', 'children'),
     Output('world-recovered', 'children'),
     Output('world-deaths', 'children'),
     Output('india-confirmed', 'children'),
     Output('india-active', 'children'),
     Output('india-recovered', 'children'),
     Output('india-deaths', 'children'),
     Output('state-confirmed', 'children'),
     Output('state-active', 'children'),
     Output('state-recovered', 'children'),
     Output('state-deaths', 'children'),],
    [Input('interval-component', 'n_intervals'),
    Input("states-dd", 'value')])
def update_summary(n, state):
    world_confirmed, world_active, world_recovered, world_deaths = data.get_world_data(data.urls['world_summary_data_url'])
    update_date, india_confirmed, india_active, india_recovered, india_deaths = data.get_india_data(data.urls['india_latest_data_url'])
    state_confirmed, state_active, state_recovered, state_deaths = data.get_state_data(data.urls['india_latest_data_url'], state)
    return update_date, world_confirmed, world_active, world_recovered, world_deaths, india_confirmed, india_active, india_recovered, india_deaths, state_confirmed, state_active, state_recovered, state_deaths
#----------------------------------------- Summary Callback End --------------------------#

#------------------------------------------ Graph 1 Callback -----------------------------#
@app.callback(Output('graph-1', 'figure'),
    [Input('interval-component', 'n_intervals')])
def graph_1(value):
    date, confirmed, recovered, deaths = data.get_india_timeline_data(data.urls['india_timeline_url'])

    trace1 = go.Scatter(
        x=date,
        y=confirmed,
        mode = "lines",
        name = "Confirmed",
    )

    trace2 = go.Scatter(
        x=date,
        y=deaths,
        mode = "lines",
        name = "Deceased",
    )

    trace3 = go.Scatter(
        x=date,
        y=recovered,
        mode = "lines",
        name = "Recovered",
    )
    layout = go.Layout(
        title={
            'text': 'Cummulative COVID-19 India Trend',
            'y':0.95,
            'x':0.45,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'color' : clr.textColor['headColor'],
                'size' : 18,
            }
        },
        xaxis_range=[date[-76],date[-1]],
        legend_orientation="h",
        plot_bgcolor='white',
        hovermode='x',
        autosize=True,
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
            fixedrange=True,
        ),
        yaxis=dict(
            showgrid=False,
            showticklabels=False,
            fixedrange=True,
        ),
        margin=dict(
            autoexpand=False,
            t=50,
            l=0,
            r=0,
        ),
    )

    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
    return fig
#------------------------------------------ Graph 1 Callback End -----------------------------#

#------------------------------------------ Graph 2 Callback -----------------------------#
@app.callback(Output('graph-2', 'figure'),
    [Input('interval-component', 'n_intervals')])
def graph_2(value):
    states, confirmed, active, recovered, deaths = data.get_states_data(data.urls['india_latest_data_url'])
    fig = go.Figure(data=[
        go.Bar(name='Confirmed', y=states, x=confirmed, orientation='h'),
        go.Bar(name='Active', y=states, x=active, orientation='h', marker_color='#AB63FA'),
        go.Bar(name='Recovered', y=states, x=recovered, orientation='h'),
        go.Bar(name='Deaths', y=states, x=deaths, orientation='h', marker_color='#EF553B')
    ])

    fig.update_layout(
        title={
            'text': 'Cummulative COVID-19 States Trend',
            'y':1,
            'x':0.45,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'color' : clr.textColor['headColor'],
                'size' : 18,
            }

        },
        barmode='group',
        xaxis_type="log",
        legend_orientation="h",
        plot_bgcolor='white',
        hovermode='y',
        autosize=True,
        yaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
            fixedrange=True,
        ),
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
            fixedrange=True,
        ),
        legend=dict(
            x=0,
            y=0
        ),
        #width=500,
        height=1800,
        margin=dict(
            t=30,
            l=100,
            r=0
        ),
    )
    return fig
#------------------------------------------ Graph 2 Callback End -----------------------------#

#------------------------------------------ Tabs Callback -----------------------------#
@app.callback(Output("tab-content", "children"),
    [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content

@app.callback(Output("resources-tab-content", "children"),
    [Input("resources-tabs", "active_tab")])
def switch_tab(at):
    if at == "resources_tab1":
        return resources_tab1_content
    elif at == "resources_tab2":
        return resources_tab2_content
    elif at == "resources_tab3":
        return resources_tab3_content
#------------------------------------------ Tabs Callback End -----------------------------#

#------------------------------------------ About feedback form Callback ------------------#
@app.callback(
    Output("modal", "is_open"),
    [Input("submit", "n_clicks"),
    Input("close", "n_clicks")],
    [State("modal", "is_open"),
    State("name", "value"),
    State("email", "value"),
    State("checklist", "value"),
    State("feedback", "value")])
def on_button_click(n1, n2, is_open, name, email, checklist, feedback):
    if n1 or n2:
        return not is_open
    return is_open
#------------------------------------- About feedback form Callback  End ------------------#

if __name__ == '__main__':
    app.run_server(debug=True)
