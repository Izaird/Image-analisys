import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
pic1=Image.open("img/pic_01.png").convert('L') #Open the image and convert to gray scale 
pic2=Image.open("img/pic_02.png").convert('L') #Open the image and convert to gray scale 
pic_arr1 = np.asarray(pic1) #converts the image to an Numpy Array
pic_arr2 = np.asarray(pic2) #converts the image to an Numpy Array

def addImageToImage(pic1,pic2):
    height =pic1.shape[0]
    width = pic1.shape[1]
    res_pic = np.ones([height, width],np.uint)
    for i in range(0,height):
        for j in range(0,width):
            res_pic[i][j]=pic1[i][j]+ pic2[i][j]
            if(res_pic[i][j]>255):
                res_pic[i][j] = 255
    return res_pic
    
add_image = addImageToImage(pic_arr1,pic_arr2)