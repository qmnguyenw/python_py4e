Access files of a devices in the same network using Python



We have so many ways to Transfer Files from one computer to another in Linux
and Ubuntu but there we have to change the permissions of the Apache Folder
and then Share the files. But in windows, we cannot share files using Apache
so here we have discussed Python Method to Share files between Systems and
Mobiles which are connected on the same network.

Python is an interpreter, User Friendly, and easy Language. Python has a vast
number of modules in it. Here we have used **http.server** module for Sharing
of files between the Systems Connected on the same Network. This module is
used for defining HTTP Servers(Web Servers). Servers are software or hardware
that processes requests and deliver data to a client.

### Step-by-Approach:

  * For implementing this you just need a small command to be run in the Command Prompt(cmd).

> python -m http.server

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210309182512/Capture2.PNG)

  * By running the above command a Window Security Alert pop-up may occur. You may choose the option as per your requirement.

![](https://media.geeksforgeeks.org/wp-content/uploads/20210309182510/12.PNG)

  

  

  * For accessing the server locally we need to visit http://localhost:8000/ or http://127.0.0.1:8000/ Here we can see all the directories of your local storage along with all the data. You can also access an HTML page, It will be rendered by your web browser as you access it.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210309182633/Screenshot41.png)

  * On the other hand, you can see the activity logs in the command prompt.

![](https://media.geeksforgeeks.org/wp-content/uploads/20210309182511/22.PNG)

  * You can access the other systems which are on the same network just by doing the above process. To turn off, the server just presses Ctrl+c in the command prompt.

In this way, one can easily access files in a device in the same network.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

