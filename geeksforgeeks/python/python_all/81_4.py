Python | Sort Numerical Records in String



Sometimes, while working with Python records we can have a problem that they
may occur in name and number format in strings. These may be required to be
sorted. This problem can occur in many domains in which data is involved. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Usingjoin() + split() + sorted() \+ list comprehension**  
The combination of above functions can be used to perform this task. In this,
we perform the task of sort using sorted(), and task of extracting numbers
using split(). We perform the task of rejoining sorted string using join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Numerical Records in String

# Using join() + split() + sorted() + list comprehension

 

# initializing string

test_str = "Akshat 15 Nikhil 20 Akash 10"

 

# printing original string

print("The original string is : " + test_str)

 

# Sort Numerical Records in String

# Using join() + split() + sorted() + list comprehension

temp1 = test_str.split()

temp2 = [temp1[idx : idx + 2] for idx in range(0,
len(temp1), 2)]

temp3 = sorted(temp2, key = lambda ele: (int(ele[1]),
ele[0]))

res = ' '.join([' '.join(ele) for ele in temp3])

 

# printing result 

print("The string after sorting records : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Akshat 15 Nikhil 20 Akash 10
    The string after sorting records : Akash 10 Akshat 15 Nikhil 20
    

**Method #2 : Using regex**  
This task can also be performed using regex. We perform task of finding number
using regex and rest sorting and joining is performed as above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Numerical Records in String

# Using regex

import re

 

# initializing string

test_str = "Akshat 15 Nikhil 20 Akash 10"

 

# printing original string

print("The original string is : " + test_str)

 

# Sort Numerical Records in String

# Using regex

temp1 = re.findall(r'([A-z]+) (\d+)', test_str)

temp2 = sorted(temp1, key = lambda ele: (int(ele[1]),
ele[0]))

res = ' '.join(' '.join(ele) for ele in temp2)

 

# printing result 

print("The string after sorting records : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Akshat 15 Nikhil 20 Akash 10
    The string after sorting records : Akash 10 Akshat 15 Nikhil 20
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

