Python – Extract Even elements in Nested Mixed Tuple



Sometimes, while working with Python tuples, we can have a problem in which we
need to get all the even elements from tuple. The tuples can be nested or
mixed. This kind of problem can occur in data domains. Let’s discuss certain
ways in which this task can be performed.

>  **Input** : test_tuple = (5, (7, 6, (2, (4, ))))  
>  **Output** : ((6, (2, (4, ))), )
>
>  **Input** : test_tuple = (5, (8, 6, (2, (4, 8))))  
>  **Output** : ((8, 6, (2, (4, 8))), )

 **Method #1 : Using recursion +isinstance() \+ loop**  
This is one of the ways in which this task can be performed. In this, we
perform task of getting the element instance to be integer using isinstance()
and function is recursed once tuple is encountered.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Even elements in Nested Mixed Tuple

# Using recursion + isinstance() + loop

 

# helper_fnc

def even_ele(test_tuple, even_fnc):

 res = tuple()

 for ele in test_tuple:

 if isinstance(ele, tuple):

 res += (even_ele(ele, even_fnc), )

 elif even_fnc(ele):

 res += (ele, )

 return res

 

# initializing tuples

test_tuple = (4, 5, (7, 6, (2, 4)), 6,
8)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Extract Even elements in Nested Mixed Tuple

# Using recursion + isinstance() + loop

res = even_ele(test_tuple, lambda x: x % 2 == 0)

 

# printing result 

print("Even elements of tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (4, 5, (7, 6, (2, 4)), 6, 8)
    Even elements of tuple : (4, (6, (2, 4)), 6, 8)
    

