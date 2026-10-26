import pandas as pd
import numpy as np
import streamlit as st

st.title("Mini Sales DashBoard")
#Upload data

uploaded = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded:
	df=pd.read_csv(uploaded)
	df["revenue"]=df["units"]*df["unit_price"]
	st.write("Data Preview:", df.head())

	#filter
	all_regions=df["region"].unique().tolist()
	region=st.sidebar.selectbox("Region",["All"]+all_regions)
	if region!="All":
		df=df[df["region"]==region]
	
	#KPIs
	st.metric("Total Revenue:")

	
	

