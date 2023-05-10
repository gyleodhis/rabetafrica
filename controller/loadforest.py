import wbgapi as wb
import plotly.express as px
from utils.config import Rabet_bg_color,Rabet_color_palette

def getPctForestArea():
    df_income = wb.data.DataFrame('AG.LND.FRST.ZS',
                                  economy=wb.region.members('AFR'),labels=True)
    df_income = df_income.reset_index(drop=True).set_index('Country')
    df_income = df_income.iloc[1:,-20:-2].reset_index()
    df_income['Pct_Lost'] = df_income['YR2003']-df_income['YR2020']
    df_income.loc[60] = df_income.mean(numeric_only=True)
    df_income['Country'] = df_income['Country'].fillna('Africa')
    df_income.sort_values(by='YR2020', inplace=True,ascending=False)
    return df_income.reset_index(drop=True)

df_PctForestArea = getPctForestArea()


def land_ag():
    df_land_ag = df_PctForestArea.copy()
    df_land_ag.sort_values(by='Country', inplace=True,ascending=True)
    df_land_ag=df_land_ag.iloc[:, [0,1,3,7,11,15,17,19]]
    df_land_ag=df_land_ag.round(2)
    return df_land_ag

df_land_ag =land_ag()

def percentlost():
    df_percent = df_PctForestArea.copy()
    df_percent.sort_values(by='Pct_Lost', inplace=True,ascending=False)
    return df_percent

df_percentlost = percentlost()

def get_top_countries():
    new_df = df_PctForestArea.iloc[[0,1,2,3,4,20,24,31,44,45], 0:19]
    cols={'index':'Year',0:'Gabon',1:'Equatorial Guinea',2:'Liberia',3:'Seychelles',
          4:'Guinea-Bissau',24:'Nigeria',44:'Kenya',45:'Tunisia',20:'Africa',31:'S.Africa'}
    new_df=new_df.transpose().reset_index()
    new_df.rename(columns=cols,inplace=True)
    new_df = new_df.iloc[1:]
    return new_df

def fig_forest_line():
    new_df=get_top_countries()
    return px.line(new_df, y=new_df.columns, x='Year',
                  markers=True,template=Rabet_bg_color,
                  labels={'value':'Percentage Cover','variable':'Country'})

def fig_forest_bar():
    return px.bar(df_percentlost.iloc[0:10, [0,1,18]], x='Country', template=Rabet_bg_color,
                  labels={'Country': 'Country','variable':'Year','value':'Pct Cover'}, y=['YR2003','YR2020'],
                   barmode='group').update_traces(marker_color=Rabet_color_palette, showlegend=True)

def fig_forest_gain_bar():
    return px.bar(df_percentlost.iloc[-11:-1, [0,1,18]], x="Country", template=Rabet_bg_color,
                  labels={"Country": "Country",'variable':'Year','value':'Pct Cover'}, y=['YR2003','YR2020'],
                   barmode="group").update_traces(marker_color=Rabet_color_palette, showlegend=True)