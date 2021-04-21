Python – Bigrams Frequency in String



Sometimes while working with Python Data, we can have problem in which we need
to extract bigrams from string. This has application in NLP domains. But
sometimes, we need to compute the frequency of unique bigram for data
collection. The solution to this problem can be useful. Lets discuss certain
ways in which this task can be performed.

 **Method #1 : UsingCounter() \+ generator expression**  
The combination of above functions can be used to solve this problem. In this,
we compute the frequency using Counter() and bigram computation using
generator expression and string slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Bigrams Frequency in String

# Using Counter() + generator expression

from collections import Counter

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Bigrams Frequency in String

# Using Counter() + generator expression

res = Counter(test_str[idx : idx + 2] for idx in
range(len(test_str) - 1))

 

# printing result 

print("The Bigrams Frequency is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original string is : geeksforgeeks  
> The Bigrams Frequency is : {‘ee’: 2, ‘ks’: 2, ‘ek’: 2, ‘sf’: 1, ‘fo’: 1,
> ‘ge’: 2, ‘rg’: 1, ‘or’: 1}

  

  

**Method #2 : UsingCounter() + zip() + map() + join**  
The combination of above functions can also be used to solve this problem. In
this, we perform the task of constructing bigrams using zip() + map() + join.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Bigrams Frequency in String

# Using Counter() + zip() + map() + join

from collections import Counter

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Bigrams Frequency in String

# Using Counter() + zip() + map() + join

res = Counter(map(''.join, zip(test_str, test_str[1:])))

 

# printing result 

print("The Bigrams Frequency is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original string is : geeksforgeeks  
> The Bigrams Frequency is : {‘ee’: 2, ‘ks’: 2, ‘ek’: 2, ‘sf’: 1, ‘fo’: 1,
> ‘ge’: 2, ‘rg’: 1, ‘or’: 1}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

