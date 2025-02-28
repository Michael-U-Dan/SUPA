
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# Streamlit app page a title
st.title("Supermarket Quantity Value Predictor" )

# input widget for getting user values for X (feature matrix value)
Unit_price = st.slider("Unit price", min_value=0, max_value=100, value=20)
Rating = st.slider("Rating", min_value=0, max_value=100, value=20)
Total = st.slider("Total", min_value=0, max_value=100, value=20)

# After selesting quantity, the user then submits the price value
if st.button("Predict"):
  # take the rating value, and format the value the right way
  prediction = model.predict([[Unit_price , Rating, Total]])[0].round(2)
  st.write("The predicted supermarket Quantity is", prediction)
