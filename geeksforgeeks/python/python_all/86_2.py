Python – Construct variables of list elements



Sometimes, while working with python lists, we can have a problem in which we
need to convert each element in list to variables and corresponding list as
value. This can have application in many domains such as web development and
day-day programming. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingdict() + zip()**  
The combination of above functions can be used to perform this task. In this,
we zip both the list into a dictionary and key of dictionary can act as
variable and value as variable value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Construct variables of list elements

# using dict() + zip()

 

# Initializing lists 

test_list1 = ['gfg', 'is', 'best']

test_list2 = [1, 2, 3]

 

# printing original lists 

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Construct variables of list elements

# using dict() + zip()

res = dict(zip(test_list1, test_list2))

 

# printing result 

print ("Variable value 1 : " + str(res['gfg']))

print ("Variable value 2 : " + str(res['best']))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['gfg', 'is', 'best']
    The original list 2 is : [1, 2, 3]
    Variable value 1 : 1
    Variable value 2 : 3
    

**Method #2 : Usingglobal() \+ loop**  
This is yet another way to initialize variables as lists. In this we use
global space to declare variables.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Construct variables of list elements

# using globals() + loop

 

# Initializing lists 

test_list1 = ['gfg', 'is', 'best']

test_list2 = [1, 2, 3]

 

# printing original lists 

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Construct variables of list elements

# using globals() + loop

for var, val in zip(test_list1, test_list2):

 globals()[var] = val

 

# printing result 

print ("Variable value 1 : " + str(gfg))

print ("Variable value 2 : " + str(best))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['gfg', 'is', 'best']
    The original list 2 is : [1, 2, 3]
    Variable value 1 : 1
    Variable value 2 : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

