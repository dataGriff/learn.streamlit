import streamlit as st
from enum import Enum
from pydantic import BaseModel, Field, ValidationError

# Constants for validation
MIN_AGE = 0
MAX_AGE = 20
MAX_NAME_LENGTH = 20

class Breed(Enum):
    GOLDEN_RETRIEVER = "Golden Retriever"
    PUG = "Pug"
    BULLDOG = "Bulldog"
    POODLE = "Poodle"
    STAFFIE = "Staffordshire Bull Terrier"

    def __str__(self):
        return self.value

class Dog(BaseModel):
    name: str = Field(..., max_length=MAX_NAME_LENGTH, description="The dog's name (20 chars max)")
    breed: Breed = Field(..., description="The dog's breed")
    age: int = Field(..., ge=MIN_AGE, le=MAX_AGE, description="The dog's age in years")

with st.form(key="sample_form"):
    dog_name = st.text_input("What is your dog's name?", key="dog_name")
    dog_breed = st.selectbox("What is your dog's breed?", list(Breed), key="dog_breed")
    dog_age = st.number_input("What is your dog's age?", key="dog_age", min_value=MIN_AGE, max_value=MAX_AGE)

    try:
        # Validate using the Pydantic model directly
        st.session_state.dog = Dog(name=dog_name, breed=dog_breed, age=dog_age)
    except ValidationError as e:
        st.error(e)

    submit_button = st.form_submit_button(label="Submit")
    dog_values = st.session_state.dog.dict()

    if submit_button:
        if not all(dog_values):
            st.error("Please fill in all the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key,value) in dog_values.items():
                st.write(f"**{key}** : {value}")
    # print(name, age)
    print(dog_values)
