import streamlit as st

st.button("Ok")
st.button("Ok", key="btn2") # key uniquely identifies the state of this button
# good practice to add keys to your widget elements

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("Set min value", 0, 50, 25)
st.session_state.slider = st.slider("Slider",min_value, 100, st.session_state.slider)

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

## using callback on_change
st.checkbox("Show Input Field", value=st.session_state.checkbox
            , on_change=toggle_input)

# when remove a component, the state is also removed!
# so set the text input to be the session state value to maintain it
if st.session_state.checkbox:
    user_input = st.text_input("Enter some text", value=st.session_state.user_input)
    st.session_state.user_input = user_input
    st.write(f"User input: {user_input}")
else:
    user_input = st.session_state.get("user_input", "")