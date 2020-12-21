html.Div(className='content', children=[
    html.Div(className='container-fluid', children=[
        # Small boxes (Stat box)
        html.Div(className='row', children=[
            html.Div(className='col-lg-3 col-6', children=[
                html.Div(className='small-box bg-info', children=[
                    html.Div(className='inner', children=[
                        html.H3(data.df_final.iloc[4]['Country/Region'])
                    ]),
                    html.Div(className='icon', children=[
                        html.I(className='ion ion-bag')
                    ]),
                    html.A('Total Cases:', className='small-box-footer', href='#'),
                    html.A(data.df_final.iloc[4]['Total_Cases'], className='small-box-footer', href='#')
                    # html.I(className='fas fa-arrow-circle-right')
                ])
            ]),
            html.Div(className='col-lg-3 col-6', children=[
                html.Div(className='small-box bg-success', children=[
                    daq.Gauge(
                        color={"gradient": True,
                               "ranges": {"green": [0, 6], "yellow": [6, 8], "red": [8, 10]}},
                        value=data.df_final.iloc[4]['Total_Recoveries'],
                        logarithmic=False,
                        label='Recoveries',
                        max=1000,
                        min=0,
                        size=150,
                    ),
                    html.Div(className='icon', children=[
                        html.I(className='ion ion-stats-bars')
                    ]),
                    html.A('Total Recoveries', className='small-box-footer', href='#'),
                    html.I(className='fas fa-arrow-circle-right')
                ])
            ]),
            html.Div(className='col-lg-3 col-6', children=[
                html.Div(className='small-box bg-warning', children=[
                    daq.Gauge(
                        color="#D2691E",
                        value=300,
                        label='Hello world',
                        max=1000,
                        min=0,
                        size=150,
                    ),
                    html.Div(className='icon', children=[
                        html.I(className='ion ion-person-add')
                    ]),
                    html.A('New Infections', className='small-box-footer', href='#'),
                    html.I(className='fas fa-arrow-circle-right')
                ])
            ]),
            html.Div(className='col-lg-3 col-6', children=[
                html.Div(className='small-box bg-danger', children=[
                    daq.Gauge(
                        color="#000000",
                        value=375,
                        label='Total Deaths',
                        max=500,
                        min=0,
                        size=150,
                    ),
                    html.Div(className='icon', children=[
                        html.I(className='ion ion-pie-graph')
                    ]),
                    html.A('More info', className='small-box-footer', href='#'),
                    html.I(className='fas fa-arrow-circle-right')
                ])
            ])
        ]),
        # End of Row
        # Main row
        html.Div(className='row', children=[
            html.Section(className='col-lg-7 connectedSortable', children=[
                # Custom tabs (Charts with tabs)
                html.Div(className='card', children=[
                    html.Div(className='card-header', children=[
                        html.H3(className='card-title', children=['Covid_19 Statistics',
                                                                  html.I(className='fas fa-universal-access ')
                                                                  ]),
                        html.Div(className='card-tools', children=[
                            html.Ul(className='nav nav-pills ml-auto', children=[
                                html.Li(className='nav-item', children=[
                                    html.A('Area', className='nav-link active', href='#', **{'data-toggle': 'tab'}),
                                    html.Div(id='hello', children=[
                                        # dcc.Graph(id='covid_per_country'),
                                        # dcc.Graph(id='values')
                                    ])
                                ]),
                                html.Li(className='nav-item', children=[
                                    html.A('Donut', className='nav-link', href='#', **{'data-toggle': 'tab'})
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])

    ])
])

dbc.FormGroup([
    html.H4("Africa"),
    dcc.Dropdown(id='country_drop_down',
                 options=[{'label': i, 'value': i} for i in data.df_final['Country/Region']],
                 value='Kenya')
]),

html.Div(className='col-sm-6', children=[
    html.H1(data.df_final.iloc[4]['Country/Region'], className='m-0 text-dark')
]),