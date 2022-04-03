import cv2
from cv2 import waitKey
import numpy as np


def Imin_Imax(Img:np.ndarray):
    """Return Min and Max Intnsity(Pixel Value) in the Image
    """
    max=0
    min=255
    for i in range(Img.shape[0]):
        for j in range(Img.shape[1]):
            if Img[i][j] <= min:min=Img[i][j]
            elif Img[i][j] >= max:max=Img[i][j]
    return min,max

# Normalization Equation: I(normalized)=((I-Min)*[(newMax-newMin)/(Max-Min)])+newMin
def Normalize(Img:np.ndarray,newMin=0,newMax=255):
    """scale pixel values of the image to the range newMin-newMax
    mostly used Ranges: (0-1), (0-255)
    Args:
        Img (np.ndarray): Image to be normalized
        newMin (int, optional):desired min value. Defaults to 0.
        newMax (int, optional):desired max value. Defaults to 255.
    """
    min,max = Imin_Imax(Img)
    for i in range(Img.shape[0]):
        for j in range(Img.shape[1]):
            Img[i][j]=(Img[i][j]-min)*(newMax-newMin)/(max-min)
    return Img