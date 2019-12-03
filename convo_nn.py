# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:17:01 2019

@author: Aditya Saxena
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import keras

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classifier = Sequential()
 
#CNN_Layer1

classifier.add(Convolution2D(32,(3,3), input_shape= (64,64,3), activation ='relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

#CNN_Layer2

classifier.add(Convolution2D(32,(3,3), activation ='relu'))

classifier.add(MaxPooling2D(pool_size = (2,2)))

#Flattening

classifier.add(Flatten())

#NN_Layer1

classifier.add(Dense(activation = 'relu',units = 128))

#NN_Layer2

classifier.add(Dense(activation = 'sigmoid',units = 1))

#Compile

classifier.compile(optimizer='adam',loss= 'binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=200,
        epochs=25,
        validation_data= test_set,
        validation_steps=800)
