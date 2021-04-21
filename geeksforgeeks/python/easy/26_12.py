Class and Instance Attributes in Python



 **Class attributes**

Class attributes belong to the class itself they will be shared by all the
instances. Such attributes are defined in the class body parts usually at the
top, for legibility.

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python code here

class sampleclass:

 count = 0 # class attribute

 

 def increase(self):

 sampleclass.count += 1

 

# Calling increase() on an object

s1 = sampleclass()

s1.increase() 

print(s1.count)

 

# Calling increase on one more

# object

s2 = sampleclass()

s2.increase()

print(s2.count)

 

print(sampleclass.count)  
  
---  
  
 __

 __

Output:

    
    
    1              
    2                           
    2

 **Instance Attributes**

Unlike class attributes, instance attributes are not shared by objects. Every
object has its own copy of the instance attribute (In case of class attributes
all object refer to single copy).

  

  

To list the attributes of an instance/object, we have two functions:-  
1\. **vars()** – This function displays the attribute of an instance in the
form of an dictionary.  
2\. **dir()** – This function displays more attributes than vars function,as
it is not limited to instance. It displays the class attributes as well. It
also displays the attributes of its ancestor classes.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# instance attributes.

class emp:

 def __init__(self):

 self.name = 'xyz'

 self.salary = 4000

 

 def show(self):

 print(self.name)

 print(self.salary)

 

e1 = emp()

print("Dictionary form :", vars(e1))

print(dir(e1))  
  
---  
  
 __

 __

Output :

    
    
    Dictionary form :{'salary': 4000, 'name': 'xyz'}
    ['__doc__', '__init__', '__module__', 'name', 'salary', 'show']

This article is contributed by **Harsh Valecha**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

