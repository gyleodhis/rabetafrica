import dash_ag_grid as dg
from controller.loadforest import df_land_ag

columnDefs = [
    {
        "headerName": "Country","field": "Country",
    },
    {
        "headerName": "2003","field": "YR2003","type": "rightAligned",
    },
    {
        "headerName": "2005","field": "YR2005","type": "rightAligned",
    },
    {
        "headerName": "2009","field": "YR2009","type": "rightAligned",
    },
    {
        "headerName": "2013","field": "YR2013","type": "rightAligned",
    },
    {
        "headerName": "2017","field": "YR2017", "type": "rightAligned",
    },
    {
        "headerName": "2019","field": "YR2019","type": "rightAligned",
    },
    {
        "headerName": "18 Yr Diff","field": "Pct_Lost","type": "rightAligned",
    },
]

defaultColDef = {
    "filter": True,
    "resizable": True,
    "sortable": True,
    "editable": False,
    "floatingFilter": True,
    "minWidth": 125
}

cellStyle = {
    "styleConditions": [
        {
            "condition": "value <= 49",
            "style": {"color": "#FF0000"},
        },
        {
            "condition": "value >= 50",
            "style": {"color": "#008000"},
        },
    ]
}

forest_table = dg.AgGrid(
    id="portfolio-grid",
    className="ag-theme-alpine-dark",
    columnDefs=columnDefs,
    rowData=df_land_ag.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef=defaultColDef,
    cellStyle=cellStyle,
#     dangerously_allow_code=True,
    dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single"},
)