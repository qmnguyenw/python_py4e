Python – Concatenate Maximum Tuples



Given a tuple list with string and its magnitude, the task is to write a
python program to join all the strings with maximum magnitudes.

 **Examples:**

>  **Input :** test_list = [(“Gfg is best”, 8), (“gfg is good”, 7), (“for”,
> 2), (“for all geeks”, 8)]
>
>  **Output :** “Gfg is best for all geeks”
>
>  **Explanation :** 8 is maximum tuple element and concatenation of keys
> yeild the result.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [(“Gfg is best”, 7), (“gfg is good”, 8), (“for”,
> 2), (“for all geeks”, 8)]
>
>  **Output :** “gfg is good for all geeks”
>
>  **Explanation :** 8 is maximum tuple element and concatenation of keys
> yeild the result.

 **Method #1 : Using** **max()** **\+ itemgetter() +** **list comprehension**
**+** **join()**

In this, we perform task of getting maximum magnitude numbers using max(),
itemgetter handles the index to query. The strings are joined by join() after
matching using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Maximum Tuples

# Using max() + itemgetter() + list comprehension + join()

from operator import itemgetter

 

# initializing list

test_list = [("Gfg is best", 8), ("gfg is good", 7),

 ("for", 2), ("for all geeks", 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting maximum

max_ele = max(test_list, key=itemgetter(1))[1]

 

# joining maximum

res = ' '.join([key for key, ele in test_list if ele
== max_ele])

 

# printing result

print("The maximum concatenated strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘Gfg is best’, 8), (‘gfg is good’, 7), (‘for’, 2),
> (‘for all geeks’, 8)]
>
> The maximum concatenated strings : Gfg is best for all geeks
>
>  
>
>
>  
>

 **Method #2 : Using** **filter()** **+** **max()** **\+ itemgetter()**

In this, we perform task of filtering using filter() rather than list
comprehension. Rest all the functionalities is similar to all the method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Maximum Tuples

# Using filter() + max() + itemgetter()

from operator import itemgetter

 

# initializing list

test_list = [("Gfg is best", 8), ("gfg is good", 7),

 ("for", 2), ("for all geeks", 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting maximum

max_ele = max(test_list, key=itemgetter(1))[1]

 

# joining maximum

# filter checks for maximum values and concats

res = " ".join([ele[0]

 for ele in filter(lambda ele: ele[1] == max_ele,
test_list)])

 

# printing result

print("The maximum concatenated strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(‘Gfg is best’, 8), (‘gfg is good’, 7), (‘for’, 2),
> (‘for all geeks’, 8)]
>
> The maximum concatenated strings : Gfg is best for all geeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

