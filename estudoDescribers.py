"""
    Implementação MachineLearning
    by: Luiz
"""

# import libs
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# functions
def toGray(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def dirImg(img):
    return "cow_horse/{}".format(img)

def HistogramHGC(image):
    rows, cols, channels = image.shape
    histogram_b = np.zeros(4)
    histogram_g = np.zeros(4)
    histogram_r = np.zeros(4)

    for row in range(rows):
        for col in range(cols):
            pixel_b = image[row, col, 0] / 64
            pixel_g = image[row, col, 1] / 64
            pixel_r = image[row, col, 2] / 64
            histogram_b[int(pixel_b)] = histogram_b[int(pixel_b)] + 1
            histogram_g[int(pixel_g)] = histogram_g[int(pixel_g)] + 1
            histogram_r[int(pixel_r)] = histogram_r[int(pixel_r)] + 1

    vector_features = np.append(histogram_b, histogram_g)
    return np.append(vector_features, histogram_r)


path = r"""C:\Projects\python_projects\MachineLearning\Integrador\cow_horse"""

listImage = []

describers = open(r"""C:\Projects\python_projects\MachineLearning\Integrador\describers_cow_horse.txt""", "a")

try:
    count = 0
    files = os.listdir(path)

    for image in files:
        count = count + 1
        
        features = HistogramHGC(cv2.imread(dirImg(image)))
        print("image {}\n{}".format(image, features))

        # escrevendo descritor no arquivo
        #describers.write("\n{}".format(features))
except:
    print("Error")


describers.close
