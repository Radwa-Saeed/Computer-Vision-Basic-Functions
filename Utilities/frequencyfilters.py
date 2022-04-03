
import cv2
import numpy as np
import matplotlib.pyplot as plt

def kernels(type):
    """
    Generate ideal lowpass and highpass filters:
    define kernels of 255*255 of zeros and ones in center in case of type "lp_filter"
    define kernels of 255*255 of ones and zeros in center in case of type "hp_filter"

    """
    if type=="lp_filter":
         filters=np.zeros([255,255],dtype=int)
         filters[126:153,126:153]=np.ones([27,27],dtype=int)
    elif(type=="hp_filter"):
        filters=np.ones([255,255],dtype=int)
        filters[126:153,126:153]=np.zeros([27,27],dtype=int)
    return filters



def frequency_filter(source: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
        Application of a Filter in frequency domain
    :param source: Source Image
    :param kernel: Kernel applied on image
    :return: Filtered Image
    """
    src = np.copy(source)

    # Convert Image to Frequency Domain
    # and decentralize the output
    originfilter = np.fft.fft2(src)
    filter_shifted = np.fft.fftshift(originfilter)

    # apply Kernel
    output_filter = np.fft.ifftshift(filter_shifted * kernel)
    output_filter = np.fft.ifft2(output_filter)

    return np.abs(output_filter)
    # return out


def high_pass_filter(source: np.ndarray) -> np.ndarray:
    """
    Frequency Domain High Pass Filter
    :param source: Source Image
    :return: Filtered Image
    """
    # When 0 is placed inside, we get edges 
    hp_kernel=kernels(type="hp_filter")
    # Apply Kernel
    output_filter = frequency_filter(source, hp_kernel)
    return output_filter.astype(np.uint8)


def low_pass_filter(source: np.ndarray) -> np.ndarray:
    """
    Frequency Domain Low Pass Filter
    :param source: Source Image
    :return: Filtered Image
    """
    # Create Kernel with ones on the edges for low frequencies


    # When one is placed inside and the zero is placed outside , we got a blurred image. 
    # Now as we increase the size of 1, blurring would be increased and the edge content would be reduced.
    lp_kernel=kernels(type="lp_filter")
    # Apply Kernel
    output_filter = frequency_filter(source, lp_kernel)
    return output_filter.astype(np.uint8)

def hybrid(image1 , image2):
    resized_image1 = cv2.resize(image1, (255,255))
    resized_image2= cv2.resize(image2, (255,255))
    img1 = low_pass_filter(resized_image1)
    img2 = high_pass_filter(resized_image2)
    hybrid_image = img1 + img2
    return hybrid_image 






