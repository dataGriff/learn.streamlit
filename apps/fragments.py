import streamlit as st

st.title("My Awesome App")

# if you want to share data between fragments use session_state

# fragments will run independently
# don't require rerun of entire app!
@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter Text")
    # st.rerun(scope="app") # if added this would rerun entire app, default fragment

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload Image")
    new_cols[2].selectbox("Select Option", ["Option 1", "Option 2", "Option 3"])
    new_cols[3].slider("Select Value", 0, 100, 50)
    new_cols[4].text_input("Enter text")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()