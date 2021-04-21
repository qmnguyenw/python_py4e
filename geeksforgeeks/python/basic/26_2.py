Python 3 basics



Python was developed by Guido van Rossum in the early 1990s and its latest
version is 3.7.1, we can simply call it as Python3. Python 3.0 was released in
2008. and is interpreted language i.e it’s not compiled and the interpreter
will check the code line by line. This article can used to learn very basics
of Python programming language.

So before moving on further.. let’s do the most popular ‘HelloWorld’ tradition
😛 and hence compare Python’s Syntax with C, C++, Java ( I have taken these 3
because they are most famous and mostly used languages).

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for "Hello World"

# nothing else to type...see how simple is the syntax.

 

print("Hello World")   
  
---  
  
__

__

**Note:** Please note that Python for its scope doesn’t depend on the braces (
{ } ), instead it uses indentation for its scope.  
Now moving on further **Lets start our basics of Python**. I will be covering
the basics in some small sections. Just go through them and trust me you’ll
learn the basics of Python very easily.

 **Introduction and Setup**

  1. If you are on **Windows OS** download Python by Clicking here and now install from the setup and in the start menu type IDLE.IDLE, you can think it as an Python’s IDE to run the Python Scripts.

It will look somehow this :  
![](https://media.geeksforgeeks.org/wp-content/uploads/Python_console.png)

  2. If you are on **Linux/Unix-like** just open the terminal and on 99% linux OS Python comes preinstalled with the OS.Just type ‘python3’ in terminal and you are ready to go.  
It will look like this :  
![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2017-07-20-18-47-54.png)

> The ” >>> ” represents the python shell and its ready to take python
> commands and code.
>
>  
>
>
>  
>

 **Variables and Data Structures**

In other programming languages like C, C++, and Java, you will need to declare
the type of variables but in Python you don’t need to do that. Just type in
the variable and when values will be given to it, then it will automatically
know whether the value given would be an int, float, or char or even a String.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to declare variables

myNumber = 3

print(myNumber)

 

myNumber2 = 4.5

print(myNumber2)

 

myNumber ="helloworld"

print(myNumber)  
  
---  
  
 __

 __

 **Output:**

    
        3
    4.5
    helloworld
    

See, how simple is it, just create a variable and assign it any value you want
and then use the print function to print it. Python have 4 types of built in
Data Structures namely List, Dictionary, Tuple and Set.

 **List** is the most basic Data Structure in python. List is a mutable data
structure i.e items can be added to list later after the list creation. It’s
like you are going to shop at the local market and made a list of some items
and later on you can add more and more items to the list.  
append() function is used to add data to the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate a list

 

# creates a empty list

nums = [] 

 

# appending data in list

nums.append(21)

nums.append(40.5)

nums.append("String")

 

print(nums)  
  
---  
  
 __

 __

 **Output:**

    
        [21, 40.5, String]

 **Comments:**

    
        # is used for single line comment in Python
    """ this is a comment """ is used for multi line comments

 **Input and Output**

  

  

In this section, we will learn how to take input from the user and hence
manipulate it or simply display it. input() function is used to take input
from the user.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# getting input from user

name = input("Enter your name: ") 

 

# user entered the name 'harssh'

print("hello", name)  
  
---  
  
 __

 __

 **Output:**

    
        hello harssh   

__

__  
__

__

__  
__  
__

# Python3 program to get input from user

 

# accepting integer from the user

# the return type of input() function is string ,

# so we need to convert the input to integer

num1 = int(input("Enter num1: "))

num2 = int(input("Enter num2: "))

 

num3 = num1 * num2

print("Product is: ", num3)  
  
---  
  
 __

 __

 **Output:**

    
        Enter num1: 8 Enter num2: 6 ('Product is: ', 48)
    

**Selection**

Selection in Python is made using the two keywords ‘if’ and ‘elif’ and else
(elseif)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# selection statement

 

num1 = 34

if(num1>12):

 print("Num1 is good")

elif(num1>35):

 print("Num2 is not gooooo....")

else:

 print("Num2 is great")  
  
---  
  
 __

 __

 **Output:**

    
        Num1 is good

 **Functions**

You can think of functions like a bunch of code that is intended to do a
particular task in the whole Python script. Python used the keyword ‘def’ to
define a function.  
 **Syntax:**

    
        def function-name(arguments):
                #function body

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# functions

def hello():

 print("hello")

 print("hello again")

hello()

 

# calling function

hello()   
  
---  
  
__

__

**Output:**

    
        hello
    hello again
    hello
    hello again
    

Now as we know any program starts from a ‘main’ function…lets create a main
function like in many other programming languages.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# function with main

def getInteger():

 result = int(input("Enter integer: "))

 return result

 

def Main():

 print("Started")

 

 # calling the getInteger function and 

 # storing its returned value in the output variable

 output = getInteger() 

 print(output)

 

# now we are required to tell Python 

# for 'Main' function existence

if __name__=="__main__":

 Main()  
  
---  
  
 __

 __

 **Output:**

    
        Started
    Enter integer: 5
    

**Iteration (Looping)**

As the name suggests it calls repeating things again and again. We will use
the most popular ‘for’ loop here.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# a simple for loop

 

for step in range(5): 

 print(step)  
  
---  
  
 __

 __

 **Output:**

    
        0
    1
    2
    3
    4
    

**Modules**

Python has a very rich module library that has several functions to do many
tasks. You can read more about Python’s standard library by Clicking here  
‘import’ keyword is used to import a particular module into your python code.
For instance consider the following program.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# math module

import math

 

def Main():

 num = -85

 

 # fabs is used to get the absolute 

 # value of a decimal

 num = math.fabs(num) 

 print(num)

 

 

if __name__=="__main__":

 Main()  
  
---  
  
 __

 __

 **Output:**

    
        85.0

These are some of the most basics of the Python programming language and I
will be covering both the intermediate and advanced level Python topics in my
upcoming articles.

This article is contributed by **Harsh Wardhan Chaudhary**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks. Your article will be reviewed first by Geeks
for Geeks team before publishing.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

