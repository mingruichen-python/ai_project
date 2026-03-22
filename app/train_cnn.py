import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import pickle

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

model = Sequential()
model.add(Conv2D(128, (3, 3), activation="relu", input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation="relu"))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=10, batch_size=64)

model.save("cnn_model.h5")

class Predictor:
    def __init__(self):
        self.m = tf.keras.models.load_model("cnn_model.h5")
    def predict(self, x):
        x = x.reshape(-1, 28, 28, 1)
        p = self.m.predict(x)
        return np.argmax(p, axis=1)

pred = Predictor()

with open("model.pkl", "wb") as f:
    pickle.dump(pred, f)
