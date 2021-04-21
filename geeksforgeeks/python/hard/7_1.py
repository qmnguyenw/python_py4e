Python | Download YouTube videos using youtube_dl module



Each and every day, you must be watching some video or another on YouTube
which may be related to Music, Movies, Studies, Research, Leisure etc. You
might want to store some video for future use where it will be required due to
lack of internet or saving data or any other reason.

What if we tell you that you can do this exact very thing using Python. Let’s
see how to download Youtube videos using **youtube_dl**module in Python.

Install the module with this command –

    
    
    pip install youtube_dl
    

Now, suppose you are watching this video on YouTube.  
![Sample Video](https://media.geeksforgeeks.org/wp-
content/uploads/20190523005044/BIBAA.jpg)

Below is the Python code –

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

import youtube_dl

 

ydl_opts = {}

 

def dwl_vid():

 with youtube_dl.YoutubeDL(ydl_opts) as ydl:

 ydl.download([zxt])

 

channel = 1

while (channel == int(1)):

 link_of_the_video = input("Copy & paste the URL of the YouTube
video you want to download:- ")

 zxt = link_of_the_video.strip()

 

 dwl_vid()

 channel = int(input("Enter 1 if you want to download more
videos \nEnter 0 if you are done "))  
  
---  
  
 __

 __

 **Output:**  
![Entering URL](https://media.geeksforgeeks.org/wp-
content/uploads/20190523005136/116-1.jpg)  
![Coding Process](https://media.geeksforgeeks.org/wp-
content/uploads/20190523005358/codinga.jpg)

And it’s done. The video you want gets downloaded in the Python folder.  
![Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190523005708/folder1.jpg)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

