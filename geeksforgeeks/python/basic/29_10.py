Python | Set 2 (Variables, Expressions, Conditions and Functions)



Introduction to Python has been dealt with in this article. Now, let us begin
with learning python.

 **Running your First Code in Python**  
Python programs are not compiled, rather they are interpreted. Now, let us
move to writing a python code and running it. Please make sure that python is
installed on the system you are working. If it is not installed, download it
from here. We will be using python 2.7.

 **Making a Python file:**  
Python files are stored with the extension “.py”. Open text editor and save a
file with the name “hello.py”. Open it and write the following code:

 __

 __  
 __

 __

 __  
 __  
 __

print "Hello World"

# Notice that NO semi-colon is to be used  
  
---  
  
 __

 __

 **Reading the file contents:**  
Linux System – Move to the directory from terminal where the created file
(hello.py) is stored by using the ‘cd’ command, and then type the following in
the terminal :

    
    
    python hello.py
    

Windows system – Open command prompt and move to the directory where the file
is stored by using the ‘cd’ command and then run the file by writing the file
name as command.

  

  

 **Variables in Python**  
Variables need not be declared first in python. They can be used directly.
Variables in python are case sensitive as most of the other programming
languages.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

a= 3

A = 4

print a

print A  
  
---  
  
 __

 __

The output is :

    
    
    3
    4
    

**Expressions in Python**  
Arithmetic operations in python can be performed by using arithmetic operators
and some of the in-built functions.

 __

 __  
 __

 __

 __  
 __  
 __

a= 2

b = 3

c = a + b

print c

d = a * b

print d  
  
---  
  
 __

 __

The output is :

    
    
    5
    6
    

**Conditions in Python**  
Conditional output in python can be obtained by using if-else and elif (else
if) statements.

 __

 __  
 __

 __

 __  
 __  
 __

a= 3

b = 9

if b % a == 0 :

 print "b is divisible by a"

elif b + 1 == 10:

 print "Increment in b produces 10"

else:

 print "You are in else statement"  
  
---  
  
 __

 __

The output is :

    
    
    b is divisible by a

 **Functions in Python**  
A function in python is declared by the keyword ‘def’ before the name of the
function. The return type of the function need not be specified explicitly in
python. The function can be invoked by writing the function name followed by
the parameter list in the brackets.

 __

 __  
 __

 __

 __  
 __  
 __

# Function for checking the divisibility

# Notice the indentation after function declaration

# and if and else statements

def checkDivisibility(a, b):

 if a % b == 0 :

 print "a is divisible by b"

 else:

 print "a is not divisible by b"

#Driver program to test the above function

checkDivisibility(4, 2)  
  
---  
  
 __

 __

The output is :

    
    
    a is divisible by b

So, python is a very simplified and less cumbersome language to code in. This
easiness of python is itself promoting its wide use.

  * Next Article- Python Data Types
  * Quiz – Functions in Python

  
This article has been contributed by **Nikhil Kumar Singh.** Please write
comments if you find anything incorrect, or you want to share more information
about the topic discussed above.  
  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

