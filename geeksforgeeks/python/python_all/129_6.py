Python | Absolute value of list elements



Sometimes, while working with Python list, we need to find the absolute number
i.e all the elements with a positive magnitude in list. This problem has an
application in various domains of Data Science. Let’s discuss certain ways in
which this task can be done.

 **Method #1 : Using list comprehension +abs()**  
This task can be performed using list comprehension technique in which we just
iterate each element and keep finding it’s absolute value using the abs().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Absolute value of list elements

# using abs() + list comprehension

 

# initialize list

test_list = [5, -6, 7, -8, -10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Absolute value of list elements

# using abs() + list comprehension

res = [abs(ele) for ele in test_list]

 

# printing result

print("Absolute value list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, -6, 7, -8, -10]
    Absolute value list : [5, 6, 7, 8, 10]
    

**Method #2 : Usingmap() + abs()**  
This task can also be performed using map(). As above, the task of map is
to perform the task of extending the absolute number logic to each element in
list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Absolute value of list elements

# using map() + abs()

 

# initialize list

test_list = [5, -6, 7, -8, -10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Absolute value of list elements

# using map() + abs()

res = list(map(abs, test_list))

 

# printing result

print("Absolute value list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, -6, 7, -8, -10]
    Absolute value list : [5, 6, 7, 8, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

