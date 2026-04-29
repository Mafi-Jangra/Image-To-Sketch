🎨 AI Image to Pencil Sketch Converter

A powerful computer vision application that transforms any photo into a professional pencil sketch using mathematical image processing.

🚀 Live Demo

You can view the live application here:

👉 Click here to try the App

✨ Features

Instant Conversion: Process images in real-time.

Dual Support: Works with local PC paths and web uploads.

Downloadable Output: Save your sketch directly as a PNG.

Responsive UI: Clean sidebar and layout built with Streamlit.

🛠️ Installation Steps:

Clone this repository

git clone [https://github.com/Mafi-Jangra/Image-To-Sketch.git](https://github.com/Mafi-Jangra/Image-To-Sketch.git)


Navigate to the project directory:

cd Image-To-Sketch


Create Virtual Environment (Using venv)

python -m venv venv


Activate the virtual environment (On Windows):

venv\Scripts\activate


Install Requirements

pip install -r requirements.txt


Run the application

streamlit run sketch.py


📦 Requirements

streamlit

opencv-python-headless

numpy

Pillow

🧠 How It Works

The application follows a 4-step image processing pipeline:

Grayscale: Removes color information.

Inversion: Flips the pixel values to create a negative.

Gaussian Blur: Softens the edges of the negative image.

Color Dodge: Blends the original grayscale with the blurred negative to highlight edges.

📝 License

Distributed under the MIT License.
