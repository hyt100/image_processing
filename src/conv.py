#!/usr/bin/python3

from skimage import data,io
from matplotlib import pyplot as plt
import numpy as np


def conv_once(arr, kernel):
    n = len(kernel)
    ret = 0
    for i in range(n):
        for j in range(n):
            ret += arr[i, j] * kernel[i, j]
    return ret

def conv(img, kernel):
    channel = len(img.shape)
    if channel == 2:
        img_out = np.zeros(img.shape)
        n = len(kernel)
        img_resize = np.zeros((img.shape[0] + n-1, img.shape[1] + n-1))
        img_resize[0:img.shape[0], 0:img.shape[1]] = img
        for i in range(img_out.shape[0]):
            for j in range(img_out.shape[1]):
                temp = img_resize[i:(i + n), j:(j+n)]
                img_out[i, j] = conv_once(temp, kernel)
        return img_out
    elif channel == 3:
        img_out = np.zeros(img.shape, dtype='uint8')
        n = len(kernel)
        img_resize = np.zeros((img.shape[0] + n-1, img.shape[1] + n-1, img.shape[2]), dtype='uint8')
        img_resize[0:img.shape[0], 0:img.shape[1], :] = img
        for i in range(img_out.shape[0]):
            for j in range(img_out.shape[1]):
                for k in range(img_out.shape[2]):
                    temp = img_resize[i:(i + n), j:(j+n), k]
                    ret = conv_once(temp, kernel)
                    ret = ret if ret < 255 else 255
                    img_out[i, j, k] = int(ret)
        return img_out
    else:
        print("error")

kernel = np.zeros((3, 3))
for i in range(len(kernel)):
    for j in range(len(kernel)):
        kernel[i, j] = 1/9
print(kernel)

test_data = np.zeros((6, 6))
for i in range(len(test_data)):
    for j in range(len(test_data)):
        test_data[i, j] = j
print(test_data)

print(conv(test_data, kernel))

test_image = io.imread(fname='../data/lena.jpg')
test_image_out = conv(test_image, kernel)
plt.subplot(121)
plt.imshow(test_image)
plt.subplot(122)
plt.imshow(test_image_out)
plt.show()