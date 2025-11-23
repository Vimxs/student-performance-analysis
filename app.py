import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("student_performance_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.title("Student Performance Predictor")


gender = st.selectbox("Gender", ["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level = st.selectbox("Parental Level of Education", [
    "associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"
])
lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])


math = st.number_input("Math Score", 0, 100, 70)
reading = st.number_input("Reading Score", 0, 100, 70)
writing = st.number_input("Writing Score", 0, 100, 70)


input_data = pd.DataFrame({
    "gender": [gender],
    "race/ethnicity": [race_ethnicity],
    "parental level of education": [parental_level],
    "lunch": [lunch],
    "test preparation course": [test_prep],
    "math score": [math],
    "reading score": [reading],
    "writing score": [writing]
})


input_encoded = pd.get_dummies(input_data)


input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)


if st.button("Predict Average Score"):
    prediction = model.predict(input_encoded)
    st.success(f" Predicted Average Score: {prediction[0]:.2f}")
