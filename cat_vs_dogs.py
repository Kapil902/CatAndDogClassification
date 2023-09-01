# -*- coding: utf-8 -*-
"""Cat Vs Dogs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zDupBHHXgsnHrni7mHs6TbsUlIEVM9F3
"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

#Directly importing the dataset from kaggle using the personal API key(Can be downloaded from the kaggle profile section)
!kaggle datasets download -d salader/dogs-vs-cats

import zipfile
zip_ref = zipfile.ZipFile('/content/dogs-vs-cats.zip', 'r')
zip_ref.extractall('/content')
zip_ref.close()

#Importing the neccessary Libraries
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,BatchNormalization,Dropout

# generators
train_ds = keras.utils.image_dataset_from_directory(
    directory = '/content/train',
    labels='inferred',
    label_mode = 'int', #cat=0 dog=1
    batch_size=32,
    image_size=(256,256) #Making all images of same size
)
#We are creating a validation dataset from the 'test' directory to evaluate the model's performance on unseen data. This dataset will be used during model
# training to assess how well the model generalizes to images it has not seen before. By specifying the 'image_size' and 'batch_size' parameters, we ensure
# that the validation images are processed in a consistent manner, and their labels are inferred as integers for model evaluation.
validation_ds = keras.utils.image_dataset_from_directory(
    directory = '/content/test',
    labels='inferred',
    label_mode = 'int',
    batch_size=32,
    image_size=(256,256)
)

# Normalize
def process(image,label):
    image = tf.cast(image/255. ,tf.float32)
    return image,label

train_ds = train_ds.map(process)
validation_ds = validation_ds.map(process)
#To make all pixel values between 0 and 1 which are between 0 and 255 in normal case

# create CNN model

model = Sequential()
#32 filter convolution layer
model.add(Conv2D(32 ,kernel_size=(3,3),padding='valid',activation='relu',input_shape=(256,256,3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))
#64 filter convolution layer
model.add(Conv2D(64,kernel_size=(3,3),padding='valid',activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))
#1128 filter convolution layer
model.add(Conv2D(128,kernel_size=(3,3),padding='valid',activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'))

model.add(Flatten())

model.add(Dense(128,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(1,activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

history = model.fit(train_ds,epochs=10,validation_data=validation_ds)

import matplotlib.pyplot as plt
#Checking the accuracy or correctness of the model by plotting the training and validation
plt.plot(history.history['accuracy'],color='red',label='train')
plt.plot(history.history['val_accuracy'],color='blue',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'],color='red',label='train')
plt.plot(history.history['val_accuracy'],color='blue',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['loss'],color='red',label='train')
plt.plot(history.history['val_loss'],color='blue',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['loss'],color='red',label='train')
plt.plot(history.history['val_loss'],color='blue',label='validation')
plt.legend()
plt.show()

import cv2

#Any random cat/dog Image for testing our model
test_img = cv2.imread('/content/dog.jpeg')

plt.imshow(test_img)

test_img.shape

#Resizing the test image
test_img = cv2.resize(test_img,(256,256))

test_input = test_img.reshape((1,256,256,3))

#Predicting the test image(Resized)
model.predict(test_input)