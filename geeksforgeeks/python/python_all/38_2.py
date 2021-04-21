Python – Count frequency of Sublist in given list



Given a List and a sublist, count occurrence of sublist in list.

>  **Input** : test_list = [4, 5, 3, 5, 7, 8, 3, 5, 7, 2, 3, 5, 7], sublist =
> [3, 5, 7]  
>  **Output** : 3  
>  **Explanation** : 3, 5, 7 occurs 3 times.
>
>  **Input** : test_list = [4, 5, 3, 5, 8, 8, 3, 2, 7, 2, 3, 6, 7], sublist =
> [3, 5, 7]  
>  **Output** : 0  
>  **Explanation** : No occurrence found.

 **Method #1 : Using list comprehension + slicing**

In this, we test for each sublist of list extracted using slicing, if found,
the element is added to list, at last length of list is computed using len().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sublist Frequency

# Using list comprehension + slicing 

 

# initializing list

test_list = [4, 5, 3, 5, 7, 8, 3, 5,
7, 2, 7, 3, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Sublist

sublist = [3, 5, 7]

 

# slicing is used to extract chunks and compare

res = len([sublist for idx in range(len(test_list)) if
test_list[idx : idx + len(sublist)] == sublist])

 

# printing result 

print("The sublist count : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 3, 5, 7, 8, 3, 5, 7, 2, 7, 3, 2]
    The sublist count : 2
    

**Method #2 : Using zip_longest() + islice() + all() + loop**

In this, we perform task of slicing using islice() and check if each element
is matching using all(), zip_longest() helps in mapping elements to check for
equality from sublist. Loop is used to get to index match with first element
of sublist in list, to make it more efficient.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sublist Frequency

# Using zip_longest() + islice() + all() + loop 

from itertools import zip_longest, islice

 

# initializing list

test_list = [4, 5, 3, 5, 7, 8, 3, 5,
7, 2, 7, 3, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Sublist

sublist = [3, 5, 7]

 

# slicing is used to extract chunks and compare

res = []

idx = 0

while True:

 try:

 

 # getting to the index

 idx = test_list.index(sublist[0], idx)

 except ValueError:

 break

 

 # using all() to check for all elements equivalence

 if all(x == y for (x, y) in zip_longest(sublist,
islice(test_list, idx, idx + len(sublist)))):

 res.append(sublist)

 idx += len(sublist)

 idx += 1

 

res = len(res)

 

# printing result 

print("The sublist count : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 3, 5, 7, 8, 3, 5, 7, 2, 7, 3, 2]
    The sublist count : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

