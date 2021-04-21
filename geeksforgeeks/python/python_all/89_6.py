Python – Specific Range Addition in List



Sometimes, while working with Python, we need to perform edition in Python
list. And sometimes we need to perform this to specific index range in it.
This kind of application can have application in many domains. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we just
iterate through the specified range in which the edition has to be performed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Specific Range Addition in List

# using loop

 

# Initializing list

test_list = [4, 5, 6, 8, 10, 11]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Initializing range 

i, j = 2, 5

 

# Specific Range Addition in List

# using loop

for idx in range(i, j):

 test_list[idx] += 3

 

# printing result 

print ("List after range addition : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 8, 10, 11]
    List after range addition : [4, 5, 9, 11, 13, 11]
    

**Method #2 : Using list comprehension**  
This task can also be performed using list comprehension. This method uses
same way as above but its a shorthand to above.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Specific Range Addition in List

# using list comprehension

 

# Initializing list

test_list = [4, 5, 6, 8, 10, 11]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Initializing range 

i, j = 2, 5

 

# Specific Range Addition in List

# using list comprehension

test_list[i : j] = [ele + 3 for ele in test_list[i : j]]

 

# printing result 

print ("List after range addition : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 8, 10, 11]
    List after range addition : [4, 5, 9, 11, 13, 11]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

