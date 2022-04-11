import pandas as pd
import numpy as np
df = pd.read_excel(r"C:\Users\sina.kian\Desktop\Quick report format V2\update\Elenco_di_Causa.xlsx")

AA=df.index[df['Tipologia di rischio (Strategica)'] == "BI DD"].tolist()
for i in AA:
    df['Tipologia di rischio (Strategica)'][i]="BI"

dff=df[['Tipologia di rischio (Strategica)','Impatto2','Probabilità ']].loc[df.groupby('Tipologia di rischio (Strategica)')['Impatto2'].idxmax()]






import plotly.graph_objects as go
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=dff['Impatto2'],
      theta=dff['Tipologia di rischio (Strategica)'],
      fill='toself',
      name='Impatto'
))
fig.add_trace(go.Scatterpolar(
      r=dff['Probabilità '],
      theta=dff['Tipologia di rischio (Strategica)'],
      fill='toself',
      name='Probabilità'
))

fig.update_layout(
  title="Radar Plot per diversi ambiti di rischi considerando impatto e probabilità",
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5],
      nticks=6
    )),
  showlegend=True
)

fig.show()

import os

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.png")
###################################

df.sort_values(by=['Tipologia di rischio (Strategica)'])
#df_causa
dfc=df[['Tipologia di rischio (Strategica)','Causa', 'Causa_ID', 'Probabilità ','Impatto2']]
dfc=dfc.sort_values(by=['Tipologia di rischio (Strategica)'])

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Impatto2'],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Causa'],
      fill='toself',
      name='Impatto'
))
fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Probabilità '],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Causa'],
      fill='toself',
      name='Probabilità'
))

fig.update_layout(
  title="Radar Plot per diverse cause di rischio BI considerando impatto e probabilità",
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5],
      nticks=6
    )),
  showlegend=True
)

fig.show()
fig.write_image("images/BI_RADAR.png")

##############################
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Impatto2'],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Causa'],
      fill='toself',
      name='Impatto'
))
fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Probabilità '],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Causa'],
      fill='toself',
      name='Probabilità'
))

fig.update_layout(
  title="Radar Plot per diverse cause di rischio A considerando impatto e probabilità",
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5],
      nticks=6

    )),
  showlegend=True
)

fig.show()
fig.write_image("images/A_RADAR.png")
############################
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Impatto2'],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Causa'],
      fill='toself',
      name='Impatto'
))
fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Probabilità '],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Causa'],
      fill='toself',
      name='Probabilità'
))

fig.update_layout(
  title="Radar Plot per diverse cause di rischio DD considerando impatto e probabilità",
  polar=dict(
  radialaxis_angle=-45,
    radialaxis=dict(
      visible=True,
      range=[0, 5],
      #ticklabelstep=2
      nticks=6

    )),
  showlegend=True
)

fig.show()
fig.write_image("images/DD_RADAR.png")
############################
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Impatto2'],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Causa'],
      fill='toself',
      name='Impatto'
))
fig.add_trace(go.Scatterpolar(
      r=dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Probabilità '],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Causa'],
      fill='toself',
      name='Probabilità'
))

fig.update_layout(
  title="Radar Plot per diverse cause di rischio R considerando impatto e probabilità",
  polar=dict(
    radialaxis=dict(
      visible=True,
      nticks=6,
      range=[0, 5]#,
#      period=3

    )),
  showlegend=True
)

fig.show()
fig.write_image("images/R_RADAR.png")
############################################
########################
#################################
#############################
#################################
#Tutto insieme
from plotly.subplots import make_subplots
import plotly
fig = make_subplots(rows=3, cols=2, specs=[[{'type': 'polar'}]*2]*3, subplot_titles = ['impatto per i diversi ambiti di rischi',"Probabilità per i diversi ambiti di rischi","diverse cause di rischio BI","Impatto per diverse cause di rischio DD","Impatto per diverse cause di rischio A","Impatto per diverse cause di rischio R"])
#fig = make_subplots(rows=3, cols=4, specs=[[{'type': 'polar'}]*4]*3)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "impatto",
      legendgroup="2017",
      r = dff['Impatto2'],
      theta = dff['Tipologia di rischio (Strategica)'],
    ), 1, 1)
fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "Probabilità",
      legendgroup="2018",
      r = dff['Probabilità '],
      theta = dff['Tipologia di rischio (Strategica)'],
      #thetaunit = "radians",
    ), 1, 2)
fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Causa'],
      showlegend=False
    ), 2, 1)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Probabilità '],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Causa'],
      showlegend=False
    ), 2, 1)


fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Causa'],
      showlegend=False
    ), 2, 2)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Probabilità '],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Causa'],
      showlegend=False
    ), 2, 2)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Causa'],
      showlegend=False
    ), 3, 1)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Probabilità '],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Causa'],
      showlegend=False
    ), 3, 1)


fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Causa'],
      showlegend=False
    ), 3, 2)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Probabilità '],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Causa'],
      showlegend=False
    ), 3, 2)
##
fig.update_traces(fill='toself')
fig.update_layout(
  title="Registro Rischi",
    polar = dict(
      radialaxis = dict(
        visible=True,
      )),
    polar2 = dict(
      radialaxis = dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar3 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar4 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar5 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar6 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
  )


fig.layout.annotations[0].update(y=1.02)
fig.layout.annotations[1].update(y=1.02)
fig.layout.annotations[2].update(y=0.63)
fig.layout.annotations[3].update(y=0.63)
fig.layout.annotations[4].update(y=0.25)
fig.layout.annotations[5].update(y=0.25)
fig.show()
fig.write_image("images/Registro.png")
##########################
##################################
#########################################
###############################################
fig = make_subplots(rows=3, cols=2, specs=[[{'type': 'polar'}]*2]*3, subplot_titles = ['impatto per i diversi ambiti di rischi',"Probabilità per i diversi ambiti di rischi","Impatto\Probabilità per diverse cause_ID di rischio BI","Impatto\Probabilità per diverse cause_ID di rischio DD","Impatto\Probabilità per diverse cause_ID di rischio A","Impatto\Probabilità per diverse cause_ID di rischio R"])
#fig = make_subplots(rows=3, cols=4, specs=[[{'type': 'polar'}]*4]*3)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "impatto",
      legendgroup="2017",
      r = dff['Impatto2'],
      theta = dff['Tipologia di rischio (Strategica)'],
    ), 1, 1)
fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "Probabilità",
      legendgroup="2018",
      r = dff['Probabilità '],
      theta = dff['Tipologia di rischio (Strategica)'],
      #thetaunit = "radians",
    ), 1, 2)
fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Causa_ID'].astype(str),
      showlegend=False
    ), 2, 1)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Probabilità '],
      theta=dfc[dfc['Tipologia di rischio (Strategica)']=="BI"]['Causa_ID'].astype(str),
      showlegend=False
    ), 2, 1)


fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Causa_ID'].astype(str),
      showlegend=False
    ), 2, 2)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Probabilità '],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="DD"]['Causa_ID'].astype(str),
      showlegend=False
    ), 2, 2)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Causa_ID'].astype(str),
      showlegend=False
    ), 3, 1)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Probabilità '],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="A"]['Causa_ID'].astype(str),
      showlegend=False
    ), 3, 1)


fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(99,110,250,0.5)',
      line_color = 'rgb(99,110,250)',
      name = "Impatto",
      legendgroup="2017",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Impatto2'],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Causa_ID'].astype(str),
      showlegend=False
    ), 3, 2)

fig.add_trace(go.Scatterpolar(
      fillcolor='rgba(239,85,59,0.5)',
      line_color = 'rgb(239,85,59)',
      name = "probabilità",
      legendgroup="2018",
      r = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Probabilità '],
      theta = dfc[dfc['Tipologia di rischio (Strategica)']=="R"]['Causa_ID'].astype(str),
      showlegend=False
    ), 3, 2)
##
fig.update_traces(fill='toself')
fig.update_layout(
  title="Registro Rischi",
    polar = dict(
      radialaxis = dict(
        visible=True,
      )),
    polar2 = dict(
      radialaxis = dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar3 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar4 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar5 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
    polar6 = dict(
      radialaxis=dict(
        visible=True,
        range=[0, 5],
        nticks=6
      )),
  )


fig.layout.annotations[0].update(y=1.02)
fig.layout.annotations[1].update(y=1.02)
fig.layout.annotations[2].update(y=0.63)
fig.layout.annotations[3].update(y=0.63)
fig.layout.annotations[4].update(y=0.25)
fig.layout.annotations[5].update(y=0.25)
fig.show()
fig.write_image("images/Registro_id.png")
fig.write_image("images/Registro_id.pdf")
