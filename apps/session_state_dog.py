import streamlit as st
from enum import Enum

class Breed(Enum):
    GOLDEN_RETRIEVER = "Golden Retriever"
    PUG = "Pug"
    BULLDOG = "Bulldog"
    POODLE = "Poodle"
    STAFFIE = "Staffordshire Bull Terrier"

    def __str__(self):
        return self.value

class Dog:
    def __init__(self, name: str, breed: Breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

if "dog" in st.session_state:
    print("before form dog name:", st.session_state.dog.name)
    print("before form dog breed:",st.session_state.dog.breed)

with st.form(key="sample form"):

    dog_name = st.text_input("What is your dog's name?", key="dog_name")
    dog_breed = st.selectbox("What is your dog's breed?", list(Breed), key="dog_breed")

    st.session_state.dog = Dog(dog_name, dog_breed)

    print(st.session_state.dog.name)
    print(st.session_state.dog.breed)
    st.write(st.session_state.dog.bark())

    st.form_submit_button(label="Submit")