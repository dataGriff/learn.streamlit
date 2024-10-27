import streamlit as st

st.set_page_config(page_title="Page One")
st.title("Page 1")
# to persist the below between pages use session state otherwise disappears
st.text_input("Enter your name", "Type Here ...")