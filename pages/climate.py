import dash
from dash import html,dcc
import dash_daq as daq
from controller.climate_data import emissions_by_sctor as es
from controller.climate_data import last_two_decades_emissions as ld
from controller.climate_data import fig_corbon_line,emission_by_continent

dash.register_page(__name__,path='/climate',name='Climate',title='Rabet',image_url='assets/img/site_meta.jpeg',
                   description='Greenhouse gases contribute significantly to global warming.'
                               'Here I analyze the highest emitters. Climate analytics with Rabet Africa')
config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}
layout = html.Div([
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
                    html.Div(className='info-box bg-success',children=[
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
                    html.Div(className='info-box bg-success',children=[
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
                    html.Div(className='info-box bg-lime',children=[
                        html.Span(className='info-box-icon',children=[
                            html.I(className='fa fa-building')
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
                    html.Div(className='info-box bg-lime',children=[
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
                        html.Div(className='card-header p-2', children=[
                            html.Ul(className='nav nav-pills',children=[
                                html.Li(className='nav-item',children=[
                                    html.A('Emissions Over Time',className='nav-link active',
                                           href='#emission', **{'data-toggle': 'tab'})
                                ]),
                                html.Li(className='nav-item',children=[
                                    html.A('Key Emissions',className='nav-link',
                                           href='#keyemissions', **{'data-toggle': 'tab'})
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='row', children=[
                                html.Div(className='col-md-12',children=[
                                    html.Div(className='tab-content',children=[
                                        html.Div(className='active tab-pane', id='emission',children=[
                                            dcc.Graph(figure=fig_corbon_line(), config=config)
                                        ]),
                                        html.Div(className='tab-pane',id='keyemissions',children=[
                                                html.Div(className='timeline timeline-inverse',children=[
                                                    html.Div(className='time-label',children=[
                                                        html.Span('Energy:',className='bg-danger')
                                                    ]),
                                                    html.Div(className='row',children=[
                                                        html.I(className='fas fa-cogs bg-primary'),
                                                        html.Div(className='timeline-item col-md-7',children=[
                                                            html.Span(className='time',children=[
                                                                html.I(' 1990 - 2015',className='far fa-clock')
                                                            ]),
                                                            html.H3('Emissions of 25 years',className='timeline-header'),
                                                            html.Div(className='timeline-body',children=[
                                                                dcc.Graph(id='graph', config=config),
                                                                # dcc.RadioItems(['Africa','Asia','Europe','North America','Oceania','South America'],
                                                                #                value='Africa',id='region',className='custom-radio')
                                                            ])
                                                        ]),
                                                        html.Div(className='timeline-item col-md-3',children=[
                                                            html.H3('Total per continent : ',className='timeline-header'),
                                                            html.Div(className='timeline-body',children=[
                                                                daq.Thermometer(id='thermo',min=100,max=2000,value=emission_by_continent(),
                                                                                showCurrentValue=True,units="Tones")
                                                            ])
                                                        ]),
                                                        html.Div(className='timeline-item col-md-11',children=[
                                                            html.Div(className='timeline-body',children=[
                                                                dcc.RadioItems(['Africa','Asia','Europe','North America','Oceania','South America'],
                                                                               value='Africa',id='region',inputStyle={'margin': '10px'})
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
                ])
            ])
        ])
    ])

])