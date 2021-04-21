Python script to open a Google Map location on clipboard



The task is to create a python script that would open the default web browser
to the Google map of the address given as the command line argument.

 **Following is the step by step process:**

  1.  **Creating the Address_string from command line input :** Command line arguments can be read through sys module. The sys.argv array has the first element as the filename and the rest of elements as command line arguments which are broken into different elements by spaces, same as raw_input().split(). Therefore, if the length of sys.argv is more than 1, then we can be sure that the command line arguments have been passed.  
Since sys.argv is a list of strings, it can be passed to join() method which
returns a single string value. Since the first element is the filename, which
is not needed, we can slice the list and join from 2nd element onwards.

 __

 __  
 __

 __

 __  
 __  
 __

#File name is Map.py

import sys

print ' '.join(sys.argv[1:])  
  
---  
  
 __

 __

    
        If we run>>> python Map.py New Delhi
    The output of the program would be New Delhi.

  2.  **Open the Web-Browser :** We will be using **web browser** module for opening the browser. The webbrowser module has a method **open()** that can launch the web browser to the specified URL. For example, the script given below will open the web browser to the home page of GeeksforGeeks.

 __

 __  
 __

 __

 __  
 __  
 __

import webbrowser

webbrowser.open('https://www.geeksforgeeks.org/')  
  
---  
  
 __

 __

  3.  **Find the URL :** Now, when we go to Google Maps and search for google maps, the URL turns out to be gibberish and of no clear pattern, as shown below.  
https://www.google.co.in/maps/place/GeeksforGeeks/@28.5011226,77.4077907,17z/data=!3m1!4b1!4m5!3m4!1s0x390ce626851f7009:0x621185133cfd1ad1!8m2!3d28.5011226!4d77.4099794?hl=en

Websites often add extra text in the URL for additional tasks like
customization and tracking. However, it can be observed that the initial few
part of URL is **https://www.google.co.in/maps/place/GeeksforGeeks** where
GeeksforGeeks is our searched keyword.  
Also, for example say while searching for New Delhi, instead of New + Delhi,
if we write only New Delhi, the + is inserted in the required places on its
own, which eases our task even further.  
Therefore, the final URL can be taken as
**https://www.google.co.in/maps/place/ _Address_String_ /**.

  4.  **Combining the two and Completing the script :** The python script to open the given command line address is given below. There will be two imported modules, **webbrowser** to open the browser to the designated URL and **sys** to work on the command line arguments.
    * The first step is to check if there is any command line given or not, which is done using the len(sys.argv).
    * Then we use the join method to form the address string of the place that is to be searched in Google Maps.
    * Finally, when we get the address, we open the browser to the address URL using the open() method of webbrowser module.

The program is run through CMD(windows) or terminal(Linux) in the following
format:

  

  

    
        >>> python [File Name] [Address to be searched]
    For eg. >>> python Map.py GeeksforGeeks

 __

 __  
 __

 __

 __  
 __  
 __

# File Name -- Map.py

import sys, webbrowser

if len(sys.argv) > 1: # Argument passed

 map_string = ' '.join(sys.argv[1:])

 webbrowser.open('https://www.google.com/maps/place/' +
map_string)

 

else:

 print "Pass the string as command line argument, Try Again"

   
  
---  
  
__

__

    
        >>> python Map.py SeeksforGeeks
    The above command will open map of GeeksforGeeks in the web browser.
    

This article is contributed by **Harshit Agrawal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

