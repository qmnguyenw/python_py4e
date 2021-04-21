Python program to hide the mouse cursor on the Terminal screen



Write a program to hide the mouse cursor on the terminal screen.

 **Approach:**

  * The curses package is imported and used for this task in C language, **napms** function call is used for the delay, and **curs_set()** function is called to make the cursor disappear.
  * In Python, a package called UniCurses, which is similar to the curses package, is imported and used. In the program, the **sleep()** function is used for the delay and the **curs_set()** function is called to make the cursor disappear and then appear again.

Below is the implementation of the above approach:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for the above approach

import curses

import time

 

# Initializing curses 

stdscr = curses.initscr()

 

# Setting the cursor to visible by 

# inserting 1 as argument

curses.curs_set(1) 

 

# Delay of 2 seconds

time.sleep(2)

 

# Setting the cursor to invisible by 

# inserting 0 as argument

curses.curs_set(0) 

 

# Delay of 2 seconds

time.sleep(2)

 

# Setting the cursor to visible by 

# inserting 1 as argument

curses.curs_set(1) 

 

# Delay of 2 seconds

time.sleep(2)

 

# Restoring terminal to it's

# original state

curses.endwin()  
  
---  
  
 __

 __

 **Output:**  
After running the program, a new window appears:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200813111813/Screenshot3478.png)

  

  

After 2 seconds, the mouse cursor disappears:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200813111815/Screenshot3479.png)

After 4 seconds, the mouse cursor appears again:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200813111813/Screenshot3478.png)

After 6 seconds, the program ends:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200813111917/Screenshot3471.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

