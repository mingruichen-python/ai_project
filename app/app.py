import streamlit as st
import numpy as np
import pickle
from PIL import Image
from streamlit_drawable_canvas import st_canvas

def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

st.title("MNIST Digit Recognition")
st.write("Draw a digit below.")

canvas = st_canvas(
    fill_color="#000000",
    stroke_width=10,
    stroke_color="#FFFFFF",
    background_color="#000000",
    width=200,
    height=200,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas.image_data is not None:
    img = Image.fromarray(canvas.image_data.astype("uint8")).convert("L")
    img = img.resize((28, 28))
    img_array = np.array(img).reshape(1, -1) / 255.0
    pred = model.predict(img_array)[0]
    st.subheader(f"Prediction: {pred}")
