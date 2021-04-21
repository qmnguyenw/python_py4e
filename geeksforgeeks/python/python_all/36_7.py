Python – Filter Tuples by Kth element from List



Given a list of tuples, filter by Kth element presence in List.

>  **Input** : test_list = [(“GFg”, 5, 9), (“is”, 4, 3), (“best”, 10, 29)],
> check_list = [4, 2, 3, 10], K = 2  
>  **Output** : [(‘is’, 4, 3)]  
>  **Explanation** : 3 is 2nd element and present in list, hence filtered
> tuple.
>
>  **Input** : test_list = [(“GFg”, 5, 9), (“is”, 4, 3), (“best”, 10, 29)],
> check_list = [4, 2, 3, 10], K = 1  
>  **Output** : [(‘is’, 4, 3), (‘best’, 10, 29)]  
>  **Explanation** : 4 and 10 are 1st elements and present in list, hence
> filtered tuples.

 **Method #1 : Using list comprehension**

In this, we check for each element of Tuple’s Kth element to be present in
list in shorthand using list comprehension and containment is tested using in
operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples by Kth element from List

# Using list comprehension

 

# initializing list

test_list = [("GFg", 5, 9), ("is", 4, 3),
("best", 10, 29)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check_list

check_list = [4, 2, 8, 10]

 

# initializing K 

K = 1

 

# checking for presence on Kth element in list 

# one liner 

res = [sub for sub in test_list if sub[K] in check_list]

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('GFg', 5, 9), ('is', 4, 3), ('best', 10, 29)]
    The filtered tuples : [('is', 4, 3), ('best', 10, 29)]
    

**Method #2 : Using filter() + lambda**

In this, lambda function checks for element presence and filter performs task
of filtering tuples.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples by Kth element from List

# Using filter() + lambda

 

# initializing list

test_list = [("GFg", 5, 9), ("is", 4, 3),
("best", 10, 29)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check_list

check_list = [4, 2, 8, 10]

 

# initializing K 

K = 1

 

# filter() perform filter, lambda func. checks for presence

# one liner 

res = list(filter(lambda sub: sub[K] in check_list,
test_list))

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('GFg', 5, 9), ('is', 4, 3), ('best', 10, 29)]
    The filtered tuples : [('is', 4, 3), ('best', 10, 29)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

