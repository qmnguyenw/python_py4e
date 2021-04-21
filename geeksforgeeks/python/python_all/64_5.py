Python – Type conversion in Nested and Mixed List



While working with Python lists, due to its heterogenous nature, we can have a
problem in which we need to convert data type of each nested element of list
to particular type. In mixed list, this becomes complex. Let’s discuss certain
way in which this task can be performed.

>  **Input** : test_list = [(‘7’, [‘8’, (‘5’, )])]  
>  **Output** : [(7, [8, (5, )])]
>
>  **Input** : test_list = [‘6’]  
>  **Output** : [6]

 **Method : Using recursion +isinstance()**  
The combination of above functions can be used to solve this problem. In this,
we use isinstance() to get the data type of element of list, and if its
container, the inner elements are recursed to perform conversion.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Type conversion in Nested and Mixed List

# Using recursion + isinstance()

 

# helper_fnc

def change_type(sub):

 if isinstance(sub, list):

 return [change_type(ele) for ele in sub]

 elif isinstance(sub, tuple):

 return tuple(change_type(ele) for ele in sub)

 else:

 return int(sub)

 

# initializing list

test_list = ['6', '89', ('7', ['8', '10']),
['11', '15']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Type conversion in Nested and Mixed List

# Using recursion + isinstance()

res = change_type(test_list)

 

# printing result 

print("Data after type conversion : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : ['6', '89', ('7', ['8', '10']), ['11', '15']]
    Data after type conversion : [6, 89, (7, [8, 10]), [11, 15]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

