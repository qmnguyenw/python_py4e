bool() in Python



The **bool()** method is used to return or convert a value to a Boolean value
i.e., True or False, using the standard truth testing procedure.  

**Syntax:**

    
    
    **bool([x])**
    

The bool() method in general takes only one parameter(here x), on which the
standard truth testing procedure can be applied. **If no parameter is passed,
then by default it returns False**. So, passing a parameter is optional. It
can return one of the two values.

  * It returns True if the parameter or value passed is True.
  * It returns False if the parameter or value passed is False.

Here are a few cases, in which Python’s bool() method returns false. Except
these all other values return True.

  * If a False value is passed.
  * If None is passed.
  * If an empty sequence is passed, such as (), [], ”, etc
  * If Zero is passed in any numeric type, such as 0, 0.0 etc
  * If an empty mapping is passed, such as {}.
  * If Objects of Classes having __bool__() or __len()__ method, returning 0 or False

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# built-in method bool()

# Returns False as x is False

x = False

print(bool(x))

# Returns True as x is True

x = True

print(bool(x))

# Returns False as x is not equal to y

x = 5

y = 10

print(bool(x==y))

# Returns False as x is None

x = None

print(bool(x))

# Returns False as x is an empty sequence

x = ()

print(bool(x))

# Returns False as x is an empty mapping

x = {}

print(bool(x))

# Returns False as x is 0

x = 0.0

print(bool(x))

# Returns True as x is a non empty string

x = 'GeeksforGeeks'

print(bool(x))  
  
---  
  
 __

 __

 **Output:**  

    
    
    False
    True
    False
    False
    False
    False
    False
    True
    
    
    

**Application**

Here is a program to find out even and odd by the use of bool() method. You
may use other inputs and check out the results.  
Example:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to check whether a number

# is even or odd using bool()

def check(num):

 return(bool(num%2==0))

# Driver Code

num = 8;

if(check(num)):

 print("Even")

else:

 print("Odd")  
  
---  
  
 __

 __

 **Output:**  

    
    
    Even
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

