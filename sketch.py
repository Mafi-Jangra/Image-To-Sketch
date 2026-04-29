import streamlit as st
import cv2
import numpy as np
import os

# 1. Page Setup
st.set_page_config(page_title="My Sketch App", layout="wide")
st.title("🎨 Image to Pencil Sketch: Local PC Version")

# 2. YOUR EXACT PC PATH
# Update 'your_photo.jpg' to the actual name of your image file
image_folder = r'C:\Users\mafij\OneDrive\Documents\Image To Sketch'
image_name = 'virat.jpg' # <--- CHANGE THIS to your filename (e.g., 'test.jpg')
full_path = os.path.join(image_folder, image_name)

# 3. Processing Logic
if os.path.exists(full_path):
    # Read the image from your PC
    img = cv2.imread(full_path)
    
    # Convert to Sketch
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256.0)

    # 4. Display on the Web Page (The blank screen you saw)
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Original Image")
        # OpenCV uses BGR, Streamlit needs RGB or it looks blue
        st.image(img, channels="BGR", use_container_width=True)
        
    with col2:
        st.header("Pencil Sketch")
        st.image(sketch, use_container_width=True)
        
    st.success(f"Successfully loaded: {image_name}")

else:
    st.error("Image Not Found!")
    st.write(f"I am looking for the image here: `{full_path}`")
    st.info("Check if the filename inside the code matches your actual image file name.")