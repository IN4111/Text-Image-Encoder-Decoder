import numpy as np
from PIL import Image as img
class Decode():
    def __init__(self,image,destination,byte_size,color_for_zeros,color_for_ones):#color in rgb#image->where decoding of image done ,destination->where decoded txt is stored
        self.image=img.open(image).convert("RGB")
        self.filepointer=open(destination,"w")
        self.max_x_pixels=self.image.size[0]#width of the image
        self.max_y_pixels=self.image.size[1]#height of the image
        self.byte_size=byte_size
        self.color_for_zeros=color_for_zeros
        self.color_for_ones=color_for_ones
        self.pixel_array=self.image.load()
        self.binary_list=[]
        self.binary_of_char=""
        self.total_pixels_filled=0
    def decode(self,):
        for i in range(0,self.max_y_pixels):
            for j in range(0,self.max_x_pixels):
                if(len(self.binary_of_char)==self.byte_size):
                    self.binary_list.append(self.binary_of_char)
                    self.binary_of_char=""
                if(self.pixel_array[j,i]==self.color_for_zeros):
                    self.binary_of_char=self.binary_of_char+"0"
                    self.total_pixels_filled+=1
                elif(self.pixel_array[j,i]==self.color_for_ones):
                    self.binary_of_char=self.binary_of_char+"1"
                    self.total_pixels_filled+=1
        print("characters filled:",str(self.total_pixels_filled))
        print("total pixels:",str(self.max_x_pixels*self.max_y_pixels))
        print("total characters:",str(len(self.binary_list)))
        self.result_string=""
        for i in self.binary_list:
            self.result_string=self.result_string+chr(int(i,2))
        self.filepointer.write(str(self.result_string))
        print("file decoded")
        print("content:\n",self.result_string)
        print("file saved")
        self.filepointer.close()
#dcc=Decode("ImageOut.png","SampleOut.txt",8,(0,0,0),(255,0,0))#RGB
#dcc.decode()
