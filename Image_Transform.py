import streamlit as st
import cv2
import numpy as np

# Function to perform image transformations
def apply_transformations(image, operation):
    if operation == "Grayscale":
        transformed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif operation == "Blur":
        transformed = cv2.GaussianBlur(image, (7, 7), 0)
    elif operation == "Rotate 90°":
        transformed = np.rot90(image)
    elif operation == "Flip":
        transformed = cv2.flip(image, 1)  # 1 flips horizontally, 0 flips vertically

    return transformed

st.title("Image Transformation App")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
    st.image(image, caption="Original Image", use_column_width=True)

    # Choose transformation
    transformation = st.selectbox("Select Transformation", ["Grayscale", "Blur", "Rotate 90°", "Flip"])
    
    if st.button("Apply Transformation"):
        transformed_image = apply_transformations(image, transformation)
        st.image(transformed_image, caption=f"{transformation} Image", use_column_width=True)
