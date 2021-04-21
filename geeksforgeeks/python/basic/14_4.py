Python | Split string in groups of n consecutive characters



Given a string (be it either string of numbers or characters), write a Python
program to split the string by every _n th_ character.

 **Examples:**

    
    
    **Input :** str = "Geeksforgeeks", n = 3
    **Output :** ['Gee', 'ksf', 'oor', 'gee', 'ks']
    
    **Input :** str = "1234567891234567", n = 4
    **Output :** [1234, 5678, 9123, 4567]

  
**Method #1: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split string

# by every 3rd number

 

# String initialization

string = "Geeksforgeeks"

 

# Defining splitting point

n = 3

 

# Using list comprehension

out = [(string[i:i+n]) for i in range(0,
len(string), n)]

 

# Printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Gee', 'ksf', 'org', 'eek', 's']
    

  
**Method #2: Usingzip_longest**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to split string of number

# and character into every 4th number

 

# Importing

from itertools import zip_longest

 

# Group function using zip_longest to split

def group(n, iterable, fillvalue=None):

 args = [iter(iterable)] * n

 return zip_longest(fillvalue=fillvalue, *args)

 

# String initialization

str = '123GeeksForGeeks4567'

 

# Split point

n=4

 

# list of separated string

out_string = [''.join(lis) for lis in group(n, str, '')]

 

# Output list initialization

out_no = []

 

# Converting list of string into list of integer

for a in out_string:

 out_no.append(a)

 

# Printing list

print(out_no)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['123G', 'eeks', 'ForG', 'eeks', '4567']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

