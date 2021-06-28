import numpy as np
import cv2
import math

def sampleImage(image, samplingRatio):
    in_row = image.shape[0]
    in_column = image.shape[1]
    row = math.ceil(in_row / samplingRatio)
    column = math.ceil(in_column / samplingRatio)

    img = np.zeros(shape=(row, column))
    for i in range(in_row):
        for j in range(in_column):
            if (i % samplingRatio == 0 & j % samplingRatio == 0):
                img[int(i/samplingRatio), int(j/samplingRatio)] = image[i, j]

    img = np.array(img, dtype=np.uint8)
    cv2.imshow("Sampled", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


