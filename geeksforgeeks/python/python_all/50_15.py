Python – Custom length tuples from String



Given a String, extract tuple list, with each tuple being of custom length,
delimited using comma.

>  **Input** : test_str = “6 6 7, 3 4, 2”
>
>  **Output** : [(6, 6, 7), (3, 4), (2, )]
>
>  **Explanation** : The customs lengths being 3, 2, 1 have been converted to
> tuple list.
>
>  **Input** : test_str = “7, 7, 4”
>
>  
>
>
>  
>
>
>  **Output** : [(7, ), (7, ), (4, )]
>
>  **Explanation** : All elements are of lenth 1.

 **Method #1 : Using int() + tuple() + split() + list comprehension**

The combination of above functions can be used to solve this problem. In this,
we perform conversion of string characters using int() and tuple() and split()
is used to split on delimiter.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom length tuples from String

# Using int() + tuple() + split() + list comprehension

 

# initializing string

test_str = '4 6 7, 1 2, 3, 4 6 8 8'

 

# printing original string

print("The original string is : " + str(test_str))

 

# split() used to split on delimiter and 

# type casted to int followed by tuple casting

test_str = test_str.split(', ')

res = [tuple(int(ele) for ele in sub.split()) for sub
in test_str]

 

# printing result 

print("The constructed custom length tuples : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 4 6 7, 1 2, 3, 4 6 8 8
    The constructed custom length tuples : [(4, 6, 7), (1, 2), (3, ), (4, 6, 8, 8)]
    
    
    

**Method #2 : Using map() + int + tuple() + list comprehension + split()**

The combination of above functions provide yet another way in which this task
can be performed. In this we perform task using similar method as above just
difference being using map() to extend logic of integer conversion to
elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom length tuples from String

# Using map() + int + tuple() + list comprehension + split()

 

# initializing string

test_str = '4 6 7, 1 2, 3, 4 6 8 8'

 

# printing original string

print("The original string is : " + str(test_str))

 

# split() used to split on delimiter and 

# using map() to extend logic of element casting

res = [tuple(map(int, sub.split())) for sub in
test_str.split(", ")]

 

# printing result 

print("The constructed custom length tuples : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 4 6 7, 1 2, 3, 4 6 8 8
    The constructed custom length tuples : [(4, 6, 7), (1, 2), (3, ), (4, 6, 8, 8)]
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

