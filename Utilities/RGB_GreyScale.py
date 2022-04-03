from matplotlib import pyplot as plt

# A function to determine whether the image is grey scale or RGB
def RGBsplit(img):                  # images loaded by opencv are in BGR fromat
    BlueImage = img[:,:,0]          # Blue intensity image
    GreenImage = img[:,:,1]         # Green intensity image
    RedImage = img[:,:,2]           # Red intensity image
    return RedImage, GreenImage, BlueImage

def RGBtoGreyScale(img):
    RedImage, GreenImage, BlueImage = RGBsplit(img)
    Greyimage_1 = (RedImage * 0.299) + (GreenImage * 0.587) + (BlueImage * 0.114)   # weighted method
    Greyimage_2 = (RedImage * 1/3) + (GreenImage * 1/3) + (BlueImage * 1/3)         # average method
    figure, axs = plt.subplots(1, 2, figsize = (12,6) )
    axs[0].imshow(Greyimage_1, cmap = "gray")
    axs[0].set_title("Weighted")
    axs[1].imshow(Greyimage_2, cmap = "gray")
    axs[1].set_title("Average")
    plt.show()

def GreyScale(img):                                                                                         
    if (img.ndim == 2):         # if the number of dimensions of the image = 2 then it is grey scale
        return True
    else:
        return False