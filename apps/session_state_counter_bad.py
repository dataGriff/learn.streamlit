import streamlit as st

# This is a bad way to use session state
# It will not work as expected
# The counter will always be 0
# This is because the session state object is created
# every time the script is run (increment button pressed)
counter = 0

st.write("Counter: ", counter)

if st.button("Increment"):
    counter += 1
    st.write("Incremented counter: ", counter)
else:
    st.write("Counter stays at: ", counter)