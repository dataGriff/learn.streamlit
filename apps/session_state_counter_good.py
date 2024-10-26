import streamlit as st

# session state is for specific user and per refresh cycle of webpage
# if I refresh the page, the session state will be reset
st.session_state.griff = "awesome" # this is a session state variable

print(st.session_state)

if "counter" not in st.session_state:
    st.session_state.counter = 0

# this one behind because of order of rerunning of script
# so where you write state update matters
st.write("Counter: ", st.session_state.counter)

if st.button("Increment"):
    st.session_state.counter += 1
    st.write("Incremented counter: ", st.session_state.counter)

if st.button("Reset"):
    st.session_state.counter = 0