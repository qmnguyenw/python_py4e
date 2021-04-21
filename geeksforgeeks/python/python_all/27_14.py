Python – Sort Dictionaries by Size



Given a Dictionary List, perform sort by size of dictionary.

>  **Input** : test_list = [{4:6, 9:1, 10:2, 2:8}, {4:3, 9:1}, {3:9}, {1:2,
> 9:3, 7:4}]  
> **Output** : [{3: 9}, {4: 3, 9: 1}, {1: 2, 9: 3, 7: 4}, {4: 6, 9: 1, 10: 2,
> 2: 8}]  
> **Explanation** : 1 < 2 < 3 < 4, sorted by number of keys of dictionary.
>
>  **Input** : test_list = [{4:3, 9:1}, {3:9}, {1:2, 9:3, 7:4}]  
> **Output** : [{3: 9}, {4: 3, 9: 1}, {1: 2, 9: 3, 7: 4}]  
> **Explanation** : 1 < 2 < 3, sorted by number of keys of dictionary.

**Method #1 : Using len() + sort()**

In this, sorting is performed using _sort()_ and _len()_ is used to get size
of dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionaries by Size

# Using len() + sort()

 

# function to get length

def get_len(sub):

 

 # return length

 return len(sub)

 

 

# initializing list

test_list = [{4: 6, 9: 1, 10: 2, 2: 8},
{

 4: 3, 9: 1}, {3: 9}, {1: 2, 9: 3,
7: 4}]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# performing inplace sort of list

test_list.sort(key=get_len)

 

# printing result

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{4: 6, 9: 1, 10: 2, 2: 8}, {4: 3, 9: 1}, {3: 9}, {1:
> 2, 9: 3, 7: 4}]  
> Sorted List : [{3: 9}, {4: 3, 9: 1}, {1: 2, 9: 3, 7: 4}, {4: 6, 9: 1, 10: 2,
> 2: 8}]

 **Method #2 : Using sorted() + len() + lambda**

Here, we perform task of sorting using _sorted()_ , and _lambda_ function is
used in place of external function to solve problem of getting length.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionaries by Size

# Using sorted() + len() + lambda

 

# initializing list

test_list = [{4: 6, 9: 1, 10: 2, 2: 8},
{

 4: 3, 9: 1}, {3: 9}, {1: 2, 9: 3,
7: 4}]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# performing sort using sorted(), lambda for filtering

res = sorted(test_list, key=lambda sub: len(sub))

 

# printing result

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [{4: 6, 9: 1, 10: 2, 2: 8}, {4: 3, 9: 1}, {3: 9}, {1:
> 2, 9: 3, 7: 4}]  
> Sorted List : [{3: 9}, {4: 3, 9: 1}, {1: 2, 9: 3, 7: 4}, {4: 6, 9: 1, 10: 2,
> 2: 8}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

