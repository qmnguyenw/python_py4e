Python | Substring Frequency between Uppercases



Sometimes while working with Strings, we can have a problem in which we have
to find substrings that occur between the uppercases and find their
frequencies. This is a very unique problem and has less of applications. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Usinggroupby() \+ regex + loop**  
The combination of above functions can be used to perform this task. In this,
we use groupby() to group the regex extracted substrings. And all is compiled
using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring Frequency between Uppercases

# Using groupby() + regex + loop

from itertools import groupby

import re

 

# initializing string

test_str = "GeEkSForGeEkS"

 

# printing original string

print("The original string is : " + test_str)

 

# Substring Frequency between Uppercases

# Using groupby() + regex + loop

res = {}

for i, j in groupby(re.findall(r'[A-Z][a-z]*\d*', test_str)):

 res[i] = res[i] + 1 if i in res.keys() else 1

 

# printing result 

print("The grouped Substring Frequency : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : GeEkSForGeEkS
    The grouped Substring Frequency : {'For': 1, 'S': 2, 'Ek': 2, 'Ge': 2}
    

**Method #2 : Using dictionary comprehension +sorted() + groupby() + regex**  
The combination of above functions can be used to perform this task. In this,
the task of cumulation is performed using dictionary comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring Frequency between Uppercases

# Using dictionary comprehension + sorted() + groupby() + regex

from itertools import groupby

import re

 

# initializing string

test_str = "GeEkSForGeEkS"

 

# printing original string

print("The original string is : " + test_str)

 

# Substring Frequency between Uppercases

# Using dictionary comprehension + sorted() + groupby() + regex

res = {i : len(list(j)) for i, j in groupby(

 sorted(re.findall(r'[A-Z][a-z]*\d*', test_str))) }

 

# printing result 

print("The grouped Substring Frequency : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : GeEkSForGeEkS
    The grouped Substring Frequency : {'For': 1, 'S': 2, 'Ek': 2, 'Ge': 2}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

