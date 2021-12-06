#!/usr/bin/python3

from skimage import data,io
from matplotlib import pyplot as plt

# image = data.coffee()
image2 = io.imread(fname='../data/lena.jpg')
plt.imshow(image2)
plt.show()
