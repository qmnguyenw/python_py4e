Python | Pair Kth character with each element



Sometimes, while working with Python, we can have a problem in which we need
to perform the pairing of each character with every other in String. This can
have application in many domains including web development and day-day. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This task can be performed using loop. This a brute force manner in which this
task can be performed. In this, we iterate each character and append the Kth
letter to each and construct a list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Pair Kth character with each element

# Using loop

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 4

 

# Pair Kth character with each element

# Using loop

res = []

for ele in test_str:

 res.append(test_str[K] + ele)

 

# printing result 

print("List after pairing : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    List after pairing : ['sg', 'se', 'se', 'sk', 'ss', 'sf', 'so', 'sr', 'sg', 'se', 'se', 'sk', 'ss']
    

**Method #2 : Usingjoin() + zip() + cycle()**  
The combination of above functions can be used to perform this task. In this,
we perform the task of joining using join(). The task of pairing with all is
done with zip() + cycle().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Pair Kth character with each element

# Using join() + zip() + cycle()

from itertools import cycle

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = 4

 

# Pair Kth character with each element

# Using join() + zip() + cycle()

res = list(map(''.join, zip(cycle(test_str[K]), test_str)))

 

# printing result 

print("List after pairing : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    List after pairing : ['sg', 'se', 'se', 'sk', 'ss', 'sf', 'so', 'sr', 'sg', 'se', 'se', 'sk', 'ss']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

