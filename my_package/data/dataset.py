# Imports
import json
from PIL import Image
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotations_path = annotation_file
        self.transforms =transforms
    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        a = open(self.annotations_path)
        a = list(a)
        return len(a)
    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following,
            1. Extract the correct annotation using the idx provided.
            2. Read the image and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the array would be (3, H, W).
            3. Scale the values in the array to be with [0, 1].
            4. Create a dictonary with both the image and annotations
            4. Perform the desired transformations.
            5. Return the transformed image and annotations as specified.
        '''
        a = open(self.annotations_path)
        a = list(a)
        a_list = []
        for i in a:
            a_list.append(json.loads(i))
        #for i in a_list:
            #   print(i)
        line_ = a_list[idx]
        img_path = 'd:/PythonPrograms/DS_Asg2/data/' + line_['img_fn']
        image = Image.open(img_path)
        for i in self.transforms:
            image = i(np.asarray(image))

        h = [[i[0] for i in j] for j in image]
        w = [[i[1] for i in j] for j in image]
        x = [[i[2] for i in j] for j in image]
        a = np.array(255)
        h = h / a
        w = w / a
        x = x / a
        image1 = np.array([h, w, x])

        result = {}
        result['image'] = image1
        stringB = line_['bboxes']
        cat = [j['category'] for j in stringB]
        ar = []
        ar = [[k for k in j['bbox']] for j in stringB]

        gtb = {}
        for i in range(len(cat)):
            gtb[cat[i]] = ar[i]
        result['gt_bboxes'] = gtb
        return result

