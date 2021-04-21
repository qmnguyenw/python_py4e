Python – Find Words with both alphabets and numbers



Sometimes, while working with Python strings, we can have problem in which we
need to extract certain words with contain both numbers and alphabets. This
kind of problem can occur in many domains like school programming and web-
development. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingany() + isdigit() + isalpha()**  
The combination of above functionalities can be used to perform this task. In
this, we iterate for all the words and check for required combination using
isdigit() and isalpha().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Words with both alphabets and numbers

# Using isdigit() + isalpha() + any()

 

# initializing string

test_str = 'geeksfor23geeks is best45 for gee34ks and cs'

 

# printing original string

print("The original string is : " + test_str)

 

# Words with both alphabets and numbers

# Using isdigit() + isalpha() + any()

res = []

temp = test_str.split()

for idx in temp:

 if any(chr.isalpha() for chr in idx) and
any(chr.isdigit() for chr in idx):

 res.append(idx)

 

# printing result 

print("Words with alphabets and numbers : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : geeksfor23geeks is best45 for gee34ks and cs  
> Words with alphabets and numbers : [‘geeksfor23geeks’, ‘best45’, ‘gee34ks’]

  

  

**Method #2 : Using regex**  
This is yet another way by which we can perform this task. In this, we feed
the string to findall(), and extract the required result. Returns strings
till the numbers only.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Words with both alphabets and numbers

# Using regex

import re

 

# initializing string

test_str = 'geeksfor23geeks is best45 for gee34ks and cs'

 

# printing original string

print("The original string is : " + test_str)

 

# Words with both alphabets and numbers

# Using regex

res = re.findall(r'(?:\d+[a-zA-Z]+|[a-zA-Z]+\d+)', test_str)

 

# printing result 

print("Words with alphabets and numbers : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : geeksfor23geeks is best45 for gee34ks and cs  
> Words with alphabets and numbers : [‘geeksfor23’, ‘best45’, ‘gee34’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

