Python – Frequency of x follow y in Number



Sometimes, while working with Numbers in Python, we can have a problem in
which we need to get the number of time one number follows other. This can
have application in many domains such as day-day programming and other
domains. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which we perform this task. In this, we traverse
list and keep checking for previous and current number for result and keep
incrementing the counter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of x follow y in Number

# using loop

 

def count_occ(num, next, prev):

 num = str(num)

 prev_chr = ""

 count = 0

 for chr in num:

 if chr == next and prev_chr == prev:

 count += 1

 prev_chr = chr

 return count

 

# initialize Number

test_num = 12457454

 

# printing original number

print("The original number : " + str(test_num))

 

# initialize i, j 

i, j = '4', '5'

 

# Frequency of x follow y in Number

# using loop

res = count_occ(test_num, j, i)

 

# printing result

print("The count of x preceding y : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original number : 12457454
    The count of x preceding y : 2
    

**Method #2 : Using loop +isinstance() \+ regex**  
This is yet another way in which this task can be performed. In this, we use
regex function to check the preceding term rather than brute approach.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Frequency of x follow y in Number

# using loop + isinstance() + regex

import re

 

def count_occ(num, next, prev):

 if not isinstance(num, str): 

 num = str(num) 

 return len(re.findall(prev + next, num)) 

 

# initialize Number

test_num = 12457454

 

# printing original number

print("The original number : " + str(test_num))

 

# initialize i, j 

i, j = '4', '5'

 

# Frequency of x follow y in Number

# using loop + isinstance() + regex

res = count_occ(test_num, j, i)

 

# printing result

print("The count of x preceding y : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original number : 12457454
    The count of x preceding y : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

