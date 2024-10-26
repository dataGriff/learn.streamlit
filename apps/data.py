import streamlit as st
import pandas as pd

st.title("Streamlit Elements Demo")

st.subheader("Dataframe")
df = pd.DataFrame({
    "Name" : ["Alice","Bob","Charlie","David"],
    "Age" : [25,32,37,45],
    "Occupation" : ["Engineer", "Doctor", "Artist", "Chef"]
})
st.dataframe(df)

st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df) # see in console, could save this to db, remember whole script running

st.subheader("Static Table")
st.table(df)

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(),1))

st.subheader("JSON and Dictionary")
sample_dict = {
    "name" : "Alice",
    "age" : 25,
    "skills" : ["Python", "Data Science", "Machine Learning"]
}
st.json(sample_dict)

st.write("Dictionary view:", sample_dict)