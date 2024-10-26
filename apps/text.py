import streamlit as st
import os

st.title("Super Simple Title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is **markdown**")
st.caption("small text")
CODE_EXAMPLE = """
def greet(name):
    print('hello')
"""
st.code(CODE_EXAMPLE, language="python")
st.divider()

# cwd - current working directory
# image has lots of properties like width etc
# TODO: test
st.image(os.path.join(os.getcwd(),"static","Staffie.jpg"))