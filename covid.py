from dash import html,dcc
from charts import *

covid_vax_page = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Covid 19 Vaccinations: Top 4 Months')
                ]),
                html.Div(className='col-sm-6', children=[
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
            # The row for top 5 months with highest vaccinations
            html.Div(className='row', children=[
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span(df_this_month()['Month'].iloc[0], className='info-box-text'),
                            html.Span(df_this_month()['pcnt_vaccination'].iloc[0].astype(str) + ' %', className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span(df_this_month()['Month'].iloc[1], className='info-box-text'),
                            html.Span(df_this_month()['pcnt_vaccination'].iloc[1].astype(str) + ' %', className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span(df_this_month()['Month'].iloc[2], className='info-box-text'),
                            html.Span(df_this_month()['pcnt_vaccination'].iloc[2].astype(str) + ' %', className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-12 col-sm-6 col-md-3', children=[
                    html.Div(className='info-box', children=[
                        html.Span(className='info-box-icon bg-info elevation-1', children=[
                            html.I(className='fas fa-users')
                        ]),
                        html.Div(className='info-box-content', children=[
                            html.Span(df_this_month()['Month'].iloc[3], className='info-box-text'),
                            html.Span(df_this_month()['pcnt_vaccination'].iloc[3].astype(str) + ' %', className='info-box-number')
                        ])
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header', children=[
                            html.H5('Monthly Recap Report', className='card-title')
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='row', children=[
                                html.Div(className='col-md-8', children=[
                                    html.P(className='text-center',
                                           children=[html.Strong('Vaccine Administration by Percentage')]),
                                    html.Div(className='position-relative', children=[
                                        dcc.Graph(figure=fig_bar_vax(), config=config)
                                    ])
                                ]),
                                html.Div(className='col-md-4', children=[
                                    html.P(className='text-center', children=[html.Strong('Vaccine Type')]),
                                    html.Div(className='progress-group', children=[
                                        html.Span(pct_vaccination()['vaccine'].iloc[0]),
                                        html.Span(pct_vaccination()['pcnt_vaccination'].iloc[0].astype(str) + ' %',
                                                  className='float-right'),
                                        html.Div(className='progress progress-sm', children=[
                                            html.Div(className='progress-bar bg-success',
                                                     style={
                                                         'width': pct_vaccination()['pcnt_vaccination'].iloc[0].astype(
                                                             str) + '%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group', children=[
                                        html.Span(pct_vaccination()['vaccine'].iloc[1]),
                                        html.Span(pct_vaccination()['pcnt_vaccination'].iloc[1].astype(str) + ' %',
                                                  className='float-right'),
                                        html.Div(className='progress progress-sm', children=[
                                            html.Div(className='progress-bar bg-primary',
                                                     style={
                                                         'width': pct_vaccination()['pcnt_vaccination'].iloc[1].astype(
                                                             str) + '%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group', children=[
                                        html.Span(pct_vaccination()['vaccine'].iloc[2]),
                                        html.Span(pct_vaccination()['pcnt_vaccination'].iloc[2].astype(str) + ' %',
                                                  className='float-right'),
                                        html.Div(className='progress progress-sm', children=[
                                            html.Div(className='progress-bar bg-warning',
                                                     style={
                                                         'width': pct_vaccination()['pcnt_vaccination'].iloc[2].astype(
                                                             str) + '%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group', children=[
                                        html.Span(pct_vaccination()['vaccine'].iloc[3]),
                                        html.Span(pct_vaccination()['pcnt_vaccination'].iloc[3].astype(str) + ' %',
                                                  className='float-right'),
                                        html.Div(className='progress progress-sm', children=[
                                            html.Div(className='progress-bar bg-danger',
                                                     style={
                                                         'width': pct_vaccination()['pcnt_vaccination'].iloc[3].astype(
                                                             str) + '%'})
                                        ])
                                    ]),
                                    html.Div(className='progress-group', children=[
                                        html.Span(pct_vaccination()['vaccine'].iloc[4]),
                                        html.Span(pct_vaccination()['pcnt_vaccination'].iloc[4].astype(str) + ' %',
                                                  className='float-right'),
                                        html.Div(className='progress progress-sm', children=[
                                            html.Div(className='progress-bar bg-danger',
                                                     style={
                                                         'width': pct_vaccination()['pcnt_vaccination'].iloc[4].astype(
                                                             str) + '%'})])])
                                ])
                            ])
                            # """I DO NOT NEED TREEMAP. IT WASTES ALOT OF COMPUTE RESOURCES"""
                            # html.Div(className='row', children=[
                            #     html.Div(className='col-md-12', children=[
                            #         html.P(className='text-center',
                            #                children=[html.Strong('Month on Month Vaccinations')]),
                            #         html.Div(className='position-relative', children=[
                            #             dcc.Graph(figure=covid_vaccine_treemap(), config=config)
                            #         ])
                            #     ])
                            # ])
                        ]),
                        html.Div(className='card-footer', children=[
                            html.P(className='text-center', children=[html.Strong('This Month vs Last Month')]),
                            html.Div(className='row', children=[
                                html.Div(className='col-sm-3 col-6', children=[
                                    html.Div(className='description-block border-right', children=[
                                        html.Span(className='description-percentage text-success', children=[
                                            html.I(last_two_months_diff(), className='fas fa-caret-up'),
                                        ]),
                                        # html.H5('3,521', className='description-header'),
                                        html.Div('Moderna', className='description-header')
                                    ])
                                ]),
                                html.Div(className='col-sm-3 col-6', children=[
                                    html.Div(className='description-block border-right', children=[
                                        html.Span(className='description-percentage text-danger', children=[
                                            html.I(last_two_months_diff('Oxford/AstraZeneca'), className='fas fa-caret-down'),
                                        ]),
                                        # html.H5('1,675', className='description-header'),
                                        html.Div('Oxford/AstraZeneca', className='description-header')
                                    ])
                                ]),
                                html.Div(className='col-sm-3 col-6', children=[
                                    html.Div(className='description-block border-right', children=[
                                        html.Span(className='description-percentage text-info', children=[
                                            html.I(last_two_months_diff('Pfizer/BioNTech'), className='fas fa-caret-up'),
                                        ]),
                                        # html.H5('4,751', className='description-header'),
                                        html.Div('Pfizer/BioNTech', className='description-header')
                                    ])
                                ]),
                                html.Div(className='col-sm-3 col-6', children=[
                                    html.Div(className='description-block border-right', children=[
                                        html.Span(className='description-percentage text-warning', children=[
                                            html.I(last_two_months_diff('Johnson&Johnson'), className='fas fa-caret-up'),
                                        ]),
                                        # html.H5('600', className='description-header'),
                                        html.Div('Johnson&Johnson', className='description-header')
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
