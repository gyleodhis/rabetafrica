from data import *
import plotly.express as px
# import calendar
import datetime

cls=['#006400','#98FB98','#7FFF00','#00FF00','#32CD32','#00FF7F','#3CB371','#2E8B57','#228B22','#008000']
def func_continent(a='Africa'):
    df_covid_cont = df_covid_data['continent'] == a
    df_cont_new = df_covid_data[df_covid_cont]
    if a == 'Africa':
        df_cont_new.at[13, 'location'] = 'DRC'
    elif a == 'Asia':
        df_cont_new.at[101, 'location'] = 'UAE'
    else:
        df_cont_new
    return df_cont_new[['date', 'location', 'total_cases', 'total_deaths', 'icu_patients','people_vaccinated', 'hosp_patients',
                        'total_tests_per_thousand', 'positive_rate', 'people_vaccinated_per_hundred']]


"""Below functions return various charts dynamically"""

config = {'displayModeBar': False, 'scrollZoom': False, 'staticPlot': False}


def fig_funnel(a='Africa'):
    return px.funnel(func_continent(a).nlargest(10, 'positive_rate'), x='positive_rate', y='location',
                     labels={"positive_rate": "New Positivity Rate", "location": "Country"},
                     color_discrete_sequence=cls)


def fig_bar(a='Africa'):
    return px.bar(func_continent(a).nlargest(10, 'total_cases'), x="location", template="simple_white",
                  labels={"location": "Country", "total_cases": "Total Cases"},
                  y="total_cases", barmode="group").update_traces(marker_color=cls)


def fig_pie(a='Africa'):
    return px.pie(func_continent(a).nlargest(10, 'people_vaccinated'), names='location', values='people_vaccinated',
                  labels={"people_vaccinated": "Total Vaccinations", "location": "Country"},
                  color_discrete_sequence=cls)


def fig_funnel_vaccine(a='Africa'):
    return px.funnel(func_continent(a).nlargest(10, 'people_vaccinated_per_hundred'),
                     x='people_vaccinated_per_hundred',
                     y='location',  color_discrete_sequence=cls,
                     labels={"people_vaccinated_per_hundred": "Vaccination per 100",
                             "location": "Country"}).update_yaxes(showticklabels=False)


"""Vaccination functions and charts"""
def covid_vaccine():
    vax_df = pd.read_csv(vax_url, index_col=0, parse_dates=['date'])
    #     vax_df.to_csv('assets/vaccines.csv')
    """Below returns months"""
    vax_df['Month'] = pd.DatetimeIndex(vax_df['date']).month_name()
    """Below returns names of months. This is depircated"""
    # vax_df['Month'] = vax_df['Month'].apply(lambda x: calendar.month_abbr[x])
    return vax_df
df_covid_vaccine = covid_vaccine()
# """I DO NOT NEED THE TREEMAP. IT WASTES ALOT OF COMPUTE RESOURCES"""


# def covid_vaccine_treemap():
#     vax_df0 = df_covid_vaccine.sort_values('date').groupby(['Month', 'location', 'vaccine']).last().reset_index()
#     vax_df1 = vax_df0[['Month', 'location', 'vaccine', 'total_vaccinations']]
#     return px.treemap(vax_df1, path=["Month", "location", "vaccine"], values="total_vaccinations",
#                       # title='Covid19 Vaccinations',
#                       labels={"total_vaccinations": "Vaccinations"})


def pct_vaccination():
    vax_by_pcnt = df_covid_vaccine[['vaccine', 'total_vaccinations']].groupby('vaccine').sum().reset_index()
    vax_by_pcnt['pcnt_vaccination'] = round(vax_by_pcnt.total_vaccinations * 100 / vax_by_pcnt.total_vaccinations.sum(),
                                            2)
    return vax_by_pcnt.sort_values(['pcnt_vaccination'], ascending=[0])

df_pct_vaccination = pct_vaccination()


def df_this_month():
    vax_by_pcnt = df_covid_vaccine[['Month', 'vaccine', 'total_vaccinations']].groupby('Month').sum().reset_index()
    vax_by_pcnt['pcnt_vaccination'] = round(vax_by_pcnt.total_vaccinations * 100 / vax_by_pcnt.total_vaccinations.sum(),
                                            2)
    return vax_by_pcnt.sort_values(['pcnt_vaccination'], ascending=[0])

df_df_this_month = df_this_month()

def last_two_months():
    df_last_60_days_vax = df_covid_vaccine[df_covid_vaccine.date > datetime.datetime.now() - pd.to_timedelta("50day")]
    df_last_60_days_vax = df_last_60_days_vax[['Month', 'vaccine', 'total_vaccinations']].groupby(
        ['vaccine', 'Month']).sum().reset_index()
    df_last_60_days_vax['pcnt_vaccination'] = round(
        df_last_60_days_vax.total_vaccinations * 100 / df_last_60_days_vax.total_vaccinations.sum(), 2)
    return df_last_60_days_vax.sort_values(['vaccine'], ascending=[0])

df_last_two_months = last_two_months()

def last_two_months_diff(a='Moderna'):
    last_two =df_last_two_months['vaccine'] == a
    month_a = df_last_two_months[last_two]['pcnt_vaccination'].iloc[0]
    month_b = df_last_two_months[last_two]['pcnt_vaccination'].iloc[1]
    return round(month_a - month_b, 2).astype('str') + '%'


def fig_bar_vax():
    return px.bar(df_pct_vaccination, x='vaccine', y='pcnt_vaccination', template="simple_white",
                  labels={'pcnt_vaccination': 'Percentage Vaccinations', 'vaccine': 'Vaccine'}).update_traces(marker_color=cls)
