import wbgapi as wb
import plotly.express as px
from utils.config import Rabet_bg_color,Rabet_color_palette

theme_color = ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

def getCo2Emission():
    df_income = wb.data.DataFrame('EN.ATM.CO2E.PC',
                                    economy=wb.region.members('AFR'),labels=True)
    df_income = df_income.reset_index(drop=True).set_index('Country')
    df_income = df_income.iloc[1:,-20:-3].reset_index()
    df_income.loc[60] = df_income.sum(numeric_only=True)
    df_income['Country'] = df_income['Country'].fillna('Africa')
    df_income['Diff_Gain'] = df_income['YR2003']-df_income['YR2019']
    df_income.sort_values(by='YR2019', inplace=True,ascending=False)
    df_income = df_income.round(2)
    return df_income.reset_index(drop=True)
df_getCo2Emission=getCo2Emission()

def c02increase():
    df_c02increase = df_getCo2Emission.copy()
    df_c02increase.sort_values(by='Diff_Gain', inplace=True,ascending=True)
    return df_c02increase

new_c02increase = c02increase()

def get_top_Carbon_countries():
    new_df = df_getCo2Emission.iloc[[0,1,2,3,4,9,21,23,25,45], 0:18]
    cols={'index':'Year',0:'Africa',1:'Libya',2:'South Africa',3:'Seychelles',
          4:'Algeria',9:'Egypt',21:'Ghana',23:'Nigeria',25:'Kenya',45:'Uganda'}
    new_df=new_df.transpose().reset_index()
    new_df.rename(columns=cols,inplace=True)
    new_df = new_df.iloc[1:]
    return new_df

def fig_carbon_line():
    new_df=get_top_Carbon_countries()
    return px.line(new_df, y=new_df.columns, x='Year',
                  markers=True,template=Rabet_bg_color,
                  labels={'value':'Emissions in Tones','variable':'Country'})

def fig_c02_bar():
    return px.bar(new_c02increase.iloc[1:11, [0,1,17]], x='Country', template=Rabet_bg_color,
                  labels={'Country': 'Country','variable':'Year','value':'Emissions in Tonnes'}, y=['YR2003','YR2019'],
                   barmode='group').update_traces(marker_color=Rabet_color_palette, showlegend=True)

def fig_c02_gain_bar():
    return px.bar(new_c02increase.iloc[-11:-1, [0,1,17]], x="Country", template=Rabet_bg_color,
                  labels={"Country": "Country",'variable':'Year','value':'Emissions in Tonnes'}, y=['YR2003','YR2019'],
                   barmode="group").update_traces(marker_color=Rabet_color_palette, showlegend=True)