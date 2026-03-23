# MNIST Digit Recognition Web App

A lightweight and interactive web application for handwritten digit recognition using a Convolutional Neural Network (CNN). Users can draw digits directly on a canvas, and the model predicts the result in real time.

--

## 🚀 Features

- Real-time digit recognition from a drawing canvas  
- High-accuracy CNN model (99%+)  
- Fast inference and smooth user experience  
- Simple to run and easy to deploy with Streamlit  

---

## 📁 Project Structure

.
├── app.py              # Streamlit web application
├── train_cnn.py        # CNN training script
├── model.pkl           # Serialized Predictor wrapper
├── cnn_model.h5        # Trained TensorFlow CNN model
├── requirement.txt     # Python dependencies
├── README.md           # Project documentation



---

## 🛠 Installation

### 1. Clone the repository

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>



### 2. Install dependencies

pip install -r requirement.txt



---

## 🧪 Training the Model (Optional)

If you want to retrain the CNN model:

python train_cnn.py



This will generate:

- `cnn_model.h5`  
- `model.pkl`

---

## ▶️ Running the Web App

Start the Streamlit app:

streamlit run app.py



Your browser will open automatically at:

http://localhost:8501


---

## ✨ How It Works

1. The user draws a digit on the canvas.  
2. The drawing is converted to a 28×28 grayscale image.  
3. The image is normalized and passed into the CNN model.  
4. The model predicts the digit and displays the result instantly.  

---

## 📦 Dependencies

- Python 3.8+
- TensorFlow
- Streamlit
- NumPy
- Pillow
- streamlit-drawable-canvas

All dependencies are listed in `requirement.txt`.

---

## 📜 License

MIT License
