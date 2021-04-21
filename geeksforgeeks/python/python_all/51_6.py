Python – Minimum value pairing for dictionary keys



Given two lists, key and value, construct a dictionary, which chooses minimum
values in case of similar key value pairing.

>  **Input** : test_list1 = [4, 7, 4, 8], test_list2 = [5, 7, 2, 9]  
>  **Output** : {8: 9, 7: 7, 4: 2}  
>  **Explanation** : For 4, there are 2 options, 5 and 2, 2 being smallest is
> paired.
>
>  **Input** : test_list1 = [4, 4, 4, 4], test_list2 = [3, 7, 2, 1]  
>  **Output** : {4: 1}  
>  **Explanation** : All elements are for 4, smallest being 1.

 **Method #1 : dict() + sorted() + zip() + lambda**

The combination of above functions can be used to solve this problem. In this,
we perform sorting using sorted(), zip() is used to map keys with values. The
dict() is used to convert result back into dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum value pairing for dictionary keys

# Using dict() + sorted() + zip() + lambda

 

# initializing lists

test_list1 = [4, 7, 4, 8, 7, 9]

test_list2 = [5, 7, 2, 9, 3, 4]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using zip() to bing key and value lists

# reverse sorting the list before assigning values 

# so as minimum values get to end, and hence avoided from 

# pairing 

res = dict(sorted(zip(test_list1, test_list2), key =
lambda ele: -ele[1]))

 

# printing result 

print("The minimum paired dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [4, 7, 4, 8, 7, 9]
    The original list 2 : [5, 7, 2, 9, 3, 4]
    The minimum paired dictionary : {8: 9, 7: 3, 4: 2, 9: 4}
    

**Method #2 : Using groupby() + itemgetter() + zip()**

The combination of above functions provide yet another way to solve this
problem. In this, the values grouping is done using groupby() and minimum
element is extracted using itemgetter().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum value pairing for dictionary keys

# Using groupby() + itemgetter() + zip()

from operator import itemgetter

from itertools import groupby

 

# initializing lists

test_list1 = [4, 7, 4, 8, 7, 9]

test_list2 = [5, 7, 2, 9, 3, 4]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using zip() to bind key and value lists

# groupby() to group similar value.

# 0th, first element is extracted to be smallest 

# using itemgetter()

temp = sorted(zip(test_list1, test_list2))

res = {key: min(val for _, val in group)

 for key, group in groupby(sorted(temp), itemgetter(0))}

 

# printing result 

print("The minimum paired dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [4, 7, 4, 8, 7, 9]
    The original list 2 : [5, 7, 2, 9, 3, 4]
    The minimum paired dictionary : {4: 2, 7: 3, 8: 9, 9: 4}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

