import streamlit as st
import pickle

df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# brand
Name = st.selectbox('Name of the Food', df['Name'].unique())

# type of laptop
C_Type = st.selectbox('C_Type', df['C_Type'].unique())

Veg_Non = st.selectbox('Non Veg or Veg', df['Veg_Non'].unique())