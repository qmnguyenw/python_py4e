Python – All possible space joins in String



Sometimes, while working with Python Strings, we can have a problem in which
we need to construct strings with single space at every possible word ending.
This kind of application can occur in domains in which we need to perform
testing. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +join()**  
This is brute force way in which this task can be performed. In this, we
perform the task of forming all possible joins using join() and task of
iterating through all strings using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible space joins in String

# Using loop + join()

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# All possible space joins in String

# Using loop + join()

res = []

temp = test_str.split(' ') 

strt_idx = 0

lst_idx = len(temp)

for idx in range(len(temp)-1): 

 frst_wrd = "".join(temp[strt_idx : idx + 1]) 

 scnd_wrd = "".join(temp[idx + 1 : lst_idx])

 res.append(frst_wrd + " " + scnd_wrd)

 

# printing result 

print("All possible spaces List : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : Geeksforgeeks is best for geeks  
> All possible spaces List : [‘Geeksforgeeks isbestforgeeks’, ‘Geeksforgeeksis
> bestforgeeks’, ‘Geeksforgeeksisbest forgeeks’, ‘Geeksforgeeksisbestfor
> geeks’]

  

  

**Method #2 : Usingenumerate() + join() + combinations()**  
The combination of above methods can be used to perform this task. In this, we
perform the task of extracting combinations using combinations(). This prints
all combinations of all occurrences of spaces rather than just one as in above
method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible space joins in String

# Using enumerate() + join() + combinations()

import itertools

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# All possible space joins in String

# Using enumerate() + join() + combinations()

res = []

temp = test_str.split(' ')

N = range(len(temp) - 1)

for idx in N:

 for sub in itertools.combinations(N, idx + 1):

 temp1 = [val + " " if i in sub else val for i, val
in enumerate(temp)]

 temp2 = "".join(temp1)

 res.append(temp2)

 

# printing result 

print("All possible spaces List : " + str(res))   
  
---  
  
__

__

**Output :**

> The original string is : Geeksforgeeks is best for geeks  
> All possible spaces List : [‘Geeksforgeeks isbestforgeeks’, ‘Geeksforgeeksis
> bestforgeeks’, ‘Geeksforgeeksisbest forgeeks’, ‘Geeksforgeeksisbestfor
> geeks’, ‘Geeksforgeeks is bestforgeeks’, ‘Geeksforgeeks isbest forgeeks’,
> ‘Geeksforgeeks isbestfor geeks’, ‘Geeksforgeeksis best forgeeks’,
> ‘Geeksforgeeksis bestfor geeks’, ‘Geeksforgeeksisbest for geeks’,
> ‘Geeksforgeeks is best forgeeks’, ‘Geeksforgeeks is bestfor geeks’,
> ‘Geeksforgeeks isbest for geeks’, ‘Geeksforgeeksis best for geeks’,
> ‘Geeksforgeeks is best for geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

