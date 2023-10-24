import streamlit as st
import cv2
import numpy as np

# Function to apply grayscale transformation
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to apply rotation transformation
def rotate(image, angle):
    rows, cols, _ = image.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(image, rotation_matrix, (cols, rows))

# Function to apply horizontal flip transformation
def flip(image):
    return cv2.flip(image, 1)

# Function to apply resize transformation
def resize(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    return cv2.resize(image, (width, height))

# Streamlit web app
st.title("Image Transformation App")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = cv2.imread(uploaded_image)

    st.image(image, caption="Original Image", use_column_width=True)

    # Transformation options
    st.sidebar.header("Transformations")
    grayscale_option = st.sidebar.checkbox("Grayscale")
    rotate_option = st.sidebar.checkbox("Rotate")
    flip_option = st.sidebar.checkbox("Flip")
    resize_option = st.sidebar.checkbox("Resize")

    if st.button("Apply Transformations"):
        if grayscale_option:
            image = grayscale(image)
        if rotate_option:
            angle = st.sidebar.slider("Rotation Angle (degrees)", -180, 180, 0)
            image = rotate(image, angle)
        if flip_option:
            image = flip(image)
        if resize_option:
            scale_percent = st.sidebar.slider("Resize Scale (%)", 10, 200, 100)
            image = resize(image, scale_percent)

        st.image(image, caption="Transformed Image", use_column_width=True)
