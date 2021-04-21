Python – Remove Duplicate subset Tuples



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform removal of tuples, which are already present as subsets in
other tuples. This kind of problem can be use ful in data preprocessing. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(6, 9, 17, 18), (15, 34, 56), (6, 7, 10), (6, 7),
> (6, 9), (15, 34)], K = 2  
>  **Output** : [(6, 9, 17, 18), (15, 34, 56), (6, 7, 10)]
>
>  **Input** : test_list = [(6, 9, 17, 18), (15, 34, 56), (6, 7, 10)], K = 2  
>  **Output** : [(6, 9, 17, 18), (15, 34, 56), (6, 7, 10)]

 **Method #1 : Usingsetdefault() \+ list comprehension**  
This is one of the way in which this task can be solved. In this, we perform
the task of initializing the list and keeping elements to compare. At last,
list comprehension is used to perform removal of subset tuples. This method
gives flexibility of size of tuples for removal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Duplicate subset Tuples

# Using setdefault() + list comprehension

 

# initializing lists

test_list = [(6, 9, 17, 18), (15, 34, 56),
(6, 7), (6, 9), (15, 34)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# Remove Duplicate subset Tuples

# Using setdefault() + list comprehension

temp = {}

for sub in test_list:

 temp2 = sub[:K]

 temp.setdefault(temp2, []).append(sub)

res = [sub for sub in test_list if len(sub) > K or
len(temp[sub]) == 1]

 

# printing result 

print("Tuple list after removal : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(6, 9, 17, 18), (15, 34, 56), (6, 7), (6, 9), (15, 34)]
    Tuple list after removal : [(6, 9, 17, 18), (15, 34, 56), (6, 7)]
    

