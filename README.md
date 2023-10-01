# Image---Text-Encoder-and-Decoder
# Demo Image
![Untitled](https://github.com/IN4111/Text-Image-Encoder-Decoder/assets/123793292/54a771ea-d89a-4f2c-99c0-6819c187ec5a)
# Install Required Packages:
 Use ```pip install -r requirements.txt``` to install required packages.
# 1)Importing Modules:
Use ```import``` to import modules (Encoder and Decoder) on the following way:
```
import Encoder as ec
import Decoder as dc
```
# 2)Encode a text File(.txt) to an image(.png/.jpg/....) by the form of:
```
Ec=ec.Encode("SampleIn.txt","ImageOut.png",n,(z1,z2,z3),(o1,o2,o3))
Ec.encode()
#SampleIn.txt:text to be encoded
#ImageOut.png:Destination of the image with encoded values
#n: bits for a value(example: x=8,represents a word lenght of 8 bits)
#(z1,z2,z3):color that needs to be represented in the pixel for zeros(note: values is in BGR)
#(o1,o2,o3):color that needs to be represented in the pixel for ones(note: values is in BGR)
```
# 3)Decode an image(.png/.jpg/....) to a text File(.txt) by the form of:
```
Dc=dc.Decode("ImageOut.png","SampleOut.txt",n,(z1,z2,z3),(o1,o2,o3))
Dc.decode()
#ImageOut.png:File(.png) that is Encoded by the Encoder(refer point-2)
#SampleOut.txt:destination of the Decoded text to a text file(.txt)
#(z1,z2,z3):values that needs to be represented in the pixel for zeros(note: values is in RGB)
#(o1,o2,o3):values that needs to be represented in the pixel for ones(note: values is in RGB)
```
