How to create a list of object in Python class



We can create list of object in Python by appending class **instances** to
**list**. By this, every index in the list can point to instance attributes
and methods of the class and can access them. If you observe it closely, a
list of objects behaves like an array of structures in C. Let’s try to
understand it better with the help of examples.

 **Example #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code here creating class

class geeks: 

 def __init__(self, name, roll): 

 self.name = name 

 self.roll = roll

 

# creating list 

list = [] 

 

# appending instances to list 

list.append( geeks('Akash', 2) )

list.append( geeks('Deependra', 40) )

list.append( geeks('Reaper', 44) )

 

for obj in list:

 print( obj.name, obj.roll, sep =' ' )

 

# We can also access instances attributes

# as list[0].name, list[0].roll and so on.  
  
---  
  
 __

 __

 **Output:**

    
    
    Akash 2
    Deependra 40
    Reaper 44
    

**Example #2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code here for creating class

class geeks: 

 def __init__(self, x, y): 

 self.x = x 

 self.y = y

 

 def Sum(self):

 print( self.x + self.y )

 

# creating list 

list = [] 

 

# appending instances to list 

list.append( geeks(2, 3) )

list.append( geeks(12, 13) )

list.append( geeks(22, 33) )

 

for obj in list:

 # calling method 

 obj.Sum()

 

# We can also access instances method

# as list[0].Sum() , list[1].Sum() and so on.  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    25
    55
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

