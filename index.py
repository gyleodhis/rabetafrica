import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np
from _datetime import datetime as dt
from plotly import graph_objects as go
import dash_daq as daq
from data import df_covid_data, df_africa
from about import profile_page
# from covid import covid_page
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# external JavaScript files
# external_scripts = [
#     # Though its not working
#     {'src':'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/js/adminlte.min.js'},
#     {'src':'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/js/demo.min.js'},
#     {'src':'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/js/pages/dashboard.min.js'},
#     {'src':'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/js/pages/dashboard3.min.js'},
#     {'src':'https://use.fontawesome.com/b7484bca63.js'}
# ]
# external CSS stylesheets
# external_stylesheets = [
#     'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/css/adminlte.min.css',
#     'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/css/alt/adminlte.components.min.css',
#     'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/css/alt/adminlte.core.min.css',
#     'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/css/alt/adminlte.extra-components.min.css',
#     'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/css/alt/adminlte.pages.min.css',
#     'https://cdnjs.cloudflare.com/ajax/libs/admin-lte/3.1.0/css/alt/adminlte.plugins.min.css',
#     'https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css',
#     'https://cesium.com/downloads/cesiumjs/releases/1.76/Build/Cesium/Widgets/widgets.css',
# ]

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server
app.title = 'Rabet'

config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}

fig = px.bar(df_africa.nlargest(10, 'new_cases'), x="location", template="simple_white",
             labels={"location": "Country", "new_cases": "New Cases"}, y="new_cases", barmode="group")
fig_world = px.bar(df_covid_data.nlargest(10, 'new_cases'), x="location", template="simple_white",
                   labels={"location": "Country", "new_cases": "New Cases"}, y="new_cases", barmode="group")

fig_pie = px.pie(df_africa.nlargest(10, 'new_vaccinations'), names='location', values='new_vaccinations',
                 labels={"new_vaccinations": "New Vaccinations", "location": "Country"})

fig_world_pie = px.pie(df_covid_data.nlargest(10, 'new_vaccinations'), names='location', values='new_vaccinations',
                       labels={"new_vaccinations": "New Vaccinations", "location": "Country"})

fig_funnel = px.funnel(df_africa.nlargest(10, 'positive_rate'), x='positive_rate', y='location',
                       labels={"positive_rate": "New Positivity Rate", "location": "Country"})
fig_world_funnel = px.funnel(df_covid_data.nlargest(10, 'positive_rate'), x='positive_rate', y='location',
                             labels={"positive_rate": "New Positivity Rate", "location": "Country"})

fig_funnel_vaccine = px.funnel(df_africa.nlargest(10, 'people_vaccinated_per_hundred'),
                               x='people_vaccinated_per_hundred',
                               y='location', color='location',
                               labels={"people_vaccinated_per_hundred": "Vaccination per 100", "location": "Country"})
fig_world_funnel_vaccine = px.funnel(df_covid_data.nlargest(10, 'people_vaccinated_per_hundred'),
                                     x='people_vaccinated_per_hundred',
                                     y='location', color='location',
                                     labels={"people_vaccinated_per_hundred": "Vaccination per 100",
                                             "location": "Country"})
fig_funnel_vaccine.update_yaxes(showticklabels=False)
fig_world_funnel_vaccine.update_yaxes(showticklabels=False)

app.layout = html.Div(className='wrapper hold-transition sidebar-mini layout-fixed', children=[
    dcc.Location(id='url', refresh=False),
    html.Div(
        className="main-header navbar navbar-expand navbar-dark navbar-light",
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
                            dcc.Input(className='form-control form-control-navbar', type='search',
                                      placeholder='Search'),
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
                   # html.A(href='#', className='brand-link',
                   #        children=[
                   #            html.Img(className='brand-image img-circle elevation-3', alt='Logo',
                   #                     src='assets/img/AdminLTELogo.png'),
                   #            html.Span('Rabet', className='brand-text font-weight-light')
                   #        ]),
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
                                                          html.A('Rabet', className='d-block',
                                                                 href='https://www.linkedin.com/in/gaylord-odhiambo-992990150/',
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
                                                                     html.A(className='nav-link active', href='#',
                                                                            children=[
                                                                                html.I(
                                                                                    className='nav-icon fas fa-globe-africa text-success'),
                                                                                html.P(children=['Covid 19', html.I(
                                                                                    className='right fas fa-angle-left')])
                                                                            ])
                                                                     # html.Ul(className='nav nav-treeview',
                                                                     #         children=[
                                                                     #             html.Li(className='nav-item',
                                                                     #                     children=[
                                                                     #                         html.A(className='nav-link active', href='/covid',
                                                                     #                                children=[
                                                                     #                                    html.I(className='far fa-circle text-info nav-icon'),
                                                                     #                                    html.P('Kenya')
                                                                     #                                ])
                                                                     #                     ]),
                                                                     #             html.Li(className='nav-item',
                                                                     #                     children=[
                                                                     #                         html.A(className='nav-link', href='#',
                                                                     #                                children=[
                                                                     #                                    html.I(className='far fa-circle text-info nav-icon'),
                                                                     #                                    html.P('Vision 2030')
                                                                     #                                ])
                                                                     #                     ]),
                                                                     #             html.Li(className='nav-item',
                                                                     #                     children=[
                                                                     #                         html.A(className='nav-link', href='#',
                                                                     #                                children=[
                                                                     #                                    html.I(className='far fa-circle text-info nav-icon'),
                                                                     #                                    html.P('SDGs')
                                                                     #                                ])
                                                                     #                     ])
                                                                     #         ])
                                                                 ]),
                                                         # html.Li(className='nav-item',
                                                         #         children=[
                                                         #             html.A(className='nav-link', href='#',
                                                         #                    children=[
                                                         #                        html.I(className='nav-icon fa fa-money'),
                                                         #                        html.P('World Bank'),
                                                         #                        html.Span('New', className='right badge badge-primary')
                                                         #                    ]),
                                                         #             html.A(className='nav-link', href ='#', children=[
                                                         #                 html.I(className='nav-icon fa fa-medkit'),
                                                         #                 html.P('WHO'),
                                                         #                 html.Span('Coming Soon', className='right badge badge-success')
                                                         #             ]),
                                                         #             html.A(className='nav-link', href='#',children=[
                                                         #                 html.I(className='nav-icon fa fa-sun-o'),
                                                         #                 html.P('Climate'),
                                                         #                 html.Span('Coming Up', className='right badge badge-danger')
                                                         #             ])
                                                         #         ])
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
        html.Strong('Rabet | Vincit Omnia Veritas')
    ])
])

covid_page = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Covid 19 Tracker: ' + str(dt.date(dt.now())))
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Covid', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            # The fow for cumulative figures
            html.Div(className='row', children=[
                html.Div(className='col-md-3', children=[
                    # html.Div(className='form-group', children=[
                    #     html.Label('Selected Countries'),
                    #     html.Select(className='select2',style={'width': '100%'},multiple='multiple', children=[
                    #         dcc.Dropdown(id='continent_drop_down',
                    #                      options=[{'label': i, 'value': i} for i in df_africa['location']],
                    #                      value=df_africa.iloc[4]['location'], multi=True),
                    #         html.Div(className='dropdown_item', id='continent_out_put')
                    #     ])
                    # ]),
                    # html.Div(className='card card-primary card-outline', children=[
                    #     # Country Dropdown menu
                    #     html.Div(className='dropdown', children=[
                    #         dcc.Dropdown(id='continent_drop_down', className='dropdown-menu',
                    #                      options=[{'label': i, 'value': i} for i in df_africa['location']],
                    #                      value=df_africa.iloc[46]['location'], multi=True),
                    #         html.Div(id='continent_out_put', className='dropdown_item')
                    #     ]),
                    #     # Country Drop Down
                    #     html.Div(className='dropdown', children=[
                    #         html.A('Select Country', className='dropdown-toggle', href='#', role='button',
                    #                **{'data-toggle': 'dropdown', 'aria-haspopup': 'true', 'aria-expanded': 'false'}),
                    #         html.Div(className='dropdown-menu', children=[
                    #             html.A('Kenya123', className='dropdown-item', href='#'),
                    #             html.A('Uganda255', className='dropdown-item', href='#')
                    #         ])
                    #     ])
                    # ]),
                ]),
                html.Div(className='col-md-12', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-info', children=[
                                html.Div(className='inner', children=[
                                    # html.H4(df_covid_data.iloc[46]['location']),
                                    html.H4('New Cases')
                                ]),
                                html.A('Africa: ', className='small-box-footer', href='#'),
                                html.A(df_africa['new_cases'].sum(), className='small-box-footer', href='#')
                                # html.A('Worldwide: ' + str(df_covid_data['new_cases'].sum()),
                                #        className='small-box-footer', href='#'),
                                # html.I(className='fas fa-arrow-circle-right')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    # html.H4(df_covid_data.iloc[46]['location']),
                                    html.H4('Positivity Rate')
                                ]),
                                html.Div(className='icon', children=[
                                    html.I(className='ion ion-bars')
                                ]),
                                html.A('Africa:', className='small-box-footer', href='#'),
                                html.A(np.round(df_covid_data['positive_rate'].mean(), 3), className='small-box-footer',
                                       href='#')
                                # html.I(className='fas fa-arrow-circle-right')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    # html.H4(df_covid_data.iloc[46]['location']),
                                    html.H4('Total Death')
                                ]),
                                html.Div(className='icon', children=[
                                    html.I(className='ion ion-pie-graph')
                                ]),
                                html.A('Africa:', className='small-box-footer', href='#'),
                                html.A(df_covid_data['new_deaths'].sum(), className='small-box-footer',
                                       href='#')
                                # html.I(className='fas fa-arrow-circle-right')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-warning', children=[
                                html.Div(className='inner', children=[
                                    # html.H4(df_covid_data.iloc[46]['location']),
                                    html.H5('Patients in ICU')
                                ]),
                                html.Div(className='icon', children=[
                                    html.I(className='ion ion-bag')
                                ]),
                                html.A('Africa:', className='small-box-footer', href='#'),
                                html.A(df_covid_data['icu_patients'].sum(), className='small-box-footer',
                                       href='#')
                                # html.I(className='fas fa-arrow-circle-right')
                            ])
                        ])
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('World', className='nav-link',
                                                                                      href='#world',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(df_africa['new_cases'].sum(), className='text-bold text-lg'),
                                            html.Span('New Cases Today')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((round(
                                                    df_africa['new_cases'].sum() / df_covid_data['new_cases'].sum(),
                                                    3)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig, config=config)
                                    ])]),
                                html.Div(className='tab-pane', id='world', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(df_covid_data['new_cases'].sum(), className='text-bold text-lg'),
                                            html.Span('Global New Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(round(
                                                    df_covid_data['new_cases'].sum() / df_covid_data.shape[0],
                                                    0),
                                                    className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Global Avg Per Country', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_world, config=config)
                                    ])])
                            ])
                            # html.Div(className='d-flex flex-row justify-content-end', children=[
                            #     html.Span(className='mr-2', children=[
                            #         html.I(className='fas fa-square text-primary'),' This Month'
                            #     ]),
                            #     html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                            # ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top Countries in Vaccinations', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_vax', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('World', className='nav-link',
                                                                                      href='#world_vax',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(df_africa['new_vaccinations'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('New Vaccinations Today')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(df_africa['new_vaccinations'].sum() / df_covid_data[
                                                    'new_vaccinations'].sum(), 3)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % to the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_pie, config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='world_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(df_covid_data['new_vaccinations'].sum(),
                                                      className='text-bold text-lg'),
                                            html.Span('Global New Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(round(
                                                    df_covid_data['new_vaccinations'].sum() / df_covid_data.shape[0],
                                                    0),
                                                    className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Global Avg Per Country', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_world_pie,
                                                  config=config)
                                    ])
                                ])
                            ])
                            # html.Div(className='d-flex flex-row justify-content-end', children=[
                            #     html.Span(className='mr-2', children=[
                            #         html.I(className='fas fa-square text-primary'),' This Month'
                            #     ]),
                            #     html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                            # ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Positivity Rate', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_pst_rate', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('World', className='nav-link',
                                                                                      href='#world_pst_rate',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round((df_africa['positive_rate'].dropna(how='any').mean()) * 100, 3),
                                                className='text-bold text-lg'),
                                            html.Span('Todays Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((round(
                                                    df_africa['positive_rate'].sum() / df_covid_data[
                                                        'positive_rate'].sum(),
                                                    3)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel,
                                                  config=config)
                                    ])
                                    # html.Div(className='d-flex flex-row justify-content-end', children=[
                                    #     html.Span(className='mr-2', children=[
                                    #         html.I(className='fas fa-square text-primary'),' This Month'
                                    #     ]),
                                    #     html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                                    # ])
                                ]),
                                html.Div(className='tab-pane', id='world_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round((df_covid_data['positive_rate'].dropna(how='any').mean()) * 100,
                                                      3),
                                                className='text-bold text-lg'),
                                            html.Span('Global Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(round(
                                                    df_covid_data['positive_rate'].sum() / df_covid_data.shape[0], 2),
                                                    className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Global Avg Per Country', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_world_funnel,
                                                  config=config)
                                    ])
                                    # html.Div(className='d-flex flex-row justify-content-end', children=[
                                    #     html.Span(className='mr-2', children=[
                                    #         html.I(className='fas fa-square text-primary'),' This Month'
                                    #     ]),
                                    #     html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                                    # ])
                                ])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Vaccinations Per 100 Persons', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_vax_100', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('World', className='nav-link',
                                                                                      href='#world_vax_100',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round(
                                                    df_africa['people_vaccinated_per_hundred'].dropna(how='any').mean(),
                                                    3),
                                                className='text-bold text-lg'),
                                            html.Span('Todays Avg Vaccination Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((round(
                                                    df_africa['people_vaccinated_per_hundred'].sum() / df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(), 3)) * 100) + '%',
                                                       className='fas fa-arrow-down')
                                            ]),
                                            html.Span('Africas % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel_vaccine,
                                                  config=config)
                                    ])
                                    # html.Div(className='d-flex flex-row justify-content-end', children=[
                                    #     html.Span(className='mr-2', children=[
                                    #         html.I(className='fas fa-square text-primary'),' This Month'
                                    #     ]),
                                    #     html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                                    # ])
                                ]),
                                html.Div(className='tab-pane', id='world_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                round(
                                                    df_covid_data['people_vaccinated_per_hundred'].dropna(how='any').mean(),
                                                    3),
                                                className='text-bold text-lg'),
                                            html.Span('Global Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(round(
                                                    df_covid_data['people_vaccinated_per_hundred'].sum(), 2),
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Global Avg Per Country', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', figure=fig_world_funnel_vaccine,
                                                  config=config)
                                    ])
                                    # html.Div(className='d-flex flex-row justify-content-end', children=[
                                    #     html.Span(className='mr-2', children=[
                                    #         html.I(className='fas fa-square text-primary'),' This Month'
                                    #     ]),
                                    #     html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                                    # ])
                                ])
                            ]),
                        ])
                    ])
                ])
            ])
        ])
    ])

])


# Updating the index callback


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/profile':
        return profile_page
    if pathname == '/':
        return covid_page


@app.callback(
    Output('continent_out_put', 'children'),
    [Input('continent_drop_down', 'value')]
)
def update_continent(value):
    # final_df = data.df_final[data.df_final['Country/Region'] == selected_coutry]
    # for i in final_df['Country/Region']():
    return 'You have selected {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
