Use of nonlocal vs use of global keyword in Python



 **Prerequisites:** Global and Local Variables in Python

Before moving to nonlocal and global in Python. Let us consider some basic
scenarios in nested functions.

 __

 __  
 __

 __

 __  
 __  
 __

def fun():

 var1 = 10

 

 def gun():

 print(var1)

 var2 = var1 + 1

 print(var2)

 

 gun()

fun()  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    11
    

The variable **var1** has scope **across entire fun** (). It will be
accessible from nested function of fun()

 __

 __  
 __

 __

 __  
 __  
 __

def fun():

 var1 = 10

 

 def gun():

 # gun() initializes a new variable var1.

 var1 = 20

 print(var1, id(var1))

 

 print(var1, id(var1))

 gun()

fun()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    10 10853920
    20 10854240
    

