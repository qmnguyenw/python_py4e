Python – All Possible unique K size combinations till N



Sometimes, while working with Python domain, we can have a problem in which we
need to produce various combination of elements. This can be K sized unique
combinations till N. This problem can have application in data domains and
school programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : N = 2, K = 3  
>  **Output** : [(0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1)]
>
>  **Input** : N = 4, K = 2  
>  **Output** : [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2,
> 2), (2, 3), (3, 3)]

 **Method #1 : Usingproduct() + setdefault() \+ loop**  
The combination of above functions offers an approach to this problem. In
this, we use product to perform all combinations and eliminate duplicates
using setdefault() and loop by brute force approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All Possible unique K size combinations till N

# Using product() + setdefault() + loop

from itertools import product

 

# initializing N

N = 4

 

# Initialize K

K = 3

 

# All Possible unique K size combinations till N

# Using product() + setdefault() + loop

temp = list(product(range(N), repeat = K))

res = {}

for tup in temp:

 key = tuple(sorted(tup))

 res.setdefault(key, []).append(tup)

res = list(res.keys())

 

# printing result 

print("The unique combinations : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The unique combinations : [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0,
> 1, 1), (0, 1, 2), (0, 1, 3), (0, 2, 2), (0, 2, 3), (0, 3, 3), (1, 1, 1), (1,
> 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2,
> 3, 3), (3, 3, 3)]

