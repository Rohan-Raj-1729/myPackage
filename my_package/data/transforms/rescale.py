#Imports
import numpy as np
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        self.size = output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        h0 = image.shape[0]
        w0 = image.shape[1]
        if isinstance(self.size, int):
            if h0 > w0:
                new_size = ()
                w = self.size
                h = (h0*w)//w0
                new_size = (w, h)

            else:
                new_size = ()
                h = self.size
                w = (w0*h)//h0
                new_size = (w, h)
            print(new_size)
        else:
            new_size = self.size[::-1]
        return np.asarray(Image.fromarray(image).resize(new_size))
        #return np.image.resize(self.size)
        # Write your code here