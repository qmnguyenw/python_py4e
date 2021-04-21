Website Blocker Using Python



This is real world program which blocks certain distracting website like
Facebook, Youtube etc during your work hours.

 **About the program :** What we are going to in this program is that we will
pass the link of websites which you think is distracting and the time that you
are working on your computer and program will block those website.

 **Program Architecture:**

  1. Every system have **host** file whether it is Mac, Windows or Linux.  
 **Host** file in Mac and Linux :

    
        /etc/hosts

 **Host** file in Windows:

  

  

    
        C:\Windows\System32\drivers\etc

  2.  **Working of host file:** Host is an operating system file which maps hostnames to IP addresses. In this program we will be mapping hostnames of websites to our localhost address. Using python file handling manipulation we will write the hostname in hosts.txt and remove the lines after your working hours.

 **Host file in Mac:**

![](https://media.geeksforgeeks.org/wp-content/uploads/Host_file_in_mac.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Run this script as root

 

import time

from datetime import datetime as dt

 

# change hosts path according to your OS

hosts_path = "/etc/hosts"

# localhost's IP

redirect = "127.0.0.1"

 

# websites That you want to block

website_list =

["www.facebook.com","facebook.com",

 "dub119.mail.live.com","www.dub119.mail.live.com",

 "www.gmail.com","gmail.com"]

 

while True:

 

 # time of your work

 if dt(dt.now().year, dt.now().month, dt.now().day,8) 

 < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):

 print("Working hours...")

 with open(hosts_path, 'r+') as file:

 content = file.read()

 for website in website_list:

 if website in content:

 pass

 else:

 # mapping hostnames to your localhost IP address

 file.write(redirect + " " + website + "\n")

 else:

 with open(hosts_path, 'r+') as file:

 content=file.readlines()

 file.seek(0)

 for line in content:

 if not any(website in line for website in
website_list):

 file.write(line)

 

 # removing hostnmes from host file

 file.truncate()

 

 print("Fun hours...")

 time.sleep(5)  
  
---  
  
 __

 __

 **Special note for Windows users :** Windows user need to create a duplicate
of OS’s host file. Now provide the path of the duplicate file in
**hosts_path** mentioned in the script.

 **Scheduling above script in Mac :** For scheduling above script in Mac you
have to open crontab in your terminal as a root.

  1. Write following command in terminal:
    
        sudo crontab -e

Your terminal should look like this:  
![](https://media.geeksforgeeks.org/wp-content/uploads/Crontab_1.png)  
![](https://media.geeksforgeeks.org/wp-content/uploads/Crontab_2.png)

  2. Now press “i” to go into insert/editing mode and write @reboot python_script_path .
  3. Save the tab by pressing first esc to quit write mode and fall back to command mode and now write “:wq” and finally press enter to validate.
  4. Restart your system and see the magic.

 **Scheduling in Windows:** Scheduling of above script is little bit trick but
I will guide you step by step-

  1. First of all change the extension of your script from “.py” to “.pyw”.
  2. Now open task scheduler. Task scheduler should look like this:  
![](https://media.geeksforgeeks.org/wp-content/uploads/Task_schduler.png)

You may see website blocker already scheduled because I have already scheduled
in my computer for my testing purpose. Follow further instruction of
scheduling carefully in order to schedule website blocker in your computer.

  3. Click on “create task”. Fill the name of your choice and flag “Run with highest privilege”.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Create_task_1.png)

  

  

![](https://media.geeksforgeeks.org/wp-content/uploads/Create_task_2.png)

  4. Now go to triggers, select “At startup” for begin the task.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Trigger.png)

  5. Go to Action bar and create a new action and give path of your script.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Action_1.png)

![](https://media.geeksforgeeks.org/wp-content/uploads/Action_2.png)

  6. Go to conditions bar and unflag the power section.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Conditions_1.png)

![](https://media.geeksforgeeks.org/wp-content/uploads/Conditions_2.png)

  7. Press ok and you can see the script scheduled.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Task_schduler-1.png)

  8. Finally restart your computer and see the magic.  
![](https://media.geeksforgeeks.org/wp-content/uploads/FB_blocked.png)  
 **Note:** You can also check instantly by clicking run button.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

