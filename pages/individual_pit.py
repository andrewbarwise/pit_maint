import streamlit as st 
import pandas as pd
from src.data_cleanse import data
from PIL import Image

st.session_state.df = data("C:\data\pit_maint\data\pit_location.xlsx")

pit_id = st.session_state.df['Fomat PIT'].values.tolist()

pits = st.selectbox("Pit ID",pit_id)

st.header("Location and Access")
location = st.selectbox("Are the pit address and GPS details correct?", ["Yes", "No", "Update Details - Pit located but address/ GPS details can be improved"])
access = st.selectbox("Is the pit accessible?", ["Yes", "No"])

st.header("Surrounds and lid level")
debris = st.selectbox("Is the pit lid free of debris?", ['Yes', 'No'])
level = st.selectbox("Is the pit lid level with the surrounding ground", ["Yes", "No"])

st.header("Physical condition and Security")
pit_lid = st.selectbox("Is the pit lid intact and undamaged?", ["Yes", "Minor Damage", "Damaged/ Unserviceable"])
collar = st.selectbox("Is the pit collar intact and undamaged?", ["Yes", "Minor Damage", "Damaged/ Unserviceable"])
lock = st.selectbox("Is the pit lid locked and secure?", ['Yes', 'No'])

st.header("Pit labelling")
label = st.selectbox("Is the pit labelled as Western Power", ["Yes", "No"])
pitlok = st.selectbox("Does the PITLOK pit enclosure collar have pit ID tag affixed", ['Yes', 'No'])

st.header("Upload Photo")
photo = st.file_uploader('Upload an image', type=["jpg", "jpeg","jfif"])

if photo is not None:
    image = Image.open(photo)
    st.image(image, caption='Uploaded image.', use_column_width=True)
    st.write("")
    st.write("Uploading...")


# ADD A SUBMIT BUTTON
