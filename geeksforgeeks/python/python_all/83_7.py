Python | Substitute character with its occurrence



Sometimes, while working with Python, we can have a problem in which we need
to substitute a character with its occurrence in a string. This a peculiar
problem but can have application in many domains. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop**  
This is brute way to solve the problem. In this, we run a loop for each
character in string and perform the substitution while increasing the counter
each time.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substitute character with its occurrence

# Using loop

 

# initializing string

test_str = "geeksforgeeks is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing letter 

test_let = 'g'

 

# Substitute character with its occurrence

# Using loop

res = ''

count = 1

for chr in test_str:

 if chr == test_let:

 res += str(count)

 count += 1

 else:

 res += chr

 

# printing result 

print("The string after performing substitution : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    The string after performing substitution : 1eeksfor2eeks is best for 3eeks
    

**Method #2 : Using lambda + regex +next()**  
The combination of above functions can be used to perform this task. In this
we perform the task of iteration using lambda, the regex and next() is used to
perform the task of count iteration and finding the target char.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substitute character with its occurrence

# Using lambda + regex + next()

from itertools import count

import re

 

# initializing string

test_str = "geeksforgeeks is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing letter 

test_let = 'g'

 

# Substitute character with its occurrence

# Using lambda + regex + next()

cnt = count(1)

res = re.sub(r"g", lambda x: "{}".format(next(cnt)),
test_str)

 

# printing result 

print("The string after performing substitution : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks is best for geeks
    The string after performing substitution : 1eeksfor2eeks is best for 3eeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

