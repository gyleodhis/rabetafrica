import pandas as pd
from datetime import datetime as dt
from functools import reduce


# covid_data = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
"""Offline Vesion."""
covid_data = 'assets/covid_data.csv'  # offline csv version

df_covid_data_v1 = pd.read_csv(covid_data)
df_covid_data_v1['date'] = pd.to_datetime(df_covid_data_v1['date'])  # converting date column to type date
df_covid_data = df_covid_data_v1.sort_values('date').groupby(['continent','location']).last().reset_index()

"""Covicd 19 Daily vaccinations data"""
# vax_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-manufacturer.csv'
"""Offline version"""
vax_url = 'assets/vaccines.csv'

# #Carbon dioxide (CO₂) emissions broken down by sector, measured in tonnes per year.
# co2_sector = 'https://raw.githubusercontent.com/gyleodhis/owid-datasets/master/datasets/CO2%20emissions%20by%20sector%20(CAIT%2C%202021)/CO2%20emissions%20by%20sector%20(CAIT%2C%202021).csv'
"""Offline version"""
co2_sector = ('assets/CO₂_Sector.csv')

