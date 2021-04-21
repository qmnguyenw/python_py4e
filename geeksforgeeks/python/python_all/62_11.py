Python – Remove Consecutive K element records



Sometimes, while working with Python records, we can have a problem in which
we need to remove records on the basis of presence of consecutive K elements
in tuple. This kind of problem is peculiar but can have applications in data
domains. Let’s discuss certain ways in which this task can be performed.

>  **Input** :  
> test_list = [(4, 5), (5, 6), (1, 3), (0, 0)]  
> K = 0  
>  **Output** : [(4, 5), (5, 6), (1, 3)]
>
>  **Input** :  
> test_list = [(4, 5), (5, 6), (1, 3), (5, 4)]  
> K = 5  
>  **Output** : [(4, 5), (5, 6), (1, 3), (5, 4)]

 **Method #1 : Usingzip() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we need to combine two consecutive segments using zip() and perform the
comparison in list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Consecutive K element records

# Using zip() + list comprehension

 

# initializing list

test_list = [(4, 5, 6, 3), (5, 6, 6, 9),
(1, 3, 5, 6), (6, 6, 7, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 6

 

# Remove Consecutive K element records

# Using zip() + list comprehension

res = [idx for idx in test_list if (K, K) not in
zip(idx, idx[1:])]

 

# printing result 

print("The records after removal : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
    The records after removal : [(4, 5, 6, 3), (1, 3, 5, 6)]
    

