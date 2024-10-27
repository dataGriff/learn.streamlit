import streamlit as st

# seems like filename is only way to change label in sidebar
st.set_page_config(page_title="Home", page_icon=":house:", layout="wide")
st.title("Home")

st.write("To share state between pages use session_state")
st.markdown("[See Multi Page Apps](https://docs.streamlit.io/develop/concepts/multipage-apps/overview)")

# you can do it unofficial way using fragments and a dictionary of
# pages in a sidebar