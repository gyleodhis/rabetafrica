import wbgapi as wb
import plotly.express as px
from utils.config import Rabet_bg_color

def getcereals():
    df_cereal = wb.data.DataFrame('AG.PRD.CREL.MT',economy=wb.region.members('AFR'), labels=True)
    df_cereal = df_cereal.reset_index(drop=True)
    df_cereal = df_cereal.drop('YR1960', axis=1)
    df_cereal.sort_values(by='YR2021', inplace=True, ascending=False)
    df_cereal = df_cereal.round(2).reset_index(drop=True)
    return df_cereal


df_getcereals = getcereals()


def get_first_last():
    df_cereal_new = df_getcereals[['Country', 'YR1961', 'YR2021']]
    return df_cereal_new.fillna(0)


def cereal_scatter(a=1):
    if a == 1:
        return px.scatter(get_first_last().head(14), x="YR2021", y="YR1961", template=Rabet_bg_color,
                          size="YR2021", color='Country', labels={'YR2021': '2021', 'YR1961': '1961'},
                          hover_name="Country", log_y=True, size_max=50)
    else:
        return px.scatter(get_first_last().tail(40), x="YR2021", y="YR1961", template=Rabet_bg_color,
                          size="YR2021", color='Country', labels={'YR2021': '2021', 'YR1961': '1961'},
                          hover_name="Country", log_y=True, size_max=50)
