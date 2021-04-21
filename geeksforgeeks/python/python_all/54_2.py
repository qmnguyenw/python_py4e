How to change any data type into a String in Python?



Python defines type conversion functions to directly convert one data type to
another which is useful in day to day and competitive programming. A string is
a sequence of characters. Strings are amongst the most popular types in
Python. We can create them simply by enclosing characters in quotes.

 **Example :** Creating strings in different ways :

 __

 __  
 __

 __

 __  
 __  
 __

# creating string using ' '

str1 = 'Welcome to the Geeks for Geeks !'

print(str1)

 

# creating string using " "

str2 = "Welcome Geek !"

print(str2)

 

# creating string using ''' '''

str3 = '''Welcome again'''

print(str3)  
  
---  
  
 __

 __

 **Output :**

    
    
    Welcome to the Geeks for Geeks!
    Welcome Geek!
    Welcome again

## Changing any data type into a String

There are two ways for changing any data type into a String in Python :

  1. Using the str() function
  2. Using the __str__() function

 **Method 1 :** Using the str() function  
Any built-in data type can be converted into its string representation by the
str() function. Built-in data type in python include:- int, float,
complex, list, tuple, dict etc.  
 **Syntax :**

  

  

    
    
    str(built-in data type)

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

# a is of type int

a = 10

print("Type before : ", type(a))

 

# converting the type from int to str

a1 = str(a)

print("Type after : ", type(a1))

 

# b is of type float

b = 10.10

print("\nType before : ", type(b))

 

# converting the type from float to str

b1 = str(b)

print("Type after : ", type(b1))

 

# type of c is list

c = [1, 2, 3]

print("\nType before :", type(c))

 

# converting the type from list to str

c1 = str(c)

print("Type after : ", type(c1))

 

# type of d is tuple

d = (1, 2, 3)

print("\nType before:-", type(d))

 

# converting the type from tuple to str

d1 = str(d)

print("Type after:-", type(d1))  
  
---  
  
 __

 __

 **Output:**

    
    
    Type before : <class 'int'>
    Type after : <class 'str'>
    
    Type before : <class 'float'>
    Type after : <class 'str'>
    
    Type before : <class 'list'>
    Type after : <class 'str'>
    
    Type before : <class 'tuple'>
    Type after : <class 'str'>
    

**Method 2 :** Defining __str__() function for a user defined class to be
converted to string representation. For a user defined class to be converted
to string representation, __str__() function needs to be defined in it.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

# class addition

class addition:

 def __init__(self):

 self.a = 10

 self.b = 10

 

 # defining __str__() function

 def __str__(self):

 return 'value of a = {} value of b = {}'.format(self.a,
self.b)

 

# creating object ad

ad = addition()

print(str(ad))

 

# printing the type

print(type(str(ad)))  
  
---  
  
 __

 __

 **Output:**

    
    
    value of a =10 value of b =10
    <class 'str'>

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

