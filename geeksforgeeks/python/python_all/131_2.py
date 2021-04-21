Python | Combinations of elements till size N in list



The problem of finding the combinations of list elements of specific size has
been discussed. But sometimes, we require more and we wish to have all the
combinations of elements of all sizes till N. Let’s discuss certain ways in
which this function can be performed.

 **Method #1 : Using list comprehension +combinations()**  
This task can be performed using the list comprehension which can perform the
task of varying the combination length and combination() can perform the
actual task of finding combinations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Combinations of elements till size N in list

# Using list comprehension + combinations()

from itertools import combinations

 

# initializing list

test_list = [4, 5, 6, 7, 3, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Combinations of elements till size N in list

# Using list comprehension + combinations()

res = [com for sub in range(3) for com in
combinations(test_list, sub + 1)]

 

# Printing result

print("The combinations of elements till length N : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [4, 5, 6, 7, 3, 8]  
> The combinations of elements till length N : [(4, ), (5, ), (6, ), (7, ),
> (3, ), (8, ), (4, 5), (4, 6), (4, 7), (4, 3), (4, 8), (5, 6), (5, 7), (5,
> 3), (5, 8), (6, 7), (6, 3), (6, 8), (7, 3), (7, 8), (3, 8), (4, 5, 6), (4,
> 5, 7), (4, 5, 3), (4, 5, 8), (4, 6, 7), (4, 6, 3), (4, 6, 8), (4, 7, 3), (4,
> 7, 8), (4, 3, 8), (5, 6, 7), (5, 6, 3), (5, 6, 8), (5, 7, 3), (5, 7, 8), (5,
> 3, 8), (6, 7, 3), (6, 7, 8), (6, 3, 8), (7, 3, 8)]

  

  

**Method 2 : Using loop +extend() + combinations()**  
This method is similar to above method, just the loop is being using to
iterate for combination size and extend() performs the task of adding the
combinations one after another to final result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Combinations of elements till size N in list

# Using loop + extend() + combinations()

from itertools import combinations

 

# initializing list

test_list = [4, 5, 6, 7, 3, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Combinations of elements till size N in list

# Using loop + extend() + combinations()

res = []

for sub in range(3):

 res.extend(combinations(test_list, sub + 1))

 

# Printing result

print("The combinations of elements till length N : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [4, 5, 6, 7, 3, 8]  
> The combinations of elements till length N : [(4, ), (5, ), (6, ), (7, ),
> (3, ), (8, ), (4, 5), (4, 6), (4, 7), (4, 3), (4, 8), (5, 6), (5, 7), (5,
> 3), (5, 8), (6, 7), (6, 3), (6, 8), (7, 3), (7, 8), (3, 8), (4, 5, 6), (4,
> 5, 7), (4, 5, 3), (4, 5, 8), (4, 6, 7), (4, 6, 3), (4, 6, 8), (4, 7, 3), (4,
> 7, 8), (4, 3, 8), (5, 6, 7), (5, 6, 3), (5, 6, 8), (5, 7, 3), (5, 7, 8), (5,
> 3, 8), (6, 7, 3), (6, 7, 8), (6, 3, 8), (7, 3, 8)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

