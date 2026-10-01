import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
st.title("Cricket Analysis Dashboard")
st.markdown("This is Data Analysis Project using Python Streamlit in Data Science and Analysis Batch 10")


df=pd.read_csv("cleanedfile.csv")

select = option_menu(
    menu_title=None,
    options=["Home","Player Analysis","Country Insights","Comparison","Data Explorer","About Project"],
    
    orientation="horizontal",
    icons=["house","person","globe","bar-chart","table"]
)

#this is home page
if select=="Home":
    st.title("Cricket Analysis Intro.")

    col1,col2,col3,col4,col5=st.columns(5)

    col1.metric("Total Player",df["Player"].nunique())
    col2.metric("Total Countries",df["country"].nunique())
    col3.metric("Total Matches",df["Matches"].sum())
    col4.metric("Total Runs",df["Runs"].sum())
    col5.metric("Total Sixes",df["6s"].sum())

    st.dataframe(df.head(5))

#this is for player analysis
elif select == "Player Analysis":
    st.title("Cricket Player Analysis")

    player = st.selectbox("Select Player",df["Player"])

    pdata= df[df["Player"]==player]

    df2=pdata[["Matches","Inns","6s","4s","100","50","Average"]]
    #st.dataframe(df2)
    df2=df2.T.reset_index() 
    st.dataframe(df2)
    fig=px.bar(df2,x="index",y=df2.columns[1],color="index")

    st.plotly_chart(fig)



elif select == "Country Insights":
    col1,col2=st.columns(2)
    with col1:
        st.title("Country Insights")
        country_runs=df.groupby("country")["Runs"].sum().reset_index()

        fig = px.pie(country_runs,names="country",values="Runs")
        st.plotly_chart(fig)
    with col2:
        st.title("Country Wise Players insights")
        country_Sel=st.selectbox("Select Country",df["country"].unique())
        c_df=df[df["country"]==country_Sel]

        fig_run = px.pie(c_df,names="Player",values="Runs")
        st.plotly_chart(fig_run,use_container_width=True)


elif select == "Comparison":
    st.title("Player Comparison")
    
    players=st.multiselect("Compare Players",df["Player"],default=df["Player"].head(3))
    compare=df[df["Player"].isin(players)]
    fig=px.scatter(compare,x="Strike_rate",y="Average",size="Runs",color="country")
    st.plotly_chart(fig)




elif select == "Data Explorer":
    st.title("Data Explorer")
    st.dataframe(df)

elif select == "About Project":
    st.title("About Project")
    st.markdown("How this project evolved with the Data Analysis Skills by Muhammad Rafay Shaikh")