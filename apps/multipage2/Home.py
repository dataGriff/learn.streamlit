import streamlit as st

# seems like filename is only way to change label in sidebar
st.set_page_config(page_title="Home", page_icon=":house:", layout="wide")
st.title("Home")

st.write("To share state between pages use session_state")