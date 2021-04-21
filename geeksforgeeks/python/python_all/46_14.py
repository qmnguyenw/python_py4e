Python – List Words Frequency in String



Given a List of Words, Map frequency of each to occurrence in String.

>  **Input** : test_str = ‘geeksforgeeks is best for geeks and best for CS’,
> count_list = [‘best’, ‘geeksforgeeks’, ‘computer’]  
>  **Output** : [2, 1, 0]  
>  **Explanation** : best has 2 occ., geeksforgeeks 1 and computer is not
> present in string.
>
>  **Input** : test_str = ‘geeksforgeeks is best for geeks and best for CS’,
> count_list = [‘better’, ‘gfg’, ‘computer’]  
>  **Output** : [0, 0, 0]  
>  **Explanation** : No word from list present in string.

 **Method #1 : Using defaultdict() + loop + list comprehension**

In this, we compute words frequency using loop + defaultdict() and then use
list comprehension to get all the counts corresponding to list of words.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Divide String into Equal K chunks

# Using list comprehension

from collections import defaultdict

 

# initializing strings

test_str = 'geeksforgeeks is best for geeks and best for CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing count_list 

count_list = ['best', 'geeksforgeeks', 'computer',
'better', 'for', 'and']

 

# computing frequency

res = defaultdict(int)

for sub in test_str.split():

 res[sub] += 1

 

# assigning to list words

res = [res[sub] for sub in count_list]

 

# printing result 

print("The list words frequency : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks and best for CS
    The list words frequency : [2, 1, 0, 0, 2, 1]
    

**Method #2 : Using Counter() + list comprehension**

In this, Counter() is used to perform task of computing frequency, post that,
list comprehension is used to asign frequency to list words.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Divide String into Equal K chunks

# Using list comprehension

from collections import Counter

 

# initializing strings

test_str = 'geeksforgeeks is best for geeks and best for CS'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing count_list 

count_list = ['best', 'geeksforgeeks', 'computer',
'better', 'for', 'and']

 

# computing frequency using Counter()

res = Counter(test_str.split())

 

# assigning to list words

res = [res[sub] for sub in count_list]

 

# printing result 

print("The list words frequency : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks is best for geeks and best for CS
    The list words frequency : [2, 1, 0, 0, 2, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

