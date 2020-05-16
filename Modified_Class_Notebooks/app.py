import streamlit as st
import pandas as pd
data = pd.read_csv("merged_data.csv")

# i want to see all the rating for selected movie

st_ms = st.multiselect("Select the movie", list(data['title'].unique()))
st.write(data[data['title']==st_ms[0]][['user_id','rating']])
