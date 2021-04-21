Python – Concatenate Rear elements in Tuple List



Given Tuple list, concatenate Rear elements.

>  **Input** : test_list = [(1, 2, “Gfg”), (“Best”, )]  
>  **Output** : Gfg Best  
>  **Explanation** : Last elements are joined.
>
>  **Input** : test_list = [(1, 2, “Gfg”)]  
>  **Output** : Gfg  
>  **Explanation** : Last elements are joined.

 **Method #1 : Using list comprehension + join()**

In this, we check for last element using “-1”, as index, and perform
concatenation using join(), list comprehension is used to iterate each tuple.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Rear elements in Tuple List

# Using join() + list comprehension

 

# initializing list

test_list = [(1, 2, "Gfg"), (4, "is"), ("Best",
)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# "-1" is used for access

res = " ".join([sub[-1] for sub in test_list]) 

 

# printing result 

print("The Concatenated result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(1, 2, 'Gfg'), (4, 'is'), ('Best', )]
    The Concatenated result : Gfg is Best
    

**Method #2 : Using map() + itemgetter() + join()**

In this, we perform task of getting last element using itemgetter(-1), and
map() is used to get all the last elements, concatenation using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Rear elements in Tuple List

# Using map() + itemgetter() + join()

from operator import itemgetter

 

# initializing list

test_list = [(1, 2, "Gfg"), (4, "is"), ("Best",
)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# "-1" is used for access

# map() to get all elements 

res = " ".join(list(map(itemgetter(-1), test_list))) 

 

# printing result 

print("The Concatenated result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(1, 2, 'Gfg'), (4, 'is'), ('Best', )]
    The Concatenated result : Gfg is Best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

