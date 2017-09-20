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

describers = open(r"""C:\Projects\python_projects\MachineLearning\Integrador\describers_test.txt""", "a")

try:
    count = 0
    files = os.listdir(path)

    for image in files:
        gray = toGray(cv2.imread(dirImg(image)))
        kps, descs = sift.detectAndCompute(gray, None)

        count = count + 1
        #print(count)
        print(descs[0])

        # escrevendo descritor no arquivo
        describers.write("\n{}".format(descs[0]))
except:
    print("Error")


describers.close
