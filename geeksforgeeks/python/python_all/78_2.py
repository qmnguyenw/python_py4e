Python – Consecutive Repetition of Characters



Sometimes, while working with character lists we can have a problem in which
we need to perform consecutive repetition of characters. This can have
application in many domains. Lets discuss certain ways in which this task can
be performed.

 **Method #1 : Using list comprehension**  
This is one of the way in which this task can be performed. In this, we
perform a brute force way to perform but in a one-liner for by multiplying
each character by magnitude.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Repetition of Characters

# Using list comprehension

 

# initializing list

test_list = ['g', 'f', 'g', 'i', 's', 'b',
'e', 's', 't']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# Consecutive Repetition of Characters

# Using list comprehension

res = [sub for ele in test_list for sub in [ele] *
K]

 

# printing result 

print("The list after Consecutive Repetition is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [‘g’, ‘f’, ‘g’, ‘i’, ‘s’, ‘b’, ‘e’, ‘s’, ‘t’]  
> The list after Consecutive Repetition is : [‘g’, ‘g’, ‘g’, ‘f’, ‘f’, ‘f’,
> ‘g’, ‘g’, ‘g’, ‘i’, ‘i’, ‘i’, ‘s’, ‘s’, ‘s’, ‘b’, ‘b’, ‘b’, ‘e’, ‘e’, ‘e’,
> ‘s’, ‘s’, ‘s’, ‘t’, ‘t’, ‘t’]

  

  

**Method #2 : Usingchain() + repeat()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of repeating using repeat() and the result construction
using chain().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Repetition of Characters

# Using chain() + repeat()

from itertools import chain, repeat

 

# initializing list

test_list = ['g', 'f', 'g', 'i', 's', 'b',
'e', 's', 't']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# Consecutive Repetition of Characters

# Using chain() + repeat()

res = list(chain.from_iterable(repeat(chr, K) for chr in
test_list))

 

# printing result 

print("The list after Consecutive Repetition is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [‘g’, ‘f’, ‘g’, ‘i’, ‘s’, ‘b’, ‘e’, ‘s’, ‘t’]  
> The list after Consecutive Repetition is : [‘g’, ‘g’, ‘g’, ‘f’, ‘f’, ‘f’,
> ‘g’, ‘g’, ‘g’, ‘i’, ‘i’, ‘i’, ‘s’, ‘s’, ‘s’, ‘b’, ‘b’, ‘b’, ‘e’, ‘e’, ‘e’,
> ‘s’, ‘s’, ‘s’, ‘t’, ‘t’, ‘t’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

