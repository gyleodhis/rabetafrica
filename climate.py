from dash import html,dcc
from climate_data import emissions_by_sctor as es
from climate_data import last_two_decades_emissions as ld
from climate_data import fig_corbon_line

config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}
carbon_page = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Carbon Dioxide Emissions')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Carbon', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            html.H5('Highest Carbon Dioxide Emitters', className='mt-4 mb-2'),
            html.Div(className='row',children=[
                html.Div(className='col-md-3 col-sm-6 col-12',children=[
                    html.Div(className='info-box bg-info',children=[
                        html.Span(className='info-box-icon',children=[
                            html.I(className='fas fa-cogs')
                        ]),
                        html.Div(className='info-box-content',children=[
                            html.Span(es().index[-1],className='info-box-text'),
                            html.Span('%s%s of total' %(es()['Percentage'][-1],'%'),className='nfo-box-number'),
                            html.Div(className='progress',children=[
                                html.Div(className='progress-bar',style={'width':es()['Percentage'][-1]})
                            ]),
                            html.Div('%s%s change in 30 years' %(ld()['% Change'][4],'%'),
                                     className='progress-description')
                        ])
                    ])
                ]),
                html.Div(className='col-md-3 col-sm-6 col-12',children=[
                    html.Div(className='info-box bg-warning',children=[
                        html.Span(className='info-box-icon',children=[
                            html.I(className='fas fa-broadcast-tower')
                        ]),
                        html.Div(className='info-box-content',children=[
                            html.Span(es().index[-2],className='info-box-text'),
                            html.Span('%s%s of total' %(es()['Percentage'][-2],'%'),className='nfo-box-number'),
                            html.Div(className='progress',children=[
                                html.Div(className='progress-bar',style={'width':es()['Percentage'][-2]})
                            ]),
                            html.Div('%s%s change in 30 years' %(abs(ld()['% Change'][-4]),'%'),
                                     className='progress-description')
                        ])
                    ])
                ]),
                html.Div(className='col-md-3 col-sm-6 col-12',children=[
                    html.Div(className='info-box bg-success',children=[
                        html.Span(className='info-box-icon',children=[
                            html.I(className='fas fa-bus')
                        ]),
                        html.Div(className='info-box-content',children=[
                            html.Span(es().index[-3],className='info-box-text'),
                            html.Span('%s%s of total' %(es()['Percentage'][-3],'%'),className='nfo-box-number'),
                            html.Div(className='progress',children=[
                                html.Div(className='progress-bar',style={'width':es()['Percentage'][-3]})
                            ]),
                            html.Div('%s%s change in 30 years' %(ld()['% Change'][2],'%'),
                                     className='progress-description')
                        ])
                    ])
                ]),
                html.Div(className='col-md-3 col-sm-6 col-12',children=[
                    html.Div(className='info-box bg-danger',children=[
                        html.Span(className='info-box-icon',children=[
                            html.I(className='fas fa-industry')
                        ]),
                        html.Div(className='info-box-content',children=[
                            html.Span(es().index[-4],className='info-box-text'),
                            html.Span('%s%s of total' %(es()['Percentage'][-4],'%'),className='nfo-box-number'),
                            html.Div(className='progress',children=[
                                html.Div(className='progress-bar',style={'width':es()['Percentage'][-4]})
                            ]),
                            html.Div('%s%s change in 30 years' %(ld()['% Change'][-2],'%'),
                                     className='progress-description')
                        ])
                    ])
                ])
            ]),
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header', children=[
                            html.P(className='text-center',children=[
                                html.Strong('Emissions Over Time')
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='row', children=[
                                html.Div(className='col-md-12',children=[
                                    dcc.Graph(figure=fig_corbon_line(), config=config)
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])
