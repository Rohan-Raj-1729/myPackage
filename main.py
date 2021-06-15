#Imports
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#from my_package.model import ObjectDetectionModel
#from my_package.data import DataSet
#from my_package.analysis import show_boxes
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage

"""
def experiment(annotation_file, detector, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    data = DataSet(annotation_file, transforms)

    #Iterate over all data items.
    ds_list = []
    for i in range(len(data)):
        ds_list.append(data[i]['gt_bboxes'])

    #Get the predictions from the detector.
    allPredictions = [detector(i['image']) for i in ds_list]


    #Draw the boxes on the image and save them.


    #Do the required analysis experiments.
    all_images = []
    my_image = Image.open('./data/imgs/2.jpg')
    my_image.save("original_img.jpg", outputs)
    all_images.append(my_image)
    A = np.asarray(my_image)

    flipped = flip.FlipImage('horizontal')
    image = Image.fromarray(flipped(A), 'RGB')
    image.save("flipped_img.jpg", outputs)
    all_images.append(image)

    blurred = blur.BlurImage(1.7)
    image = Image.fromarray(blurred(A), 'RGB')
    image.save("blurred_img.jpg", outputs)
    all_images.append(image)

    shapeA = A.shape()

    resized2x = rescale.RescaleImage((shapeA[0]*2, shapeA[1]*2))
    image = Image.fromarray(resized2x(A), 'RGB')
    image.save("2x_img.jpg", outputs)
    all_images.append(image)

    resizedHalf = rescale.RescaleImage((shapeA[0]//2, shapeA[1]//2))
    image = Image.fromarray(resizedHalf(A), 'RGB')
    image.save("halfResized_img.jpg", outputs)
    all_images.append(image)

    rotated90CW = RotateImage(-90)
    image = Image.fromarray(rotated90CW(A), 'RGB')
    image.save("rotated90_img.jpg", outputs)
    all_images.append(image)

    rotated45ACW = RotateImage(45)
    image = Image.fromarray(rotated45ACW(A), 'RGB')
    image.save("rotated45_img.jpg", outputs)
    all_images.append(image)

    plt.figure(1)
    for i in range(len(all_images)):
        plt.subplot(7, i, 1)
        plt.imshow(all_images[i])
    
"""
def main():
    #detector = ObjectDetectionModel()
    #experiment('./data/annotations.jsonl', detector, [FlipImage(), BlurImage()], "./Outputs") # Sample arguments to call experiment()


    img = Image.open('./data/imgs/2.jpg')
    A = np.asarray(img)
    image = Image.fromarray(A, 'RGB')
    image.show()

    #cropped = CropImage([1000, 100])
    #image = Image.fromarray(cropped(A), 'RGB')
    #image.show()

    R = RotateImage(90)
    image = Image.fromarray(R(A), 'RGB')
    image.show()
    # F=FlipImage('horizontal')
    # C=CropImage((300,300,))
    #B = BlurImage(1)
    #Re = RescaleImage(100)
    #transforms = [R, B, Re]
    #ds = DataSet("./data/annotations.jsonl", transforms)
    #print(ds[2])



if __name__ == '__main__':
    main()