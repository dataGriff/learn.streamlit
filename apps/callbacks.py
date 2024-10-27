import streamlit as st

# callback is triggered before anything else
# so make sure you use if need to happen before stuff on rerun

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

def go_to_step2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2

def go_step1():
    st.session_state.step = 1

if st.session_state.step == 1:
    st.header("part 1: Info")
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))

    ## tuple being passed in which is why comma for args is needed
    ## onclick is a function that will be called when the button is clicked
    ## so happens first now as a callback
    st.button("Next", on_click=go_to_step2, args=(name,))
        
elif st.session_state.step == 2:
    st.header("part 2: Review")
    st.subheader("Please review the information you provided")
    st.write(f"Name: {st.session_state.info.get('name',"")}")

    if st.button("Submit"):
        st.success("Information submitted successfully!")
        st.balloons()
        st.session_state.info = {}

    st.button("Back", on_click=go_step1)
