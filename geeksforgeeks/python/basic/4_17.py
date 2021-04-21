MoviePy – Resizing Video File



In this article we will see how we can resize video file clip in MoviePy.
MoviePy is a Python module for video editing, which can be used for basic
operations on videos and GIF’s. Resizing video file means. Image/frame
interpolation occurs when you resize or distort your frame of vdideo from one
pixel grid to another. Video resizing is necessary when we need to increase or
decrease the total number of pixels, whereas remapping can occur when you are
correcting for lens distortion or rotating an video.

> In order to do this we will use resize method with the VideoFileClip
> object
>
>  **Syntax :** clip.resize(n)
>
>  **Argument :** It takes float value i.e multiplier
>
>  **Return :** It returns VideoFileClip object
>
>  
>
>
>  
>

Below is the implementation

 __

 __  
 __

 __

 __  
 __  
 __

# Import everything needed to edit video clips

from moviepy.editor import *

 

# loading video dsa gfg intro video and getting only first 5 seconds

clip1 = VideoFileClip("dsa_geek.webm").subclip(0, 5)

 

# getting width and height of clip 1

w1 = clip1.w

h1 = clip1.h

 

print("Width x Height of clip 1 : ", end = " ")

print(str(w1) + " x ", str(h1))

 

print("---------------------------------------")

 

 

# resizing video downsize 50 % clip2 = clip1.resize(0.5)

 

# getting width and height of clip 1

w2 = clip2.w

h2 = clip2.h

 

print("Width x Height of clip 2 : ", end = " ")

print(str(w2) + " x ", str(h2))

 

print("---------------------------------------")

 

 

 

# showing final clip

clip2.ipython_display(width = 480)  
  
---  
  
 __

 __

 **Output :**

    
    
    Width x Height of clip 1 :  854 x  480
    ---------------------------------------
    Width x Height of clip 2 :  427 x  240
    ---------------------------------------
    Moviepy - Building video __temp__.mp4.
    Moviepy - Writing video __temp__.mp4
    
                                                                                                                           
    Moviepy - Done !
    Moviepy - video ready __temp__.mp4

https://media.geeksforgeeks.org/wp-content/uploads/20200722004427/116.mp4

Another example

 __

 __  
 __

 __

 __  
 __  
 __

# Import everything needed to edit video clips

from moviepy.editor import *

 

# loading video gfg

clip = VideoFileClip("geeks.mp4")

 

# getting subclip

clip1 = clip.subclip(0, 7)

 

# getting width and height of clip 1

w1 = clip1.w

h1 = clip1.h

 

print("Width x Height of clip 1 : ", end = " ")

print(str(w1) + " x ", str(h1))

 

print("---------------------------------------")

 

 

# resizing video downsize 50 % clip2 = clip1.resize(0.5)

 

# getting width and height of clip 1

w2 = clip2.w

h2 = clip2.h

 

print("Width x Height of clip 2 : ", end = " ")

print(str(w2) + " x ", str(h2))

 

print("---------------------------------------")

 

 

 

# showing final clip

clip2.ipython_display()  
  
---  
  
 __

 __

 **Output :**

    
    
    Width x Height of clip 1 :  656 x  404
    ---------------------------------------
    Width x Height of clip 2 :  328 x  202
    ---------------------------------------
    Moviepy - Building video __temp__.mp4.
    MoviePy - Writing audio in __temp__TEMP_MPY_wvf_snd.mp3
                                                                                                                           
    MoviePy - Done.
    Moviepy - Writing video __temp__.mp4
    
                                                                                                                           
    Moviepy - Done !
    Moviepy - video ready __temp__.mp4

https://media.geeksforgeeks.org/wp-content/uploads/20200722004527/29.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

