from SimpleCV import Image, Color
import os, sys, argparse
import cv2

def findBlobs(image_name,r,b,g):
    img = Image(image_name)
    color_distance = img.colorDistance(Color.RED).invert() * r + img.colorDistance(Color.BLUE).invert() * b + img.colorDistance(Color.GREEN).invert() * g
    # we should consider using multiple color filters; using r/g/b or custom
    # this /might/ improve accuracy

    binarized = color_distance.binarize()

    blobs = binarized.findBlobs( minsize=50, maxsize=500 )

    #blobs.draw(width=2)

    overlay = color_distance.dl()
    if (blobs):
        for blob in blobs:
            overlay.rectangle( blob.topLeftCorner(), (blob.width(), blob.height()), Color.RED, width = 2)
            croppedBlob = img.crop(blob)
        img.addDrawingLayer(overlay)

    return img;

img = Image("peter1.png")
findBlobs("peter1.png",2.5,0,0)
img.save("masonoutput.jpg")








import cv2
import numpy as np
from SimpleCV import Image, Color
import os, sys, argparse
import cv2

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((1,1,3), np.uint8)
image = Image("peter1.png")
#img = cv2.imread("peter1.png")
cv2.namedWindow('image')



# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

while(1):

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')

    print r, g, b
    imageOut = findBlobs("peter1.png",r/100.0,g/100.0,b/100.0)
    imageOut.show()
    #image.show()
    #img = imageOut.getNumpy()


    #cv2.imshow('image',img)
    cv2.waitKey(1000)

cv2.destroyAllWindows()
