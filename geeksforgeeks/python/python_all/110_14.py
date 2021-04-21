Python – Remove the row if all elements equal to N



Sometimes, while handling data, especially in Machine Learning domain, we need
to go through a lot of similar of N equal data. We sometimes need to eliminate
the rows which are all equal to N. Let’s discuss certain ways to remove the
rows that have all N values as list columns.

 **Method #1 : Using list comprehension + count() + len()**  
We can perform this particular task using the list comprehension recipe,
partnered with the combination of len and count function to check for
similarity element counter equating to the length of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# N row deletion in Matrix

# using list comprehension + count() + len()

 

# initializing matrix

test_list = [[1, 4, 2], [False, 9, 3],

 [6, 6, 6], [1, 0, 1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N 

N = 6

 

# using list comprehension + count() + len()

# N row deletion in Matrix

res = [sub for sub in test_list if sub.count(N) !=
len(sub)]

 

# print result

print("The list after removal of N rows : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 4, 2], [False, 9, 3], [6, 6, 6], [1, 0, 1]]
    The list after removal of N rows : [[1, 4, 2], [False, 9, 3], [1, 0, 1]]
    

**Method #2 : Using list comprehension +set()**  
This particular task can also be performed by converting the entire row into a
set and then checking for the single value N set for equality and removing if
a match is found.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# N row deletion in Matrix

# using list comprehension + set()

 

# initializing matrix

test_list = [[1, 4, 2], [False, 9, 3],

 [6, 6, 6], [1, 0, 1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N 

N = 6

 

# using list comprehension + set()

# N row deletion in Matrix

res = [sub for sub in test_list if set(sub) != {N}]

 

# print result

print("The list after removal of N rows : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 4, 2], [False, 9, 3], [6, 6, 6], [1, 0, 1]]
    The list after removal of N rows : [[1, 4, 2], [False, 9, 3], [1, 0, 1]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

