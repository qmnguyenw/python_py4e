Python | String List to Column Character Matrix



Sometimes, while working with Python lists, we can have a problem in which we
need to convert the string list to Character Matrix where each row is String
list column. This can have possible application in data domains. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
This is one of the way in which this task can be performed. In this, we
iterate for each String element and construct rows using index elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String List to Column Character Matrix

# Using list comprehension

 

# initializing list

test_list = ["123", "456", "789"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# String List to Column Character Matrix

# Using list comprehension

res = [[sub[idx] for sub in test_list] for idx in
range(len(test_list[0]))]

 

# printing result 

print("The Character Matrix : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['123', '456', '789']
    The Character Matrix : [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    

**Method #2 : Usingzip() + map()**  
The combination of above functions can be used to perform this task. In this,
we construct the columns using zip() and map() is used to compile all the
nested lists.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String List to Column Character Matrix

# Using zip() + map()

 

# initializing list

test_list = ["123", "456", "789"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# String List to Column Character Matrix

# Using zip() + map()

res = list(map(list, zip(*test_list)))

 

# printing result 

print("The Character Matrix : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['123', '456', '789']
    The Character Matrix : [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

