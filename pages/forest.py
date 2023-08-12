import dash
from dash import html, dcc
import controller.my_functions as mf
from controller.loadforest import df_PctForestArea,df_percentlost,fig_forest_line,fig_forest_bar,fig_forest_gain_bar
from controller.forest_ag import forest_table

dash.register_page(__name__,path='/forestcover',name='Forest Cover',title='Rabet',image_url='assets/img/site_meta.jpeg',
                   description='Africa forest cover statistics. As directly reported world bank. Rabet Analytics platform')
config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Africa\'s Forest Cover')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Forest', className='breadcrumb-item active')
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
                                    html.P('%s%%'%mf.round_up(df_PctForestArea['YR2020'].iloc[19],2))
                                ]),
                                html.A('Current Forest cover',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3 col-sm-6', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_PctForestArea['Country'].iloc[0]),
                                    html.P('%s%%'%mf.round_up(df_PctForestArea['YR2020'].iloc[0],2))
                                ]),
                                html.A('Most Covered Country',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3 col-sm-6', children=[
                            html.Div(className='small-box bg-lime', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_PctForestArea['Country'].iloc[-1]),
                                    html.P('%s%%'%mf.round_up(df_PctForestArea['YR2020'].iloc[-1],2))
                                ]),
                                # html.Div(className='icon',children=[
                                #     html.Img(className='ion ion-bag',src='https://flagcdn.com/w40/ga.png')
                                # ]),
                                html.A('Least Covered Country',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3 col-sm-6', children=[
                            html.Div(className='small-box bg-lime', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_percentlost['Country'].iloc[0]),
                                    html.P('%s%%'%mf.round_up(df_percentlost['Pct_Lost'].iloc[0],2))
                                ]),
                                # html.Div(className='icon',children=[
                                #     html.Img(className='ion ion-bag',src='https://flagcdn.com/w40/ga.png')
                                # ]),
                                html.A('Highest Loss in 18 Yrs',className='small-box-footer', href='#')
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
                                        html.Li(className='nav-item', children=html.A('Losers', className='nav-link active',
                                                                                      href='#topl',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Gainers', className='nav-link',
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
                                            html.Span(className='text-danger', children=[
                                                html.I('%s%%'%mf.round_up(df_PctForestArea['Pct_Lost'].iloc[19],2), className='fas fa-arrow-down')
                                            ]),
                                            html.Span('Pct Lost by the continent', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=dcc.Graph(figure=fig_forest_line(), config=config))
                                    ])]),
                                html.Div(className='active tab-pane', id='topl', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('2003 - 2020 Comparison',
                                                      className='text-bold text-lg'),
                                            html.Span('Countries Loosing cover')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I('%s%%'%mf.round_up(df_percentlost['Pct_Lost'].iloc[0],2),className='fas fa-arrow-down')
                                            ]),
                                            html.Span('Highest Looser', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=dcc.Graph(figure=fig_forest_bar(), config=config))
                                    ])]),
                                html.Div(className='tab-pane', id='topg', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('2003 - 2020 Comparison',className='text-bold text-lg'),
                                            html.Span('Countries Increasing Cover')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I('%s%%'%mf.round_up(df_percentlost['Pct_Lost'].iloc[-2]*-1,2),
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Highest Gainer', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=dcc.Graph(figure=fig_forest_gain_bar(), config=config))
                                    ])])
                            ])
                        ])
                    ])
                ])
            ]),
            #Forest land table
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Percentage Cover Year on Year', className='card-title')
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', children=[
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=html.Div(forest_table))
                                    ])] )
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])