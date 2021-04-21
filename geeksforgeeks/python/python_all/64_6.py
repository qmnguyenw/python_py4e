Python – Group Records on Similar index elements



Sometimes, while working with Python records, we can have a problem in which
we need to perform grouping of particular index of tuple, on basis of
similarity of rest of indices. This type of problems can have possible
application in Web development domain. Let’s discuss certain ways in which
this task can be performed.

>  **Input** : test_list = [(4, 5, 10), (4, 5, 7), (4, 5, 12)]  
>  **Output** : ((4, 5, [10, 7, 12]), )
>
>  **Input** : test_list = [(4, 5, 10)]  
>  **Output** : [(4, 5, [10])]

 **Method #1 : Usingdefaultdict() \+ loop**  
The combination of above functions offer a brute approach to solve this
problem. In this, we group elements and club into one using defaultdict() on
basis of equality of rest of elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Records on Similar index elements

# Using defaultdict() + loop

from collections import defaultdict

 

# initializing list

test_list = [(4, 7, 13), (4, 5, 7), (6,
7, 10), (4, 5, 15), (6, 7, 12)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Group Records on Similar index elements

# Using defaultdict() + loop

temp = defaultdict(list)

for a, b, c in test_list:

 temp[a, b].append(c)

res = tuple((*key, val) for key, val in temp.items())

 

# printing result 

print("Tuples after grouping : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(4, 7, 13), (4, 5, 7), (6, 7, 10), (4, 5, 15), (6, 7, 12)]
    Tuples after grouping : ((4, 7, [13]), (4, 5, [7, 15]), (6, 7, [10, 12]))
    

