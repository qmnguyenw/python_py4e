Python | Custom Consecutive Character Pairing



Sometimes, while working with Python Strings, we can have problem in which we
need to perform the pairing of consecutive strings with deliminator. This can
have application in many domains. Lets discuss certain ways in which this task
can be performed.

 **Method #1 : Usingjoin() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we perform the task of joining the characters using join() and perform the
compilation using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Consecutive Character Pairing

# Using join() + list comprehension

import string

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing Delim

delim = '_'

 

# Custom Consecutive Character Pairing

# Using join() + list comprehension

res = [delim.join(test_str[idx : idx + 2]) for idx in
range(len(test_str) - 1)]

 

# printing result 

print("The List of joined Characters : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The List of joined Characters : ['g_e', 'e_e', 'e_k', 'k_s', 's_f', 'f_o', 'o_r', 'r_g', 'g_e', 'e_e', 'e_k', 'k_s']
    

**Method #2 : Usingwindowed() \+ loop**  
This is one of the method to solve this problem. In this task of forming pairs
is done using windowed(). You need to install more_itertools module externally
for its execution.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Consecutive Character Pairing

# Using windowed() + loop

import more_itertools

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + test_str)

 

# initializing Delim

delim = '_'

 

# Custom Consecutive Character Pairing

# Using windowed() + loop

res = []

for ele in more_itertools.windowed(test_str, 2):

 res.append(ele[0] + delim + ele[1])

 

# printing result 

print("The List of joined Characters : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The List of joined Characters : ['g_e', 'e_e', 'e_k', 'k_s', 's_f', 'f_o', 'o_r', 'r_g', 'g_e', 'e_e', 'e_k', 'k_s']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

