import numpy as np

# Signal To Noise Ratio (SNR) ==> Noisy_Image = Input_Image*SNR + Noise*(1-SNR)
def Salt_Paper_Noise (SNR:float,Img:np.ndarray):
    """
    (SNR=0): Img << Noise  -- (SNR=0): Img = Noise -- (SNR=0.5): Img/Noise = 0.5
    """
    # Additive Noise Mask of (0,1,2) with Propabilities of [(1-SNR)/2 ,(1-SNR)/2 ,SNR] Respectively, with the same Size of the img
    Noise_Mask = np.random.choice(a=(0,1,2) ,size=Img.shape, p=[(1-SNR)/2 ,(1-SNR)/2 ,SNR])
    # Pepper Pixels where Pixel = 0
    Img[Noise_Mask==0]=0
    # Salt Pixels where Pixel = 255
    Img[Noise_Mask==1]=255
    return Img

def Uniform_Noise (SNR:float,Img:np.ndarray):
    """
    (SNR=0): Img << Noise  -- (SNR=0): Img = Noise -- (SNR=0.5): Img/Noise = 0.5 
    """
    # Additive Noise Mask Uniformally Distributed from -255 to +255, with the same Size of the img
    Noise_Mask = np.random.uniform (low=-255 ,high=255 ,size=Img.shape )
    # Appling the Mask with respect to SNR => Noisy_Image = Input_Image*SNR + Noise*(1-SNR)
    Noisy_Image = Img*SNR + Noise_Mask*(1-SNR) 
    # limiting the Noisy_Image to the original Intensity range => (0:255)  
    for i in range(Noisy_Image.shape[0]):
        for j in range(Noisy_Image.shape[1]):
            if Noisy_Image[i][j] <= 0 :
                Noisy_Image[i][j]= 0
            elif Noisy_Image[i][j]>=255:
                Noisy_Image[i][j]= 255
    return Noisy_Image

def Gaussian_Noise(SNR:float, Img:np.ndarray, Mean=0, Std=50):
    """
    (SNR=0): Img << Noise  -- (SNR=0): Img = Noise -- (SNR=0.5): Img/Noise = 0.5 
    The Higher The Standard Deviation => The Wider The Curve Is
    """
    # Additive Noise Mask Gaussian Distributed with µ=0 and σ=std 
    Noise_Mask=np.random.normal(loc=Mean,scale=Std,size=Img.shape)
    # Appling the Mask with respect to SNR => Noisy_Image = Input_Image*SNR + Noise*(1-SNR)
    Noisy_Image = Img*SNR + Noise_Mask*(1-SNR) 
    # limiting the Noisy_Image to the original Intensity range => (0:255)  
    for i in range(Noisy_Image.shape[0]):
        for j in range(Noisy_Image.shape[1]):
            if Noisy_Image[i][j] <= 0 :
                Noisy_Image[i][j]= 0
            elif Noisy_Image[i][j]>=255:
                Noisy_Image[i][j]= 255
    return Noisy_Image




# def Salt_Pepper_Noise(img):
# 	row , col = img.shape
#     # Salt pixels
# 	number_of_pixels = random.randint(300, 10000)
# 	for i in range(number_of_pixels):	
# 		y_coord=random.randint(0, row - 1)
# 		x_coord=random.randint(0, col - 1)
# 		img[y_coord][x_coord] = 255
#     # Papper pixels
# 	number_of_pixels = random.randint(300 , 10000)
# 	for i in range(number_of_pixels):
# 		y_coord=random.randint(0, row - 1)
# 		x_coord=random.randint(0, col - 1)
# 		img[y_coord][x_coord] = 0	
# 	return img

# def sp_noise(image,prob):
#     output=np.zeros(image.shape, np.uint8)
#     thres = 1 - prob
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = 0
#             elif rdn > thres:
#                 output[i][j] = 255
#             else:
#                 output[i][j] = image[i][j]
#     return output


