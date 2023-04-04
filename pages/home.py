import dash
from dash import html, dcc
from controller.charts import *
import controller.my_functions as mf

dash.register_page(__name__,path='/',name='Home',title='Rabet',image_url='assets/img/site_meta.jpeg',
                   description='Insights, facts and analytics across the African continent. World Bank Statistics. Visualizing Africa. Data Analytics and Reports on Africa ')
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Covid 19 Snapshot: 04-02-2023')
                ]),
                html.Div(className='col-sm-6', children=[
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
            html.Div(className='row', children=[
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-success', children=[
                        html.Div(className='inner', children=[
                            html.H4('Total Cases')
                        ]),
                        html.A('Africa: %s M' % round(func_continent()['total_cases'].sum() / 1000000, 2),
                               className='small-box-footer', href='#'),
                        html.A('Worldwide: %s M' % round(df_covid_data['total_cases'].sum() / 1000000, 2),
                               className='small-box-footer', href='#')
                    ])
                ]),
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-success', children=[
                        html.Div(className='inner', children=[
                            html.H4('Positivity Rate')
                        ]),
                        html.Div(className='icon', children=[
                            html.I(className='ion ion-bars')
                        ]),
                        html.A('Africa: %s' % round(func_continent()['positive_rate'].mean(), 2),
                               className='small-box-footer', href='#'),
                        html.A('Worldwide: %s' % round(df_covid_data['positive_rate'].mean(), 2),
                               className='small-box-footer', href='#')
                    ])
                ]),
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-lime', children=[
                        html.Div(className='inner', children=[
                            # html.H4(df_covid_data.iloc[46]['location']),
                            html.H4('Total Death')
                        ]),
                        html.Div(className='icon', children=[
                            html.I(className='ion ion-pie-graph')
                        ]),
                        html.A('Africa: %s M' % round(func_continent()['total_deaths'].sum() / 1000000, 2),
                               className='small-box-footer', href='#'),
                        html.A('Worldwide: %s M' % round(df_covid_data['total_deaths'].sum() / 1000000, 2),
                               className='small-box-footer', href='#')
                    ])
                ]),
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-lime', children=[
                        html.Div(className='inner', children=[
                            html.H5('Total Vaccinations')
                        ]),
                        html.Div(className='icon', children=[
                            html.I(className='ion ion-bag')
                        ]),
                        html.A('Africa: %s M' % round(func_continent()['people_vaccinated'].sum() / 1000000, 2),
                               className='small-box-footer', href='#'),
                        html.A('Worldwide: %s B' % round(df_covid_data['people_vaccinated'].sum() / 1000000000, 2),
                               className='small-box-footer', href='#')
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item',
                                                children=html.A('N. America', className='nav-link',
                                                                href='#namerica',
                                                                **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % round(func_continent()['total_cases'].sum() / 1000000, 2),
                                                className='text-bold text-lg'),
                                            html.Span('Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent()['total_cases'].sum() / df_covid_data[
                                                        'total_cases'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(children=[dcc.Graph(figure=fig_bar(),config=config)],
                                                    type='circle',color='#006400')
                                    ])]),
                                html.Div(className='tab-pane', id='asia', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % round(func_continent('Asia')['total_cases'].sum() / 1000000,
                                                               2),
                                                className='text-bold text-lg'),
                                            html.Span('Asia Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Asia')['total_cases'].sum() / df_covid_data[
                                                        'total_cases'].sum(),
                                                    2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(children=[dcc.Graph(figure=fig_bar('Asia'),config=config)],
                                                    type='circle',color='#006400')
                                    ])]),
                                html.Div(className='tab-pane', id='europe', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % round(func_continent('Europe')['total_cases'].sum() / 1000000,
                                                               2),
                                                className='text-bold text-lg'),
                                            html.Span('Europe Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Europe')['total_cases'].sum() / df_covid_data[
                                                        'total_cases'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(children=[dcc.Graph(figure=fig_bar('Europe'),config=config)],
                                                    type='circle',color='#006400',)
                                    ])]),
                                html.Div(className='tab-pane', id='namerica', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(
                                                func_continent('North America')['total_cases'].sum() / 1000000, 2),
                                                      className='text-bold text-lg'),
                                            html.Span('N. America Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('North America')['total_cases'].sum() /
                                                    df_covid_data[
                                                        'total_cases'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(children=[dcc.Graph(figure=fig_bar('North America'),config=config)],
                                                    type='circle',color='#006400',)
                                    ])])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top Countries in Vaccinations', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_vax', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia_vax',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe_vax',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('N.America', className='nav-link',
                                                                                      href='#namerica_vax',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % round(func_continent()['people_vaccinated'].sum() / 1000000,
                                                               2),
                                                className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str(
                                                    (mf.round_up(
                                                        func_continent()['people_vaccinated'].sum() / df_covid_data[
                                                            'people_vaccinated'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % to the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_pie(),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s B' % round(
                                                func_continent('Asia')['people_vaccinated'].sum() / 1000000000, 2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Asia')['people_vaccinated'].sum() / df_covid_data[
                                                        'people_vaccinated'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_pie('Asia'),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(
                                                func_continent('Europe')['people_vaccinated'].sum() / 1000000, 2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Europe')['people_vaccinated'].sum() / df_covid_data[
                                                        'people_vaccinated'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_pie('Europe'),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(
                                                func_continent('North America')['people_vaccinated'].sum() / 1000000,
                                                2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('North America')['people_vaccinated'].sum() /
                                                    df_covid_data['people_vaccinated'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_pie('North America'),config=config)])
                                    ])
                                ])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Positivity Rate', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_pst_rate', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia_pst_rate',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe_pst_rate',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('N.America', className='nav-link',
                                                                                      href='#namerica_pst_rate',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    (func_continent()['positive_rate'].dropna(how='any').mean()) * 100,
                                                    2),
                                                className='text-bold text-lg'),
                                            html.Span('Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent()['positive_rate'].sum() / df_covid_data[
                                                        'positive_rate'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_funnel(),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up((func_continent('Asia')['positive_rate'].dropna(
                                                    how='any').mean()) * 100, 2),
                                                className='text-bold text-lg'),
                                            html.Span('Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Asia')['positive_rate'].sum() / df_covid_data[
                                                        'positive_rate'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_funnel('Asia'),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up((func_continent('Europe')['positive_rate'].dropna(
                                                    how='any').mean()) * 100, 2),
                                                className='text-bold text-lg'),
                                            html.Span('Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Europe')['positive_rate'].sum() / df_covid_data[
                                                        'positive_rate'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_funnel('Europe'),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up((func_continent('North America')['positive_rate'].dropna(
                                                    how='any').mean()) * 100, 2),
                                                className='text-bold text-lg'),
                                            html.Span('Positivity Rate')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-warning', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('North America')['positive_rate'].sum() /
                                                    df_covid_data[
                                                        'positive_rate'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(figure=fig_funnel('North America'),config=config)])
                                    ])
                                ]),
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Vaccinations Per 100 Persons', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa_vax_100', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia_vax_100',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe_vax_100',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('N.America', className='nav-link',
                                                                                      href='#namerica_vax_100',
                                                                                      **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    func_continent()['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(), 2),
                                                className='text-bold text-lg'),
                                            html.Span('Avg Vaccination Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent()['people_vaccinated_per_hundred'].sum() /
                                                    df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-down')
                                            ]),
                                            html.Span('Africas % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(className='md-12', figure=fig_funnel_vaccine(),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    func_continent('Asia')['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(), 2),
                                                className='text-bold text-lg'),
                                            html.Span('Asia Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Asia')['people_vaccinated_per_hundred'].sum() /
                                                    df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(className='md-12', figure=fig_funnel_vaccine('Asia'),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    func_continent('Europe')['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(), 2),
                                                className='text-bold text-lg'),
                                            html.Span('Europe Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Europe')['people_vaccinated_per_hundred'].sum() /
                                                    df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(className='md-12', figure=fig_funnel_vaccine('Europe'),config=config)])
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    func_continent('North America')[
                                                        'people_vaccinated_per_hundred'].dropna(how='any').mean(), 2),
                                                className='text-bold text-lg'),
                                            html.Span('N. America Vaccinations Per 100')]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('North America')[
                                                        'people_vaccinated_per_hundred'].sum() / df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',
                                                    children=[dcc.Graph(className='md-12', figure=fig_funnel_vaccine('North America'),config=config)])])
                                ])
                            ]),
                        ])
                    ])
                ])
            ])
        ])
    ])

])