import streamlit as st

# magic commands
st.write("Hello World 1234")
st.write({"key": "value"})
st.write(123)
st.write(True)
3 + 4
"hello griff"
"hello world" if False else "bye"


# see this change in console, button has state, when
# refresh becomes false again
# the entire app runs again when refresh
# when press any of this the entire script reruns so need to understand
# this for the apps - feels like be inefficient??
print("Run ")
pressed = st.button("Pressed me")
print("First", pressed)
pressed2 = st.button("Second button")
print("Second", pressed2)
