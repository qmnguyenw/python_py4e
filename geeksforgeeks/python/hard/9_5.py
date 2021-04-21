Pytube | Python library to download youtube videos



  
YouTube is very popular video sharing website. Downloading a video from
YouTube is a tough job. Downloading the Downloader and get the video using
that or go to any other website which fetches the video and saves on your
computer. Using Python, this task is very easy. Few lines of code will
download the video from YouTube for you. For this, there a python library
named as ‘pytube’. pytube is a lightweight, dependency-free Python library
which is used for downloading videos from the web.  
pytube is not the native library. You need to install it before using it.
Installation is easy when you have pip. In the Terminal or Command Prompt,
type the following command to install pytube.

    
    
    pip install pytube
    

In case you don’t have pip, install it as an external library.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Downloading a single video**

pytube library makes the video downloading very easy. Create the object of the
YouTube module by passing the link as the parameter. Then, get the appropriate
extension and resolution of the video. You can set the name of the file as
your convenience, in another case original name will be kept. After that,
download the file using the download function which has one parameter which is
the location where to download the file.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

from pytube import YouTube 

 

# where to save 

SAVE_PATH = "E:/" #to_do 

 

# link of the video to be downloaded 

link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

 

try: 

 # object creation using YouTube

 # which was imported in the beginning 

 yt = YouTube(link) 

except: 

 print("Connection Error") #to handle exception 

 

# filters out all the files with "mp4" extension 

mp4files = yt.filter('mp4') 

 

#to set the name of the file

yt.set_filename('GeeksforGeeks Video') 

 

# get the video with the extension and

# resolution passed in the get() function 

d_video =
yt.get(mp4files[-1].extension,mp4files[-1].resolution) 

try: 

 # downloading the video 

 d_video.download(SAVE_PATH) 

except: 

 print("Some Error!") 

print('Task Completed!')   
  
---  
  
__

__

Downloading a file takes some time as a very large amount of data is being
dowloaded from the web. Depending on the speed of the connection, time taken
to execute the program varies. In case you wish to download the number of
files, go with the next case.

 **Downloading multiple videos**

The basic task of downloading the multiple videos is same as downloading a
single video. We can use a for loop for downloading the video.

 __

 __  
 __

 __

 __  
 __  
 __

from pytube import YouTube 

 

#where to save 

SAVE_PATH = "E:/" #to_do 

 

#link of the video to be downloaded 

link=["https://www.youtube.com/watch?v=xWOoBJUqlbI", 

 "https://www.youtube.com/watch?v=xWOoBJUqlbI"

 ]

 

for i in link: 

 try: 

 

 # object creation using YouTube

 # which was imported in the beginning 

 yt = YouTube(i) 

 except: 

 

 #to handle exception 

 print("Connection Error") 

 

 #filters out all the files with "mp4" extension 

 mp4files = yt.filter('mp4') 

 

 # get the video with the extension and

 # resolution passed in the get() function 

 d_video =
yt.get(mp4files[-1].extension,mp4files[-1].resolution) 

 try: 

 # downloading the video 

 d_video.download(SAVE_PATH) 

 except: 

 print("Some Error!") 

print('Task Completed!')   
  
---  
  
__

__

In this, we have used a for loop for downloading multiple files as shown. One
can use file handling for keeping the all the links in a file which needs to
be downloaded.

 **Download multiple videos using File Handling**

Using file handling, we can open the file which has the group of links in it.
Traversing every link of a text file and applying the very basic video
downloading program is done here. Here, we have a text file named as
“links_file.txt” which has all the links which need to be downloaded.

 __

 __  
 __

 __

 __  
 __  
 __

from pytube import YouTube 

 

# where to save 

SAVE_PATH = "E:/" #to_do 

 

# link of the video to be downloaded 

# opening the file 

link=open('links_file.txt','r') 

 

for i in link: 

 try: 

 

 # object creation using YouTube

 # which was imported in the beginning 

 yt = YouTube(i) 

 except: 

 

 #to handle exception

 print("Connection Error") 

 

 #filters out all the files with "mp4" extension 

 mp4files = yt.filter('mp4') 

 

 # get the video with the extension and

 # resolution passed in the get() function 

 d_video =
yt.get(mp4files[-1].extension,mp4files[-1].resolution) 

 try: 

 

 # downloading the video 

 d_video.download(SAVE_PATH) 

 except: 

 print("Some Error!") 

print('Task Completed!')   
  
---  
  
__

__

**Important Points:**

  1. Make sure you are connected to the internet to download the videos. Otherwise it will raise an error.
  2. Don’t use the set_filename() function in any loop. In this case, only one video will be downloaded.
  3. You can modify the names everytime using another array of names.
  4. Connection Intruption in between will also raise an error and video will not be downloaded in that case.

This article is contributed by **Rishabh Bansal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

