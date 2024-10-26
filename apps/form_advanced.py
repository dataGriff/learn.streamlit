import streamlit as st
from datetime import datetime

st.title("User Information Form")

min_date = datetime(1900, 1, 1)
max_date = datetime.now()

def age (date_of_birth):
    today = datetime.now()
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

with st.form(key="user_info_form"):

    name = st.text_input("Enter your name")
    date_of_birth = st.date_input("Date of Birth",min_value=min_date
                            , max_value=max_date)
    
    st.write(f"Age: {age(date_of_birth)}")

    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if not name or not date_of_birth:
            st.error("Please fill in all the fields")
        else:
            st.success("Form submitted successfully")
            st.balloons()
            st.write(f"Name: {name}")
            st.write(f"Date of Birth: {date_of_birth}")

