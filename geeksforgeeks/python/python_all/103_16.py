Python – Get Indices of Even Elements from list



Sometimes, while working with Python lists, we can have a problem in which we
wish to find Even elements. This task can occur in many domains such as web
development and while working with Databases. We might sometimes, require to
just find the indices of them. Let’s discuss certain way to find indices of
Even elements.

 **Method #1 : Using loop**  
This is brute force method in which this task can be performed. In this, we
check for even element in list and append its index accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Even Elements indices

# using loop

 

# initialize list

test_list = [5, 6, 10, 4, 7, 1, 19]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Even Elements indices

# using loop

res = []

for idx, ele in enumerate(test_list):

 if ele % 2 == 0:

 res.append(idx)

 

# printing result

print("Indices list Even elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 10, 4, 7, 1, 19]
    Indices list Even elements is : [1, 2, 3]
    

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

# Even Elements indices

# using list comprehension

 

# initialize list

test_list = [5, 6, 10, 4, 7, 1, 19]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Even Elements indices

# using list comprehension

res = [idx for idx, ele in enumerate(test_list) if ele %
2 == 0]

 

# printing result

print("Indices list Even elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 10, 4, 7, 1, 19]
    Indices list Even elements is : [1, 2, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

