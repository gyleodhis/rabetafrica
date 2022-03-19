import pandas as pd
# import numpy as np
import plotly.express as px
from data import co2_sector

def load_data(a):
    return pd.read_csv(a,index_col=None)
def carbon_dioxide():
    cos_sector_df = load_data(co2_sector)
    cos_sector_df.drop(cos_sector_df.columns[[0]], axis=1, inplace=True)
    # cos_sector_df.to_csv('assets/CO₂_Sector.csv')
    return cos_sector_df

def emissions_by_year():
    co2_sector_df=carbon_dioxide().iloc[:,[0,1,3,5,7,9,11,13,17,24]]
    return co2_sector_df.groupby(['Year']).mean()

def emissions_by_sctor():
    new_co2 = emissions_by_year().iloc[-1].to_frame().dropna()
    new_co2.rename(columns={2018:'Amount'},inplace = True)
    # i = [0,7,6]
    # for a in i:new_co2=new_co2.drop(new_co2.index[a])
    new_co2['Percentage'] = round(new_co2.Amount*100/new_co2.Amount.sum(),2)
    new_co2.index = new_co2.index.str.replace(' \(per capita\)','')
    return new_co2.sort_values(by='Percentage')

def last_two_decades_emissions():
    last_two = round((emissions_by_year().iloc[-1]-emissions_by_year().
                      iloc[0])*100/emissions_by_year().iloc[0]).to_frame()
    last_two.index = last_two.index.str.replace(' \(per capita\)','')
    last_two.rename(columns={0:'% Change'},inplace = True)
    return last_two.sort_values(by='% Change')

def top_emitters_by_year():
    top_co2_sector_df=carbon_dioxide().iloc[:,[0,1,3,5,7]]
    return top_co2_sector_df.groupby(['Year']).mean().reset_index()

def fig_corbon_line():
    return px.line(top_emitters_by_year(), x='Year', y=top_emitters_by_year().columns,
                  markers=True,template="simple_white",
                  labels={'value':'Amt in Tonnes','variable':'Sector'})