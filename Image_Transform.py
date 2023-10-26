import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to apply grayscale transformation
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to apply horizontal flip transformation
def flip(image):
    return cv2.flip(image, 1)

# Function to apply invert colors transformation
def invert_colors(image):
    return 255 - image  # Invert colors by subtracting each pixel value from 255

# Function to apply blur transformation
def blur(image):
    return cv2.GaussianBlur(image, (7, 7), 0)

# Streamlit web app
st.title("Image Transformation App")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    image = np.array(image)

    st.image(image, caption="Original Image", use_column_width=True)

    # Transformation options
    st.sidebar.header("Transformations")
    grayscale_option = st.sidebar.checkbox("Grayscale")
    flip_option = st.sidebar.checkbox("Flip")
    invert_colors_option = st.sidebar.checkbox("Invert Colors")
    blur_option = st.sidebar.checkbox("Blur")

    if st.button("Apply Transformations"):
        if grayscale_option:
            image = grayscale(image)
        if flip_option:
            image = flip(image)
        if invert_colors_option:
            image = invert_colors(image)
        if blur_option:
            image = blur(image)

        st.image(image, caption="Transformed Image", use_column_width=True)
