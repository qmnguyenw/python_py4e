Python – Dictionary construction from front-rear key values



Given a list, construct dictionary using key as first half values and values
starting from last.

>  **Input** : test_list = [4, 10, 5, 3]  
>  **Output** : {4: 3, 10: 5}  
>  **Explanation** : First (4) is paired with rear (3) and so on.
>
>  **Input** : test_list = [5, 3]  
>  **Output** : {5: 3}  
>  **Explanation** : First (5) is paired with rear (3).

>  **Input** : test_dict = {“Apple” : 2, “Mango” : 2, “Grapes” : 2}, {“Apple”
> : 2, “Mango” : 2, “Grapes” : 2}  
>  **Output** : 12  
>  **Explanation** : (2*2) + (2*2) + (2*2) = 12.
>
>  **Input** : test_dict = {“Apple” : 3, “Mango” : 2, “Grapes” : 3}, {“Apple”
> : 2, “Mango” : 2, “Grapes” : 2}  
>  **Output** : 16  
>  **Explanation** : The summation of product leads to 16 as above.
>
>  
>
>
>  
>

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we run a loop
from beginning and extract values from beg-end, and construct key value
mapping accordingly.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary construction from front-rear key values

# Using loop

 

# initializing list

test_list = [4, 6, 3, 10, 5, 3]

 

# printing original list

print("The original list : " + str(test_list))

 

 

# initializing size and empty Dictionary

n = len(test_list)

res = dict()

 

# running loop till mid

for idx in range(n // 2):

 

 # mapping as required

 res.__setitem__(test_list[idx], test_list[n - idx - 1]) 

 

# printing result 

print("The mapped dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 3, 10, 5, 3]
    The mapped dictionary : {4: 3, 6: 5, 3: 10}
    

**Method #2 : Using zip() + dict()**

This is yet another way in which this task can be performed. In this, we
perform the task of zipping key and value elements using zip() and dict() is
used to convert result to dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary construction from front-rear key values

# Using zip() + dict()

 

# initializing list

test_list = [4, 6, 3, 10, 5, 3]

 

# printing original list

print("The original list : " + str(test_list))

 

# using zip to cut first and second half 

n = len(test_list)

res = dict(zip(test_list[:n // 2], test_list[n //
2:][::-1]))

 

# printing result 

print("The mapped dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 3, 10, 5, 3]
    The mapped dictionary : {4: 3, 6: 5, 3: 10}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

