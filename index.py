import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
# import data
from about import profile_page
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
        html.Strong('Copyright 2021 RabetAfrica')
    ])
])

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