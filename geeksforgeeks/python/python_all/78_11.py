Python – Characters occurring in multiple Strings



Sometimes, while working with Python strings, we can have problem in which we
need to extract the characters which have occurrences in more than one string
in string list. This kind of problem usually occurs in web development and
Data Science domains. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : UsingCounter() + set()**  
This is one of the ways in which this task can be performed. In this, we check
for all the strings and compute the character frequency in each string and
return the character which have more than one string occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Characters occurring in multiple Strings

# Using Counter() + set()

from itertools import chain

from collections import Counter

 

# initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeks',
'and', 'cs']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Characters occurring in multiple Strings

# Using Counter() + set()

temp = (set(sub) for sub in test_list)

cntr = Counter(chain.from_iterable(temp))

res = [chr for chr, count in cntr.items() if count >=
2]

 

# printing result 

print("Characters with Multiple String occurrence : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [‘gfg’, ‘is’, ‘best’, ‘for’, ‘geeks’, ‘and’, ‘cs’]  
> Characters with Multiple String occurrence : [‘g’, ‘e’, ‘f’, ‘s’]

  

  

**Method #2 : Using list comprehension + Counter() + set()**  
This is one of the way in which this task can be performed. In this, we
perform similar task as above, the difference is that we perform in compact
and one-liner way using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Characters occurring in multiple Strings

# Using list comprehension + Counter() + set()

from itertools import chain

from collections import Counter

 

# initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeks',
'and', 'cs']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Characters occurring in multiple Strings

# Using list comprehension + Counter() + set()

res = [key for key, val in Counter([ele for sub in
test_list 

 for ele in set(sub)]).items()

 if val > 1]

 

# printing result 

print("Characters with Multiple String occurrence : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [‘gfg’, ‘is’, ‘best’, ‘for’, ‘geeks’, ‘and’, ‘cs’]  
> Characters with Multiple String occurrence : [‘g’, ‘e’, ‘f’, ‘s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

