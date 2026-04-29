import streamlit as st
import cv2
import numpy as np
import os
from PIL import Image

st.set_page_config(page_title="Pencil Sketcher", layout="wide")
st.title("🎨 Image to Pencil Sketch Converter")

# --- 1. LOCAL PATH SETUP ---
# We keep your path here for local testing
local_path = r'C:\Users\mafij\OneDrive\Documents\Image To Sketch\virat.jpg'

# --- 2. IMAGE SELECTION LOGIC ---
img = None

# First, try to see if we can find the local file (works on your PC)
if os.path.exists(local_path):
    st.sidebar.success("Found local image: virat.jpg")
    img = cv2.imread(local_path)
    source = "Local PC File"
else:
    # If on the web, the local path fails, so we show the uploader
    st.sidebar.info("Running in Cloud Mode")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        source = "Uploaded File"

# --- 3. PROCESSING & DISPLAY ---
if img is not None:
    # Processing steps
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256.0)

    # Display columns
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original")
        st.image(img, channels="BGR", use_container_width=True)
    with col2:
        st.header("Sketch")
        st.image(sketch, use_container_width=True)
    
    st.write(f"Currently displaying: **{source}**")
else:
    st.warning("No image found. Please upload an image using the button above.")