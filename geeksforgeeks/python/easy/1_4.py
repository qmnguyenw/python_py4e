How to download public YouTube captions in XML using Pytube in Python?



 **Prerequisite** : Pytube

Pytube is a dependency-free lightweight Python library for downloading YouTube
videos **.** There are various APIs to fetch metadata from YouTube. In this
article, we are going to see how to download public YouTube captions in XML
using Python.

 **Before starting we need to install this module:**

    
    
    pip install pytube

 **Approach:**

  * Import pytube : **from pytube import YouTube.**
  * Instantiate the object using **YouTube() function** which takes in the youtube video link as a parameter.
  * The instance for e.g. in the code below is **‘src’** which has a caption attribute to get a list of languages and their respective language code for a particular video.
  * To get a Caption in a particular language we use **get_by_language_code(‘en’)** en stands for English as shown in the code below.
  * By default, the captions are downloaded in XML format only.
  * To explicitly convert it into string data type we need to typecast it using ‘ **generate_srt_captions()** ‘ as shown in the code below.

 **Below is the implementation:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from pytube import YouTube

 

link =
'https://www.youtube.com/watch?v=wjTn_EkgQRg&index;=1&list;=PLgJ7b1NurjD2oN5ZXbKbPjuI04d_S0V1K'

src = YouTube(link)

 

# prints all avaliable captions in various languages.

print('Captions Available: ', src.captions)

print()

 

# Getting only English captions by specifying 'en' as parameter

en_caption = src.captions.get_by_language_code('en')

print(en_caption.xml_captions)

 

# Instead of Captions in XML format we are converting it to string format.

en_caption_convert_to_srt = (en_caption.generate_srt_captions())

print(en_caption_convert_to_srt)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210228112135/captions.JPG)

XML Captions

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

