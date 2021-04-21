YouTube Media/Audio Download using Python – pafy



This tutorial will help you download youtube video or audio with python using
pafy library. Pafy library is used to retrieve YouTube content and metadata.

 **Features of Pafy**  
(i) Retrieve metadata such as viewcount, duration, rating, author, thumbnail,
keywords.  
(ii) Download video or audio at requested resolution / bitrate / format /
filesize  
(iii) Command line tool (ytdl) for downloading directly from the command line  
(iv) Download video only (no audio) in m4v or webm format  
(v) Download audio only (no video) in ogg or m4a format  
(vi) Works with Python 2.6+ and 3.3+  
(vii) Optionally depends on youtube-dl (recommended; more stable)

 **Installation**

    
    
    virtualenv venv
    pip install pafy
    

**Library Imported**

    
    
     import pafy

 **Example1:**  
Retrieve metadata such as viewcount, duration, rating, author, description.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import pafy

 

# url of video

url = "https://www.youtube.com/watch?v=Ns4LCeeOFS4&t;=320s"

 

# instant created

video = pafy.new(url)

 

# print title

print(video.title)

 

# print rating

print(video.rating)

 

# print viewcount

print(video.viewcount)

 

# print author & video length

print(video.author, video.length)

 

# print duration, likes, dislikes & description

print(video.duration, video.likes, video.dislikes, video.description)  
  
---  
  
 __

 __

Output:

    
    
    Dynamic Programming | Set 3 (Longest Increasing Subsequence) | GeeksforGeeks
    4.30275249481
    57739
    GeeksforGeeks 396
    00:06:36 180 38 Explanation for the article: http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
    

**Example2:**  
Download best resolution video regardless of extension

 __

 __  
 __

 __

 __  
 __  
 __

import pafy

 

url = "https://www.youtube.com/watch?v=eACohWVwTOc"

video = pafy.new(url)

 

streams = video.streams

for i in streams:

 print(i)

 

# get best resolution regardless of format

best = video.getbest()

 

print(best.resolution, best.extension)

 

# Download the video

best.download()  
  
---  
  
 __

 __

Output:

    
    
    normal:3gp@176x144
    normal:3gp@320x180
    normal:webm@640x360
    normal:mp4@640x360
    normal:mp4@1280x720
    1280x720 mp4
      25, 707, 969 Bytes [100.00%] received. Rate: [ 506 KB/s].  ETA: [0 secs]  
    

**Example3:**  
Download video of a particular format specified (let say .3gp)

 __

 __  
 __

 __

 __  
 __  
 __

import pafy

 

url = "https://www.youtube.com/watch?v=eACohWVwTOc"

video = pafy.new(url)

 

streams = video.streams

for i in streams:

 print(i)

 

# get best resolution of a specific format

# set format out of(mp4, webm, flv or 3gp)

best = video.getbest(preftype ="3gp")

 

best.download()  
  
---  
  
 __

 __

Output:

    
    
    normal:3gp@176x144
    normal:3gp@320x180
    normal:webm@640x360
    normal:mp4@640x360
    normal:mp4@1280x720
      6, 049, 643 Bytes [100.00%] received. Rate: [ 241 KB/s].  ETA: [0 secs]   
    

**Example4:**  
Download a specific format audio.

 __

 __  
 __

 __

 __  
 __  
 __

import pafy 

 

url = "https://www.youtube.com/watch?v =eACohWVwTOc"

video = pafy.new(url)

 

audiostreams = video.audiostreams

for i in audiostreams:

 print(a.bitrate, i.extension, i.get_filesize())

 

audiostreams[3].download()  
  
---  
  
 __

 __

Output:

    
    
    160k webm 1365668
    160k webm 1811815
    160k m4a 3470205
    160k webm 3301003
    160k webm 3588746
    

**Example5:**  
Download the bestaudio

 __

 __  
 __

 __

 __  
 __  
 __

import pafy 

 

url = "https://www.youtube.com/watch?v=eACohWVwTOc"

video = pafy.new(url)

 

bestaudio = video.getbestaudio()

bestaudio.download()  
  
---  
  
 __

 __

Output:

    
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/1-61.png)
    

References:  
https://pypi.python.org/pypi/pafy

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

