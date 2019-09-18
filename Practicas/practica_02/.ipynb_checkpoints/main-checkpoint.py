import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
filepath="img/" #The current directory
#filename="mark.jpeg" #The File name
filename="logo.jpg"
pic=Image.open(filepath+filename).convert("L") #Open the image and convert to gray scale 
pic #Diplays the image in the notebook

pic_arr = np.asarray(pic,np.uint) #converts the image to an Numpy Array
pic_arr.shape #(height,width,#of channels)
H=pic_arr.shape[0]
W=pic_arr.shape[1]
#for i in range (0,W):
print(H,W,pic_arr.shape[2])
print(pic_arr.dtype)
#Wtest=[2,2,1,0,1,3,3,2]
#print(pic_arr)

plt.imshow(pic_arr)

print(len(pic_arr[:,0,0]))
print(len(pic_arr[0,:,0]))

newHeight=2500
newWidth=1750
res_picW= np.ones([H, newWidth,3],np.uint)
res_pic= np.ones([newHeight,newWidth,3],np.uint)
print(res_pic.shape)
print(res_pic.dtype)
print(res_picW.shape)
print(res_picW.dtype)
#print(newrow)

#%%cython -a
import numpy as np
basefactorW = W/newWidth
factorH = H/newHeight
print("Width factor", basefactorW)
print("H factor", factorH)
for i in range (0,H): 
    res_picW[i,0,0:3]=pic_arr[i,0,0:3]
    res_picW[i,-1,0:3]=pic_arr[i,-1,0:3]
    for j in range (1,newWidth-1):
        #print("---Posicion---",j)
        x=basefactorW*j
        #print("X = ", x)
        x1 = math.floor(x)
        x2 = math.ceil(x)
        if(x1>=W or x2>=W):
            x1 = W-1
            x2 = W-1
        
            
        y1 = pic_arr[i,x1,0]
        y2 = pic_arr[i,x2,0]
        #print("(x1,y1) = ",x1,y1)
        #print("(x2,y2) = ",x2,y2)
        if(x1 == x2):
            y= y1
        else:
            
            op1=(int(y2)-int(y1))/(x2 - x1)
            op2=x-x1
            #print("x-x1=",op2)
            op3=op1*op2
            #print("op1*op2=",op3)
            y = op3+y1
          # print("y=",y)
            
        res_picW[i,j,0:3] = int(round(y))
plt.imshow(res_picW)

for i in range (0,newWidth): 
    res_pic[0,i,0:3]=res_picW[0,i,0:3]
    res_pic[-1,i,0:3]=res_picW[-1,i,0:3]
    for j in range (1,newHeight-1):
        #print("---Posicion---",j)
        x=factorH*j
        #print("X = ", x)
        x1 = math.floor(x)
        x2 = math.ceil(x)
        if(x1>=H or x2>=H):
            x1 = H-1
            x2 = H-1
        
            
        y1 = res_picW[x1,i,0]
        y2 = res_picW[x2,i,0]
        #print("(x1,y1) = ",x1,y1)
        #print("(x2,y2) = ",x2,y2)
        if(x1 == x2):
            y= y1
        else:
            
            op1=(int(y2)-int(y1))/(x2 - x1)
            op2=x-x1
            #print("x-x1=",op2)
            op3=op1*op2
            #print("op1*op2=",op3)
            y = op3+y1
          # print("y=",y)
            
        res_pic[j,i,0:3] = int(round(y))
plt.imshow(res_pic)