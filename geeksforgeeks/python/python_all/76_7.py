Python – Custom Split Comma Separated Words



While working with Python, we can have problem in which we need to perform the
task of splitting the words of string on spaces. But sometimes, we can have
comma separated words, which have comma’s joined to words and require to split
them separately. Lets discuss certain ways in which this task can be
performed.  
 **Method #1 : Using replace()**  
Using replace() is one way to solve this problem. In this, we just separate
the joined comma from string to spaced so that they can be splitted along with
other words correctly.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Split Comma Separated Words

# Using replace()

# initializing string

test_str = 'geeksforgeeks, is, best, for, geeks'

# printing original string

print("The original string is : " + str(test_str))

# Distance between occurrences

# Using replace()

res = test_str.replace(", ", " , ").split()

# printing result

print("The strings after performing splits : " + str(res))  
  
---  
  
 __

 __

 **Output :**

The original string is : geeksforgeeks, is, best, for, geeks  
The strings after performing splits : [‘geeksforgeeks’, ‘, ‘, ‘is’, ‘, ‘,
‘best’, ‘, ‘, ‘for’, ‘, ‘, ‘geeks’]

  
**Method #2 : Using re.findall()**  
This problem can also be used using regex. In this, we find the occurrences of
non space word and perform a split on that basis.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Split Comma Separated Words

# Using re.findall()

import re

# initializing string

test_str = 'geeksforgeeks, is, best, for, geeks'

# printing original string

print("The original string is : " + str(test_str))

# Distance between occurrences

# Using re.findall()

res = re.findall(r'\w+|\S', test_str)

# printing result

print("The strings after performing splits : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

The original string is : geeksforgeeks, is, best, for, geeks  
The strings after performing splits : [‘geeksforgeeks’, ‘, ‘, ‘is’, ‘, ‘,
‘best’, ‘, ‘, ‘for’, ‘, ‘, ‘geeks’]

