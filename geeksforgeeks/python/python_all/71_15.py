Python – Variable Operations Dictionary update



Sometimes, while working with Python dictionaries we can have a problem in
which we need to perform a population of dictionary values using assigned
variables after certain operation among them. This can have application in
day-day programming. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using lambda + dictionary comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform the assignment using dictionary comprehension and values
computations using lambda functions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Variable Operations Dictionary update

# Using lambda + dictionary comprehension

 

# helpr functions

hlper_fnc = {'Gfg': lambda: x + y,

 'best': lambda: x * y}

 

# initializing variables

x = 6

y = 7

 

# Variable Operations Dictionary update

# Using lambda + dictionary comprehension

res = {key: val() for key, val in hlper_fnc.items()}

 

# printing result 

print("The Initialized dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The Initialized dictionary : {'best': 42, 'Gfg': 13}
    

**Method #2 : Using operators library**  
This task can also be performed using above functionality. In this, we use
inbuilt operations provided by the operator library to achieve this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Variable Operations Dictionary update

# Using lambda + dictionary comprehension

from operator import add, mul

 

# helpr functions

hlper_fnc = {'Gfg': add,

 'best': mul}

 

# initializing variables

x = 6

y = 7

 

# Variable Operations Dictionary update

# Using lambda + dictionary comprehension

res = {'Gfg' : hlper_fnc['Gfg'](x, y), 'best' :
hlper_fnc['best'](x, y)}

 

# printing result 

print("The Initialized dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The Initialized dictionary : {'best': 42, 'Gfg': 13}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

