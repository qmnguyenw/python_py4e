Windows 10 Toast Notifications with Python



Python is a general-purpose language, can be used to develop both desktop and
web applications. By using a package available in Python named **win10toast**
, we can create desktop notifications. It is an easy way to get notified when
some event occurs.

The package is available in Pypi and it is installed using pip.

    
    
    pip install win10toast

About show_toast() function:

>  **Syntax:** show_toast(title=’Notification’, message=’Here comes the
> message’, icon_path=None, duration=5, threaded=False)
>
>  **Parameters:**  
>  **title** : It contains notification title.  
>  **message** : It contains notification message.  
>  **icon_path** : It contains the path to .ico file.  
>  **duration** “: It specifies the notification destruction active duration.
>
>  
>
>
>  
>

To create notifications we have to import the win10toast module. Then create
an object to ToastNotifier class and by using the method show_toast we
create a notification. It contains _header_ or title of that notification,
actual message, duration of that notification and icon for that notification.
show_toast method is a instance of notification settings.

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# import win10toast

from win10toast import ToastNotifier

 

# create an object to ToastNotifier class

n = ToastNotifier()

 

n.show_toast("GEEKSFORGEEKS", "You got notification", duration =
10,

 icon_path ="https://media.geeksforgeeks.org/wp-
content/uploads/geeks.ico")  
  
---  
  
 __

 __

 **Output:**  
![null](https://media.geeksforgeeks.org/wp-content/uploads/gee-1.png)

 **Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# import win10toast

from win10toast import ToastNotifier

 

# create an object to ToastNotifier class

n = ToastNotifier()

 

n.show_toast("GEEKSFORGEEKS", "Notification body", duration =
20,

 icon_path ="https://media.geeksforgeeks.org/wp-
content/uploads/geeks.ico")  
  
---  
  
 __

 __

 **Output:**  
![null](https://media.geeksforgeeks.org/wp-content/uploads/geek-5.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

