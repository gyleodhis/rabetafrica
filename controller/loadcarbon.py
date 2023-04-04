import wbgapi as wb
import plotly.express as px

theme_color = ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

def getCo2Emission():
    df_income = wb.data.DataFrame('EN.ATM.CO2E.PC',
                                    economy=wb.region.members('AFR'),labels=True)
    df_income = df_income.reset_index(drop=True).set_index('Country')
    df_income = df_income.iloc[1:,-19:-2].reset_index()
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
                  markers=True,template=theme_color[2],
                  labels={'value':'Emissions in Tones','variable':'Country'})

def fig_c02_bar():
    cls=['#006400','#008000','#228B22','#2E8B57','#3CB371','#98FB98','#7FFF00','#00FF00','#32CD32','#00FF7F']
    return px.bar(new_c02increase.iloc[1:11, [0,1,17]], x='Country', template=theme_color[2],
                  labels={'Country': 'Country','variable':'Year','value':'Emissions in Tonnes'}, y=['YR2003','YR2019'],
                   barmode='group').update_traces(marker_color=cls, showlegend=True)

def fig_c02_gain_bar():
    cls=['#98FB98','#7FFF00','#00FF00','#32CD32','#00FF7F','#3CB371','#2E8B57','#228B22','#008000','#006400']
    return px.bar(new_c02increase.iloc[-11:-1, [0,1,17]], x="Country", template=theme_color[2],
                  labels={"Country": "Country",'variable':'Year','value':'Emissions in Tonnes'}, y=['YR2003','YR2019'],
                   barmode="group").update_traces(marker_color=cls, showlegend=True)