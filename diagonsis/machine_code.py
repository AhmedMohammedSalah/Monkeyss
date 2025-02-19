#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os

# All libraries
from tensorflow import keras
# TensorFlow and tf.keras
import tensorflow as tf
# resnet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from .models import MedicalTest

def update_result (test:MedicalTest):
    img_path = test.image.path
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0) 
    # قم بتحميل النموذج المحفوظ مسبقًا
    

    model_path = r"/home/ahmed/@work25/Monkeyss/diagonsis/my_model"
    if os.path.exists(model_path):
        generated_model = keras.models.load_model(model_path)
    else:
        raise FileNotFoundError(f"Model file not found at {model_path}")    
    img_preprocessed = preprocess_input(img_batch)
    prediction = generated_model.predict(img_preprocessed)
    res =str(prediction)
    if res== "[[0.]]":
        test.result ="The result is positive. You have monkeypox"
        test.save()
    else:
        test.result ="The result is negative. You do not have monkeypox"
        test.save()
    

# In[2]:


# It can be used to reconstruct the model identically.
# in this path the all model is saved 
# generated_model = keras.models.load_model(r"/home/ahmed/Desktop/@work/Django Projects/monkey/monkey-dashboard/src/diagonsis/my_model")

# 0 >> "The result is positive. You have monkeypox"
# 1 >> "The result is negative. You do not have monkeypox"
# In[3]:


# this cell to load & read an image 
# img_path = r"/home/ahmed/Desktop/@work/Django Projects/monkey/results/__results___files/three.jpeg"
# img = image.load_img(img_path, target_size=(64, 64))

# # plt.imshow(img)
# # plt.show()
# # [[0]]>>0 
# # 1 


# # In[4]:


# # this cell to handel or modigy the image to be suitable for the model 
# # يعني الخلية دي عبارة عن تعديلات علي الصورة علشان اعرف ادخلها للموديل 

# img_array = image.img_to_array(img)
# img_batch = np.expand_dims(img_array, axis=0)
# img_preprocessed = preprocess_input(img_batch)


# # In[5]:


# # this cell to predict the modified image 
# prediction = generated_model.predict(img_preprocessed)


# # In[6]:


# 0 ==> Monkeypox
# # 1 ==> Others
# print(prediction)
# pr =str(prediction)#"[[0.]]"
# print (type(pr))

# In[ ]:




