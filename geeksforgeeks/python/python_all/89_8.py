Python – Incremental K sized Row Matrix Initialization



Sometimes, while working with Python, we can have a problem in which we need
to perform initialization of matrix with Incremental numbers. This kind of
application can come in Data Science domain. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop + list slicing**  
This task can be performed in brute way using loop. In this, we run a loop
skipping by K (size of row required), to adjust numbers addition ahead.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental K sized Row Matrix Initialization

# using loop + list slicing

 

# Initialization of row size 

K = 3

 

# Incremental K sized Row Matrix Initialization

# using loop + list slicing

res = []

for idx in range(1, 10, K):

 sub = [idx, idx + 1, idx + 2]

 res.append(sub)

 

# printing result 

print ("The Incremental Initialized Matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The Incremental Initialized Matrix is : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    

**Method #2 : Using list comprehension**  
This is just another way to perform this task. This performs in similar way as
above, but in a shorter way.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental K sized Row Matrix Initialization

# using list comprehension

 

# Initialization of row size 

K = 3

 

# Incremental K sized Row Matrix Initialization

# using list comprehension

res = [[i, i + 1, i + 2] for i in range(1,
10, K)]

 

# printing result 

print ("The Incremental Initialized Matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The Incremental Initialized Matrix is : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

