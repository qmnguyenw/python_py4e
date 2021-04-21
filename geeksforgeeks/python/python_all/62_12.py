Python – Remove K from Records



Sometimes, while working with Python tuples, we can have a problem in which we
need to remove all K from lists. This task can have application in many
domains such as web development and day-day programming. Let’s discuss certain
ways in which this task can be performed.

>  **Input** :  
> test_list = [(5, 6, 7), (2, 5, 7)]  
> K = 7  
>  **Output** : [(5, 6), (2, 5)]
>
>  **Input** :  
> test_list = [(5, 6, 7), (2, 5, 7)]  
> K = 5  
>  **Output** : [(6, 7), (2, 7)]

 **Method #1 : Using list comprehension**  
This is one of the way in which this task can be performed. In this, we
perform the task of getting conditional checks and recreating new list using
list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K from Records

# Using list comprehension

 

# initializing list

test_list = [(5, 6, 7), (2, 5), (1, ), (7,
8), (9, 7, 2, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 7

 

# Remove K from Records

# Using list comprehension

res = [tuple(ele for ele in sub if ele != K) for
sub in test_list]

 

# printing result 

print("The records after removing K : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(5, 6, 7), (2, 5), (1, ), (7, 8), (9, 7, 2, 1)]
    The records after removing K : [(5, 6), (2, 5), (1, ), (8, ), (9, 2, 1)]
    

