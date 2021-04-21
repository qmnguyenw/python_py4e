Python – Filter consecutive elements Tuples



Given a Tuple list, filter tuples which are made from consecutive elements,
i.e diff is 1.

>  **Input** : test_list = [(3, 4, 5, 6), (5, 6, 7, 2), (1, 2, 4), (6, 4, 6,
> 3)]  
>  **Output** : [(3, 4, 5, 6)]  
>  **Explanation** : Only 1 tuple adhers to condition.
>
>  **Input** : test_list = [(3, 4, 5, 6), (5, 6, 7, 2), (1, 2, 3), (6, 4, 6,
> 3)]  
>  **Output** : [(3, 4, 5, 6), (1, 2, 3)]  
>  **Explanation** : Only 2 tuples adher to condition.

 **Method #1 : Using loop**

In this, for each tuple, we call consecutive elements utility which returns
True if tuple is consecutive.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter consecutive elements Tuples

# Using loop

 

# hlpr_func 

def consec_check(tup):

 for idx in range(len(tup) - 1):

 

 # returns false if any element is not consec.

 if tup[idx + 1] != tup[idx] + 1:

 return False

 

 return True

 

# initializing list

test_list = [(3, 4, 5, 6), (5, 6, 7, 2),
(1, 2, 3), (6, 4, 6, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 # calls fnc to check consec.

 if consec_check(sub):

 res.append(sub)

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 4, 5, 6), (5, 6, 7, 2), (1, 2, 3), (6, 4, 6, 3)]
    The filtered tuples : [(3, 4, 5, 6), (1, 2, 3)]
    

**Method #2 : Using list comprehension**

In this, we performs similar function as in above, just in one-liner shorthand
using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter consecutive elements Tuples

# Using list comprehension

 

# hlpr_func 

def consec_check(tup):

 for idx in range(len(tup) - 1):

 

 # returns false if any element is not consec.

 if tup[idx + 1] != tup[idx] + 1:

 return False

 

 return True

 

# initializing list

test_list = [(3, 4, 5, 6), (5, 6, 7, 2),
(1, 2, 3), (6, 4, 6, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# one-liner to solve problem, using list comprehension

res = [sub for sub in test_list if consec_check(sub)]

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 4, 5, 6), (5, 6, 7, 2), (1, 2, 3), (6, 4, 6, 3)]
    The filtered tuples : [(3, 4, 5, 6), (1, 2, 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

