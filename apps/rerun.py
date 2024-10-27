import streamlit as st

st.title("Counter Example with Immediate Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    st.session_state.count += 1
    st.rerun() # ensures the write text below is displayed correctly

# we may want this order but currently 
# count wil be lagging behind if don't rerun before get here
# so add rerun to function - feels expensive?
st.write(f"Count = {st.session_state.count}")

if st.button("Increment and update immediately"):
    increment_and_rerun()