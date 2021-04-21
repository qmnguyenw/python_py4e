Python | Count String occurrences in mixed list



Sometimes, while working with data, we can have a problem in which we need to
check for the occurrences of a particular data type. In this, we can also have
a problem in which we need to check for string occurrences. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingisinstance() \+ list comprehension**  
The combination of above methods can be used to perform this task. In this, we
check for each element of list for string instance and built list with only
string and return it’s length.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check String occurrences in mixed list

# using isinstance() + list comprehension

 

# initialize list 

test_list = ['gfg', 1, True, 'is', 2, 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Check String occurrences in mixed list

# using isinstance() + list comprehension

res = len([val for val in test_list if isinstance(val,
str)])

 

# printing result

print("Number of strings in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 1, True, 'is', 2, 'best']
    Number of strings in list : 3
    

**Method #2 : Usingsum() + isinstance() \+ generator expression**  
The combination of above functionalities can be used to perform this task. In
this, we compute the True instances of string check and return it’s sum
counting string instances.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check String occurrences in mixed list

# using sum() + isinstance() + generator expression

 

# initialize list 

test_list = ['gfg', 1, True, 'is', 2, 'best']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Check String occurrences in mixed list

# using sum() + isinstance() + generator expression

res = sum(isinstance(ele, str) for ele in test_list)

 

# printing result

print("Number of strings in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 1, True, 'is', 2, 'best']
    Number of strings in list : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

