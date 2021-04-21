Python Desktop Notifier using Plyer module



This article demonstrates how to create a simple **Desktop Notifier**
application using Python. A desktop notifier is a simple application which
produces a notification message in form of a pop-up message on desktop. We
will be using plyer module for the same.

### Module Needed

  1.  **time:** This module works with the time object and is installed by default
  2.  **Plyer:** Plyer module is used to access the features of the hardware. This module does not comes built-in with Python. We need to install it externally. To install this module type the below command in the terminal.

    
    
    pip install plyer 

**Approach:**

 **Step 1)** Import the notification class from the plyer module

    
    
    from plyer import notification

 **Step 2)** After that you just need to call the notify method of this class.

>  **Syntax:** notify(title=”, message=”, app_name=”, app_icon=”, timeout=10,
> ticker=”, toast=False)
>
>  
>
>
>  
>
>
>  **Parameters:**
>
>   *  **title** ( _str_ ) – Title of the notification
>   *  **message** ( _str_ ) – Message of the notification
>   *  **app_name** ( _str_ ) – Name of the app launching this notification
>   *  **app_icon** ( _str_ ) – Icon to be displayed along with the message
>   *  **timeout** ( _int_ ) – time to display the message for, defaults to 10
>   *  **ticker** ( _str_ ) – text to display on status bar as the
> notification arrives
>   *  **toast** ( _bool_ ) – simple Android message instead of full
> notification
>

 **Step 3)** Add the sleep function to show that notification again.

Below is the implemenation.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import time

from plyer import notification

 

 

if __name__=="__main__":

 

 notification.notify(

 title = "HEADING HERE",

 message=" DESCRIPTION HERE" ,

 

 # displaying time

 timeout=2

)

 # waiting time

 time.sleep(7)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200527184413/pythonnotification.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

