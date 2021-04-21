Python – Incremental Range Initialization in Matrix



Sometimes, while working with Python, we can have a problem in which we need
to perform the initialization of Matrix. Simpler initialization is easier. But
sometimes, we need to perform range incremental initialization. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we iterate
through the list and increase the value of element with the range specified.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental Range Initialization in Matrix

# using loop

 

# Initializing row

r = 4

 

# Initializing col

c = 3

 

# Initializing range 

rang = 5

 

# Incremental Range Initialization in Matrix

# using loop

res = []

temp = []

temp2 = 0

for idx in range(r):

 for idx in range(c):

 temp.append(temp2)

 temp2 = temp2 + rang

 res.append(temp)

 temp = []

 

# printing result 

print ("Matrix after Initialization : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Matrix after Initialization : [[0, 5, 10], [15, 20, 25], [30, 35, 40], [45, 50, 55]]
    

**Method #2 : Using list comprehension**  
This task can also be performed using list comprehension. The method is
similar to above. The difference is this is a shorthand to perform this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental Range Initialization in Matrix

# using list comprehension

 

# Initializing row

r = 4

 

# Initializing col

c = 3

 

# Initializing range 

rang = 5

 

# Incremental Range Initialization in Matrix

# using list comprehension

res = [[rang * c * y + rang * x for x in
range(c)] for y in range(r)]

 

# printing result 

print ("Matrix after Initialization : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Matrix after Initialization : [[0, 5, 10], [15, 20, 25], [30, 35, 40], [45, 50, 55]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

