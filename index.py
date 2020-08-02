import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import data
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div( className='wrapper', children=[
    html.Div(
        className="main-header navbar navbar-expand navbar-white navbar-light",
        # Left navbar links
        children=[
            html.Ul(className="navbar-nav",
                    children=[
                        html.Li(className='nav-item',
                                children=[
                                    html.A(className='nav-link', href='#', **{'data-widget': 'pushmenu'}, role='button',
                                           children=[html.I(className='fas fa-bars')])
                                ]),
                        html.Li(className='nav-item d-none d-sm-inline-block',
                                children=[
                                    html.A('Home', className='nav-link', href='#')
                                ]),
                        html.Li(className='nav-item d-none d-sm-inline-block',
                                children=[
                                    html.A('About Me', className='nav-link', href='#')
                                ]),
                        html.Li(className='nav-item d-none d-sm-inline-block',
                                children=[
                                    html.A('Contact Me', className='nav-link', href='#')
                                ])
                    ]),
            html.Form(
                className='form-inline ml-3',
                children=[
                    html.Div(
                        className='input-group input-group-sm',
                        children=[
                            dcc.Input(className='form-control form-control-navbar', type='search', placeholder='Search'),
                            html.Div(className='input-group-append',
                                     children=[
                                         html.Button(className='btn btn-navbar', type='submit',
                                                     children=html.I(className='fas fa-search'))
                                     ])
                        ]
                    )
                ]
            )
        ]
    ),
    # Main Sidebar Container
    html.Aside(className='main-sidebar sidebar-dark-primary elevation-4',
               # Logo container
               children=[
                   html.A(href='#', className='brand-link',
                          children=[
                              html.Img(className='brand-image img-circle elevation-3', alt='Logo',
                                       src='assets/img/AdminLTELogo.png'),
                              html.Span('RabetAfrica', className='brand-text font-weight-light')
                          ]),
                   # Sidebar container
                   html.Div(className='sidebar',
                            children=[
                                html.Div(className='user-panel mt-3 pb-3 mb-3 d-flex',
                                         children=[
                                             html.Div(className='image',
                                                      children=[
                                                          html.Img(className='img-circle elevation-2', alt='Gyleodhis',
                                                                   src='https://pbs.twimg.com/profile_images/1271865573010522112/G11XJjmR_400x400.jpg')
                                                      ]),
                                             html.Div(className='info',
                                                      children=[
                                                          html.A('Gyleodhis', className='d-block', href='#')
                                                      ])
                                         ]),
                                # Sidebar Menu
                                html.Div(className='mt-2',
                                         children=[
                                             html.Ul(className='nav nav-pills nav-sidebar flex-column', role='menu',
                                                     **{'data-widget': 'treeview', 'data-accordion': 'false'},
                                                     # Add icons to the links using the .nav-icon class
                                                     # with font-awesome or any other icon font library
                                                     children=[
                                                         html.Li(className='nav-item has-treeview menu-open',
                                                                 children=[
                                                                    html.A(className='nav-link active', href='#',
                                                                           children=[
                                                                               html.I(className='nav-icon fas fa-tachometer-alt'),
                                                                               dbc.FormGroup([
                                                                                   html.H4("Select Country"),
                                                                                   dcc.Dropdown(id='country_drop_down',
                                                                                                options=[{'label': i, 'value': i} for i in data.df_final['Country/Region']],
                                                                                                value='Kenya')
                                                                               ]),
                                                                               html.I(className='right fas fa-angle-left')
                                                                           ]),
                                                                     html.Ul(className='nav nav-treeview',
                                                                             children=[
                                                                                 html.Li(className='nav-item',
                                                                                         children=[
                                                                                             html.A(className='nav-link active', href='#',
                                                                                                    children=[
                                                                                                        html.I(className='far fa-circle nav-icon'),
                                                                                                        html.P('Dasboard V1')
                                                                                                    ])
                                                                                         ]),
                                                                                 html.Li(className='nav-item',
                                                                                         children=[
                                                                                             html.A(className='nav-link', href='#',
                                                                                                    children=[
                                                                                                        html.I(className='far fa-circle nav-icon'),
                                                                                                        html.P('Dasboard V2')
                                                                                                    ])
                                                                                         ]),
                                                                                 html.Li(className='nav-item',
                                                                                         children=[
                                                                                             html.A(className='nav-link', href='#',
                                                                                                    children=[
                                                                                                        html.I(className='far fa-circle nav-icon'),
                                                                                                        html.P('Dasboard V3')
                                                                                                    ])
                                                                                         ])
                                                                             ])
                                                                 ]),
                                                         html.Li(className='nav-item',
                                                                 children=[
                                                                     html.A(className='nav-link', href='#',
                                                                            children=[
                                                                                html.I(className='nav-icon fas fa-th'),
                                                                                html.P('Widgets'),
                                                                                html.Span('New', className='right badge badge-danger')
                                                                            ])
                                                                 ])
                                                     ])
                                         ])
                            ])
               ]),
    # Content Wrapper. Contains page content
    html.Div(className='content-wrapper',
             # Content Header (Page header)
             children=[
                    html.Div(className='content-header',
                             children=[
                                 html.Div(className='container-fluid',
                                          children=[
                                              html.Div(className='row mb-2', children=[
                                                  html.Div(className='col-sm-6', children=[
                                                      html.H1(data.df_final.iloc[4]['Country/Region'], className='m-0 text-dark')
                                                  ]),
                                                  html.Div(className='col-sm-6', children=[
                                                      html.Ol(className='breadcrumb float-sm-right', children=[
                                                          html.Li(className='breadcrumb-item', children=[
                                                              html.A('Home', href='#')
                                                          ]),
                                                          html.Li(className='breadcrumb-item active', children=[
                                                              html.A('COVID_19', href='#')
                                                          ])
                                                      ])
                                                  ])
                                              ])
                                          ])
                             ]),
                 # Main content
                 html.Div(className='content', children=[
                     html.Div(className='container-fluid', children=[
                         # Small boxes (Stat box)
                         html.Div(className='row', children=[
                             html.Div(className='col-lg-3 col-6', children=[
                                 html.Div(className='small-box bg-info', children=[
                                     html.Div(className='inner', children=[
                                         html.H3(data.df_final.iloc[4]['Country/Region'])
                                     ]),
                                     html.Div(className='icon', children=[
                                         html.I(className='ion ion-bag')
                                     ]),
                                     html.A('Total Cases:', className='small-box-footer', href='#'),
                                     html.A(data.df_final.iloc[4]['Total_Cases'], className='small-box-footer', href='#')
                                     # html.I(className='fas fa-arrow-circle-right')
                                 ])
                             ]),
                             html.Div(className='col-lg-3 col-6', children=[
                                 html.Div(className='small-box bg-success', children=[
                                     daq.Gauge(
                                         color={"gradient": True,
                                                "ranges": {"green": [0, 6], "yellow": [6, 8], "red": [8, 10]}},
                                         value=data.df_final.iloc[4]['Total_Recoveries'],
                                         logarithmic=False,
                                         label='Recoveries',
                                         max=1000,
                                         min=0,
                                         size=150,
                                     ),
                                     html.Div(className='icon', children=[
                                         html.I(className='ion ion-stats-bars')
                                     ]),
                                     html.A('Total Recoveries', className='small-box-footer', href='#'),
                                     html.I(className='fas fa-arrow-circle-right')
                                 ])
                             ]),
                             html.Div(className='col-lg-3 col-6', children=[
                                 html.Div(className='small-box bg-warning', children=[
                                     daq.Gauge(
                                         color="#D2691E",
                                         value=300,
                                         label='Hello world',
                                         max=1000,
                                         min=0,
                                         size=150,
                                     ),
                                     html.Div(className='icon', children=[
                                         html.I(className='ion ion-person-add')
                                     ]),
                                     html.A('New Infections', className='small-box-footer', href='#'),
                                     html.I(className='fas fa-arrow-circle-right')
                                 ])
                             ]),
                             html.Div(className='col-lg-3 col-6', children=[
                                 html.Div(className='small-box bg-danger', children=[
                                     daq.Gauge(
                                         color="#000000",
                                         value=375,
                                         label='Total Deaths',
                                         max=500,
                                         min=0,
                                         size=150,
                                     ),
                                     html.Div(className='icon', children=[
                                         html.I(className='ion ion-pie-graph')
                                     ]),
                                     html.A('More info', className='small-box-footer', href='#'),
                                     html.I(className='fas fa-arrow-circle-right')
                                 ])
                             ])
                         ]),
                         # End of Row
                         # Main row
                         html.Div(className='row', children=[
                             html.Section(className='col-lg-7 connectedSortable', children=[
                                 # Custom tabs (Charts with tabs)
                                 html.Div(className='card', children=[
                                     html.Div(className='card-header', children=[
                                         html.H3(className='card-title', children=['Covid_19 Statistics',
                                             html.I(className='fas fa-universal-access ')
                                         ]),
                                         html.Div(className='card-tools', children=[
                                             html.Ul(className='nav nav-pills ml-auto', children=[
                                                 html.Li(className='nav-item', children=[
                                                     html.A('Area', className='nav-link active', href='#', **{'data-toggle': 'tab'}),
                                                     html.Div(id='hello', children=[
                                                         # dcc.Graph(id='covid_per_country'),
                                                         # dcc.Graph(id='values')
                                                     ])
                                                 ]),
                                                 html.Li(className='nav-item', children=[
                                                     html.A('Donut', className='nav-link', href='#', **{'data-toggle': 'tab'})
                                                 ])
                                             ])
                                         ])
                                     ])
                                 ])
                             ])
                         ])

                     ])
                 ])
             ]),
    html.Footer(className='main-footer', children=[
        html.Strong('Copyright 2020 RabetAfrica')
    ])
])
# @app.callback(
#     Output('covid_per_country', 'figure'),
#     [Input('country_drop_down', 'value')]
# )
# def update_figure(selected_coutry):
#     final_df = data.df_final[data.df_final['Country/Region'] == selected_coutry]
#     for i in final_df['Country/Region']():

if __name__ == '__main__':
    app.run_server(debug=False)