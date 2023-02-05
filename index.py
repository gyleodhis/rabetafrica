from dash import dash,html, dcc
from charts import *
import my_functions as mf
from about import profile_page
from covid import covid_vax_page
from climate import carbon_page
from social import social_page
from forest import forest_page
from dash.dependencies import Input, Output
from climate_data import fig_top_emitter_by_year,emission_by_continent

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server
app.title = 'Rabet'

app.layout = html.Div(className='hold-transition dark-mode sidebar-mini layout-fixed layout-footer-fixed layout-navbar-fixed',
                      children=[
    html.Div(className='wrapper',children=[
        dcc.Location(id='url', refresh=False),
        html.Nav(className="main-header navbar navbar-expand navbar-dark",
        # Left navbar links
        children=[
            html.Ul(className="navbar-nav",children=[
                        html.Li(className='nav-item',children=[
                                    html.A(className='nav-link', href='#', **{'data-widget':'pushmenu'}, role='button',
                                           children=[html.I(className='fas fa-bars')])]),
                        html.Li(className='nav-item d-sm-inline-block',children=[
                                    html.A('Home', className='nav-link', href='/')]),
                        html.Li(className='nav-item d-sm-inline-block',children=[
                                    html.A('Profile', className='nav-link', href='/profile')])
                    ]),
            html.Ul(className='navbar-nav ml-auto',children=[
                html.Form(className='form-inline ml-3', children=[
                html.Div(className='input-group input-group-sm', children=[
                        dcc.Input(className='form-control form-control-navbar', type='search',
                                  placeholder='Search'),
                        html.Div(className='input-group-append',
                                 children=[
                                     html.Button(className='btn btn-navbar', type='submit',
                                                 children=html.I(className='fas fa-search'))
                                 ])])])])
        ]),
        # Main Sidebar Container
        html.Aside(className='main-sidebar sidebar-dark-primary elevation-4',
                   # Logo container
                   children=[
                       html.A(className='brand-link',href='https://www.linkedin.com/in/gaylord-odhiambo-992990150/',
                              target='_blank',children=[
                               html.Img(className='brand-image img-circle elevation-3',src='assets/img/gyle.jpg',alt='Gyleodhis',
                                        style={'opacity':.8}),
                               html.Span('Rabet', className='brand-text font-weight-light')
                           ]),
                       html.Div(className='sidebar',children=[
                                # html.Div(className='user-panel mt-3 pb-3 mb-3 d-flex',children=[
                                #              html.Div(className='image',children=[
                                #                           html.Img(className='img-circle elevation-2', alt='Gyleodhis',
                                #                                    src='assets/img/gyle.jpg')]),
                                #              html.Div(className='info',children=[
                                #                           html.A('Rabet', className='d-block',
                                #                                  href='https://www.linkedin.com/in/gaylord-odhiambo-992990150/',
                                #                                  target='_blank')])
                                #          ]),
                                # Sidebar Menu
                                html.Div(className='mt-2',children=[
                                             html.Ul(className='nav nav-pills nav-sidebar flex-column', role='menu',
                                                     **{'data-widget': 'treeview', 'data-accordion': 'false'},children=[
                                                     html.Li(className='nav-item active',children=[
                                                         html.A(className='nav-link', href='/',children=[
                                                             html.I(className='nav-icon fas fa-globe-africa text-success'),
                                                             html.P(children=['Home'])])
                                                     ]),
                                                     html.Li(className='nav-item',children=[
                                                         html.A(className='nav-link', href='/vaccine',children=[
                                                             html.I(className='nav-icon fa fa-syringe'),
                                                             html.P('Covid-19 Vaccine')
                                                             # html.Span('New',className='right badge badge-success')
                                                         ])]),
                                                     html.Li(className='nav-item',children=[
                                                         html.A(className='nav-link', href='/climate',children=[
                                                             html.I(className='nav-icon fa fa-sun-o'),
                                                             html.P('Climate')
                                                         ])]),
                                                     html.Li(className='nav-item',children=[
                                                         html.A(className='nav-link', href='/social',children=[
                                                             html.I(className='nav-icon fa fa-twitter'),
                                                             html.P('Twitter'),
                                                             html.Span('Pre-Release',className='right badge badge-danger')
                                                         ])]),
                                                     html.Li(className='nav-item',children=[
                                                         html.A(className='nav-link', href='/forestcover',children=[
                                                             html.I(className='nav-icon fa fa-tree'),
                                                             html.P('Forest Cover'),
                                                             html.Span('New',className='right badge badge-success')
                                                         ])])
                                                     ])
                                         ])
                            ])
               ]),
    # Content Wrapper. Contains page content
    html.Div(className='content-wrapper',
             # Content Header (Page header)
             children=[
                 html.Div(id='page-content')
             ]),
    html.Footer(className='main-footer', children=[
        html.Strong('Rabet© | Visualizing Africa | 2023')
    ])])
])

covid_page = html.Div([
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
                                html.A('Africa: %s M' % round(func_continent()['total_cases'].sum()/1000000,2), className='small-box-footer', href='#'),
                                html.A('Worldwide: %s M' % round(df_covid_data['total_cases'].sum()/1000000,2),className='small-box-footer', href='#')
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
                                html.A('Africa: %s' %round(func_continent()['positive_rate'].mean(), 2), className='small-box-footer', href='#'),
                                html.A('Worldwide: %s' % round(df_covid_data['positive_rate'].mean(),2),className='small-box-footer', href='#')
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
                                html.A('Africa: %s M' %round(func_continent()['total_deaths'].sum()/1000000,2), className='small-box-footer', href='#'),
                                html.A('Worldwide: %s M' % round(df_covid_data['total_deaths'].sum()/1000000,2),className='small-box-footer', href='#')
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
                                html.A('Africa: %s M' %round(func_continent()['people_vaccinated'].sum()/1000000,2), className='small-box-footer', href='#'),
                                html.A('Worldwide: %s B' % round(df_covid_data['people_vaccinated'].sum()/1000000000,2),className='small-box-footer', href='#')
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
                                            html.Span('%s M' % round(func_continent()['total_cases'].sum()/1000000,2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent()['total_cases'].sum() / df_covid_data[
                                                        'total_cases'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_bar(), config=config)
                                    ])]),
                                html.Div(className='tab-pane', id='asia', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(func_continent('Asia')['total_cases'].sum()/1000000,2),
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
                                        dcc.Graph(figure=fig_bar('Asia'), config=config)
                                    ])]),
                                html.Div(className='tab-pane', id='europe', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(func_continent('Europe')['total_cases'].sum()/1000000,2),
                                                      className='text-bold text-lg'),
                                            html.Span('Europe Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Europe')['total_cases'].sum() / df_covid_data[
                                                        'total_cases'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_bar('Europe'), config=config)
                                    ])]),
                                html.Div(className='tab-pane', id='namerica', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(func_continent('North America')['total_cases'].sum()/1000000,2),
                                                      className='text-bold text-lg'),
                                            html.Span('N. America Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('North America')['total_cases'].sum() / df_covid_data[
                                                        'total_cases'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(figure=fig_bar('North America'), config=config)
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
                                            html.Span('%s M' % round(func_continent()['people_vaccinated'].sum()/1000000,2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str(
                                                    (mf.round_up(func_continent()['people_vaccinated'].sum() / df_covid_data[
                                                        'people_vaccinated'].sum(), 2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % to the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_pie(),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s B' % round(func_continent('Asia')['people_vaccinated'].sum()/1000000000,2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Asia')['people_vaccinated'].sum() / df_covid_data[
                                                        'people_vaccinated'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_pie('Asia'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(func_continent('Europe')['people_vaccinated'].sum()/1000000,2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Europe')['people_vaccinated'].sum() / df_covid_data[
                                                        'people_vaccinated'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_pie('Europe'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_vax', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span('%s M' % round(func_continent('North America')['people_vaccinated'].sum()/1000000,2),
                                                      className='text-bold text-lg'),
                                            html.Span('Total Vaccinations')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('North America')['people_vaccinated'].sum() /
                                                    df_covid_data['people_vaccinated'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph',
                                                  figure=fig_pie('North America'),config=config)
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
                                                        'positive_rate'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africas % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel(),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up((func_continent('Asia')['positive_rate'].dropna(
                                                    how='any').mean()) * 100,2),
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
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel('Asia'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up((func_continent('Europe')['positive_rate'].dropna(
                                                    how='any').mean()) * 100,2),
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
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel('Europe'),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_pst_rate', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up((func_continent('North America')['positive_rate'].dropna(
                                                    how='any').mean()) * 100,2),
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
                                        dcc.Graph(className='md-12', id='example_graph',
                                                  figure=fig_funnel('North America'),
                                                  config=config)
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
                                                        how='any').mean(),2),
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
                                        dcc.Graph(className='md-12', id='example_graph', figure=fig_funnel_vaccine(),
                                                  config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='asia_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    func_continent('Asia')['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(),2),
                                                className='text-bold text-lg'),
                                            html.Span('Asia Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Asia')['people_vaccinated_per_hundred'].sum() /
                                                    df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Asia % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', figure=fig_funnel_vaccine('Asia'), config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='europe_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    func_continent('Europe')['people_vaccinated_per_hundred'].dropna(
                                                        how='any').mean(),2),
                                                className='text-bold text-lg'),
                                            html.Span('Europe Vaccinations Per 100')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('Europe')['people_vaccinated_per_hundred'].sum() /
                                                    df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Europe % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', figure=fig_funnel_vaccine('Europe'), config=config)
                                    ])
                                ]),
                                html.Div(className='tab-pane', id='namerica_vax_100', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                mf.round_up(
                                                    func_continent('North America')[
                                                        'people_vaccinated_per_hundred'].dropna(how='any').mean(),2),
                                                className='text-bold text-lg'),
                                            html.Span('N. America Vaccinations Per 100')]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-success', children=[
                                                html.I(str((mf.round_up(
                                                    func_continent('North America')[
                                                        'people_vaccinated_per_hundred'].sum() / df_covid_data[
                                                        'people_vaccinated_per_hundred'].sum(),2)) * 100) + '%',
                                                       className='fas fa-arrow-up')
                                            ]),
                                            html.Span('N. America % of the World', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Graph(className='md-12', figure=fig_funnel_vaccine('North America'),
                                                  config=config)])
                                ])
                            ]),
                        ])
                    ])
                ])
            ])
        ])
    ])

])



@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return covid_page
    elif pathname == '/profile':
        return profile_page
    elif pathname == '/vaccine':
        return covid_vax_page
    elif pathname == '/climate':
        return carbon_page
    elif pathname == '/social':
        return social_page
    elif pathname =='/forestcover':
        return forest_page

@app.callback(
    Output('graph', 'figure'),
    Output('thermo', 'value'),
    Input('region', 'value'))
def update_area_chart(region):
    return fig_top_emitter_by_year(region),emission_by_continent(region)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=3000,debug=False)
