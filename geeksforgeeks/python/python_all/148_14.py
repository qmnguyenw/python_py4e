Python | Split K elements after every N values



The simple list slicing has many applications and along with it many
variations of list splitting also exists and can come to us to solve. One such
problem can be to split K elements after every N values. Let’s discuss ways in
which this particular problem can be solved.

 **Method #1 : Using loops**  
This is the Naive and brute force method to solve this particular problem with
the help of loop, we can form a new list to check for K occurrences of
elements after every N elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Getting K elements after N values

# using loops

 

# initializing list

test_list = [4, 5, 2, 7, 8, 4, 10, 9,
11, 13]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N and K

N = 2

K = 3

 

# using loops

# Getting K elements after N values

res =[]

while test_list:

 res += test_list[:K]

 test_list = test_list[K + N:]

 

# print result

print("The list after selective slicing : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 2, 7, 8, 4, 10, 9, 11, 13]
    The list after selective slicing : [4, 5, 2, 4, 10, 9]
    

**Method #2 : Using list comprehension**  
This particular task can be performed using the shortened way of the above
method using the list comprehension, we also use list slicing in this method
to perform necessary slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Getting K elements after N values

# using list comprehension

 

# initializing list

test_list = [4, 5, 2, 7, 8, 4, 10, 9,
11, 13]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N and K

N = 2

K = 3

 

# using list comprehension

# Getting K elements after N values

res = [y for x in [test_list[i : i + K] for i in

 range(0, len(test_list), N + K)] for y in x] 

 

# print result

print("The list after selective slicing : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 2, 7, 8, 4, 10, 9, 11, 13]
    The list after selective slicing : [4, 5, 2, 4, 10, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

