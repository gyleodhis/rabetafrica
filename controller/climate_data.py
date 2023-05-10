import pandas as pd
# import numpy as np
import dash_daq as daq
import plotly.express as px
from controller.data import co2_sector,df_covid_data
from utils.config import Rabet_bg_color

def load_data(a):
    return pd.read_csv(a,index_col=None)
def carbon_dioxide():
    cos_sector_df = load_data(co2_sector)
    cos_sector_df.drop(cos_sector_df.columns[[0]], axis=1, inplace=True)
    # cos_sector_df.to_csv('assets/CO₂_Sector.csv',index=False)
    return cos_sector_df
df_carbon_dioxide = carbon_dioxide()

def emissions_by_year():
    co2_sector_df=df_carbon_dioxide.iloc[:,[0,1,3,5,7,9,11,13,17,24]]
    return co2_sector_df.groupby(['Year']).mean()

df_emissions_by_year = emissions_by_year()

def emissions_by_sctor():
    new_co2 = df_emissions_by_year.iloc[-1].to_frame().dropna()
    new_co2.rename(columns={2018:'Amount'},inplace = True)
    # i = [0,7,6]
    # for a in i:new_co2=new_co2.drop(new_co2.index[a])
    new_co2['Percentage'] = round(new_co2.Amount*100/new_co2.Amount.sum(),2)
    new_co2.index = new_co2.index.str.replace(' \(per capita\)','', regex=True)
    return new_co2.sort_values(by='Percentage')

def last_two_decades_emissions():
    last_two = round((df_emissions_by_year.iloc[-1]-df_emissions_by_year.
                      iloc[0])*100/df_emissions_by_year.iloc[0]).to_frame()
    last_two.index = last_two.index.str.replace(' \(per capita\)','', regex=True)
    last_two.rename(columns={0:'% Change'},inplace = True)
    return last_two.sort_values(by='% Change')

def top_emitters_by_year():
    top_co2_sector_df=df_carbon_dioxide.iloc[:,[0,1,3,5,7]]
    return top_co2_sector_df.groupby(['Year']).mean().reset_index()

df_top_emitters_by_year = top_emitters_by_year()

def fig_corbon_line():
    return px.line(df_top_emitters_by_year, x='Year', y=top_emitters_by_year().columns,
                  markers=True,template=Rabet_bg_color,
                  labels={'value':'Amt in Tonnes','variable':'Sector'})

def emission_with_continent():
    cos_with_continent = load_data(co2_sector).iloc[:,[0,1,2,4,6,8,10,12,14,16]]
    cos_with_continent.rename(columns={'Entity':'location'},inplace = True)
    df_continent = df_covid_data[['continent','location']]
    cos_with_continent = cos_with_continent[cos_with_continent['Year']%5==0]
    return pd.merge(df_continent,cos_with_continent)

def top_emitter_by_year(a='Africa'):
    """Possible values for a are Africa,Asia,Europe,North America,Oceania,South America"""
    top_emitters_year=emission_with_continent().iloc[:,[0,2,6]]
    df_top_emitters_year = top_emitters_year['continent'] == a
    top_emitters_year_new = top_emitters_year[df_top_emitters_year]
    top_emitters_year_new=top_emitters_year_new.groupby(['continent','Year']).mean()
    return top_emitters_year_new.reset_index()

def fig_top_emitter_by_year(a='Africa'):
    return px.area(top_emitter_by_year(a), x='Year', y="Energy", color="continent",
                   markers=True,template=Rabet_bg_color,labels={'Energy':'Amt in Tonnes'})

def emission_by_continent(a='Africa'):
    return round(top_emitter_by_year(a).Energy.sum(),2)

def fig_emission_by_continent(a='Africa'):
    return daq.Thermometer(min=100,max=2000,value=emission_by_continent(a),color = 'green',
                           showCurrentValue=True,units="Tones")
