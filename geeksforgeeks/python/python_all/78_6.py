Python – Convert String Records to Tuples Lists



Sometimes, while working with data, we can have problem in which we need to
convert the data list which in string format to list of tuples. This can occur
in domains in which we have cross type inputs. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop +eval()**  
The combination of above methods can be used to solve this task. In this we
remake the string after processing for input to eval function to convert to
Tuple lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String Records to Tuples Lists

# Using loop + eval()

 

# initializing string

test_str = '[(gfg, ), (is, ), (best, )]'

 

# printing original string

print("The original string is : " + test_str)

 

# Convert String Records to Tuples Lists

# Using loop + eval()

res = ''

temp = True

for chr in test_str:

 if chr == '(' and temp:

 res += '("'

 temp = False

 continue

 if chr == ', ' and not temp:

 res += '"'

 temp = True

 res += chr

res = eval(res)

 

# printing result 

print("The list of Tuples is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : [(gfg, ), (is, ), (best, )]
    The list of Tuples is : [('gfg', ), ('is', ), ('best', )]
    

**Method #2 : Using regex + list comprehension**  
The combination of above functionalities is used to perform this task. In
this, we employ regex function to perform the task of resolving the String and
list comprehension helps in reconstruction of record list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String Records to Tuples Lists

# Using regex + list comprehension

import re

 

# initializing string

test_str = '[(gfg, ), (is, ), (best, )]'

 

# printing original string

print("The original string is : " + test_str)

 

# Convert String Records to Tuples Lists

# Using regex + list comprehension

regex = re.compile(r'\((.*?)\)')

temp = regex.findall(test_str)

res = [tuple(sub.split(', ')) for sub in temp]

 

# printing result 

print("The list of Tuples is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : [(gfg, ), (is, ), (best, )]
    The list of Tuples is : [('gfg', ''), ('is', ''), ('best', '')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

