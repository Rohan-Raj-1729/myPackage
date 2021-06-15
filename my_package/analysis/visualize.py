#Imports
from PIL import Image, ImageDraw as D
from my_package import ObjectDetectionModel
import numpy as np

def plot_boxes(image, output_): # Write the required arguments
    image=Image.open(image)
    image1=np.array(image)
    h = [[i[0] for i in j] for j in image1]
    w = [[i[1] for i in j] for j in image1]
    x = [[i[2] for i in j] for j in image1]
    a = np.array(255)
    h = h / a
    w = w / a
    x = x / a

    image1 = np.array([x, h, w])
    x=ObjectDetectionModel()
    box,clas,score=x(image1)
    score,box,clas=(list(t) for t in zip(*sorted(zip(score,box,clas),reverse=True)))
    draw = D.Draw(image)
    if len(box)>5:
        for i in range(5):
            draw.rectangle(box[i],fill=None,outline='red',width=1)
            draw.text(box[i][0],clas[i],fill="red",font=None,align="up")
            print(score[0])
    if len(box) <= 5:
        for i in range(box):
            draw.rectangle(box[i], fill=None, outline='red', width=1)
            draw.text(box[i][0], clas[i], fill="red", font=None, align="up")
            print(score[0])

    image.save(output_)
    image.show()
    return image