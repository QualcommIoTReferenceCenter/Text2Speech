#!/usr/bin/env python
'''This program detects the text portion of an image,
then uses Tesseract to recognize the text written and 
finally reads the text using text2speech


Uses Google gTTS and googletrans APIs so
has to be connected to the internet

usage: press 's' to take a picture of the text image
press 'q' to stop application
'''

import cv2
import argparse
# this libraries were created for this application
from libs.text_recog import *
from libs.process_image import *
from libs.trans_text import *
from libs.speech import *



if __name__ == '__main__':
    # creating input arguments: input PDF, translate or not,
    # source language,
    # destination language (for translation and it will pronounce using this language)
    # camera index
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--translate", default='n',
                    help="Translate the text ['y'/'n']")
    ap.add_argument("-s", "--source_lang", default='en',
                    help="source language (ex.: 'en' = English, 'es' = Spanish, 'pt' = Portuguese")
    ap.add_argument("-d", "--destination_lang", default='en',
                    help="destination language (ex.: 'en' = English, 'es' = Spanish, 'pt' = Portuguese")
    ap.add_argument("-c", "--camera", type = int, default=0,
                    help="camera index (0, 1, 2, ...")
    args = vars(ap.parse_args())

    cam = cv2.VideoCapture(args["camera"])
    key = None
    print("\nPress 's' to take a picture of the text image \nOR \npress 'q' to stop the application")


    while(True):
        key = cv2.waitKey(2) & 0xFF
        if key == ord('q'):
            break
        status_frame, frame = cam.read()
        if status_frame == True:
            cv2.imshow('Original', frame)
            if key == ord('s'):
                # converts the image to gray scale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # cuts only the text portion within the image
                text_im = process_image(gray)

                # Does the text recognition
                text_string = text_recog(text_im)

                # Translates the text if translation is activated
                if args["translate"] == 'y':
                    text_string = trans_text(text_string, args["destination_lang"], args["source_lang"])
                # says the text out loud
                speech(text_string, args["destination_lang"])
        else:
            # tries to reconnect to the camera if the video feed stops
            while status_frame == False:
                print(args["camera"])
                cam = cv2.VideoCapture(args["camera"])
                status_frame, frame = cam.read()
                print("Error reading camera")


    cam.release()
    cv2.destroyAllWindows()