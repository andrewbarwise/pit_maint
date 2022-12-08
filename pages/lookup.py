import streamlit as st 
import pandas as pd
from src.data_cleanse import data
from PIL import Image
from datetime import date
import os
from os import listdir

st.session_state.df = data("C:\data\pit_maint\data\pit_location.xlsx")
st.session_state.service_update_df = pd.read_csv("C:\data\pit_maint\data\service_update.csv")

pit_id = st.session_state.df['Fomat PIT'].values.tolist()
# get current date
today = date.today()
date_updated = today.strftime("%d/%m/%Y")

pits = st.selectbox("Pit ID",pit_id)

if st.button("Select"):
    # put a if statement to catch empty folder and return message
        folder_dir = f"C:\data\pit_maint\data\photos\{pits}"
        for images in os.listdir(folder_dir):
            img = Image.open(f"C:\data\pit_maint\data\photos\{pits}\{images}")
            st.image(img)

