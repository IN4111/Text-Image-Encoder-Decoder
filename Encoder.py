import cv2
import numpy as np
from PIL import Image as img
class Encode():                                                                         
    def __init__(self,filepointer,image,destination,byte_size,color_for_zeros,color_for_ones):#color:bgr#filepointer -> text need to be encoded ,image->where encoding of image done ,destination->where encoded image is stored
        self.image=img.open(image)
        self.filepointer=open(filepointer,"r")
        self.destination=destination
        self.max_x_pixels=self.image.size[0]#image width
        self.max_y_pixels=self.image.size[1]#image height
        self.text=self.filepointer.read()
        self.total_binary_list=[]
        self.byte_size=byte_size
        self.color_for_zeros=color_for_zeros
        self.color_for_ones=color_for_ones
    def encode(self,):
        for i in self.text:
            char_to_binary=bin(ord(i)).replace("0b","").rjust(8,"0")#removing 0b********
            self.total_binary_list.append(char_to_binary)
        print("characters can be filled:",str((self.max_x_pixels*self.max_y_pixels)//self.byte_size))
        print("total characters:",len(self.total_binary_list))
        print("total pixels:",str(self.max_x_pixels*self.max_y_pixels))
        print("Total pixels needed: ",str(len(self.total_binary_list)*self.byte_size))
        try:
            if(len(self.total_binary_list)*self.byte_size>self.max_x_pixels*self.max_y_pixels):
                raise(ValueError("image is unable hold the data"))
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
                if self.current_x_pixel==self.max_x_pixels-1:
                    self.current_x_pixel=0
                    self.current_y_pixel+=1
            self.image_in_numpy=np.array(self.image,dtype="uint8")
            cv2.imshow("Encoded_image",self.image_in_numpy)
            cv2.imwrite(self.destination,self.image_in_numpy)
            print("image saved")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            print("nmber of character is higher than the pixels on image")
#ecc=Encode("SampleIn.txt","ImageIn.png","ImageOut.png",8,(0,0,0),(0,0,255))#BGR
#ecc.encode()
