import pandas as pd
import datetime as dt
from functools import reduce

this_month = dt.datetime.today().month
covid_data = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
# covid_data = 'assets/covid_data.csv' # offline csv version

df_covid_data_v1 = pd.read_csv(covid_data)
df_covid_data_v1['date'] = pd.to_datetime(df_covid_data_v1['date']) #converting date column to type date
df_covid_data = df_covid_data_v1.sort_values('date').groupby(['continent','location']).last()
df_covid_data = df_covid_data.reset_index()

# africa_all = df_covid_data_v1['continent'] == 'Africa'
# df_covid_data_v1 = df_covid_data_v1['dates'].dt.month == this_month
# Africa dataframe. convert this into a class
df_afric = df_covid_data['continent'] == 'Africa'
df_afric_new = df_covid_data[df_afric]
df_afric_new.at[13,'location'] = 'DRC'
df_africa = df_afric_new[{'date','location','new_cases','new_deaths','icu_patients','hosp_patients',
                          'new_tests_per_thousand','positive_rate','new_vaccinations','people_vaccinated_per_hundred'}]
# df_africa.to_csv('assets/africa.csv', index=False)