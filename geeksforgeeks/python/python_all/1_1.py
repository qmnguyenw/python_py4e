Python Program to find tuple indices from other tuple list



Given Tuples list and search list consisting of tuples to search, our task is
to write a Python Program to extract indices of matching tuples.

>  **Input :** test_list = [(4, 5), (7, 6), (1, 0), (3, 4)], search_tup = [(3,
> 4), (8, 9), (7, 6), (1, 2)]
>
>  **Output :** [3, 1]
>
>  **Explanation :** (3, 4) from search list is found on 3rd index on
> test_list, hence included in result.
>
>  **Input :** test_list = [(4, 5), (7, 6), (1, 0), (3, 4)], search_tup = [(3,
> 4), (8, 9), (7, 6), (1, 0)]
>
>  
>
>
>  
>
>
>  **Output :** [3, 1, 2]
>
>  **Explanation :** (3, 4) from search list is found on 3rd index on
> test_list, hence included in result.

 **Method #1 : Using** **lookup dictionary** **+** **enumerate()** **+**
**list comprehension**

In this, a lookup dictionary is formed to map all the tuples with matching
one’s indices. Then lookup dictionary is used to get indices of mapped tuples
as result using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Find tuple indices from other tuple list

# Using lookup dictionary + enumerate() + list comprehension

 

# initializing list

test_list = [(4, 5), (7, 6), (1, 0), (3,
4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search tuple 

search_tup = [(3, 4), (8, 9), (7, 6), (1,
2)]

 

# creating lookup_dict

lookup_dict = {val: key for key,val in enumerate(test_list)}

 

# creating result list

res = [lookup_dict[idx] for idx in search_tup if idx in
lookup_dict]

 

# printing result

print("The match tuple indices : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [(4, 5), (7, 6), (1, 0), (3, 4)]
    The match tuple indices : [3, 1]

 **Method #2 : Using list comprehension + enumerate()**

In this, we perform the task of getting indices using enumerate(), and list
comprehension is used for the task of iteration of all the elements of tuple
and matching for equality.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Find tuple indices from other tuple list

# Using list comprehension + enumerate()

 

# initializing list

test_list = [(4, 5), (7, 6), (1, 0), (3,
4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing search tuple 

search_tup = [(3, 4), (8, 9), (7, 6), (1,
2)]

 

# enumerate() gets all the indices 

res = [idx for idx, val in enumerate(test_list) for ele
in search_tup if ele == val]

 

# printing result

print("The match tuple indices : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [(4, 5), (7, 6), (1, 0), (3, 4)]
    The match tuple indices : [1, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

