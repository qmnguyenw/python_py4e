Working with the Python Debugger



Python Debugger may be a new word for the beginner developers . In this post ,
we will try to explain the meaning of Debugging and Debugging with Python .

## What is Debugging?

Debugging means the complete control over the program execution. Developers
use debugging to overcome program from any bad issues. So debugging is a
healthier process for the program and keeps the diseases bugs far away. Python
also allows developers to debug the programs using pdb module that comes with
standard Python by default. We just need to import pdb module in the Python
script. Using pdb module, we can set breakpoints in the program to check the
current status. We can Change the flow of execution by using **** jump, ****
continue statements . Let’s understand debugging with a Python program.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Program to print Multiplication

# table of a Number

n=5

for x in range(1,11) :

 print( n , '*' , x , '=' , n*x )  
  
---  
  
 __

 __

 **Output:**

    
    
    5 * 1 = 5
    5 * 2 = 10
    5 * 3 = 15
    5 * 4 = 20
    5 * 5 = 25
    5 * 6 = 30
    5 * 7 = 35
    5 * 8 = 40
    5 * 9 = 45
    5 * 10 = 50

This program simply print multiplication table but now we need to debug the
loop steps using set_trace() function call to pdb module .

  

  

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to print Multiplication Table

# We want to debug the for loop so we use

# set_trace() call to pdb module

 

import pdb

 

 

# It means , the Start of Debugging Mode

pdb.set_trace()

 

n=5

for x in range(1,11) :

 print( n , '*' , x , '=' , n*x )  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200616140747/pythondebugging1.png)

### Basic Commands to use Python Debugger

**list** command to see entire program .

![list command in pdb debugger](https://media.geeksforgeeks.org/wp-
content/uploads/20200613035653/listcommandPythonDebuggerpdb.PNG)

list command

 **list 3 , 6** to see the program lines from 3 to 5 only .

![list command in pdb debugger](https://media.geeksforgeeks.org/wp-
content/uploads/20200613035654/listlinescommandPythonDebuggerpdb-300x142.PNG)

list lines command in pdb debugger

**break** command to stop the program execution at particular line .

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200613035650/breakcommandPythonDebuggerpdb-300x45.PNG)

break command in pdb debugger

**continue** command to see the next step in the loop .

![continue command in pdb debugger](https://media.geeksforgeeks.org/wp-
content/uploads/20200613035651/continuecommandPythonDebuggerpdb-300x134.PNG)

continue command in pdb debugger

 **jump** command allows us to go on any particular line in the program .

![jump command in pdb debugger](https://media.geeksforgeeks.org/wp-
content/uploads/20200613035652/jumpcommandPythonDebuggerpdb-300x50.PNG)

jump command in pdb debugger

**pp** command to see variable value at the current position in the program .

![pp command in pdb debugger](https://media.geeksforgeeks.org/wp-
content/uploads/20200613035655/ppcommandinpdbdebugger-300x88.PNG)

pp command in pdb debugger

 **disable** command to disable the current line output and we can use
continue command to skip this line in program. We use quit or exit command to
come outside the debugging mode .

## Conclusion

Debugging helps developers to analyze programs line by line. Developers see
the every interpreted line by using debugging mode in programs. Python comes
with by default debugger that is easy to import and use. So it is good to
start with debugger when confused about execution of large loops, current
variable values and all .

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

