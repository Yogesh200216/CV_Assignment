import streamlit as st
import cv2
# Streamlit app title
st.title("First Name Printer")

# Input for the first name
first_name = st.text_input("Enter your first name:")

# Print the first name when a value is entered
if first_name:
    st.write(f"Your first name is: {first_name}")
