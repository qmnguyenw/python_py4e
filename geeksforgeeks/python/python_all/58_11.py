Python – Remove Kth Index Duplicates in Tuple



Sometimes, while working with Python records, we can have a problem in which
we need to remove all the tuples, which have similar Kth index elements in
list of records. This kind of problem is common in day-day and web development
domain. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(4, 5, 6), (2, 3, 4), (1, 3, 4), (7, 6, 4), (1, 2,
> 6)], K = 1  
>  **Output** : [(4, 5, 6), (2, 3, 4), (7, 6, 4), (1, 2, 6)]
>
>  **Input** : test_list = [(4, 5, 6), (2, 3, 4), (1, 3, 4), (7, 6, 4), (1, 2,
> 6)], K = 0  
>  **Output** : [(4, 5, 6), (2, 3, 4), (1, 3, 4), (7, 6, 4)]

 **Method #1 : Using loop**  
This is one of the ways in which this task can be performed. In this, we
perform the task of memoizing already occurred Kth index element in set, and
check each time with new value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Kth Index Duplicates in Tuple

# Using loop

 

# initializing lists

test_list = [(4, 5, 6), (2, 3, 4), (1, 3,
4), (7, 6, 4), (1, 2, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

# Remove Kth Index Duplicates in Tuple

# Using loop

keep = set() 

res = []

for sub in test_list:

 if sub[K] not in keep:

 res.append(sub)

 keep.add(sub[K])

 

# printing result 

print("Filtered Tuples : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 5, 6), (2, 3, 4), (1, 3, 4), (7, 6, 4), (1, 2, 6)]
    Filtered Tuples : [(4, 5, 6), (2, 3, 4)]
    

