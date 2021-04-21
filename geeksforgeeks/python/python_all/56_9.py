Python – Maximum of Similar Keys in Tuples



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform maximum of all values of the equal keys in Tuple list. This
kind of application in useful in many domains such as web development and day-
day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [(4, 8), (4, 2), (4, 2), (4, 6)]  
>  **Output** : [(4, 18)]
>
>  **Input** : test_list = [(1, 8), (2, 2), (3, 6), (4, 2)]  
>  **Output** : [(1, 8), (2, 2), (3, 6), (4, 2)]

 **Method #1 : Usingmax() + groupby() \+ lambda + loop**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of grouping using groupby() and maximum is extrated using
max(), and result is compiled using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum of Similar Keys in Tuples

# Using max() + groupby() + lambda + loop

from itertools import groupby

 

# initializing lists

test_list = [(4, 8), (3, 2), (2, 2), (4,
6), (3, 7), (4, 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Maximum of Similar Keys in Tuples

# Using max() + groupby() + lambda + loop

test_list.sort(key = lambda sub: sub[0]) 

temp = groupby(test_list, lambda ele: ele[0])

res = []

for key, val in temp:

 res.append((key, sum([ele[1] for ele in val])))

 

# printing result 

print("Maximum grouped elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [(4, 8), (3, 2), (2, 2), (4, 6), (3, 7), (4, 5)]
    Maximum grouped elements : [(2, 2), (3, 7), (4, 8)]
    

