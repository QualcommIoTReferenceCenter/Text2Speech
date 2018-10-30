import cv2
import numpy as np
import os
import time
import pytesseract
from PIL import Image


def text_recog(text_im):
    # Create a sharpening kernel
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    # applying the sharpening kernel to the image
    text_im = cv2.filter2D(text_im, -1, kernel_sharpening)

    #apply thresholding to binarize the image
    text_im = cv2.threshold(text_im, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    #apply erosion to the binary image
    kernel = np.ones((3, 3), np.uint8)
    text_im = cv2.erode(text_im, kernel, iterations=1)
    cv2.imshow('Processed', text_im)

    # write the image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, text_im)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print("----------------------------------")
    print(text)
    return text