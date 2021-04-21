Python | Accessing variable value from code scope



Sometimes, we just need to access a variable other than the usual way of
accessing by it’s name. There are many method by which a variable can be
accessed from the code scope. These are by default dictionaries that are
created and which keep the variable values as dictionary key-value pair. Let’s
talk about some of this functions.

 **Method #1 : Usinglocals()**  
This is a function that stores the values of all variables in local scope of
function if in a function or of global scope if outside.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Accessing variable value from code scope

# using locals

 

# initialize variable

test_var = "gfg is best"

 

# printing original variable

print("The original variable : " + str(test_var))

 

# Accessing variable value from code scope

# using locals

res = locals()['test_var']

 

# printing result

print("Variable accessed using dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original variable : gfg is best
    Variable accessed using dictionary : gfg is best
    

**Method #2 : Usingglobals()**  
This is yet another function that maintains a dictionary of variables of
global scope.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Accessing variable value from code scope

# using globals

 

# initialize variable

test_var = "gfg is best"

 

# printing original variable

print("The original variable : " + str(test_var))

 

# Accessing variable value from code scope

# using globals

res = globals()['test_var']

 

# printing result

print("Variable accessed using dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original variable : gfg is best
    Variable accessed using dictionary : gfg is best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

