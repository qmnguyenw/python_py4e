Dunder or magic methods in Python



Dunder or magic methods in Python are the methods having two prefix and suffix
underscores in the method name. Dunder here means “Double Under
(Underscores)”. These are commonly used for operator overloading. Few examples
for magic methods are: __init__, __add__, __len__, __repr__ etc.

The __init__ method for initialization is invoked without any call, when an
instance of a class is created, like constructors in certain other programming
languages such as C++, Java, C#, PHP etc. These methods are the reason we can
add two strings with ‘+’ operator without any explicit typecasting.

Here’s a simple implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# declare our own string class

class String:

 

 # magic method to initiate object

 def __init__(self, string):

 self.string = string

 

# Driver Code

if __name__ == '__main__':

 

 # object creation

 string1 = String('Hello')

 

 # print object location

 print(string1)  
  
---  
  
 __

 __

 **Output :**

    
    
    <__main__.String object at 0x7fe992215390>
    

  
The above snippet of code prints only the memory address of the string object.
Let’s add a __repr__ method to represent our object.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# declare our own string class

class String:

 

 # magic method to initiate object

 def __init__(self, string):

 self.string = string

 

 # print our string object

 def __repr__(self):

 return 'Object: {}'.format(self.string)

 

# Driver Code

if __name__ == '__main__':

 

 # object creation

 string1 = String('Hello')

 

 # print object location

 print(string1)  
  
---  
  
 __

 __

 **Output :**

    
    
    Object: Hello
    

  
**If we try to add a string to it :**

 __

 __  
 __

 __

 __  
 __  
 __

# declare our own string class

class String:

 

 # magic method to initiate object

 def __init__(self, string):

 self.string = string

 

 # print our string object

 def __repr__(self):

 return 'Object: {}'.format(self.string)

 

# Driver Code

if __name__ == '__main__':

 

 # object creation

 string1 = String('Hello')

 

 # concatenate String object and a string

 print(string1 +' world')  
  
---  
  
 __

 __

 **Output :**

    
    
    **TypeError** : unsupported operand type(s) for +: 'String' and 'str'
    

  
Now add __add__ method to String class :

 __

 __  
 __

 __

 __  
 __  
 __

# declare our own string class

class String:

 

 # magic method to initiate object

 def __init__(self, string):

 self.string = string 

 

 # print our string object

 def __repr__(self):

 return 'Object: {}'.format(self.string)

 

 def __add__(self, other):

 return self.string + other

 

# Driver Code

if __name__ == '__main__':

 

 # object creation

 string1 = String('Hello')

 

 # concatenate String object and a string

 print(string1 +' Geeks')  
  
---  
  
 __

 __

Output :

    
    
    Hello Geeks
    

**Reference :** docs.python.org.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

