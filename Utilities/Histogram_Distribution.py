import numpy as np
from matplotlib import pyplot as plt
from Utilities.RGB_GreyScale import *
from Utilities.Equalization import *




def DistCurve(img):                                                       
    # Grey image
    if (GreyScale(img)):                                                       
        intensities      = np.arange(256)                                 # array of intensities    
        intensitiesFreq  = histogram(img)                                 # calculate the frequency of each intensity from 0 to 2555
        plt.plot(intensities, intensitiesFreq, color = 'black')
        plt.xlabel('Intensities')
        plt.ylabel('Frequency')
        plt.title('Distribution curve')
        plt.show()
    # RGB image
    else:                                                                
        Red, Green, Blue = RGBsplit(img)
        # print(Red, Green, Blue)
        RintensitiesFreq  = histogram(Red) 
        GintensitiesFreq  = histogram(Green)  
        BintensitiesFreq  = histogram(Blue)                       
        intensities      = np.arange(256)                       
        plt.plot(intensities, RintensitiesFreq, color = 'r', label = "RED")
        plt.plot(intensities, GintensitiesFreq, color = 'g', label = "GREEN")
        plt.plot(intensities, BintensitiesFreq, color = 'b', label = "BLUE")
        plt.xlabel('Intensities')
        plt.ylabel('Frequency')
        plt.title('Distribution curve')
        plt.legend()
        plt.show()

def Histogram(img):
    # Grey image
    if (GreyScale(img)):
        # number of bins with width of 5
        # 256/4 = 64 bin 
        binsNum      = np.arange(64)    
        # fequency of each bin
        binsHeight   = [0] * 64
        i = 0
        for bin in binsNum:
            limit1 = i
            limit2 = i+4
            binsHeight[bin] = np.count_nonzero( img >= limit1 ) - np.count_nonzero( img > limit2 )
            i = i + 4
        plt.bar(binsNum, binsHeight,  color = ['grey'])
        plt.xlabel('Bins')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.show()
    # RGB image
    else:
        Red, Green, Blue = RGBsplit(img)
        binsNum      = np.arange(64)
        RbinsHeight   = [0] * 64
        GbinsHeight   = [0] * 64
        BbinsHeight   = [0] * 64
        limit1 = 0
        limit2 = 3
        for bin in binsNum:
            RbinsHeight[bin] = np.count_nonzero( Red >= limit1 ) - np.count_nonzero( Red > limit2 )
            GbinsHeight[bin] = np.count_nonzero( Green >= limit1 ) - np.count_nonzero( Green > limit2 )
            BbinsHeight[bin] = np.count_nonzero( Blue >= limit1 ) - np.count_nonzero( Blue > limit2 )
            limit1 += 4
            limit2 += 4
        plt.bar(binsNum, RbinsHeight,  color = ['red'], label = "red", alpha = 0.7)
        plt.bar(binsNum, GbinsHeight,  color = ['green'], label = "green", alpha = 0.7)
        plt.bar(binsNum, BbinsHeight,  color = ['blue'], label = "blue", alpha = 0.7)
        plt.xlabel('Bins')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.legend()
        plt.show()
