Python – Sort by Frequency of second element in Tuple List



Given list of tuples, sort by frequency of second element of tuple.

>  **Input** : test_list = [(6, 5), (1, 7), (2, 5), (8, 7), (9, 8), (3, 7)]  
>  **Output** : [(1, 7), (8, 7), (3, 7), (6, 5), (2, 5), (9, 8)]  
>  **Explanation** : 7 occurs 3 times as 2nd element, hence all tuples with 7,
> are aligned first.
>
>  **Input** : test_list = [(1, 7), (8, 7), (9, 8), (3, 7)]  
>  **Output** : [(1, 7), (8, 7), (3, 7), (9, 8)]  
>  **Explanation** : 7 occurs 3 times as 2nd element, hence all tuples with 7,
> are aligned first.

 **Method #1 : Using sorted() + loop + defaultdict() + lambda**

In this, we compute the frequency using defaultdict() and use this result to
pass as param to lambda function to perform sorting using sorted() on basis of
it.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Frequency of second element in Tuple List

# Using sorted() + loop + defaultdict() + lambda

from collections import defaultdict

 

# initializing list

test_list = [(6, 5), (2, 7), (2, 5), (8,
7), (9, 8), (3, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# constructing mapping

freq_map = defaultdict(int)

for idx, val in test_list:

 freq_map[val] += 1

 

# performing sort of result 

res = sorted(test_list, key = lambda ele: freq_map[ele[1]],
reverse = True)

 

# printing results

print("Sorted List of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    Sorted List of tuples : [(2, 7), (8, 7), (3, 7), (6, 5), (2, 5), (9, 8)]
    

**Method #2 : Using Counter() + lambda + sorted()**

In this, the task of frequency computation is done using Counter(), rest all
functionality is similar to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Frequency of second element in Tuple List

# Using Counter() + lambda + sorted()

from collections import Counter

 

# initializing list

test_list = [(6, 5), (2, 7), (2, 5), (8,
7), (9, 8), (3, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# constructing mapping using Counter

freq_map = Counter(val for key, val in test_list)

 

# performing sort of result 

res = sorted(test_list, key = lambda ele: freq_map[ele[1]],
reverse = True)

 

# printing results

print("Sorted List of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    Sorted List of tuples : [(2, 7), (8, 7), (3, 7), (6, 5), (2, 5), (9, 8)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

