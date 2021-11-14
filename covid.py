import dash_html_components as html
import dash_core_components as dcc
from charts import covid_vaccine_treemap,config

covid_vax_page = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Covid 19 Vaccinations')
                ]),
                html.Div(className='col-sm-6',children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Vaccine', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            # The fow for cumulative figures
            html.Div(className='row', children=[
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span('Mordana', className='info-box-text'),
                            html.Span('1235', className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span('Pferzer', className='info-box-text'),
                            html.Span('34637', className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span('Johnson', className='info-box-text'),
                            html.Span('567', className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span('Sputnic', className='info-box-text'),
                            html.Span('1235', className='info-box-number')
                        ])
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row',children=[
                html.Div(className='col-md-12',children=[
                    html.Div(className='card',children=[
                        html.Div(className='card-header',children=[
                            html.H5('Monthly Recap Report', className='card-title')
                        ]),
                        html.Div(className='card-body',children=[
                            html.Div(className='row',children=[
                                html.Div(className='col-md-8',children=[
                                    html.P( className='text-center',children=[html.Strong('Month on Month Vaccinations')]),
                                    html.Div(className='position-relative', children=[
                                        dcc.Graph(figure=covid_vaccine_treemap(), config=config)
                                    ])
                                ]),
                                html.Div(className='col-md-4',children=[
                                    html.P(className='text-center',children=[html.Strong('Vaccine Type')]),
                                    html.Div(className='progress-group',children=[
                                        html.Span('Mordana'),
                                        html.Span('30 %',className='float-right'),
                                        html.Div(className='progress progress-sm',children=[
                                            html.Div(className='progress-bar bg-primary', style={'width': '30%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group',children=[
                                        html.Span('Pfizer'),
                                        html.Span('25 %',className='float-right'),
                                        html.Div(className='progress progress-sm',children=[
                                            html.Div(className='progress-bar bg-success', style={'width': '25%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group',children=[
                                        html.Span('Johnson'),
                                        html.Span('15 %',className='float-right'),
                                        html.Div(className='progress progress-sm',children=[
                                            html.Div(className='progress-bar bg-warning', style={'width': '15%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group',children=[
                                        html.Span('AstraZeneca'),
                                        html.Span('10 %',className='float-right'),
                                        html.Div(className='progress progress-sm',children=[
                                            html.Div(className='progress-bar bg-warning', style={'width': '10%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group',children=[
                                        html.Span('Sputnic V'),
                                        html.Span('10 %',className='float-right'),
                                        html.Div(className='progress progress-sm',children=[
                                            html.Div(className='progress-bar bg-danger', style={'width': '10%'})
                                        ])
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-footer',children=[
                            html.P(className='text-center',children=[html.Strong('This Month vs Last Month')]),
                            html.Div(className='row',children=[
                                html.Div(className='col-sm-3 col-6',children=[
                                    html.Div(className='description-block border-right',children=[
                                        html.Span(className='description-percentage text-success',children=[
                                            html.I('17%', className='fas fa-caret-up'),
                                        ]),
                                        html.H5('3,521', className='description-header'),
                                        html.Span('Moderna', className='description-header')
                                    ])
                                ]),
                                html.Div(className='col-sm-3 col-6',children=[
                                    html.Div(className='description-block border-right',children=[
                                        html.Span(className='description-percentage text-danger',children=[
                                            html.I('-23%', className='fas fa-caret-down'),
                                        ]),
                                        html.H5('1,675', className='description-header'),
                                        html.Span('AstraZeneca', className='description-header')
                                    ])
                                ]),
                                html.Div(className='col-sm-3 col-6',children=[
                                    html.Div(className='description-block border-right',children=[
                                        html.Span(className='description-percentage text-info',children=[
                                            html.I('20%', className='fas fa-caret-up'),
                                        ]),
                                        html.H5('4,751', className='description-header'),
                                        html.Span('Pfizer', className='description-header')
                                    ])
                                ]),
                                html.Div(className='col-sm-3 col-6',children=[
                                    html.Div(className='description-block border-right',children=[
                                        html.Span(className='description-percentage text-warning',children=[
                                            html.I('02%', className='fas fa-caret-up'),
                                        ]),
                                        html.H5('600', className='description-header'),
                                        html.Span('Sputnic V', className='description-header')
                                    ])
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])