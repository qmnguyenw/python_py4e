Introduction to pywhatkit module



Python offers numerous inbuilt libraries to ease our work. Among them
**pywhatkit** is a Python library for sending WhatsApp messages at a certain
time, it has several other features too.

Following are some features of pywhatkit module:

  1. Send WhatsApp messages.
  2. Play a YouTube video.
  3. Perform a Google Search.
  4. Get information on particular topic.

In Python3 pywhatkit module will not come pre-installed, so you can install it
by using the command:

> pip install pywhatkit

###  **1\. Send Whatsapp Messages:**

Here, we will learn the simplest way of using pywhatkit module which utilises
the WhatsApp webpage to automate messages sending to any number on WhatsApp.
But make sure that you have logged into your WhatsApp in your browser.

  

  

>  **Syntax:** pywhatkit.sendmsg(“receiver mobile
> number”,”message”,hours,minutes)
>
>  **Parameters:**
>
>   *  **Receiver mobile number:** The Receiver’s mobile number must be in
> string format and the country code must be mentioned before the mobile
> number.
>   *  **Message:** Message to be sent(Must be in string format).
>   *  **Hours:** This module follows the 24 hrs time format.
>   *  **Minutes:** Mention minutes of the scheduled time for the
> message(00-59).
>

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import pywhatkit

 

# using Exception Handling to avoid 

# unprecedented errors

try:

 

 # sending message to reciever

 # using pywhatkit

 pywhatkit.sendwhatmsg("+91xxxxxxxxxx", 

 "Hello from GeeksforGeeks", 

 22, 28)

 print("Successfully Sent!")

 

except:

 

 # handling exception 

 # and printing error message

 print("An Unexpected Error!")  
  
---  
  
 __

 __

###  **2\. Play a YouTube video:**

Function **pywhatkit.playonyt()** , opens the YouTube in your default browser
and plays the video you mentioned in the function. If you pass the topic name
as parameter, it plays the random video on that topic. On passing the URL of
the video as the parameter, it open that exact video.

>  **Syntax:** pywhatkit.playonyt(“url/topic name”)
>
>  **Parameters:**
>
>   *  **URL/Topic Name:** Mention the topic name or URL of the YouTube video
>

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import pywhatkit

 

# using Exception Handling

# to avoid exceptions

try:

 

 # it plays a random YouTube

 # video of GeeksforGeeks

 pywhatkit.playonyt("GeeksforGeeks")

 print("Playing...")

 

except:

 

 # printing the error message

 print("Network Error Occured")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200825160249/pywhatkityoutube-300x255.PNG)

###  **3\. Perform Google Search:**

You can perform a Google search using the following simple command. It opens
your browser and searches for the topic you have given in your code.

>  **Syntax:** pywhatkit.search(“Keyword”)
>
>  **Parameters:**
>
>   *  **Keyword:** It open your browser and performs search operation.
>

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import pywhatkit

 

# use Try Except to

# handle the Exceptions

try:

 

 # it will perform the Google search

 pywhatkit.search("GeeksforGeeks")

 print("Searching...")

 

except:

 

 # Printing Error Message

 print("An unknown error occured")  
  
---  
  
 __

 __

 ****

**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200825160540/pywhatkitgoogle-300x243.PNG)

###  **4\. Get information on particular topic:**

We can get brief information on a particular topic. We can also limit the
number of lines to be printed. Also, make sure that you are searching for the
topics that are available on Wikipedia.

>  **Syntax:** pywhatkit.info(“topic”,lines=x)
>
>  **Parameters:**
>
>   *  **Topic:** Gives the output on the topic mentioned.
>   *  **lines:** It prints the searched topic in the specified number of
> lines.
>

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import pywhatkit

 

# using Exception Handling for

# handling unprecendented errors

try:

 

 # it will perform google search

 pywhatkit.info("Google", lines = 4)

 print("\nSuccessfully Searched")

 

except:

 

 # printing error message

 print("An Unknown Error Occured")  
  
---  
  
 __

 __

 **Output:**

> Google LLC is an American multinational technology company that specializes
> in Internet-related services and products, which include online advertising
> technologies, a search engine, cloud computing, software, and hardware. It
> is considered one of the Big Four technology companies alongside Amazon,
> Apple and Microsoft.Google was founded in September 1998 by Larry Page and
> Sergey Brin while they were Ph.D. students at Stanford University in
> California. Together they own about 14 percent of its shares and control 56
> percent of the stockholder voting power through supervoting stock. They
> incorporated Google as a California privately held company on September 4,
> 1998, in California.
>
> Successfully Searched

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

