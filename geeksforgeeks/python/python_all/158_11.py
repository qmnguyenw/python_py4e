Python | Combine two lists by maintaining duplicates in first list



Given two lists, the task is to combine two lists and removing duplicates,
without removing duplicates in original list.

 **Example:**

    
    
     **Input :**
    list_1 = [11, 22, 22, 15]
    list_2 = [22, 15, 77, 9]
    **Output :**
    OutList = [11, 22, 22, 15, 77, 9]

 **

Code #1: using extend

**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to combine two lists

# and removing duplicates, without

# removing duplicates in original list.

 

# Initialisation of first list

list1 = [111, 222, 222, 115]

 

# Initialisation of Second list

list2 = [222, 115, 77, 19]

 

output = list(list1)

 

# Using extend function

output.extend(y for y in list2 if y not in output)

 

# printing result

print(output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [111, 222, 222, 115, 77, 19]
    

