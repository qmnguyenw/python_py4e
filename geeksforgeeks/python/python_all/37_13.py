Python – Filter Tuples with Integers



Given Tuple list, filter tuples which are having just int data type.

>  **Input** : [(4, 5, “GFg”), (3, ), (“Gfg”, )]  
>  **Output** : [(3, )]  
>  **Explanation** : 1 tuple (3, ) with all integral values.
>
>  **Input** : [(4, 5, “GFg”), (3, “Best” ), (“Gfg”, )]  
>  **Output** : []  
>  **Explanation** : No tuple with all integers.

 **Method #1 : Using loop + isinstance()**

In this, we iterate the each tuple and check for data type other than int,
using isinstance(), if found tuple is flagged off and omitted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples with Integers

# Using loop + isinstance()

 

# initializing list

test_list = [(4, 5, "GFg"), (5, 6), (3, ),
("Gfg", )]

 

# printing original list

print("The original list is : " + str(test_list))

 

res_list = []

for sub in test_list:

 res = True

 for ele in sub:

 

 # checking for non-int.

 if not isinstance(ele, int):

 res = False

 break

 if res :

 res_list.append(sub)

 

# printing results

print("Filtered tuples : " + str(res_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 'GFg'), (5, 6), (3, ), ('Gfg', )]
    Filtered tuples : [(5, 6), (3, )]
    

**Method #2 : Using all() + list comprehension + isinstance()**

In this, all() is used to check if all elements are integers using
isinstance(), if that checks, tuples are added to result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter Tuples with Integers

# Using all() + list comprehension + isinstance()

 

# initializing list

test_list = [(4, 5, "GFg"), (5, 6), (3, ),
("Gfg", )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension to encapsulate in 1 liner 

res = [sub for sub in test_list if all(isinstance(ele,
int) for ele in sub)]

 

# printing results

print("Filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(4, 5, 'GFg'), (5, 6), (3, ), ('Gfg', )]
    Filtered tuples : [(5, 6), (3, )]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

