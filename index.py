import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
# import data
import about
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = dash.Dash(__name__)
server = app.server
app.title = 'RabetAfrica'

app.layout = html.Div(className='wrapper', children=[
    dcc.Location(id='url',refresh=False),
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
                                    html.A('Home', className='nav-link', href='/')
                                ]),
                        html.Li(className='nav-item d-none d-sm-inline-block',
                                children=[
                                    html.A('Profile', className='nav-link', href='/profile')
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
                                                                   src='assets/img/gyle.jpg')
                                                      ]),
                                             html.Div(className='info',
                                                      children=[
                                                          html.A('Gyleodhis', className='d-block', href='https://www.linkedin.com/in/gyle-odhiambo-992990150/',
                                                                 target='_blank')
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
                                                                    html.A(className='nav-link', href='#',
                                                                           children=[
                                                                               html.I(className='nav-icon fas fa-globe-africa text-success'),
                                                                               html.I(className='right fas fa-angle-left'),
                                                                               html.P('Africa')
                                                                           ]),
                                                                     html.Ul(className='nav nav-treeview',
                                                                             children=[
                                                                                 html.Li(className='nav-item',
                                                                                         children=[
                                                                                             html.A(className='nav-link active', href='#',
                                                                                                    children=[
                                                                                                        html.I(className='far fa-circle text-info nav-icon'),
                                                                                                        html.P('Kenya')
                                                                                                    ])
                                                                                         ]),
                                                                                 html.Li(className='nav-item',
                                                                                         children=[
                                                                                             html.A(className='nav-link', href='#',
                                                                                                    children=[
                                                                                                        html.I(className='far fa-circle text-info nav-icon'),
                                                                                                        html.P('Vision 2030')
                                                                                                    ])
                                                                                         ]),
                                                                                 html.Li(className='nav-item',
                                                                                         children=[
                                                                                             html.A(className='nav-link', href='#',
                                                                                                    children=[
                                                                                                        html.I(className='far fa-circle text-info nav-icon'),
                                                                                                        html.P('SDGs')
                                                                                                    ])
                                                                                         ])
                                                                             ])
                                                                 ]),
                                                         html.Li(className='nav-item',
                                                                 children=[
                                                                     html.A(className='nav-link', href='#',
                                                                            children=[
                                                                                html.I(className='nav-icon fa fa-money'),
                                                                                html.P('World Bank'),
                                                                                html.Span('New', className='right badge badge-primary')
                                                                            ]),
                                                                     html.A(className='nav-link', href ='#', children=[
                                                                         html.I(className='nav-icon fa fa-medkit'),
                                                                         html.P('WHO'),
                                                                         html.Span('Coming Soon', className='right badge badge-success')
                                                                     ]),
                                                                     html.A(className='nav-link', href='#',children=[
                                                                         html.I(className='nav-icon fa fa-sun-o'),
                                                                         html.P('Climate'),
                                                                         html.Span('Coming Up', className='right badge badge-danger')
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
                 html.Div(id='page-content')
             ]),
    html.Footer(className='main-footer', children=[
        html.Strong('Copyright 2020 RabetAfrica')
    ])
])

profile_page = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Profile')
                ]),
                html.Div(className='col-sm-6',children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('My Profile', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid',children=[
            html.Div(className='row', children=[
                html.Div(className='col-md-3', children=[
                    # Profile Image
                    html.Div(className='card card-primary card-outline', children=[
                        html.Div(className='card-body box-profile', children=[
                            html.Div(className='text-center', children=[
                                html.Img(className='profile-user-img img-fluid img-circle', src='assets/img/gyle.jpg',
                                         alt='Profile picture')
                            ]),
                            html.H3('Gyle Odhiambo', className='profile-username text-center'),
                            html.P('Data Engineer', className='text-muted text-center'),
                            html.Ul(className='list-group list-group-unbordered mb-3', children=[
                                html.Li(className='list-group-item', children=[
                                    html.B('Twitter'),
                                    html.A('300', className='float-right')
                                ]),
                                html.Li(className='list-group-item', children=[
                                    html.B('LinkedIn'),
                                    html.A('+1000', className='float-right')
                                ]),
                                html.Li(className='list-group-item', children=[
                                    html.B('Github'),
                                    html.A('12', className='float-right')
                                ])
                            ]),
                            html.A(className='btn btn-primary btn-block', href='https://twitter.com/gyleodhis',
                                   target='_blank', children=[
                                    html.B('Follow')
                                ])
                        ]) # card body
                    ]), #card
                    # About Me Box
                    html.Div(className='card card-primary', children=[
                        html.Div(className='card-header', children=[
                            html.H3('About Me', className='card-title')
                        ]),
                    # card-header
                        html.Div(className='card-body',children=[
                            html.Strong(children=[
                                html.I(className='fas fa-book mr-1'), ' Education'
                            ]),
                            html.P('B.S. in Computer Science from Jomo Kenyatta University of Agriculture and Technology',
                                   className='text-muted'),
                            html.Hr(),
                            html.Strong(children=[
                                html.I(className='fas fa-map-marker-alt mr-1'), ' Location'
                            ]),
                            html.P('Nairobi, Kenya',
                                   className='text-muted'),
                            html.Hr(),
                            html.Strong(children=[
                                html.I(className='fas fa-pencil-alt mr-1'), ' Skills'
                            ]),
                            html.P(className='text-muted', children=[
                                html.Span('Data Science ', className='tag tag-success'),
                                html.Span('Machine Learning ', className='tag tag-success'),
                                html.Span('Data Engineering ', className='tag tag-success'),
                                html.Span('Apache Spark ', className='tag tag-success'),
                                html.Span('Big Data ', className='tag tag-success'),
                                html.Span('Python ', className='tag tag-info'),
                                html.Span('Qlik Sense ', className='tag tag-info')
                            ]),
                            html.Hr(),
                            html.Strong(children=[
                                html.I(className='fas fa-envelope-open-text mr-1'), ' Contact'
                            ]),
                            html.P(className='text-muted', children=[
                                html.Span('gaylordodhiambo@gmail.com ', className='tag tag-info'),
                                html.Br(),
                                html.Span('gyleodhis@outlook.com', className='tag tag-info')
                            ])
                        ]) #card-body
                    ]) #Card
                ]), #Col-md-3
                html.Div(className='col-md-9',children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header p-2',children=[
                            html.Ul(className='nav nav-pills',children=[
                                html.Li(className='nav-item',children=[
                                    html.A('Activity', className='nav-link active',href='#activity', **{'data-toggle': 'tab'})
                                ]),
                                html.Li(className='nav-item',children=[
                                    html.A('Bucket List', className='nav-link',href='#bucket_list', **{'data-toggle': 'tab'})
                                ]),
                                html.Li(className='nav-item',children=[
                                    html.A('Timeline', className='nav-link',href='#timeline', **{'data-toggle': 'tab'})
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ]),
    dcc.Dropdown(id='profile-2-dropdown',
                 options=[{'label': i, 'value': i} for i in ['NRB','MBS','KSM','KAK']],
                 value='NRB'),
    html.Div(id='profile-2-content'),
    html.Br(),
    dcc.Link('Go to Profile', href='/profile'),
    html.Br(),
    dcc.Link('Home',href='/')

])


@app.callback(dash.dependencies.Output('profile-2-content','children'),
              [dash.dependencies.Input('profile-2-dropdown', 'value')])
def profile_2_dropdown(value):
    return 'You have selected' "{}".format(value)

# Updating the index callback


@app.callback(dash.dependencies.Output('page-content','children'),
             [dash.dependencies.Input('url','pathname')])
def display_page(pathname):
    if pathname == '/profile':
        return profile_page
# @app.callback(
#     Output('covid_per_country', 'figure'),
#     [Input('country_drop_down', 'value')]
# )
# def update_figure(selected_coutry):
#     final_df = data.df_final[data.df_final['Country/Region'] == selected_coutry]
#     for i in final_df['Country/Region']():

if __name__ == '__main__':
    app.run_server(debug=False)