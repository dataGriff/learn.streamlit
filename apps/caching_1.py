import streamlit as st
import time

# cache is global across all sessions and all users
@st.cache_data(ttl=60) # cache data for 60 seconds
# if had arguments would cache the outcomes based on those combos
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3) # Delays to mimic an API call
    return {"data" : "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)