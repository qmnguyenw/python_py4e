Python | Pair the consecutive character strings in a list



Sometimes while programming, we can face a problem in which we need to perform
consecutive element concatenation. This problem can occur at times of school
programming or competitive programming. Let’s discuss certain ways in which
this problem can be solved.

 **Method #1 : Using list comprehension +zip()**  
Combination of above functionalities can be used to solve this problem. In
this, we iterate the list using list comprehension and formation of pairs
using zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element pairing in list

# using list comprehension + zip()

 

# initialize list 

test_list = ["G", "F", "G", "I", "S", "B",
"E", "S", "T"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Consecutive element pairing in list

# using list comprehension + zip()

res = [i + j for i, j in zip(test_list,
test_list[1:])]

 

# printing result

print("List after Consecutive concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’]  
> List after Consecutive concatenation is : [‘GF’, ‘FG’, ‘GI’, ‘IS’, ‘SB’,
> ‘BE’, ‘ES’, ‘ST’]

  

  

**Method #2 : Usingmap() + concat()**  
The combination of these functions can also perform this task. In this
traversal logic is done by map() and concat performs the task of pairing. It’s
more efficient than above method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element pairing in list

# using map() + concat

import operator

 

# initialize list 

test_list = ["G", "F", "G", "I", "S", "B",
"E", "S", "T"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Consecutive element pairing in list

# using map() + concat

res = list(map(operator.concat, test_list[:-1],
test_list[1:]))

 

# printing result

print("List after Consecutive concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [‘G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’]  
> List after Consecutive concatenation is : [‘GF’, ‘FG’, ‘GI’, ‘IS’, ‘SB’,
> ‘BE’, ‘ES’, ‘ST’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

