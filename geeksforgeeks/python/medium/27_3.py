Birthday Reminder Application in Python



This app helps in reminding birthdays and notifying you friend’s birthdays.
This app uses Python and Ubuntu notifications to notify users on every startup
of the system.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program For

# Birthday Reminder Application

 

# time module is must as reminder 

# is set with the help of dates

import time

 

# os module is used to notify user 

# using default "Ubuntu" notification bar

import os

 

# Birthday file is the one in which the actual birthdays

# and dates are present. This file can be 

# manually edited or can be automated. 

# For simplicity, we will edit it manually.

# Birthdays should be written in this file in

# the format: "MonthDay Name Surname" (Without Quotes)

 

birthdayFile = '/path/to/birthday/file'

 

def checkTodaysBirthdays():

 fileName = open(birthdayFile, 'r')

 today = time.strftime('%m%d')

 flag = 0

 for line in fileName:

 if today in line:

 line = line.split(' ')

 flag =1

 # line[1] contains Name and line[2] contains Surname

 os.system('notify-send "Birthdays Today: ' + line[1]

 + ' ' + line[2] + '"')

 if flag == 0:

 os.system('notify-send "No Birthdays Today!"')

 

if __name__ == '__main__':

 checkTodaysBirthdays()  
  
---  
  
 __

 __

 **Adding the script to Startup**

After writing the above code now it is the time to add this Python script to
startup. This can be done in **Ubuntu** as follows:

  1. Firstly, we have to create an executable file for our reminder.py script
  2. This can be done by typing the following command in the terminal
    
         **sudo chmod +x reminder.py** , where reminder.py is our script file name 

  3. Now we have to transfer this file to the path where Linux searches for its default files:  
Type this command in terminal:

    
         **sudo cp /path/to/our/reminder.py /usr/bin**

. This will add our executable script to /usr/bin.

  4. In global search, search for **Startup Applications**
  5. Click on Add and Give a desired Name for your process
  6. Type in the command. For example, our file name is **reminder.py** then type reminder.py in the command field and Select Add

 **NOTE** : The script runs automatically(once added to startup) everytime you
start your system. Also, If you have more than two birthdays on the same day,
both the birthdays will be notified in the notification.

  

  

 **How the birthday file should look like**

![](https://media.geeksforgeeks.org/wp-content/uploads/text-1-300x142.png)

 **Output after running the script**

![](https://media.geeksforgeeks.org/wp-content/uploads/b-1-300x158.png)

This article is contributed by **Omkar Pathak**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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

