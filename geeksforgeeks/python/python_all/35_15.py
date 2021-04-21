Python – Sequence Assignment to Words



Given a String of words, assign index to each word.

>  **Input** : test_str = ‘geekforgeeks is best’  
>  **Output** : {0: ‘geekforgeeks’, 1: ‘is’, 2: ‘best’}  
>  **Explanation** : Index assigned to each word.
>
>  **Input** : test_str = ‘geekforgeeks best’  
>  **Output** : {0: ‘geekforgeeks’, 1: ‘best’}  
>  **Explanation** : Index assigned to each word.

 **Method #1 : Using enumerate() + dict() + split()**

In this, we first perform task of split() and then add index component to map
each word with index using enumerate().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sequence Assignment to Words

# Using split() + enumerate() + dict()

 

# initializing string

test_str = 'geekforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using dict() to convert result in idx:word manner 

res = dict(enumerate(test_str.split()))

 

# printing result 

print("The Assigned Sequence : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks is best for geeks
    The Assigned Sequence : {0: 'geekforgeeks', 1: 'is', 2: 'best', 3: 'for', 4: 'geeks'}
    

**Method #2 : Using zip() + count() + dict()**

In this, the count() component renders the index logic and pairing of each
word to index is done using zip().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sequence Assignment to Words

# Using zip() + count() + dict()

from itertools import count

 

# initializing string

test_str = 'geekforgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using dict() to convert result in idx:word manner 

# count() from itertools used for this task

res = dict(zip(count(), test_str.split()))

 

# printing result 

print("The Assigned Sequence : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks is best for geeks
    The Assigned Sequence : {0: 'geekforgeeks', 1: 'is', 2: 'best', 3: 'for', 4: 'geeks'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

