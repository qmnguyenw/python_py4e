Python – Modify Equal Tuple Rows



Sometimes, while working with Python Records, we can have a problem in which
we need to perform the modification of element records on equality of records.
This can have a problem in domains that involve data. Let’s discuss certain
ways in which this task can be performed.

>  **Input** :  
> test_list = [[(12, 5)], [(13, 2)], [(6, 7)]]  
> test_row = [(13, 2)]  
>  **Output** : [[(12, 5)], [(13, 8)], [(6, 7)]]
>
>  **Input** :  
> test_list = [[(12, 5), (7, 6)]]  
> test_row = [(13, 2)]  
>  **Output** : [[(12, 5), (7, 6)]]

 **Method #1 : Using loop +enumerate()**  
The combination of above functions can be used to solve this problem. In this,
we apply brute force for performing task of checking for equality and
performing required modification.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Modify Equal Tuple Rows

# Using loop + enumerate()

 

# initializing list

test_list = [[(12, 5), (13, 6)], [(12, 2),
(13, 2)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check row 

test_row = [(12, 2), (13, 2)]

 

# Modify Equal Tuple Rows

# Using loop + enumerate()

# multiple y coordinate by 4

for idx, val in enumerate(test_list):

 if val == test_row:

 temp = []

 for sub in val:

 ele = (sub[0], sub[1] * 4)

 temp.append(ele)

 test_list[idx] = temp

 

# printing result 

print("List after modification : " + str(test_list))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [[(12, 5), (13, 6)], [(12, 2), (13, 2)]]
    List after modification : [[(12, 5), (13, 6)], [(12, 8), (13, 8)]]
    

