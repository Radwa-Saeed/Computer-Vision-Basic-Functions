import numpy as np
import cv2

def histogram(image):
    Count =np.zeros(shape=(256,1))  #from 0 to 255
    s = image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            image_pixel = image[i,j]
            Count[image_pixel,0] += 1
    return Count

def Cumalative_dist (image):
    # calculate the image histogram
    hist = histogram(image)
    x = hist.reshape(1,256)
    y = np.array([])
    y=np.append(y,x[0,0])
    s=image.shape
    for i in range(255):
       nx = x[0 ,i+1] + y[i] #number of pixels
       y = np.append(y,nx) 
    CDF = (y/(s[0]*s[1]))
    return CDF

def Equalize(image):
    s=image.shape
    CDF = Cumalative_dist(image)
    L = 256
    y = np.round(CDF*(L-1))
    for i in range(s[0]):
        for j in range (s[1]):
            #change every pixel value in image array to value present in y array
            new_value = image[i,j]
            image[i,j] = y[new_value]
    return image
    # print('equ' , image)
    # cv2.imshow('Equalized image' , image)
