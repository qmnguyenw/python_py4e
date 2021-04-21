Python – Groups Strings on Kth character



Sometimes, while working with Python Strings, we can have a problem in which
we need to perform Grouping of Python Strings on basis of its Kth character.
This kind of problem can come in day-day programming. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop**  
This is one way in which this task can be performed. In this, we perform the
task of grouping using brute force approach. We iterate each string, and group
the dictionary after conditional check using conditional statement.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Groups Strings on Kth character

# Using loop

from collections import defaultdict

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# Groups Strings on Kth character

# Using loop

res = defaultdict(list)

for word in test_list:

 res[word[K - 1]].append(word)

 

# printing result 

print("The strings grouping : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list is : [‘gfg’, ‘is’, ‘best’, ‘for’, ‘geeks’]  
> The strings grouping : {‘f’: [‘gfg’], ‘s’: [‘is’], ‘e’: [‘best’, ‘geeks’],
> ‘o’: [‘for’]}

  

  

**Method #2 : Using map() \+ loop**  
This is yet another way to solve this problem. In this variant additional test
of valid character is added using map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Groups Strings on Kth character

# Using loop + map()

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# Groups Strings on Kth character

# Using loop + map()

res = dict()

for char in map(chr, range(97, 123)):

 words = [idx for idx in test_list if idx[K - 1]
== char]

 if words:

 res[char] = words

 

# printing result 

print("The strings grouping : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [‘gfg’, ‘is’, ‘best’, ‘for’, ‘geeks’]  
> The strings grouping : {‘f’: [‘gfg’], ‘s’: [‘is’], ‘e’: [‘best’, ‘geeks’],
> ‘o’: [‘for’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

