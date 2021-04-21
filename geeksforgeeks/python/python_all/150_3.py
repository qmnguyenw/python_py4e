Python | Convert list of strings to list of tuples



Sometimes we deal with different types of data types and we require to inter
convert from one data type to another and hence inter conversion always a
useful tool to have knowledge about. The interconversion from tuples to other
formats have been discussed earlier. This article deals with the converse
case. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingmap() + split() + tuple()**

This task can be achieved using the combination of these functions. The map
function can be used to link the logic to each string, split function is
used to split the inner contents of list to different tuple attributes and
tuple function performs the task of forming a tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# convert list of strings to list of tuples

# Using map() + split() + tuple()

 

# initializing list

test_list = ['4, 1', '3, 2', '5, 3']

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + split() + tuple()

# convert list of strings to list of tuples

res = [tuple(map(int, sub.split(', '))) for sub in
test_list] 

 

# print result

print("The list after conversion to tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['4, 1', '3, 2', '5, 3']
    The list after conversion to tuple list : [(4, 1), (3, 2), (5, 3)]
    

  

  

**Method #2 : Usingmap() \+ eval**  
This is the most elegant way to perform this particular task. Where map
function is used to extend the function logic to the whole list eval function
internally performs interconversions and splitting.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# convert list of strings to list of tuples

# Using map() + eval

 

# initializing list

test_list = ['4, 1', '3, 2', '5, 3']

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + eval

# convert list of strings to list of tuples

res = list(map(eval, test_list))

 

# print result

print("The list after conversion to tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['4, 1', '3, 2', '5, 3']
    The list after conversion to tuple list : [(4, 1), (3, 2), (5, 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

