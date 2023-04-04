import dash
from dash import html, dcc
import controller.my_functions as mf
import controller.loadcereal as lc

dash.register_page(__name__,path='/cereals',name='Cereal Productions',title='Rabet',image_url='assets/img/site_meta.jpeg',
                   description='Africa\'s  Cereal production in metric tonnes')
config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Africa\'s Cereal Production')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Cereal Production', className='breadcrumb-item active')
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
                        html.Div(className='col-md-3 col-sm-6', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4('Entire Continent'),
                                    html.P('%s%s'%((lc.df_getcereals['YR2021'].sum()/1000000).round(2),'M Tones'))
                                ]),
                                html.A('Emissions in 2019',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3 col-sm-6', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4(lc.df_getcereals['Country'].iloc[0]),
                                    html.P('%s%s'%((lc.df_getcereals['YR2021'].iloc[0]/1000000).round(2),'M Tones'))
                                ]),
                                html.A('Highest Producer',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3 col-sm-6', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4(lc.df_getcereals['Country'].iloc[1]),
                                    html.P('%s%s'%((lc.df_getcereals['YR2021'].iloc[1]/1000000).round(2),'M Tones'))
                                ]),
                                html.A('2nd Highest Producer',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3 col-sm-6', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4(lc.df_getcereals['Country'].iloc[-3]),
                                    html.P('%s%s'%(lc.df_getcereals['YR2021'].iloc[-3],'M Tones'))
                                ]),
                                html.A('Least Producer',className='small-box-footer', href='#')
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
                                html.H3('Production by Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item', children=html.A('Top 15', className='nav-link active',
                                                                                      href='#topl',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Others', className='nav-link',
                                                                                      href='#topg',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='topl', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('1962 - 2021 Comparison',
                                                      className='text-bold text-lg')
                                            # html.Span('Countries Increasing Emissions')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I('%s%s' %(mf.round_up((lc.get_first_last()['YR2021'].head(14).mean())/1000000,2), 'M Tones'),
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Average Production', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=dcc.Graph(figure=lc.cereal_scatter(), config=config))
                                    ])]),
                                html.Div(className='tab-pane', id='topg', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('1961 - 2021 Comparison',className='text-bold text-lg')
                                            # html.Span('Average Production')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I('%s%s' %(mf.round_up((lc.get_first_last()['YR2021'].tail(40).mean())/1000000,2),'M Tones'),
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Highest Reducer', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=dcc.Graph(figure=lc.cereal_scatter(2), config=config))
                                    ])])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])