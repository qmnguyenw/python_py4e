Python | K Divided Indices List



Sometimes, while working with Python lists, we can have a problem in which we
wish to find Modulo K elements. This task can occur in many domains such as
web development and while working with Databases. We might sometimes, require
to just find the indices of them. Let’s discuss certain way to find indices of
modulo K elements.

 **Method #1 : Using loop**  
This is brute force method in which this task can be performed. In this, we
check for % K element in list and append its index accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K Divident Indices List

# using loop 

 

# initialize list 

test_list = [5, 6, 10, 4, 7, 1, 19] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# initializing K 

K = 5

 

# K Divident Indices List

# using loop 

res = [] 

for idx, ele in enumerate(test_list): 

 if ele % K == 0: 

 res.append(idx) 

 

# printing result 

print("Indices list modulo K elements is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [5, 6, 10, 4, 7, 1, 19]
    Indices list modulo K elements is : [0, 2]
    

**Method #2 : Using list comprehension**  
This is the shorthand by which this task can be performed. This method works
in similar way as the above method. The difference is that it’s a one liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K Divident Indices List

# using list comprehension 

 

# initialize list 

test_list = [5, 6, 10, 4, 7, 1, 19] 

 

# printing original list 

print("The original list is : " + str(test_list))

 

# initializing K

K = 5

 

# K Divident Indices List

# using list comprehension 

res = [idx for idx, ele in enumerate(test_list) if ele %
K == 0] 

 

# printing result 

print("Indices list modulo K elements is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [5, 6, 10, 4, 7, 1, 19]
    Indices list modulo K elements is : [0, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

