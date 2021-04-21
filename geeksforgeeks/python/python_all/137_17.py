Python | Animated Banner showing ‘GeeksForGeeks’



Want to be fancy and create an animated banner? This program is going to print
a cool animated banner to the Python console. Initially, it is suitable just
for showing **‘GeeksForGeeks’**. Consider it as a challenge by adding more
characters yourself.

 **IMPORTANT NOTE:- For this to work, you have to open the file in the
console, and not through the editor/IDLE.**

Python implementation:

 __

 __  
 __

 __

 __  
 __  
 __

import os

import time

 

#You can change the width of the display according to your wish.

WIDTH = 250

 

# Written below currently is GeeksForGeeks. If you wish to get more

# written, you have to add each alphabet manually.

message = "geeksforgeeks".upper()

 

#The message will get printed here.

printedMessage = [
"","","","","","","","","","","","","","", ]

 

"""

What we have done here is a dictionary mapping the letters to their line.

These mapped indexes identify itself to each letter in the dictionary and 

also for each line in the display.

"""

characters = { " " : [ " ",

 " ",

 " ",

 " ",

 " ",

 " ",

 " " ],

 

 "E" : [ "*****",

 "* ",

 "* ",

 "*****",

 "* ",

 "* ",

 "*****" ],

 

 "O" : [ "*****",

 "* *",

 "* *",

 "* *",

 "* *",

 "* *",

 "*****" ],

 

 "K" : [ " * *",

 " * * ",

 " * * ",

 " ** ",

 " * * ",

 " * * ",

 " * *" ],

 

 "S" : [" **** ",

 " * ",

 " * ",

 " *** ",

 " * ",

 " * ",

 " **** " ],

 

 

 "G" : [" *** ",

 "* * ",

 "* ",

 "* *** ",

 "* * ",

 "* * ",

 " *** " ],

 

 

 "F" : ["***** ",

 "* ",

 "* ",

 "**** ",

 "* ",

 "* ",

 "* " ],

 

 "R" : [" **** ",

 " * * ",

 " * * ",

 " **** ",

 " * * ",

 " * * ",

 " * * " ]

 

 

 }

 

 

for row in range(7):

 for char in message:

 printedMessage[row] += (str(characters[char][row]) + " ")

 

offset = WIDTH

while True:

 os.system("cls")

 

 for row in range(7):

 print(" " * offset +
printedMessage[row][max(0,offset*-1):WIDTH - offset])

 

 offset -=1

 

 if offset <= ((len(message)+2)*6) * -1:

 offset = WIDTH

 

 #Use this to change the speed of the animation that you wish to keep.

 time.sleep(0.10)  
  
---  
  
 __

 __

 **Output (The original output will be moving from right to left. Basically,
it’s an animation.):**  
![Organized Folder](https://media.geeksforgeeks.org/wp-
content/uploads/20190525223000/animated.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

