Python – Extract elements from Ranges in List



Given a list, and a list of tuples with ranges, extract all elements in those
ranges from list.

>  **Input** : test_list = [4, 5, 4, 6, 7, 5, 4, 5, 6, 10], range_list = [(2,
> 4), (7, 8)]  
>  **Output** : [4, 6, 7, 5, 6]  
>  **Explanation** : 4, 6, 7 are elements at idx 2, 3, 4 and 5, 6 at idx 7, 8.
>
>  **Input** : test_list = [4, 5, 4, 6, 7, 5, 4, 5, 6, 10], range_list = [(2,
> 6)]  
>  **Output** : [4, 6, 7, 5, 4]  
>  **Explanation** : Elements from 2-6 index are extracted.

 **Method #1 : Using loop + list slicing**

In this, we extract each range using list slicing and using loop iterate for
each range and keep extending the extracting slices to extending list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements from Ranges in List

# Using loop + list slicing 

 

# initializing list

test_list = [4, 5, 4, 6, 7, 5, 4, 5,
4, 6, 4, 6, 9, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing ranges

range_list = [(2, 4), (7, 8), (10, 12)]

 

res = []

for ele in range_list:

 

 # extending ranges

 res.extend(test_list[ele[0] : ele[1] + 1])

 

# printing result 

print("Ranges elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 4, 6, 7, 5, 4, 5, 4, 6, 4, 6, 9, 8]
    Ranges elements : [4, 6, 7, 5, 4, 4, 6, 9]
    

**Method #2 : Using list comprehension**

In this, we apply similar method as above function, difference being that list
comprehension is used to solve this in compact form.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements from Ranges in List

# Using list comprehension

from itertools import chain

 

# initializing list

test_list = [4, 5, 4, 6, 7, 5, 4, 5,
4, 6, 4, 6, 9, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing ranges

range_list = [(2, 4), (7, 8), (10, 12)]

 

# using one-liner to solve this problem

res = list(chain.from_iterable([test_list[ele[0] : ele[1] +
1] for ele in range_list]))

 

# printing result 

print("Ranges elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 5, 4, 6, 7, 5, 4, 5, 4, 6, 4, 6, 9, 8]
    Ranges elements : [4, 6, 7, 5, 4, 4, 6, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

