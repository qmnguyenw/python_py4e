Python – K elements Reversed Slice



Given List of elements, perform K elements reverse slice.

>  **Input** : test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18], K = 3  
>  **Output** : [18, 16, 15]  
>  **Explanation** : 3 elements sliced from rear end.
>
>  **Input** : test_list = [2, 4, 6, 8], K = 3  
>  **Output** : [8, 6, 4]  
>  **Explanation** : 3 elements sliced from rear end, 8, 6 and 4.

 **Method #1 : Using list slicing**

This is one of the ways in which this task can be performed. In this, we
perform reverse slice using reversing and negative slicing capabilities of
list slicing.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K elements Reversed Slice

# Using list slicing 

 

# initializing list

test_list = [2, 4, 6, 8, 3, 9, 12, 15,
16, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 6

 

# using double slice to solve problem.

# "-" sign for slicing from rear 

res = test_list[-K:][::-1]

 

# printing result 

print("The sliced list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
    The sliced list : [18, 16, 15, 12, 9, 3]
    

**Method #2 : Using islice() + reversed()**

This is functional approach to solve this problem. In this, we perforom
slicing using islice(), and then list is reversed using reversed().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K elements Reversed Slice

# Using K elements Reversed Slice

from itertools import islice

 

# initializing list

test_list = [2, 4, 6, 8, 3, 9, 12, 15,
16, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 6

 

# using revered and islice to slice 

# and then perform reverse

res = list(islice(reversed(test_list), K))

 

# printing result 

print("The sliced list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
    The sliced list : [18, 16, 15, 12, 9, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

