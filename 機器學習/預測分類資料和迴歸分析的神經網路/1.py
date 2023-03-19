# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:48:46 2020

@author: USER
"""

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
df = pd.read_csv("./iris_data.csv")
print(df.shape)
print(df.head())
print(df.describe())
dataset = df.values
np.random.shuffle(dataset)
X= dataset[:, 0:4]
Y= dataset[:, 4]
Y = to_categorical(Y)
X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:] 
model = Sequential()
model.add(Dense(6,input_shape=(4,),activation="softmax"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="sigmoid"))
model.summary()
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train, Y_train, epochs=100, batch_size=5)
loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))
Y_pred = model.predict(X_test)
Y_pred = np.argmax(Y_pred, axis=1)
print(Y_pred)
Y_target = dataset[:,4][120:].astype(int)
print(Y_target)
tb=pd.crosstab(Y_target, Y_pred, rownames= ["label"], colnames=["predict"])
print(tb)
