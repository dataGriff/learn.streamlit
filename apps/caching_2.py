import streamlit as st

file_path = "data/example.txt"

# caching with something mutable that can be changed
# , this is why cache resource
@st.cache_resource
def get_file_handler():
    # open the file in append mode which creates the file if it doesn't exist
    file = open(file_path, "a+")
    return file

# use the cached file handler
file_handler = get_file_handler()

# write to the file using the cached handler
if st.button("Write to file"):
    file_handler.write("Hello, World!\n")
    file_handler.flush()
    st.write("Wrote to file!")

if st.button("Read from file"):
    file_handler.seek(0)
    st.write(file_handler.read())

# once done ths cannot do anything with file anymore
st.button("Close file", on_click=file_handler.close)