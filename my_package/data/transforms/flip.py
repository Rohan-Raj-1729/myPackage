
import numpy as np
class FlipImage(object):
    def __init__(self, flip_type='horizontal'):
        self.flip_type = flip_type

    def __call__(self, image):
        if self.flip_type == 'horizontal':
            flippedH = np.asarray([i[::-1] for i in image])
            return flippedH
        elif self.flip_type == 'vertical':
            flippedV = image[::-1]
            return flippedV
       