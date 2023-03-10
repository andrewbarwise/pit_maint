import streamlit as st 
import pandas as pd
from src.data_cleanse import data
from PIL import Image
from datetime import date, datetime
import os

st.session_state.df = data("C:\data\pit_maint\data\pit_location.xlsx")
st.session_state.service_update_df = pd.read_csv("C:\data\pit_maint\data\service_update.csv")

pit_id = st.session_state.df['Fomat PIT'].values.tolist()
# get current date
today = date.today()
date_updated = today.strftime("%d-%m-%Y")

with st.form("Form inputs", clear_on_submit=True):
    pits = st.selectbox("Pit ID",pit_id)

    location = st.selectbox("Are the pit address and GPS details correct?", ["Yes", "No", "Update Details - Pit located but address/ GPS details can be improved"])
    access = st.selectbox("Is the pit accessible?", ["Yes", "No"])

    debris = st.selectbox("Is the pit lid free of debris?", ['Yes', 'No'])
    level = st.selectbox("Is the pit lid level with the surrounding ground", ["Yes", "No"])

    pit_lid = st.selectbox("Is the pit lid intact and undamaged?", ["Yes", "Minor Damage", "Damaged/ Unserviceable"])
    collar = st.selectbox("Is the pit collar intact and undamaged?", ["Yes", "Minor Damage", "Damaged/ Unserviceable"])
    lock = st.selectbox("Is the pit lid locked and secure?", ['Yes', 'No'])

    label = st.selectbox("Is the pit labelled as Western Power", ["Yes", "No"])
    pitlok = st.selectbox("Does the PITLOK pit enclosure collar have pit ID tag affixed", ['Yes', 'No'])

    comments = st.text_input("Please add any additional comments.")

    camera_image = st.camera_input("Take a picture")

    submitted = st.form_submit_button("Submit")

    image_counter = 0

    if camera_image is not None:
        img = Image.open(camera_image)
        st.image(img, caption='Uploaded image.', use_column_width=True)
        st.write("")

    if submitted:    
        new_entry = [{'Pit Id' : pits, 'Date' : date_updated, 'Address' : location, 'Accessible' : access, 'Debris Free' : debris, \
            'Lid Level' : level, 'Lid Intact' : pit_lid, 'Collar Intact' : collar, 'Lid Locked' : lock, 'Pit Labelled' : label, \
                'PitLok' : pitlok, 'Comments' : comments}]
        st.session_state.service_update_df = st.session_state.service_update_df.append(new_entry)

        image_counter += 1
        if not os.path.exists(f'data\photos\{pits}'):
            os.makedirs(f'data\photos\{pits}')

        #img.save(f'data\photos\{pits}\{date_updated}.jpg')
        img.save(f'data\photos\{pits}\{date_updated + str(image_counter)}.jpg')
        try:
            st.session_state.service_update_df.to_csv("C:\data\pit_maint\data\service_update.csv", index = False)
            st.caption("Data has been uploaded")

        except PermissionError:
            st.caption("Please close the file and then reclick the Update button. ")

