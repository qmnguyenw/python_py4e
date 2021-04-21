Downloading files from web using Python



Requests is a versatile HTTP library in python with various applications. One
of its applications is to download a file from web using the file URL.  
 **Installation:** First of all, you would need to download the requests
library. You can directly install it using pip by typing following command:

    
    
    pip install requests

Or download it directly from here and install manually.

 **Downloading files**

 __

 __  
 __

 __

 __  
 __  
 __

# imported the requests library

import requests

image_url = "https://www.python.org/static/community_logos/python-logo-
master-v3-TM.png"

 

# URL of the image to be downloaded is defined as image_url

r = requests.get(image_url) # create HTTP response object

 

# send a HTTP request to the server and save

# the HTTP response in a response object called r

with open("python_logo.png",'wb') as f:

 

 # Saving received content as a png file in

 # binary format

 

 # write the contents of the response (r.content)

 # to a new file in binary mode.

 f.write(r.content)  
  
---  
  
 __

 __

This small piece of code written above will download the following image from
the web. Now check your local directory(the folder where this script resides),
and you will find this image:

All we need is the URL of the image source. (You can get the URL of image
source by right-clicking on the image and selecting the View Image option.)

  

  

 **Download large files**

The HTTP response content ( **r.content** ) is nothing but a string which is
storing the file data. So, it won’t be possible to save all the data in a
single string in case of large files. To overcome this problem, we do some
changes to our program:

* Since all file data can’t be stored by a single string, we use **r.iter_content** method to load data in chunks, specifying the chunk size.
    
    
     r = requests.get(URL, stream = True)

Setting **stream** parameter to **True** will cause the download of response
headers only and the connection remains open. This avoids reading the content
all at once into memory for large responses. A fixed chunk will be loaded each
time while **r.iter_content** is iterated.

