import cv2
import math
import numpy as np
from PIL import Image as img
class Encode():
    def __init__(self,filepointer,destination,byte_size,color_for_zeros,color_for_ones):#color:bgr#filepointer -> text need to be encoded ,destination->where encoded image is stored
        self.filepointer=open(filepointer,"r")
        self.destination=destination
        self.text=self.filepointer.read()
        self.total_binary_list=[]
        self.byte_size=byte_size
        self.color_for_zeros=color_for_zeros
        self.color_for_ones=color_for_ones
    def encode(self,):
        for i in self.text:
            char_to_binary=bin(ord(i)).replace("0b","").rjust(8,"0")#removing 0b********
            self.total_binary_list.append(char_to_binary)
        self.image_size=(800,math.ceil((len(self.total_binary_list)*self.byte_size)/800))
        self.image=img.new(mode="RGB",size=self.image_size)
        print("total pixels needed :",len(self.total_binary_list)*self.byte_size)
        print("total pixels in picture:",self.image.size[0]*self.image.size[1])
        self.current_x_pixel=0
        self.current_y_pixel=0
        self.total_lines="".join(self.total_binary_list)
        for i in self.total_lines:
            if(i=="0"):
                self.image.putpixel((self.current_x_pixel,self.current_y_pixel),self.color_for_zeros)
                self.current_x_pixel+=1
            else:
                self.image.putpixel((self.current_x_pixel,self.current_y_pixel),self.color_for_ones)
                self.current_x_pixel+=1
            if (self.current_x_pixel==self.image_size[0]):
                self.current_x_pixel=0
                self.current_y_pixel+=1
        self.image_in_numpy=np.array(self.image,dtype="uint8")
        cv2.imshow("Encoded_image",self.image_in_numpy)
        cv2.imwrite(self.destination,self.image_in_numpy)
        print("image saved in ",self.destination)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#ecc=Encode("SampleIn.txt","ImageOut.png",8,(0,0,0),(0,0,255))#BGR
#ecc.encode()
