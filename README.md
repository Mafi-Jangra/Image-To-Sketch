# 🎨 AI Image to Pencil Sketch Converter

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)

A powerful yet simple computer vision application that transforms any portrait or landscape photograph into a professional-looking pencil sketch using mathematical image processing.

---

## 🚀 Live Demo
You can view the live application here:  
**[Click Here to Try the Live App](https://sketchpy-4e6vfwnqcx88zuzyfzadgn.streamlit.app/)**

---

## ✨ Features
* **Instant Conversion:** Process images in real-time.
* **Hybrid Support:** Works with local hardcoded paths (PC) and browser uploads (Web).
* **Downloadable Output:** Save your sketch directly to your computer.
* **Responsive UI:** Beautiful sidebar and layout built with Streamlit.

---

## 🧠 How It Works (The Logic)
The application follows a 4-step image processing pipeline to simulate a hand-drawn sketch:
1.  **Grayscale:** Converts the input image to black and white to focus on intensity.
2.  **Inversion:** Flips the pixel values (creates a negative).
3.  **Gaussian Blur:** Blurs the negative image to spread out the edges.
4.  **Color Dodge:** Blends the original grayscale image with the blurred negative to highlight the contrast lines (the "sketch").



---

## 🛠️ Installation & Local Setup

### 1. Clone the repository
```bash
git clone [https://github.com/Mafi-Jangra/Image-To-Sketch.git]
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
#Install Dependencies
pip install -r requirements.txt
#Run the App
streamlit run sketch.py
## 📂 Requirements
- streamlit
- opencv-python-headless
- numpy
- Pillow