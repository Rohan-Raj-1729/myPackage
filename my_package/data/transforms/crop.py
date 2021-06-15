#Imports
import numpy as np
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.crop_type = crop_type
        self.shape = shape

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''



        if self.crop_type=="center":
            h0 = int(image.shape[0] / 2)
            w0 = int(image.shape[1] / 2)
            h = int(self.shape[0] / 2)
            w = int(self.shape[1] / 2)

            h = min(h, h0)
            w = min(w, w0)

            ccropped = image[h0-h:h0+h, w0-w:w0+w]
            return np.asarray(ccropped)
        elif self.crop_type=="random":
            h0 = int(image.shape[0])
            w0 = int(image.shape[1])
            h = random.randint(0, h0 - self.shape[0])
            w = random.randint(0, w0 - self.shape[1])

            h = min(h,h0)
            w = min(w,w0)

            rcropped = image[h:h + h0, w:w + w0]
            return np.asarray(rcropped)


        

 