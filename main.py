from numpy import equal
from Utilities.Read_Show import *
from Utilities.Noise import *
from Utilities.Histogram_Distribution import *
from Utilities.Equalization import *
from Utilities.Normalization import *
from Utilities.filters import *
from Utilities.frequencyfilters import *
#from Utilities.kernels import *
#from Utilities.convolve2D import *
# path ="./images/apple.jpg"

path ="./images/lennaGrey.png"

img=Read_Img(path)

# Show_Img("Original",img)

############## 1 ##################
# Show_Img("Salt_Pepper Noise",Salt_Paper_Noise(0.5,img))
# Show_Img("Uniform Noise",Uniform_Noise(0.5,img))
# Show_Img("Gaussian Noise",Gaussian_Noise(0.5,img,Std=100))

# ############ 2 #####################
# Average_filter_img = average_filter(Uniform_Noise(0.5,img),3)
# Show_Img("After Average filter",Average_filter_img)

# Gaussian_filter_img=gaussian_filter(Gaussian_Noise(0.5,img,Std=100),3)
# Show_Img("After gaussian filter",Gaussian_filter_img)

# Median_filter_img=median_Filter(Salt_Paper_Noise(0.5,img),3)
# Show_Img("After Median Filter",Median_filter_img)

############## 3 #######################
# Perwitt_filter_img = perwitt_filter(img2,kernel_size = 3, direction = "xy")
# Show_Img("After Perwitt filter in xy direction",Perwitt_filter_img)

# Roberts_filter_img = roberts_filter(img2, direction = "xy")
# Show_Img("After Roberts filter in xy direction",Roberts_filter_img)

# sobel_filter_img = sobel_filter(img2, kernel_size = 3, direction = "xy")
# Show_Img("After Sobel filter in xy direction",sobel_filter_img)

# canny_filter_img = canny_filter(img2,std = 2, low_ratio=0.05, high_ratio=0.2)
# Show_Img("After Canny filter",canny_filter_img)


############## 4 & 8 ##################

# DistCurve(img)
# Histogram(img)
# RGBtoGreyScale(img)


# ############## 5 ##################
# Show_Img("Equalized",Equalize(img))
# equalized_image = Equalize(img)
# Histogram(equalized_image)
# DistCurve(equalized_image)



# ############## 6 ##################
# Show_Img("Normalized",Normalize(img))
# normalized_image = Normalize(img)
# Histogram(normalized_image)
# DistCurve(normalized_image)


# ############## 7 ##################

# global_threshold_img = global_threshold(img,125)
# Show_Img("After Global Threshold",global_threshold_img)

# local_threshold_img = local_threshold(img,5)
# Show_Img("After local Threshold",local_threshold_img)

################ 9 ########################

# img=cv2.resize(img,(255,255))
# #=== HP filtered Image======#
# hpf_img = high_pass_filter(img)
# Show_Img("hpf img",hpf_img)
# cv2.waitKey(0)
# #=== LP filtered Image======#
# lpf_img = low_pass_filter(img)
# Show_Img("lpf img",lpf_img)

# ############## 10 ##################

# path1 ="./images/lennaGrey.png"
# path2 ="./images/finger.png"
# image1=Read_Img(path1)
# image2=Read_Img(path2)
# Show_Img("image 1",image1)
# Show_Img("image 2",image2)
# Show_Img("Hybrid",hybrid(image1,image2))


cv2.waitKey(0)

print("Done")
