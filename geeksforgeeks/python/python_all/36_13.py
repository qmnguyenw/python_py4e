Python – Convert Tuple Matrix to Tuple List



Given a Tuple Matrix, flatten to tuple list with each tuple representing each
column.

>  **Input** : test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]]  
>  **Output** : [(4, 7, 10, 18), (5, 8, 13, 17)]  
>  **Explanation** : All column number elements contained together.
>
>  **Input** : test_list = [[(4, 5)], [(10, 13)]]  
>  **Output** : [(4, 10), (5, 13)]  
>  **Explanation** : All column number elements contained together.

 **Method #1 : Using list comprehension + zip()**

In this, we perform task of flattening using list comprehension and zip() is
used to perform column pairing to render as tuple pairs.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple Matrix to Tuple List

# Using list comprehension + zip()

 

# initializing list

test_list = [[(4, 5), (7, 8)], [(10, 13),
(18, 17)], [(0, 4), (10, 1)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# flattening 

temp = [ele for sub in test_list for ele in sub]

 

# joining to form column pairs

res = list(zip(*temp))

 

# printing result 

print("The converted tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]
    The converted tuple list : [(4, 7, 10, 18, 0, 10), (5, 8, 13, 17, 4, 1)]
    

**Method #2 : Using chain.from_iterable() + zip()**

In this, task of flattening is performed using chain.from_iterable() and zip()
is used to perform the task of column pairing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple Matrix to Tuple List

# Using chain.from_iterable() + zip()

from itertools import chain

 

# initializing list

test_list = [[(4, 5), (7, 8)], [(10, 13),
(18, 17)], [(0, 4), (10, 1)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# flattening using from_iterable

res = list(zip(*chain.from_iterable(test_list)))

 

# printing result 

print("The converted tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]
    The converted tuple list : [(4, 7, 10, 18, 0, 10), (5, 8, 13, 17, 4, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

