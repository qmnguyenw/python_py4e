Global and Local Variables in Python



Global variables are the one that is defined and declared outside a function
and we need to use them inside a function.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# This function uses global variable s

def f():

 print(s)

# Global scope

s = "I love Geeksforgeeks"

f()  
  
---  
  
 __

 __

 **Output:**  

    
    
     
    I love Geeksforgeeks

The variable s is defined as the string “I love Geeksforgeeks” before we call
the function f(). The only statement in f() is the “print s” statement. As
there are no locals, the value from the globals will be used.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# This function has a variable with

# name same as s.

def f():

 s = "Me too."

 print(s)

# Global scope

s = "I love Geeksforgeeks"

f()

print(s)  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    Me too.
    I love Geeksforgeeks.

If a variable with the same name is defined inside the scope of function as
well then it will print the value given inside the function only and not the
global value.  
The question is, what will happen if we change the value of s inside of the
function f()? Will it affect the globals as well? We test it in the following
piece of code:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def f():

 print(s)

 # This program will NOT show error

 # if we comment below line.

 s = "Me too."

 print(s)

# Global scope

s = "I love Geeksforgeeks"

f()

print(s)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Line 2: undefined: Error: local variable 's' referenced before assignment

To make the above program work, we need to use the “global” keyword. We only
need to use the global keyword in a function if we want to do assignments /
change them. global is not needed for printing and accessing. Why? Python
“assumes” that we want a local variable due to the assignment to s inside of
f(), so the first print statement throws this error message. Any variable
which is changed or created inside of a function is local if it hasn’t been
declared as a global variable. To tell Python, that we want to use the global
variable, we have to use the keyword **“global”** , as can be seen in the
following example:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# This function modifies the global variable 's'

def f():

 global s

 print(s)

 s = "Look for Geeksforgeeks Python Section"

 print(s)

# Global Scope

s = "Python is great!"

f()

print(s)  
  
---  
  
 __

 __

Now there is no ambiguity.  
 **Output:**  

    
    
    Python is great!
    Look for Geeksforgeeks Python Section.
    Look for Geeksforgeeks Python Section.

A Good Example  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

a= 1

# Uses global because there is no local 'a'

def f():

 print('Inside f() : ', a)

# Variable 'a' is redefined as a local

def g(): 

 a = 2

 print('Inside g() : ', a)

# Uses global keyword to modify global 'a'

def h(): 

 global a

 a = 3

 print('Inside h() : ', a)

# Global scope

print('global : ',a)

f()

print('global : ',a)

g()

print('global : ',a)

h()

print('global : ',a)  
  
---  
  
 __

 __

 **Output:**  

    
    
    global :  1
    Inside f() :  1
    global :  1
    Inside g() :  2
    global :  1
    Inside h() :  3
    global :  3

This article is contributed by **Shwetanshu Rohatgi**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

