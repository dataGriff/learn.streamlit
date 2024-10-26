import streamlit as st
import pandas as pd

st.title("Streamlit Form Demo")

# only once press submit will the app re-run in this scenario for form
# the with form holds this behaviour
with st.form(key="sample form"):

    st.subheader("Text Inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Enter your feedback")

    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Select your time of choice")

    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"]) 
    slider_value = st.select_slider("Select a arange", options=range(1, 51))   

    st.subheader("Toggles & Checkboxes")
    notifications = st.checkbox("Receive notifications")
    toggle_value = st.checkbox("Enable to dark mode?", value=False)

    st.form_submit_button(label="Submit")