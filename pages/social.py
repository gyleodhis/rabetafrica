import dash
from dash import html
from datetime import date as dt
from controller.tweets import df_getTopTweets, df_getTopAccount,df_getNegativeTweets,df_getLocations,df_getDevice,getSummary

dash.register_page(__name__,path='/social',name='Twitter',title='Rabet',image_url='assets/img/site_meta.jpeg',
                   description='Social media analytics with Rabet Africa')
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Tweets About: King Charles III Coronation')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Twitter', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row',children=[
                html.Div(className='col-12 col-sm-6 col-md-3',children=[
                    html.Div(className='info-box',children=[
                        html.Span(className='info-box-icon bg-success elevation-1',children=[
                            html.I(className='fa fa-download')]),
                        html.Div(className='info-box-content',children=[
                            html.Span('Downloaded Tweets',className='info-box-text'),
                            html.Span(getSummary('ttl'),className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-sm-6 col-md-3',children=[
                    html.Div(className='info-box',children=[
                        html.Span(className='info-box-icon bg-success elevation-1',children=[
                            html.I(className='fa fa-eye')]),
                        html.Div(className='info-box-content',children=[
                            html.Span('Total Interactions',className='info-box-text'),
                            html.Span(getSummary('ttl2'),className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-sm-6 col-md-3',children=[
                    html.Div(className='info-box',children=[
                        html.Span(className='info-box-icon bg-danger elevation-1',children=[
                            html.I(className='fa fa-thumbs-down')]),
                        html.Div(className='info-box-content',children=[
                            html.Span('Negative Tweets',className='info-box-text'),
                            html.Span(6,className='info-box-number')
                        ])
                    ])
                ]),
                html.Div(className='col-sm-6 col-md-3',children=[
                    html.Div(className='info-box',children=[
                        html.Span(className='info-box-icon bg-warning elevation-1',children=[
                            html.I(className='fa fa-spinner fa-spin fa-pulse')]),
                        html.Div(className='info-box-content',children=[
                            html.Span('Last Live Stream',className='info-box-text'),
                            html.Span( '2023-09-25',className='info-box-number')
                        ])
                    ])
                ])
            ]),# The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='card',children=[
                        html.Div(className='card-header border-0',children=[
                            html.Div(className='d-flex justify-content-between',children=[
                                html.H3('Major Tweet Locations', className='card-title'),
                                html.Div(className='card-tools',children=[
                                    html.Button(className='btn btn-tool',type='button',
                                                **{'data-card-widget':'collapse'},children=[
                                            html.I(className='fas fa-minus')
                                        ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body',children=[
                            html.Div(className='progress-group',children=[
                                html.Span(df_getLocations['Location'].iloc[0]),
                                html.Span(df_getLocations['df_pct'].iloc[0].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-success',
                                             style={'width': df_getLocations['df_pct'].iloc[0].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getLocations['Location'].iloc[1]),
                                html.Span(df_getLocations['df_pct'].iloc[1].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-success',
                                             style={'width': df_getLocations['df_pct'].iloc[1].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getLocations['Location'].iloc[2]),
                                html.Span(df_getLocations['df_pct'].iloc[2].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-olive',
                                             style={'width': df_getLocations['df_pct'].iloc[2].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getLocations['Location'].iloc[3]),
                                html.Span(df_getLocations['df_pct'].iloc[3].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-olive',
                                             style={'width': df_getLocations['df_pct'].iloc[3].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getLocations['Location'].iloc[4]),
                                html.Span(df_getLocations['df_pct'].iloc[4].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-lime',
                                             style={'width': df_getLocations['df_pct'].iloc[4].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getLocations['Location'].iloc[5]),
                                html.Span(df_getLocations['df_pct'].iloc[5].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-lime',
                                             style={'width': df_getLocations['df_pct'].iloc[5].astype(
                                                     str) + '%'})
                                ])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card',children=[
                        html.Div(className='card-header border-0',children=[
                            html.Div(className='d-flex justify-content-between',children=[
                                html.H3('Major Devices', className='card-title'),
                                html.Div(className='card-tools',children=[
                                    html.Button(className='btn btn-tool',type='button',
                                                **{'data-card-widget':'collapse'},children=[
                                            html.I(className='fas fa-minus')
                                        ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body',children=[
                            html.Div(className='progress-group',children=[
                                html.Span(df_getDevice['Device'].iloc[0]),
                                html.Span(df_getDevice['df_pct'].iloc[0].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-black',
                                             style={'width': df_getDevice['df_pct'].iloc[0].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getDevice['Device'].iloc[1]),
                                html.Span(df_getDevice['df_pct'].iloc[1].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-black',
                                             style={'width': df_getDevice['df_pct'].iloc[1].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getDevice['Device'].iloc[2]),
                                html.Span(df_getDevice['df_pct'].iloc[2].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-gray-dark',
                                             style={'width': df_getDevice['df_pct'].iloc[2].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getDevice['Device'].iloc[3]),
                                html.Span(df_getDevice['df_pct'].iloc[3].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-gray-dark',
                                             style={'width': df_getDevice['df_pct'].iloc[3].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getDevice['Device'].iloc[4]),
                                html.Span(df_getDevice['df_pct'].iloc[4].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-gray',
                                             style={'width': df_getDevice['df_pct'].iloc[4].astype(
                                                     str) + '%'})
                                ])
                            ]),
                            html.Div(className='progress-group',children=[
                                html.Span(df_getDevice['Device'].iloc[5]),
                                html.Span(df_getDevice['df_pct'].iloc[5].astype(str) + ' %',
                                          className='float-right'),
                                html.Div(className='progress progress-sm', children=[
                                    html.Div(className='progress-bar bg-gray',
                                             style={'width': df_getDevice['df_pct'].iloc[5].astype(
                                                     str) + '%'})
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            html.Div(className='row', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='card direct-chat direct-chat-warning', children=[
                        html.Div(className='card-header', children=[
                            # html.H3('Top Tweets',className='card-title'),
                            html.Div(className='card-tools', children=[
                                html.Ul(className='nav nav-pills ml-auto', children=[
                                    html.Li(className='nav-item',
                                            children=html.A('Most Engaged', className='nav-link active',
                                                            href='#top5', **{'data-toggle': 'tab'})),
                                    html.Li(className='nav-item',
                                            children=html.A('Most Negative', className='nav-link',
                                                            href='#neg5',**{'data-toggle': 'tab'}))
                                ])
                                # html.Span('5',className='badge badge-info',title='Top 5 Tweets')
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='top5', children=[
                                    html.Div(className='direct-chat-messages', children=[
                                        html.Div(className='direct-chat-msg', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getTopTweets.iloc[0]['Author'],
                                                          className='direct-chat-name float-left'),
                                                html.Span(df_getTopTweets.iloc[0]['Tweet Date'],
                                                          className='direct-chat-timestamp float-right')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getTopTweets.iloc[0]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getTopTweets.iloc[0]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getTopTweets.iloc[0]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg right', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getTopTweets.iloc[1]['Author'],
                                                          className='direct-chat-name float-right'),
                                                html.Span(df_getTopTweets.iloc[1]['Tweet Date'],
                                                          className='direct-chat-timestamp float-left')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getTopTweets.iloc[1]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getTopTweets.iloc[1]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getTopTweets.iloc[1]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getTopTweets.iloc[2]['Author'],
                                                          className='direct-chat-name float-left'),
                                                html.Span(df_getTopTweets.iloc[2]['Tweet Date'],
                                                          className='direct-chat-timestamp float-right')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getTopTweets.iloc[2]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getTopTweets.iloc[2]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getTopTweets.iloc[2]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg right', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getTopTweets.iloc[3]['Author'],
                                                          className='direct-chat-name float-right'),
                                                html.Span(df_getTopTweets.iloc[3]['Tweet Date'],
                                                          className='direct-chat-timestamp float-left')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getTopTweets.iloc[3]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getTopTweets.iloc[3]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getTopTweets.iloc[3]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getTopTweets.iloc[4]['Author'],
                                                          className='direct-chat-name float-left'),
                                                html.Span(df_getTopTweets.iloc[4]['Tweet Date'],
                                                          className='direct-chat-timestamp float-right')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getTopTweets.iloc[4]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getTopTweets.iloc[4]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getTopTweets.iloc[4]['Retweets'])
                                        ])
                                    ])]),
                                html.Div(className='tab-pane', id='neg5', children=[
                                    html.Div(className='direct-chat-messages', children=[
                                        html.Div(className='direct-chat-msg', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getNegativeTweets.iloc[0]['Author'],
                                                          className='direct-chat-name float-left'),
                                                html.Span(df_getNegativeTweets.iloc[0]['Tweet Date'],
                                                          className='direct-chat-timestamp float-right')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getNegativeTweets.iloc[0]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getNegativeTweets.iloc[0]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getNegativeTweets.iloc[0]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg right', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getNegativeTweets.iloc[1]['Author'],
                                                          className='direct-chat-name float-right'),
                                                html.Span(df_getNegativeTweets.iloc[1]['Tweet Date'],
                                                          className='direct-chat-timestamp float-left')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getNegativeTweets.iloc[1]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getNegativeTweets.iloc[1]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getNegativeTweets.iloc[1]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getNegativeTweets.iloc[2]['Author'],
                                                          className='direct-chat-name float-left'),
                                                html.Span(df_getNegativeTweets.iloc[2]['Tweet Date'],
                                                          className='direct-chat-timestamp float-right')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getNegativeTweets.iloc[2]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getNegativeTweets.iloc[2]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getNegativeTweets.iloc[2]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg right', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getNegativeTweets.iloc[3]['Author'],
                                                          className='direct-chat-name float-right'),
                                                html.Span(df_getNegativeTweets.iloc[3]['Tweet Date'],
                                                          className='direct-chat-timestamp float-left')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getNegativeTweets.iloc[3]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getNegativeTweets.iloc[3]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getNegativeTweets.iloc[3]['Retweets'])
                                        ]),
                                        html.Div(className='direct-chat-msg', children=[
                                            html.Div(className='direct-chat-infos clearfix', children=[
                                                html.Span(df_getNegativeTweets.iloc[4]['Author'],
                                                          className='direct-chat-name float-left'),
                                                html.Span(df_getNegativeTweets.iloc[4]['Tweet Date'],
                                                          className='direct-chat-timestamp float-right')
                                            ]),
                                            html.Img(className='direct-chat-img', src=df_getNegativeTweets.iloc[4]['Profile'],
                                                     alt='pic'),
                                            html.Div(df_getNegativeTweets.iloc[4]['Tweet Text'], className='direct-chat-text',
                                                     title='Retweets: %s' % df_getNegativeTweets.iloc[4]['Retweets'])
                                        ])
                                    ])])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header', children=[
                            html.Div('Most Influential Members', className='card-title'),
                            html.Div(className='card-tools', children=[
                                html.Span('10', title='10 Most influential members', className='badge badge-info'),
                                html.Button(className='btn btn-tool',type='button',
                                                **{'data-card-widget':'collapse'},children=[
                                            html.I(className='fas fa-minus')
                                        ])])
                        ]),
                        html.Div(className='card-body p-0', children=[
                            html.Ul(className='users-list clearfix', children=[
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[0]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[0][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[0]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[0]['Follower Count'],
                                              className='users-list-date')
                                ]),
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[1]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[1][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[1]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[1]['Follower Count'],
                                              className='users-list-date')
                                ]),
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[2]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[2][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[2]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[2]['Follower Count'],
                                              className='users-list-date')
                                ]),
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[3]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[3][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[3]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[3]['Follower Count'],
                                              className='users-list-date')
                                ]),
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[4]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[4][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[4]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[4]['Follower Count'],
                                              className='users-list-date')
                                ]),
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[5]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[5][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[5]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[5]['Follower Count'],
                                              className='users-list-date')
                                ]),
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[6]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[6][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[6]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[6]['Follower Count'],
                                              className='users-list-date')
                                ]),
                                html.Li(children=[
                                    html.Img(src=df_getTopAccount.iloc[7]['Profile'], alt='pic',
                                             title='Joined Twitter on: %s' % df_getTopAccount.iloc[7][
                                                 'Accout Creation']),
                                    html.Span(df_getTopAccount.iloc[7]['Author'], className='users-list-name'),
                                    html.Span('Followers: %s' % df_getTopAccount.iloc[7]['Follower Count'],
                                              className='users-list-date')
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])
