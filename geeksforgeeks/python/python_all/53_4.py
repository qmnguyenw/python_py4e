Python – Sort dictionary by Tuple Key Product



Given dictionary with tuple keys, sort dictionary items by tuple product of
keys.

>  **Input** : test_dict = {(2, 3) : 3, (6, 3) : 9, (8, 4): 10, (10, 4): 12}  
>  **Output** : {(2, 3) : 3, (6, 3) : 9, (8, 4): 10, (10, 4): 12}  
>  **Explanation** : 6 < 18 < 32 < 40, key products hence retains order.
>
>  **Input** : test_dict = {(20, 3) : 3, (6, 3) : 9, (8, 4): 10, (10, 4): 12}  
>  **Output** : {(6, 3) : 9, (8, 4): 10, (10, 4): 12, (20, 3) : 3, }  
>  **Explanation** : 18 < 32 < 40 < 60, key products hence adjusts order.

 **Method #1 : Using dictionary comprehension + lambda + sorted()**

This is one of the ways in which this task can be performed. In this, we
perform sort() using sorted() and lambda function is used to compute product
over which sort can be performed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionary by Tuple Key Product

# Using dictionary comprehension + sorted() + lambda

 

# initializing dictionary

test_dict = {(5, 6) : 3, (2, 3) : 9, (8,
4): 10, (6, 4): 12}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# sorted() over lambda computed product 

# dictionary comprehension reassigs dictionary by order 

res = {key: test_dict[key] for key in sorted(test_dict.keys(),
key = lambda ele: ele[1] * ele[0])}

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {(5, 6): 3, (2, 3): 9, (8, 4): 10, (6, 4): 12}
    The sorted dictionary : {(2, 3): 9, (6, 4): 12, (5, 6): 3, (8, 4): 10}
    

**Method #2 : Using dict() + sorted() + lambda**

The combination of above functions can be used to solve this problem. In this,
similar method is used as above method. The only difference being items
arrangement done using dict() rather than dictionary comprehension after
computing keys ordering .

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionary by Tuple Key Product

# Using dict() + sorted() + lambda

 

# initializing dictionary

test_dict = {(5, 6) : 3, (2, 3) : 9, (8,
4): 10, (6, 4): 12}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# sorted() over lambda computed product 

# dict() used instead of dictionary comprehension for rearrangement

res = dict(sorted(test_dict.items(), key = lambda ele:
ele[0][1] * ele[0][0]))

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {(5, 6): 3, (2, 3): 9, (8, 4): 10, (6, 4): 12}
    The sorted dictionary : {(2, 3): 9, (6, 4): 12, (5, 6): 3, (8, 4): 10}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

