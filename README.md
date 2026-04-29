# 🎨 AI Image to Pencil Sketch Converter

This project transforms any photo into a professional pencil sketch using Python and OpenCV.

## 🚀 Live Link
[Add your Streamlit URL here after you deploy]

## 🛠️ How to Run Locally
1. Activate your virtual environment:
   `.\venv\Scripts\activate`
2. Install libraries:
   `pip install -r requirements.txt`
3. Run the app:
   `streamlit run sketch.py`

## 🧠 The Logic
The app uses a 4-step process:
1. **Grayscale:** Removes color.
2. **Inversion:** Flips the image colors.
3. **Blurring:** Softens the edges.
4. **Dodge Blend:** Combines the layers to create the sketch effect.



## 📂 Requirements
- streamlit
- opencv-python-headless
- numpy
- Pillow