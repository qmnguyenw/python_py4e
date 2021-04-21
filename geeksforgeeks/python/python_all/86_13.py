Python – Numeric Sort in Mixed Pair String List



Sometimes, while working with data records, we can have a problem in which we
receive data in custom format, and we need to perform a sort. We can receive
both name of person and space-separated score and require to get the best to
worst sorting. Lets discuss a way in which this particular problem can be
solved.

 **Method #1 : Usingsplit() + sort() \+ key function**  
The combination of above functionalities can be used to perform this task. In
this, we perform a sort using external function in which we split the string
and extract the numeric part.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Numeric Sort in Mixed Pair String List

# using split() + sort() + key function

 

# helper function 

def helper_func(ele):

 name, val = ele.split()

 return int(val)

 

# Initializing list

test_list = ["Manjeet 5", "Akshat 7", "Akash 6", "Nikhil
10"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Numeric Sort in Mixed Pair String List

# using split() + sort() + key function

test_list.sort(key = helper_func, reverse = True)

 

# printing result 

print ("The reverse sorted numerics are : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Manjeet 5', 'Akshat 7', 'Akash 6', 'Nikhil 10']
    The reverse sorted numerics are : ['Nikhil 10', 'Akshat 7', 'Akash 6', 'Manjeet 5']
    

**Method #2 : Usingsplit() + lambda + sorted()**  
The combination of above methods can be used to perform this task. In this, we
perform split on numbers as above. The difference is that it is one liner and
use lambda function to perform.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Numeric Sort in Mixed Pair String List

# using split() + sorted() + lambda

 

# Initializing list

test_list = ["Manjeet 5", "Akshat 7", "Akash 6", "Nikhil
10"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Numeric Sort in Mixed Pair String List

# using split() + sorted() + lambda

res = sorted(test_list, reverse = True, key = lambda ele:
int(ele.split()[1]))

 

# printing result 

print ("The reverse sorted numerics are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Manjeet 5', 'Akshat 7', 'Akash 6', 'Nikhil 10']
    The reverse sorted numerics are : ['Nikhil 10', 'Akshat 7', 'Akash 6', 'Manjeet 5']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

