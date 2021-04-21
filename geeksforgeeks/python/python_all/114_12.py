Python | Removing newline character from string



Many times, while working with Python strings, we can have a problem in which
we have huge amount of data and we need to perform preprocessing of certain
kind. This can also be removing stray newline characters in strings. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This task can be perform using brute force in which we check for “\n” as a
string in a string and replace that from each string using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing newline character from string

# using loop

 

# initialize list 

test_list = ['gf\ng', 'i\ns', 'b\nest', 'fo\nr',
'geeks\n']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Removing newline character from string

# using loop

res = []

for sub in test_list:

 res.append(sub.replace("\n", ""))

 

# printing result

print("List after newline character removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gf\ng', 'i\ns', 'b\nest', 'fo\nr', 'geeks\n']
    List after newline character removal : ['gfg', 'is', 'best', 'for', 'geeks']
    

**Method #2 : Using regex**  
This task can also be executed using regex functions which can also perform
the global replace of all the newline characters with empty string. Advantage
over above method is that above method just removes one occurrences and this
method checks every occurrence.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing newline character from string

# Using regex

import re

 

# initialize list 

test_list = ['gf\ng', 'i\ns', 'b\nest', 'fo\nr',
'geeks\n']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Removing newline character from string

# Using regex

res = []

for sub in test_list:

 res.append(re.sub('\n', '', sub))

 

# printing result

print("List after newline character removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gf\ng', 'i\ns', 'b\nest', 'fo\nr', 'geeks\n']
    List after newline character removal : ['gfg', 'is', 'best', 'for', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

