import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Qwon\Desktop\Dev\data_science_projects\chicago\jannov.csv")
#df=data.head(100658)
figcrashtype=px.bar( df["FIRST_CRASH_TYPE"].value_counts(),
           color=df["FIRST_CRASH_TYPE"].value_counts(),
           color_continuous_scale="thermal",
           #facet_col=df["CRASH_HOUR"],
          # hover_data=df["CRASH_HOUR"],
           height=600,
           width=600
            )

figprim=px.bar( df["PRIM_CONTRIBUTORY_CAUSE"].value_counts().tail(37),
           color=df["PRIM_CONTRIBUTORY_CAUSE"].value_counts().tail(37),
           color_continuous_scale="thermal",
          text_auto=True,
           title="Primary cause of accident",
           width=1200,
          # hover_dat=df["CRASH_HOUR"],
           height=1000
           # 
           )
#mask=dm["STREET_NAME"].value_counts().head(20)
#df.groupby("FIRST_CRASH_TYPE")["STREET_NAME"].value_counts()
street=px.bar( df["STREET_NAME"].value_counts().head(20),
           color=df["STREET_NAME"].value_counts().head(20),
           title="20 Most crash prone steets in chicago",
           color_continuous_scale="thermal",
          text_auto=True,
           #facet_col=df["CRASH_HOUR"],
          # hover_data=df["CRASH_HOUR"],
           height=800,
           width=1000
            )
sun=px.sunburst(data_frame=df,
                path=["CRASH_MONTH","CRASH_DAY_OF_WEEK"],
                color="CRASH_DAY_OF_WEEK",
                color_continuous_scale="thermal",
                height=800,
                width=800,
                #values="CRASH_MONTH",   
                )
map_fig=px.scatter_mapbox(data_frame=df,
                      lat="LATITUDE",
                      lon="LONGITUDE",
                      color="CRASH_TYPE",
                      hover_data="PRIM_CONTRIBUTORY_CAUSE",
                      mapbox_style="carto-positron",
                     # animation_group="DATE",
                      height=1000,
                      width=1200,
                      animation_frame="CRASH_MONTH",
                      zoom=9.5,
                      title="ACCIDENTS IN CHICAGO FROM JAN 2023 TO NOV 2023"
                      )

#option=st.selectbox("Group by month",(df["CRASH_MONTH"].unique()))
#st.write('You selected?', option)
st.markdown("This a  simple analyssis of Crashes in chigoco city")
st.write(figprim)
st.write(map_fig)
st.write(street)
st.write(sun)



