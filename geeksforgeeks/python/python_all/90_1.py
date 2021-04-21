Python | Merge Consecutive digits Strings



Sometimes, while workings with data, we can have a problem in which we need to
peform a merge of digits. This is a simpler problem. But it becomes complex
once we need to perform merger of certain elements like numbers that too
consecutive. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +groupby() + isdigit()**  
The combination of above functions can be used to perform this task. In this,
we first group all the digits consecutive and then perform the concatenation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Merge Consecutive digits Strings

# using list comprehension + groupby() + isdigit()

from itertools import groupby

 

# Initializing list

test_list = ['gfg', '1', '2', 'is', '5', 'best',
'6', '7']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Merge Consecutive digits Strings

# using list comprehension + groupby() + isdigit()

res = [sub for i, j in groupby(test_list, str.isdigit) for
sub in ([''.join(j)] if i else j)]

 

# printing result 

print ("List after digit merge : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', '1', '2', 'is', '5', 'best', '6', '7']
    List after digit merge : ['gfg', '12', 'is', '5', 'best', '67']
    

**Method #2 : Using regex +join()**  
The combinations of above functions can also be used to deal with this. In
this, we find the digits using regex function and perform merger using join().
Works only with single characters.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Merge Consecutive digits Strings

# using regex() + join()

import re

 

# Initializing list

test_list = ['g', '1', '2', 'i', '5', 'b',
'6', '7']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Merge Consecutive digits Strings

# using regex() + join()

res = re.findall('\d+|.', ''.join(test_list))

 

# printing result 

print ("List after digit merge : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['g', '1', '2', 'i', '5', 'b', '6', '7']
    List after digit merge : ['g', '12', 'i', '5', 'b', '67']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

