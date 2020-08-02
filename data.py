import pandas as pd
import numpy as np
from functools import reduce
confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

df_confirmed = pd.read_csv(confirmed)
df_deaths = pd.read_csv(deaths)
df_recovered = pd.read_csv(recovered)

# Total cases
df_confirmed['Total_Cases']=df_confirmed.iloc[:, 4:].sum(axis=1)
df_deaths['Total_Deaths']=df_deaths.iloc[:, 4:].sum(axis=1)
df_recovered['Total_Recoveries']=df_recovered.iloc[:, 4:].sum(axis=1)

# Combining the above into one dataframe
new_df_confirmed=df_confirmed.iloc[:,[1,-1]]
new_df_recovered=df_recovered.iloc[:,[1,-1]]
new_df_deaths=df_deaths.iloc[:,[1,-1]]
# df_combined=pd.merge(left=new_df_confirmed, right=new_df_recovered, how='left', left_on=new_df_confirmed.iloc[:,0], right_on=new_df_recovered.iloc[:,0])
df_combined = [new_df_confirmed, new_df_recovered,df_deaths]
df_final = reduce(lambda left,right: pd.merge(left,right,on='Country/Region'), df_combined)
df_final = df_final.drop('Province/State', 1)
country = df_final['Country/Region']
