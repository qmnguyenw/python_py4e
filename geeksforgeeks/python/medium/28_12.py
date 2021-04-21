Create a Website Alarm Using Python



We use Bookmarks to remember the important websites which we think we will use
them very often in future.  
Here’s a simple python code which takes the URL of the website as its first
input and the time you want to open it as the second input.

As the time reaches your given value of the time, it’ll open the URL that you
requested in the web browser automatically.  
In this code, we’ll import two python modules – Time and Webbrowser.

 __

 __  
 __

 __

 __  
 __  
 __

# Import the time module, it provides various time-related

# functions. 

import time 

 

# Import the webbrowser module, it is used to 

# display various HTML documents to the user. 

import webbrowser 

 

# First Input: It is the time of the form 

# 'Hours:Minutes:Seconds' that you'll 

# use to set the alarm. 

Set_Alarm = input("Set the website alarm as H:M:S:") 

 

# Second Input: It is the URL that you want 

# to open on the given time. 

url = input("Enter the website you want to open:") 

 

# This is the actual time that we will use to print. 

Actual_Time = time.strftime("%I:%M:%S") 

 

# This is the while loop that'll print the time 

# until it's value will be equal to the alarm time 

while (Actual_Time != Set_Alarm): 

 print ("The time is " + Actual_Time) 

 Actual_Time = time.strftime("%I:%M:%S") 

 time.sleep(1) 

 

 

# This if statement plays the role when its the 

# alarm time and executes the code within it. 

if (Actual_Time == Set_Alarm): 

 print ("You should see your webpage now :-)")

 

 # We are calling the open() 

 # function from the webrowser module. 

 webbrowser.open(url)   
  
---  
  
__

__

You can contribute to the code by goinghere.

This article is contributed by **Shivam Sharma**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

You can contribute to the code by going here.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

