Changing Class Members in Python



In the previous fact, we have seen that Python doesn’t have static keyword.
All variables that are assigned a value in class declaration are class
variables

 _ **We should be careful when changing value of class variable**_. If we try
to change class variable using object, a new instance (or non-static) variable
for that particular object is created and this variable shadows the class
variables. Below is Python program to demonstrate the same.

 __

 __  
 __

 __

 __  
 __  
 __

# Class for Computer Science Student

class CSStudent: 

 stream = 'cse' # Class Variable 

 def __init__(self, name, roll): 

 self.name = name 

 self.roll = roll 

 

# Driver program to test the functionality 

# Creating objects of CSStudent class 

a = CSStudent("Geek", 1) 

b = CSStudent("Nerd", 2) 

 

print ("Initially")

print ("a.stream =", a.stream )

print ("b.stream =", b.stream )

 

# This thing doesn't change class(static) variable 

# Instead creates instance variable for the object 

# 'a' that shadows class member. 

a.stream = "ece"

 

print ("\nAfter changing a.stream")

print ("a.stream =", a.stream )

print ("b.stream =", b.stream )  
  
---  
  
 __

 __

Output:

    
    
    Initially
    a.stream = cse
    b.stream = cse
    
    After changing a.stream
    a.stream = ece
    b.stream = cse

 _ **We should change class variables using class name only.**_

 __

 __  
 __

 __

 __  
 __  
 __

# Program to show how to make changes to the

# class variable in Python

 

# Class for Computer Science Student

class CSStudent:

 stream = 'cse' # Class Variable 

 def __init__(self, name, roll):

 self.name = name 

 self.roll = roll

 

# New object for further implementation

a = CSStudent("check", 3)

print "a.tream =", a.stream

 

# Correct way to change the value of class variable

CSStudent.stream = "mec"

print "\nClass variable changes to mec"

 

# New object for further implementation

b = CSStudent("carter", 4)

 

print "\nValue of variable steam for each object"

print "a.stream =", a.stream

print "b.stream =", b.stream  
  
---  
  
 __

 __

Output:

  

  

    
    
    a.tream = cse
    
    Class variable changes to mec
    
    Value of variable steam for each object
    a.stream = mec
    b.stream = mec
    

This article is contributed by **Nikhil Kumar Singh**. If you like
GeeksforGeeks and would like to contribute, you can also write an article and
mail your article to contribute@geeksforgeeks.org. See your article appearing
on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

