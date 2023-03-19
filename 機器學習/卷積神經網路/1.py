#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
print(X_train[0])
print(Y_train[0])


# In[2]:


import matplotlib.pyplot as plt

plt.imshow(X_train[0], cmap="gray")
plt.title("Label: " + str(Y_train[0]))
plt.axis("off")
plt.show()


# In[3]:


sub_plot= 330
for i in range(0, 9):
	ax = plt.subplot(sub_plot+i+1)
	ax.imshow(X_train[i], cmap="gray")
	ax.set_title("Label: " + str(Y_train[i]))
	ax.axis("off")

plt.subplots_adjust(hspace = .5)
plt.show()


# In[39]:


from keras.models import Sequential
from keras.layers import Dense
import keras
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
Y_train = keras.utils.to_categorical(Y_train)
Y_test = keras.utils.to_categorical(Y_test)
model = Sequential()
model.add(Dense(256,input_shape=(784,),activation="relu"))
model.add(Dense(10,  activation="softmax"))
model.compile(loss="categorical_crossentropy",optimizer="adam", metrics=["accuracy"])
history = model.fit(X_train, Y_train,validation_data = (X_test, Y_test), epochs = 150,verbose=1,batch_size=10)


# In[41]:


import matplotlib.pyplot as plt
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


# In[45]:


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


# In[ ]:




