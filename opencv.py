import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('example/her86.jpg')
cv2.imshow(img)
cv2.waitKey(0)