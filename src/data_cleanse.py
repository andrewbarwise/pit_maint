import pandas as pd
import streamlit as st

path_to_file = "C:\data\pit_maint\data\pit_location.xlsx"

def data(path_to_file):
    # read file
    req_cols = 'A,B,C,F'
    df = pd.read_excel(path_to_file, usecols = req_cols, engine = "openpyxl")
    return df
