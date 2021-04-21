Python | All possible permutations of N lists



Computing permutations is always a necessary task in many of the practical
applications and a concept widely used in Mathematics to achieve solutions to
many practical problems. Lets discuss certain ways in which one can perform
the task of getting all the permutations of N lists.

 **Method #1 : Using list comprehension**  
List comprehension can be used to convert the naive method task into a single
line, hence more compact. This method checks for each element available
elements and makes pairs accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to compute all possible permutations

# using list comprehension 

 

# initializing lists

list1 = [1, 3, 4]

list2 = [6, 7, 9]

list3 = [8, 10, 5]

 

# printing lists 

print ("The original lists are : " + str(list1) +

 " " + str(list2) +

 " " + str(list3))

 

# using list comprehension 

# to compute all possible permutations

res = [[i, j, k] for i in list1 

 for j in list2

 for k in list3]

 

# printing result

print ("All possible permutations are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original lists are : [1, 3, 4] [6, 7, 9] [8, 10, 5]  
> All possible permutations are : [[1, 6, 8], [1, 6, 10], [1, 6, 5], [1, 7,
> 8], [1, 7, 10], [1, 7, 5], [1, 9, 8], [1, 9, 10], [1, 9, 5], [3, 6, 8], [3,
> 6, 10], [3, 6, 5], [3, 7, 8], [3, 7, 10], [3, 7, 5], [3, 9, 8], [3, 9, 10],
> [3, 9, 5], [4, 6, 8], [4, 6, 10], [4, 6, 5], [4, 7, 8], [4, 7, 10], [4, 7,
> 5], [4, 9, 8], [4, 9, 10], [4, 9, 5]]

 **Method #2 : Usingitertools.product()**  
Using product function, one can easily perform this task in more pythonic and
concise manner. This is most recommended method to perform this task of
computing cartesian product.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to compute all possible permutations

# using itertools.product() 

import itertools

 

# initializing list of list 

all_list = [[1, 3, 4], [6, 7, 9], [8, 10,
5] ]

 

# printing lists 

print ("The original lists are : " + str(all_list))

 

# using itertools.product() 

# to compute all possible permutations

res = list(itertools.product(*all_list))

 

# printing result

print ("All possible permutations are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original lists are : [[1, 3, 4], [6, 7, 9], [8, 10, 5]]  
> All possible permutations are : [(1, 6, 8), (1, 6, 10), (1, 6, 5), (1, 7,
> 8), (1, 7, 10), (1, 7, 5), (1, 9, 8), (1, 9, 10), (1, 9, 5), (3, 6, 8), (3,
> 6, 10), (3, 6, 5), (3, 7, 8), (3, 7, 10), (3, 7, 5), (3, 9, 8), (3, 9, 10),
> (3, 9, 5), (4, 6, 8), (4, 6, 10), (4, 6, 5), (4, 7, 8), (4, 7, 10), (4, 7,
> 5), (4, 9, 8), (4, 9, 10), (4, 9, 5)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

