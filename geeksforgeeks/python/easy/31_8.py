Namedtuple in Python



Python supports a type of container like dictionaries called “
**namedtuple()** ” present in module, “ **collections** “. Like dictionaries
they contain keys that are hashed to a particular value. But on contrary, it
supports both access from key value and iteration, the functionality that
dictionaries lack.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate namedtuple()

 

from collections import namedtuple 

 

# Declaring namedtuple() 

Student = namedtuple('Student',['name','age','DOB']) 

 

# Adding values 

S = Student('Nandini','19','2541997') 

 

# Access using index 

print ("The Student age using index is : ",end ="") 

print (S[1]) 

 

# Access using name 

print ("The Student name using keyname is : ",end ="") 

print (S.name)  
  
---  
  
 __

 __

 **Output:**

    
    
    The Student age using index is : 19
    The Student name using keyname is : Nandini

 **Let’s see various Operations on namedtuple() :**

## Access Operations

 ****

  

  

* Access by index :

