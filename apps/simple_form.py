import streamlit as st
from enum import Enum
from datetime import datetime

st.title("User Information Form")

class Gender(Enum):
    Male = 1
    Female = 2
    Other = 3

form_values = {
    "name": str,
    "height": int,
    "gender" : Gender,
    "dob" : datetime.date
}

min_date = datetime(1900, 1, 1)
max_date = datetime.now()

with st.form(key="user_info_form"):
    # name = st.text_input("Enter your name")
    # age = st.number_input("Enter your age")

    form_values["name"] = st.text_input("Enter your name")
    form_values["height"] = st.number_input("Enter your height (m)")
    form_values["gender"] = st.selectbox("Gender", [e.name for e in Gender])
    form_values["dob"] = st.date_input("Date of Birth",min_value=min_date
                            , max_value=max_date)
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.error("Please fill in all the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key,value) in form_values.items():
                st.write(f"**{key}** : {value}")
    # print(name, age)
    print(form_values)
