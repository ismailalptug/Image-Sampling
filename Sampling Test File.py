import cv2
from Sampling import sampleImage

inimg = cv2.imread("BLOCKS.TIF",0)
cv2.imshow("Original", inimg)
sampleImage(inimg, 4)