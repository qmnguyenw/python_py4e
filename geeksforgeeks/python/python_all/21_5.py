Python – Sort Dictionary by key-value Summation



Given a Dictionary, sort by summation of key and value.

> **Input** : test_dict = {3:5, 1:3, 4:6, 2:7, 8:1}  
> **Output** : {1: 3, 3: 5, 2: 7, 8: 1, 4: 6}  
> **Explanation** : 4 < 8 < 9 = 9 < 10 are increasing summation of keys and
> values.  
>
>
> **Input** : test_dict = {3:5, 1:3, 4:6, 2:7}  
> **Output** : {1: 3, 3: 5, 2: 7, 4: 6}  
> **Explanation** : 4 < 8 < 9 < 10 are increasing summation of keys and
> values.

**Method : Using sorted() + lambda + items()**

In this sort operation is performed using _sorted(), lambda_ function is used
to provide addition logic. The _items()_ is used to get both keys and values.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by key-value Summation

# Using sorted() + lambda + items()

 

# initializing dictionary

test_dict = {3: 5, 1: 3, 4: 6, 2: 7,
8: 1}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# sorted() to sort, lambda provides key-value addition

res = sorted(test_dict.items(), key=lambda sub: sub[0] +
sub[1])

 

# converting to dictionary

res = {sub[0]: sub[1] for sub in res}

 

# printing result

print("The sorted result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original dictionary is : {3: 5, 1: 3, 4: 6, 2: 7, 8: 1}
    The sorted result : {1: 3, 3: 5, 2: 7, 8: 1, 4: 6}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

