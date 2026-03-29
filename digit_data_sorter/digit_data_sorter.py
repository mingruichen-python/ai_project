from sklearn.datasets import load_digits as ld
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sb
import random as r

pl.style.use("default")

digit = ld()
X = digit.data
y = digit.target
images = digit.images

df = pd.DataFrame(X)
labels = pd.Series(y)

counts = labels.value_counts().sort_index()
mean_image = np.mean(images, axis=0)

pl.figure(figsize=(10,8.6))

pl.subplot(2,3,1)
counts.plot(kind='bar', color='black')
pl.title("Digit Amount")
pl.xlabel("Digit")
pl.ylabel("Count(The amount of them)")

pl.subplot(2,3,3)
sb.heatmap(mean_image, cmap='binary')
pl.title("Average Digit Image")

pl.subplot(2,3,4)
pl.hist(X.flatten(), bins=40, color='black')
pl.title("Pixel Distribution")
pl.xlabel("Pixel")
pl.ylabel("Frequency Of Apearing")

num=r.randint(0,100)
pl.subplot(2,3,6)
pl.imshow(images[num], cmap='gray')
pl.title(f"Digit: {y[num]}")
pl.axis("off")

pl.show()