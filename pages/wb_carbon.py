import dash
from dash import html, dcc
import controller.my_functions as mf
from controller.loadcarbon import df_getCo2Emission,new_c02increase,fig_carbon_line,fig_c02_bar,fig_c02_gain_bar

dash.register_page(__name__,path='/carbon',name='Carbon Emissions',title='Rabet',image_url='assets/img/site_meta.jpeg',
                   description='Africa carbon emission stats. As directly reported World Bank. Rabet Analytics platform')
config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Africa\'s Carbon Emission')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Carbon Emission', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4('Entire Continent'),
                                    html.P('%s %s'%(df_getCo2Emission['YR2019'].iloc[0],'Tones'))
                                ]),
                                html.A('Emissions in 2019',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_getCo2Emission['Country'].iloc[0]),
                                    html.P('%s %s'%(df_getCo2Emission['YR2019'].iloc[1],'Tones'))
                                ]),
                                html.A('Highest Emitter',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-lime', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_getCo2Emission['Country'].iloc[-1]),
                                    html.P('%s %s'%(df_getCo2Emission['YR2019'].iloc[-1],'Tones'))
                                ]),
                                # html.Div(className='icon',children=[
                                #     html.Img(className='ion ion-bag',src='https://flagcdn.com/w40/ga.png')
                                # ]),
                                html.A('Highest Emitter',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-lime', children=[
                                html.Div(className='inner', children=[
                                    html.H4(new_c02increase['Country'].iloc[0]),
                                    html.P('%s %s'%(abs(new_c02increase['Diff_Gain'].iloc[0]),'Tones'))
                                ]),
                                # html.Div(className='icon',children=[
                                #     html.Img(className='ion ion-bag',src='https://flagcdn.com/w40/ga.png')
                                # ]),
                                html.A('Highest Increase in 18 Yrs',className='small-box-footer', href='#')
                            ])
                        ])
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Average', className='nav-link',
                                                                href='#avg', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Increasing', className='nav-link active',
                                                                                      href='#topl',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Decreasing', className='nav-link',
                                                                                      href='#topg',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='tab-pane', id='avg', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('18 Year Progression',className='text-bold text-lg')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I('%s %s'%(df_getCo2Emission['Diff_Gain'].iloc[0],'Tones'), className='fas fa-arrow-down')
                                            ]),
                                            html.Span('Total Decrease', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=dcc.Graph(figure=fig_carbon_line(), config=config))
                                    ])]),
                                html.Div(className='active tab-pane', id='topl', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('2003 - 2020 Comparison',
                                                      className='text-bold text-lg'),
                                            html.Span('Countries Increasing Emissions')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I('%s %s' %(new_c02increase['Diff_Gain'].iloc[1],'Tones'),className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Highest Increase', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=dcc.Graph(figure=fig_c02_bar(), config=config))
                                    ])]),
                                html.Div(className='tab-pane', id='topg', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('2003 - 2020 Comparison',className='text-bold text-lg'),
                                            html.Span('Countries Reducing Emissions')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I('%s %s' %(new_c02increase['Diff_Gain'].iloc[-1]*-1,'Tones'),
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Highest Reducer', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=dcc.Graph(figure=fig_c02_gain_bar(), config=config))
                                    ])])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])