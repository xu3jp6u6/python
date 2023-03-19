# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:43:24 2020

@author: USER
"""

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
df = pd.read_csv("./boston_housing.csv")
print(df.head())
dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:13]
Y = dataset[:, 13]
X -= X.mean(axis=0)
X /= X.std(axis=0)
X_train, Y_train = X[:404], Y[:404]     
X_test, Y_test = X[404:], Y[404:]
def build_model():
    model = Sequential()
    model.add(Dense(32, input_shape=(X_train.shape[1],), activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam", metrics=["mae"])
    return model
k = 4
nb_val_samples = len(X_train) // k
nb_epochs = 80
mse_scores = []
mae_scores = []
for i in range(k):
    print("Processing Fold #" + str(i))
    X_val = X_train[i*nb_val_samples: (i+1)*nb_val_samples]
    Y_val = Y_train[i*nb_val_samples: (i+1)*nb_val_samples]
    X_train_p = np.concatenate([X_train[:i*nb_val_samples], X_train[(i+1)*nb_val_samples:]], axis=0)
    Y_train_p = np.concatenate([Y_train[:i*nb_val_samples], Y_train[(i+1)*nb_val_samples:]], axis=0)
model = build_model()
model.fit(X_train_p, Y_train_p, epochs=nb_epochs, batch_size=16, verbose=0)
mse, mae = model.evaluate(X_val, Y_val)
mse_scores.append(mse)
mae_scores.append(mae)


     