Python – Assign Frequency to Tuples



Given tuple list, assign frequency to each tuple in list.

>  **Input** : test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (9, ), (2, 7)]  
>  **Output** : [(6, 5, 8, 2), (2, 7, 2), (9, 1)]  
>  **Explanation** : (2, 7) occurs 2 times, hence 2 is appened in tuple.
>
>  **Input** : test_list = [(2, 7), (2, 7), (6, 5, 8), (9, ), (2, 7)]  
>  **Output** : [(6, 5, 8, 1), (2, 7, 3), (9, 1)]  
>  **Explanation** : (2, 7) occurs 3 times, hence 3 is appened in tuple.

 **Method #1 : Using Counter() + items() + * operator + list comprehension**

In this, we extract the frequency using Counter(), fetch frequency numbers
using items(), * operator is used to unpack elements and list comprehension is
used to assign this to all elements in tuple list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign Frequency to Tuples

# Using Counter() + items() + * operator + list comprehension

from collections import Counter

 

# initializing list

test_list = [(6, 5, 8), (2, 7), (6, 5,
8), (6, 5, 8), (9, ), (2, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# one-liner to solve problem

# assign Frequency as last element of tuple

res = [(*key, val) for key, val in
Counter(test_list).items()]

 

# printing results

print("Frequency Tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
    Frequency Tuple list : [(6, 5, 8, 3), (2, 7, 2), (9, 1)]
    

**Method #2 : Using most_common() + Counter() + * operator + list
comprehension**

This is similar to the above method, just most_common() performs sort
operation on list, which is not necessary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign Frequency to Tuples

# Using most_common() + Counter() + * operator + list comprehension

from collections import Counter

 

# initializing list

test_list = [(6, 5, 8), (2, 7), (6, 5,
8), (6, 5, 8), (9, ), (2, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# most_common performs sort on arg. list

# assign Frequency as last element of tuple

res = [(*key, val) for key, val in
Counter(test_list).most_common()]

 

# printing results

print("Frequency Tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
    Frequency Tuple list : [(6, 5, 8, 3), (2, 7, 2), (9, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

