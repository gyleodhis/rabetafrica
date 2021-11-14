import pandas as pd
from datetime import datetime as dt
from functools import reduce


# covid_data = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
covid_data = 'assets/covid_data.csv'  # offline csv version

df_covid_data_v1 = pd.read_csv(covid_data)
df_covid_data_v1['date'] = pd.to_datetime(df_covid_data_v1['date'])  # converting date column to type date

"""Covicd 19 Daily vaccinations data"""
# vax_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-manufacturer.csv'
"""Offline version"""
vax_url = 'assets/vaccines.csv'

