# from functools import reduce
import plotly.express as px
from data import *

df_global_data = df_covid_data_v1.sort_values('date').groupby(['continent', 'location']).last().reset_index()

def func_continent(a='Africa'):
    # df_covid_data = df_covid_data_v1.sort_values('date').groupby(['continent', 'location']).last().reset_index()
    #     df_covid_data = df_covid_data.reset_index()
    df_covid_cont = df_global_data['continent'] == a
    df_cont_new = df_global_data[df_covid_cont]
    if a == 'Africa':
        df_cont_new.at[13, 'location'] = 'DRC'
    elif a == 'Asia':
        df_cont_new.at[101, 'location'] = 'UAE'
    else:
        df_cont_new
    return df_cont_new[{'date', 'location', 'new_cases', 'new_deaths', 'icu_patients', 'hosp_patients',
                        'new_tests_per_thousand', 'positive_rate', 'new_vaccinations', 'people_vaccinated_per_hundred'}]


"""Below functions return various charts dynamically"""

config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}


def fig_funnel(a='Africa'):
    return px.funnel(func_continent(a).nlargest(10, 'positive_rate'), x='positive_rate', y='location',
                     labels={"positive_rate": "New Positivity Rate", "location": "Country"})


def fig_bar(a='Africa'):
    return px.bar(func_continent(a).nlargest(10, 'new_cases'), x="location", template="simple_white",
                  labels={"location": "Country", "new_cases": "New Cases"}, y="new_cases", barmode="group")


def fig_pie(a='Africa'):
    return px.pie(func_continent(a).nlargest(10, 'new_vaccinations'), names='location', values='new_vaccinations',
                 labels={"new_vaccinations": "New Vaccinations", "location": "Country"})


def fig_funnel_vaccine(a='Africa'):
    return px.funnel(func_continent(a).nlargest(10, 'people_vaccinated_per_hundred'),
                               x='people_vaccinated_per_hundred',
                               y='location', color='location',
                               labels={"people_vaccinated_per_hundred": "Vaccination per 100", "location": "Country"}).update_yaxes(showticklabels=False)
