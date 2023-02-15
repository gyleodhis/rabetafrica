import dash
from dash import Dash, html, dcc
# from pages.home import covid_page
# from pages.about import profile_page
# from pages.covid import covid_vax_page
# from pages.climate import carbon_page
# from pages.social import social_page
# from pages.forest import forest_page
from dash.dependencies import Input, Output
from controller.climate_data import fig_top_emitter_by_year, emission_by_continent

app = Dash(__name__,use_pages=True)
server = app.server
app.title = 'Rabet'

app.layout = html.Div(
    className='hold-transition dark-mode sidebar-mini layout-fixed layout-footer-fixed layout-navbar-fixed',
    children=[
        html.Div(className='wrapper', children=[
            # dcc.Location(id='url', refresh=False),
            html.Nav(className="main-header navbar navbar-expand navbar-dark",
                     # Left navbar links
                     children=[
                         html.Ul(className="navbar-nav", children=[
                             html.Li(className='nav-item', children=[
                                 html.A(className='nav-link', href='#', **{'data-widget': 'pushmenu'}, role='button',
                                        children=[html.I(className='fas fa-bars')])]),
                             html.Li(className='nav-item d-sm-inline-block', children=[
                                 html.A('Home', className='nav-link', href=dash.page_registry['pages.home']['path'])]),
                             html.Li(className='nav-item d-sm-inline-block', children=[
                                 html.A('Profile', className='nav-link', href=dash.page_registry['pages.about']['path'])])
                         ]),
                         html.Ul(className='navbar-nav ml-auto', children=[
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
                           html.A(className='brand-link',
                                  href='https://www.linkedin.com/in/gaylord-odhiambo-992990150/',
                                  target='_blank', children=[
                                   html.Img(className='brand-image img-circle elevation-3', src='assets/img/gyle.jpg',
                                            alt='Gyleodhis',
                                            style={'opacity': .8}),
                                   html.Span('Rabet', className='brand-text font-weight-light')
                               ]),
                           html.Div(className='sidebar', children=[
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
                               html.Div(className='mt-2', children=[
                                   html.Ul(className='nav nav-pills nav-sidebar flex-column',**{'data-widget': 'treeview', 'data-accordion': 'false'},
                                           role='menu',children=[
                                           html.Li(className='nav-item active', children=[
                                               html.A(className='nav-link', href=dash.page_registry['pages.home']['path'], children=[
                                                   html.I(className='nav-icon fas fa-globe-africa text-success'),
                                                   html.P(children=['Home'])])
                                           ]),
                                           html.Li(className='nav-item', children=[
                                               html.A(className='nav-link', href=dash.page_registry['pages.covid']['path'],
                                                      children=[
                                                   html.I(className='nav-icon fa fa-syringe'),
                                                   html.P('Covid-19 Vaccine')
                                                   # html.Span('New',className='right badge badge-success')
                                               ])]),
                                           html.Li(className='nav-item', children=[
                                               html.A(className='nav-link', href=dash.page_registry['pages.climate']['path'], children=[
                                                   html.I(className='nav-icon fa fa-sun-o'),
                                                   html.P('Climate')
                                               ])]),
                                           html.Li(className='nav-item', children=[
                                               html.A(className='nav-link', href=dash.page_registry['pages.social']['path'], children=[
                                                   html.I(className='nav-icon fa fa-twitter'),
                                                   html.P('Twitter'),
                                                   html.Span('Discontinued', className='right badge badge-danger')
                                               ])]),
                                           html.Li(className='nav-item menu-open', children=[
                                               html.A(className='nav-link', href='#', children=[
                                                   html.I(className='nav-icon fa fa-money'),
                                                   html.P(children=[
                                                       'World Bank',
                                                       html.I(className='fas fa-angle-left right')])
                                               ]),
                                               html.Ul(className='nav nav-treeview', children=[
                                                   html.Li(className='nav-item', children=[
                                                       html.A(className='nav-link', href=dash.page_registry['pages.forest']['path'],
                                                              children=[
                                                           html.I(className='nav-icon fa fa-tree'),
                                                           html.P('Forest Cover'),
                                                           html.Span('New', className='right badge badge-success')
                                                       ])])
                                               ])])
                                       ])
                               ])
                           ])
                       ]),
            # Content Wrapper. Contains page content
            html.Div(className='content-wrapper',
                     # Content Header (Page header)
                     children=[
                         dash.page_container
                         # html.Div(id='page-content')
                     ]),
            html.Footer(className='main-footer', children=[
                html.Strong('Rabet© | Visualizing Africa | 2023')
            ])])
    ])


# @app.callback(Output('page-content', 'children'),
#               Input('url', 'pathname'))
# def display_page(pathname):
#     if pathname == '/':
#         return covid_page
#     elif pathname == '/profile':
#         return profile_page
#     elif pathname == '/vaccine':
#         return covid_vax_page
#     elif pathname == '/climate':
#         return carbon_page
#     elif pathname == '/social':
#         return social_page
#     elif pathname == '/forestcover':
#         return forest_page


@app.callback(
    Output('graph', 'figure'),
    Output('thermo', 'value'),
    Input('region', 'value'))
def update_area_chart(region):
    return fig_top_emitter_by_year(region), emission_by_continent(region)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=3000, debug=False)
