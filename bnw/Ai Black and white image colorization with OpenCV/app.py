#!/usr/bin/env python
# coding: utf-8

import numpy as np
import cv2
import streamlit as st
from PIL import Image

# Function to convert any image to black & white
def convert_to_black_and_white(img):
    """Convert any image (color or grayscale) to black and white (grayscale)."""

    # Convert RGBA (4 channels) to RGB (3 channels) if needed
    if img.shape[-1] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Convert back to 3-channel grayscale image for display
    img_gray_3ch = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

    return img_gray_3ch


# Streamlit UI
st.set_page_config(page_title="Convert Image to Black & White", layout="wide")
st.title("🖼️ Convert Images to Black & White")
st.write("Upload an image to convert it to **black and white** (grayscale).")

# File uploader
file = st.sidebar.file_uploader("Upload an image file (JPG/PNG)", type=["jpg", "png"])

# If no file is uploaded, show a message
if file is None:
    st.warning("⚠️ Please upload an image file to proceed.")
else:
    # Open image and convert to numpy array
    image = Image.open(file)
    img = np.array(image)

    # Create two columns for comparison
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌈 Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("⚫ Converted Black & White Image")
        try:
            bw_image = convert_to_black_and_white(img)
            st.image(bw_image, use_container_width=True)
            st.success("✅ Conversion successful!")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
