Python – Group Adjacent Coordinates



Sometimes, while working with Python lists, we can have a problem in which we
need to perform the grouping of all the coordinates which occur adjacent on a
matrix, i.e horizontally and vertically at distance 1. This is called
**Manhatten** distance. This kind of problem can occur in competitive
programming domain. Let’s discuss certain way in which this task can be
performed.

>  **Input** : test_list = [(4, 4), (6, 4), (7, 8)]  
>  **Output** : [[(7, 8)], [(6, 4)], [(4, 4)]]
>
>  **Input** : test_list = [(4, 4), (5, 4)]  
>  **Output** : [[(5, 4), (4, 4)]]

 **Method : Usingproduct() + groupby() \+ list comprehension**  
The combination of above methods can be used to solve this problem. In this,
we perform the task of grouping of elements using groupby() and check for
pairs using product(). The logic driving this solution is similar to union
find algorithm.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Adjacent Coordinates

# Using product() + groupby() + list comprehension

from itertools import groupby, product

 

def Manhattan(tup1, tup2):

 return abs(tup1[0] - tup2[0]) + abs(tup1[1] -
tup2[1])

 

# initializing list

test_list = [(4, 4), (6, 4), (7, 8), (11,
11), 

 (7, 7), (11, 12), (5, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Group Adjacent Coordinates

# Using product() + groupby() + list comprehension

man_tups = [sorted(sub) for sub in product(test_list, repeat
= 2)

 if Manhattan(*sub) == 1]

 

res_dict = {ele: {ele} for ele in test_list}

for tup1, tup2 in man_tups:

 res_dict[tup1] |= res_dict[tup2]

 res_dict[tup2] = res_dict[tup1]

 

res = [[*next(val)] for key, val in groupby(

 sorted(res_dict.values(), key = id), id)]

 

# printing result 

print("The grouped elemets : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 4), (6, 4), (7, 8), (11, 11), (7, 7), (11, 12), (5, 4)]
    The grouped elemets : [[(6, 4), (5, 4), (4, 4)], [(7, 8), (7, 7)], [(11, 12), (11, 11)]]
    

