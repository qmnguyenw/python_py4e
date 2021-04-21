Polymorphism in Python



 **What is Polymorphism :** The word polymorphism means having many forms. In
programming, polymorphism means same function name (but different signatures)
being uses for different types.

 **Example of inbuilt polymorphic functions :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate in-built poly-

# morphic functions

 

# len() being used for a string

print(len("geeks"))

 

# len() being used for a list

print(len([10, 20, 30]))  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    3
    

**Examples of used defined polymorphic functions :**

 __

 __  
 __

 __

 __  
 __  
 __

# A simple Python function to demonstrate

# Polymorphism

 

def add(x, y, z = 0): 

 return x + y+z

 

# Driver code 

print(add(2, 3))

print(add(2, 3, 4))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    5
    9
    

