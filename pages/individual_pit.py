import streamlit as st 
import pandas as pd
from src.data_cleanse import data
from PIL import Image
from datetime import date
import os

st.session_state.df = data("C:\data\pit_maint\data\pit_location.xlsx")
st.session_state.service_update_df = pd.read_csv("C:\data\pit_maint\data\service_update.csv")

# file that will hold data captured 

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

st.header("Additional Comments")
comments = st.text_input("Please add any additional comments.")

st.header("Upload Photo")
photo = st.file_uploader('Upload an image', type=["jpg", "jpeg","jfif"])

if photo is not None:
    image = Image.open(photo)
    st.image(image, caption='Uploaded image.', use_column_width=True)
    st.write("")
    
# ADD A SUBMIT BUTTON
if st.button('Update'):
    # get current date
    today = date.today()
    date_updated = today.strftime("%d/%m/%Y")
    
    new_entry = [{'Pit Id' : pits, 'Date' : today, 'Address' : location, 'Accessible' : access, 'Debris Free' : debris, \
        'Lid Level' : level, 'Lid Intact' : pit_lid, 'Collar Intact' : collar, 'Lid Locked' : lock, 'Pit Labelled' : label, \
            'PitLok' : pitlok, 'Comments' : comments}]
    st.session_state.service_update_df = st.session_state.service_update_df.append(new_entry)

    if not os.path.exists(f'data\photos\{pits}'):
        os.makedirs(f'data\photos\{pits}')

    image.save(f'data\photos\{pits}\{today}.jpg')

    try:
        st.session_state.service_update_df.to_csv("C:\data\pit_maint\data\service_update.csv", index = False)

    except PermissionError:
        st.caption("Please close the file and then reclick the Update button. ")

    st.caption("Data has been uploaded")
