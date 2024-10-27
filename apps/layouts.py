import streamlit as st

st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elemtents like sliders, buttons and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("This is the first tab")

with tab2:
    st.write("This is the second tab")

with tab3:
    st.write("This is the third tab")
    col31  = st.columns(1)[0]
    with col31:
        st.header("This is the first column in tab 3")
        st.write("Content for column 1 tab 3.")

col1, col2 = st.columns(2)
with col1:
    st.header("This is the first column")
    st.write("Content for column 1.")
    st.button("Click me")
with col2:
    st.header("This is the second column")
    st.write("Content for column 2.")

with st.container(border=True):
    st.write("This is a container")
    st.write("You can group elements inside a container")
    st.write("Containers help manage sections of the page")

placeholder = st.empty()
placeholder.write("This is a placeholder, useful for dynamic content")  

if st.button("Update placeholder"):
    placeholder.write("The content of the placeholder was updated")

with st.expander("Click to expand"):
    st.write("This is additional information hidden by default")
    st.write("You can use expanders to keep your interface cleaner")

# only works in browser
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip")

if sidebar_input:
    st.write(f"You entered: {sidebar_input}")




