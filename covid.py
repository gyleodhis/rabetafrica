import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from data import df_covid_data

covid_page333 = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Covid 19 Statistics')
                ]),
                html.Div(className='col-sm-6',children=[
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
                    html.Div(className='card card-primary card-outline', children=[
                        # Continent Dropdown menu
                        html.Div(className='dropdown', children=[
                            dcc.Dropdown(className='dropdown-menu', id='continent_drop_down',
                                         options=[{'label': i, 'value': i} for i in df_covid_data['location']],
                                         value='Kenya', multi=True),
                            html.Div(className='dropdown_item', id='continent_out_put')
                        ]),
                        # Country Drop Down
                        html.Div(className='dropdown', children=[
                            html.A('Select Country', className='dropdown-toggle', href='#', role='button',
                                   **{'data-toggle': 'dropdown', 'aria-haspopup': 'true', 'aria-expanded': 'false'}),
                            html.Div(className='dropdown-menu', children=[
                                html.A('Kenya', className='dropdown-item', href='#')
                            ])
                        ])
                    ]),
                ]),
                   html.Div(className='col-md-9', children=[
                       html.Div(className='row', children=[
                           html.Div(className='col-md-3', children=[
                               html.Div(className='small-box bg-info', children=[
                                   html.Div(className='inner', children=[
                                       html.H3(df_covid_data.iloc[25]['location'])
                                   ]),
                                   html.Div(className='icon', children=[
                                       html.I(className='ion ion-bag')
                                   ]),
                                   html.A('Total Cases:', className='small-box-footer', href='#'),
                                   html.A(df_covid_data.iloc[25]['total_cases'], className='small-box-footer',
                                          href='#'),
                                   html.I(className='fas fa-arrow-circle-right')
                               ])
                           ]),
                           html.Div(className='col-md-3', children=[
                               html.Div(className='small-box bg-success', children=[
                                   html.Div(className='inner', children=[
                                       html.H3(df_covid_data.iloc[25]['location'])
                                   ]),
                                   html.Div(className='icon', children=[
                                       html.I(className='ion ion-bars')
                                   ]),
                                   html.A('Total Tests:', className='small-box-footer', href='#'),
                                   html.A(df_covid_data.iloc[25]['total_tests'], className='small-box-footer',
                                          href='#'),
                                   html.I(className='fas fa-arrow-circle-right')
                               ])
                           ]),
                           html.Div(className='col-md-3', children=[
                               html.Div(className='small-box bg-danger', children=[
                                   html.Div(className='inner', children=[
                                       html.H3(df_covid_data.iloc[25]['location'])
                                   ]),
                                   html.Div(className='icon', children=[
                                       html.I(className='ion ion-pie-graph')
                                   ]),
                                   html.A('Total Deaths:', className='small-box-footer', href='#'),
                                   html.A(df_covid_data.iloc[25]['total_deaths'], className='small-box-footer',
                                          href='#'),
                                   html.I(className='fas fa-arrow-circle-right')
                               ])
                           ]),
                           html.Div(className='col-md-3', children=[
                               html.Div(className='small-box bg-warning', children=[
                                   html.Div(className='inner', children=[
                                       html.H3(df_covid_data.iloc[25]['location'])
                                   ]),
                                   html.Div(className='icon', children=[
                                       html.I(className='ion ion-bag')
                                   ]),
                                   html.A('Patients in ICU:', className='small-box-footer', href='#'),
                                   html.A(df_covid_data.iloc[25]['icu_patients'], className='small-box-footer',
                                          href='#'),
                                   html.I(className='fas fa-arrow-circle-right')
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
                                   html.H3('Africa Statistics', className='card-title')
                               ])
                           ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='d-flex', children=[
                                html.P(className='d-flex flex-column', children=[
                                    html.Span(2000, className='text-bold text-lg'),
                                    html.Span('Total Infections')
                                ]),
                                html.P(className='ml-auto d-flex flex-column text-right', children=[
                                    html.Span(className='text-success', children=[
                                        html.I(className='fas fa-arrow-down'),
                                        '12.5%'
                                    ]),
                                    html.Span('Since last month', className='text-muted')
                                ])
                            ]),
                            html.Div(className='position-relative mb-4', children=[
                                html.Canvas(height='200', children=[
                                    dcc.Graph(id = 'example_graph', figure=fig)
                                ])
                            ]),
                            html.Div(className='d-flex flex-row justify-content-end', children=[
                                html.Span(className='mr-2', children=[
                                    html.I(className='fas fa-square text-primary'),' This Month'
                                ]),
                                html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                            ])
                        ])
                       ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                           html.Div(className='card-header border-0', children=[
                               html.Div(className='d-flex justify-content-between', children=[
                                   html.H3('Africa Statistics', className='card-title')
                               ])
                           ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='d-flex', children=[
                                html.P(className='d-flex flex-column', children=[
                                    html.Span(2000, className='text-bold text-lg'),
                                    html.Span('Total Infections')
                                ]),
                                html.P(className='ml-auto d-flex flex-column text-right', children=[
                                    html.Span(className='text-success', children=[
                                        html.I(className='fas fa-arrow-down'),
                                        '12.5%'
                                    ]),
                                    html.Span('Since last month', className='text-muted')
                                ])
                            ]),
                            html.Div(className='position-relative mb-4', children=[
                                html.Canvas(height='200')
                                # 'Put Chart here'
                            ]),
                            html.Div(className='d-flex flex-row justify-content-end', children=[
                                html.Span(className='mr-2', children=[
                                    html.I(className='fas fa-square text-primary'),' This Month'
                                ]),
                                html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                            ])
                        ])
                       ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                           html.Div(className='card-header border-0', children=[
                               html.Div(className='d-flex justify-content-between', children=[
                                   html.H3('Africa Statistics', className='card-title')
                               ])
                           ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='d-flex', children=[
                                html.P(className='d-flex flex-column', children=[
                                    html.Span(2000, className='text-bold text-lg'),
                                    html.Span('Total Infections')
                                ]),
                                html.P(className='ml-auto d-flex flex-column text-right', children=[
                                    html.Span(className='text-success', children=[
                                        html.I(className='fas fa-arrow-down'),
                                        '12.5%'
                                    ]),
                                    html.Span('Since last month', className='text-muted')
                                ])
                            ]),
                            html.Div(className='position-relative mb-4', children=[
                                html.Canvas(height='200')
                                # 'Put Chart here'
                            ]),
                            html.Div(className='d-flex flex-row justify-content-end', children=[
                                html.Span(className='mr-2', children=[
                                    html.I(className='fas fa-square text-primary'),' This Month'
                                ]),
                                html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                            ])
                        ])
                       ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                           html.Div(className='card-header border-0', children=[
                               html.Div(className='d-flex justify-content-between', children=[
                                   html.H3('Africa Statistics', className='card-title')
                               ])
                           ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='d-flex', children=[
                                html.P(className='d-flex flex-column', children=[
                                    html.Span(2000, className='text-bold text-lg'),
                                    html.Span('Total Infections')
                                ]),
                                html.P(className='ml-auto d-flex flex-column text-right', children=[
                                    html.Span(className='text-success', children=[
                                        html.I(className='fas fa-arrow-down'),
                                        '12.5%'
                                    ]),
                                    html.Span('Since last month', className='text-muted')
                                ])
                            ]),
                            html.Div(className='position-relative mb-4', children=[
                                html.Canvas(height='200')
                                # 'Put Chart here'
                            ]),
                            html.Div(className='d-flex flex-row justify-content-end', children=[
                                html.Span(className='mr-2', children=[
                                    html.I(className='fas fa-square text-primary'),' This Month'
                                ]),
                                html.Span(children=[html.I(className='fas fa-square text-gray'), ' Last Moth'])
                            ])
                        ])
                       ])
                ])
            ])
        ])
    ])

])