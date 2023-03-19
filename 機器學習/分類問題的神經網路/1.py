# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:13:46 2020

@author: USER
"""

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as plt
df = pd.read_csv("./titanic_train.csv")
df1 = pd.read_csv("./titanic_test.csv")
dataset = df.values
dataset1 = df1.values
np.random.shuffle(dataset)
np.random.shuffle(dataset1)
X = dataset[:, 0:9]
Y = dataset[:, 9]
X1 = dataset1[:, 0:9]
Y1 = dataset1[:, 9]
X -= X.mean(axis=0)
X /= X.std(axis=0)
Y = to_categorical(Y)
X1 -= X1.mean(axis=0)
X1 /= X1.std(axis=0)
Y1 = to_categorical(Y1)
model = Sequential()
model.add(Dense(10,input_shape=(9,),activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(2,  activation="softmax"))
model.compile(loss="binary_crossentropy",optimizer="adam", metrics=["accuracy"])
model.fit(X, Y, epochs=150, batch_size=10)
history = model.fit(X, Y,validation_split=0.2,validation_data = (X1, Y1), epochs = 25,batch_size=10)
loss = history.history["loss"]
epochs = range(1, len(loss)+1)
val_loss = history.history["val_loss"]
plt.plot(epochs, loss, "bo", label="Training Loss")
plt.plot(epochs, val_loss, "r", label="Validation Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()
acc = history.history["accuracy"]
epochs = range(1, len(acc)+1)
val_acc = history.history["val_accuracy"]
plt.plot(epochs, acc, "b-", label="Training Acc")
plt.plot(epochs, val_acc, "r--", label="Validation Acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()
loss, accuracy = model.evaluate(X, Y)
print(" 訓練資料集的準確度 ={:.2f}".format(accuracy))
loss, accuracy = model.evaluate(X1, Y1)
print(" 測試資料集的準確度 ={:.2f}".format(accuracy))
Y_pred = model.predict(X1, batch_size=10,verbose=0)
print(Y_pred[0])