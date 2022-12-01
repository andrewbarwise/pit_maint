import pandas as pd
import streamlit as st
from src.data_cleanse import data
import warnings

st.session_state.df = data("C:\data\pit_maint\data\pit_location.xlsx")

st.title("Pit Inspections")

pit_id = st.session_state.df['Fomat PIT'].values.tolist()

pits = st.selectbox("Pit ID",pit_id)

if st.button('Select'):
    selected_pit = st.session_state.df[st.session_state.df['Fomat PIT'] == pits]
    st.dataframe(selected_pit)

st.map(selected_pit[["latitude", "longitude"]], zoom= 10, use_container_width=True)
