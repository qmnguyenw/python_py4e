Python | Count K character between consecutive characters



Sometimes, while working with strings, we can have a problem in which we need
to check the count of each character between the consecutive character. This
type of problem can have application in day-day and web development domain.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate the list counting the K character between each of characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count K character between consecutive characters

# Using loop

 

# initializing string

test_str = "g...f..g.i..s....b..e....s...t"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing K 

K = '.'

 

# Count K character between consecutive characters

# Using loop

count = 0

res = []

for ele in test_str:

 if ele == K:

 count += 1

 else:

 res.append(count)

 count = 0

res = res[1:]

 

# printing result 

print("List of character count : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : g...f..g.i..s....b..e....s...t
    List of character count : [3, 2, 1, 2, 4, 2, 4, 3]
    

**Method #2 : Using list comprehension +findall()**  
This is yet another way in which this problem can be solved. In this, we check
for occurring K character using findall() and list comprehension is used to
iterate about the string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count K character between consecutive characters

# Using list comprehension + findall()

import re

 

# initializing string

test_str = "g---f--g-i--s----b--e----s---t"

 

# printing original string

print("The original string is : " + test_str)

 

# Count K character between consecutive characters

# Using list comprehension + findall()

res = [len(ele) for ele in
re.findall('(?<=[a-z])-*(?=[a-z])', test_str)]

 

# printing result 

print("List of character count : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : g---f--g-i--s----b--e----s---t
    List of character count : [3, 2, 1, 2, 4, 2, 4, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

