Python | Convert Integral list to tuple list



Sometimes, while working with data, we can have a problem in which we need to
perform type of interconversions of data. There can be a problem in which we
may need to convert integral list elements to single element tuples. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
List comprehension can be used as a shorthand method to solve this particular
problem. In this, we iterate through the list and convert each integer element
into a tuple object.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Integral list to tuple list

# using list comprehension

 

# initialize list 

test_list = [1, 4, 6, 8, 9]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert Integral list to tuple list

# using list comprehension

res = [(ele, ) for ele in test_list]

 

# printing result

print("List after conversion to tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [1, 4, 6, 8, 9]  
> List after conversion to tuple list : [(1, ), (4, ), (6, ), (8, ), (9, )]

  

  

**Method #2 : Usingzip() + list()**  
This is the simplest method to perform this particular task. The zip() when
applied to list of integers, it converts each element to tuple. It returns a
zip object and hence it has to converted back to list using list().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Integral list to tuple list

# using zip() + list()

 

# initialize list 

test_list = [1, 4, 6, 8, 9]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert Integral list to tuple list

# using zip() + list()

res = list(zip(test_list))

 

# printing result

print("List after conversion to tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [1, 4, 6, 8, 9]  
> List after conversion to tuple list : [(1, ), (4, ), (6, ), (8, ), (9, )]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

