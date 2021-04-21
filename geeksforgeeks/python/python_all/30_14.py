Python program to find the frequency of the elements which are common in a
list of strings



Given list of strings. The task is to find the frequency of the elements which
are common in all strings given in the list of strings.

 **Examples:**

    
    
     **Input** : test_list = ["gegek", "gfgk", "kingg"]
    **Output** : {'g': 2, 'k': 1}
    **Explanation** : g occurs twice in all Strings.
    
    **Input** : test_list = ["gefgek", "gfgk", "kinfgg"]
    **Output** : {'g': 2, 'k': 1, 'f' : 1}
    **Explanation** : f occurs once in all Strings.

 **Method : Using reduce() + lamdba + Counter()**

The combination of above functions can be used to solve this problem. In this,
we perform the key role of counting using Counter() and lambda coupled with
reduce() is used to perform intersection and extension of logic to all the
strings respectively.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strings list intersection

# Using reduce() + lamdba + Counter()

from functools import reduce

from collections import Counter

 

# initializing list

test_list = ["geek", "gfgk", "king"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using & operator to perform intersection

res = reduce(lambda a, b: a & b, (Counter(ele) for ele in
test_list[1:]),

 Counter(test_list[0]))

 

# printing result

print("String intersection and frequency : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['geek', 'gfgk', 'king']
    String intersection and frequency : {'g': 1, 'k': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

