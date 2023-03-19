# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:47:13 2021

@author: USER
"""

import numpy as np
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Dense, Input
seed = 7
np.random.seed(seed)
(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0],28*28).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28*28).astype("float32")
X_train = X_train / 255
X_test = X_test / 255
input_img = Input(shape=(784,))
x = Dense(128, activation="relu")(input_img)
encoded = Dense(64, activation="relu")(x)
x = Dense(128, activation="relu")(encoded)
decoded = Dense(784, activation="sigmoid")(x)
autoencoder = Model(input_img, decoded)
encoder = Model(input_img, encoded)
decoder_input = Input(shape=(64,))
decoder_layer = autoencoder.layers[-2](decoder_input)
decoder_layer = autoencoder.layers[-1](decoder_layer)
decoder = Model(decoder_input, decoder_layer)
autoencoder.compile(loss="binary_crossentropy",
optimizer="adam", metrics=["accuracy"])
autoencoder.fit(X_train, X_train, validation_data=(X_test,X_test), epochs=10, batch_size=256, shuffle=True,verbose=2)
encoded_imgs = encoder.predict(X_test)
decoded_imgs = decoder.predict(encoded_imgs)
import matplotlib.pyplot as plt
n = 10  # how many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(X_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
