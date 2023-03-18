import tensorflow as tf
from tensorflow import keras
import matplotlib
import numpy as np

dataset= tf.keras.datasets.fashion_mnist
(train_images,train_label),(test_images,test_label )=dataset.load_data()
index = 0 
np.set_printoptions(linewidth=320)
print(f'LABEL : {train_label[index]}')
print(f'\nImage Pixel Array :\n {train_images[index]}')