Python – Incremental and Cyclic Repetition of List Elements



Sometimes, while working with Python lists, we can have a problem in which we
need to repeat elements K times. But we can have variations in this and have
to repeat elements in cyclic and incremental way. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using loop +enumerate()**  
This is brute force way in which this task can be performed. In this, we
iterate the elements and perform the required number of repetition using mod
operator and multiplication logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental and Cyclic Repetition of List Elements

# using loop + enumerate()

 

# Initializing list

test_list = ['g', 'f', 'g', 'C', 'S']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing range 

i, j = 2, 4

 

# Incremental and Cyclic Repetition of List Elements

# using loop + enumerate()

res = []

temp = list(range(i, j + 1))

for idx, ele in enumerate(test_list):

 res.append(ele * temp[idx % len(temp)])

 

# printing result 

print ("Repetition List is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['g', 'f', 'g', 'C', 'S']
    Repetition List is : ['gg', 'fff', 'gggg', 'CC', 'SSS']
    

**Method #2 : Usingcycle() + loop + zip()**  
The combination of these tasks can also be used to perform this task. In this,
we iterate using loop and cycling and repetion is performed using cycle().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Incremental and Cyclic Repetition of List Elements

# using cycle() + loop + zip()

from itertools import cycle

 

# Initializing list

test_list = ['g', 'f', 'g', 'C', 'S']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing range 

i, j = 2, 4

 

# Incremental and Cyclic Repetition of List Elements

# using cycle() + loop + zip()

res = []

for k, l in zip(cycle(range(i, j + 1)), test_list):

 res.append(k * l)

 

# printing result 

print ("Repetition List is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['g', 'f', 'g', 'C', 'S']
    Repetition List is : ['gg', 'fff', 'gggg', 'CC', 'SSS']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

