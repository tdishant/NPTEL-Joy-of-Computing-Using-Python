'''
from PIL import Image
#flipping the image
#opening the image
#images are opened by the computers in the form of matrices 
img = Image.open("image_processing_1.jpeg")
#thus image flipping means matrix transposition
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#save it to a file in human understandable format
transposed_img.save("flipped_image_1.jpeg")
'''

#image enhancement using CLAHE (Contrast Limited adapetive histogram equalization)

import cv2

#read the image
img = cv2.imread("image_processing_2.png")

#preparation for CLAHE
clahe = cv2.createCLAHE()

#convert to gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply enhancement
enh_img = clahe.apply(gray_img)

#save it to a file
cv2.imwrite('enhanced_img.png', enh_img)
