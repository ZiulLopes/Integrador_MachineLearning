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
    return "horse/{}".format(img)


path = r"""C:\Projects\python_projects\MachineLearning\Integrador\horse"""

listImage = []
sift = cv2.xfeatures2d.SIFT_create()

describers = open(r"""C:\Projects\python_projects\MachineLearning\Integrador\describers_horse.txt""", "a")

try:
    files = os.listdir(path)

    for image in files:
        gray = toGray(cv2.imread(dirImg(image)))
        kps, descs = sift.detectAndCompute(gray, None)
        listImage.append("{}".format(descs[0]))
        for line in listImage:
            describers.write("{}".format(line))
            print(line)

        describers.close
except:
    print("Error")
