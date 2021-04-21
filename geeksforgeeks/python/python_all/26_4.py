Python – Remove Tuples from the List having every element as None



Given a Tuple list, remove all tuples with all None values.

>  **Input** : test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None,
> )]  
> **Output** : [(None, 2), (3, 4), (12, 3)]  
> **Explanation** : All None tuples are removed.
>
>  **Input** : test_list = [(None, None), (None, None), (3, 4), (12, 3),
> (None, )]  
> **Output** : [(3, 4), (12, 3)]  
> **Explanation** : All None tuples are removed.  
>

**Method #1 : Using** **all()** **+** **list comprehension**

In this, we use all() to check for all None values for discarding and list
comprehension does task of iteration.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove None Tuples from List

# Using all() + list comprehension

 

# initializing list

test_list = [(None, 2), (None, None), (3, 4),
(12, 3), (None, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# negating result for discarding all None Tuples

res = [sub for sub in test_list if not all(ele ==
None for ele in sub)]

 

# printing result 

print("Removed None Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(None, 2), (None, None), (3, 4), (12, 3), (None,)]  
> Removed None Tuples : [(None, 2), (3, 4), (12, 3)]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ all()**

In this method, task of filtering None tuples is done using filter() and
lambda function to provide None checking functionality using all().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove None Tuples from List

# Using filter() + lambda + all()

 

# initializing list

test_list = [(None, 2), (None, None), (3, 4),
(12, 3), (None, )]

 

# printing original list

print("The original list is : " + str(test_list))

 

# filter() + lambda to drive logic of discarding tuples

res = list(filter(lambda sub : not all(ele == None
for ele in sub), test_list))

 

# printing result 

print("Removed None Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(None, 2), (None, None), (3, 4), (12, 3), (None,)]  
> Removed None Tuples : [(None, 2), (3, 4), (12, 3)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

