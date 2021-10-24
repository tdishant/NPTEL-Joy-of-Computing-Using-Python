import scipy.misc
from PIL import Image
import numpy as np
import random
import imageio
#to read the image
img = imageio.imread('image.png')
count_pun = 0
count_in = 0
count = 0

#dimensions of the image : 544 × 583

while(count <= 10000):
    #to pace a random dot
    x = random.randint(0, 582)
    y = random.randint(0, 543)
    z = 0
    
    if(img[x][y][z] == 60):
        #corresponds to india
        count_in += 1
    elif(img[x][y][z] == 80):
        count_pun += 1
    
    count += 1
    
area_pun = (count_pun/count_in)*3287263

print(area_pun)