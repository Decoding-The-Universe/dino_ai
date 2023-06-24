'''
#image resizing

import cv2
x = 100
y=100
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (x, y))
cv2.imshow('hi', img)

cv2.waitKey(0)
'''


from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from numpy import asarray
import numpy as np

def process_input_image(image):
    for i in range(200):
        for j in range(200):
            if image[i][j] < 150:
                image[i][j] = 0
            else:
                image[i][j] = 1


#create model
model = Sequential()
#add model layers

#................change dimensions of layers................
model.add(Conv2D(9, kernel_size=3, activation='relu', input_shape=(200,200, 1)))# 1 says it is grey scale
model.add(Conv2D(4, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(2, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
def predict_move():
    im = np.array(Image.open(r"C:\Users\BASWA HARICHANDANA\Desktop\Dhanush\input_image.jpg"))
    process_input_image(im)
    im = np.asarray(im).reshape(200, 200, 1)
    # print(im.shape)
    # print(np.array([im]))
    im=np.expand_dims(im, 0)
    # image shape should be (1, 200,200, 1)
    output = model.predict(im)
    output= output[0]
    return [output, im]


    # model.predict(im)
