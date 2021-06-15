#Imports
from PIL import ImageFilter, Image
import numpy as np

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius

        

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''
        img = Image.fromarray(image, 'RGB')
        gaussBlur = img.filter(ImageFilter.GaussianBlur(self.radius))
        return np.asarray(gaussBlur)
        

