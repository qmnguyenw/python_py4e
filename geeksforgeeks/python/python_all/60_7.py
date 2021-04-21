Python – Get all numbers combinations in list



Sometimes, while working with Python lists, we can have a problem in which we
need to concatenate each number with other create new number. This kind of
problem is peculiar but can have application in many domains such as day-day
programming and gaming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [7, 3, 4, 5]  
>  **Output** : [73, 74, 75, 34, 35, 45]
>
>  **Input** : test_list = [2, 5]  
>  **Output** : [25]

 **Method #1 : Using list comprehension +combination()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of finding all combination using combination() and
f-strings can be used to perform concatenation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All numbers combinations

# Using list comprehension + combinations

from itertools import combinations

 

# initializing list

test_list = [59, 236, 31, 38, 23]

 

# printing original list 

print("The original list : " + str(test_list))

 

# All numbers combinations

# Using list comprehension + combinations

res = [int(f"{x}{y}") for x, y in combinations(test_list,
2)]

 

# printing result 

print("All numbers combinations : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

> The original list : [59, 236, 31, 38, 23]  
> All numbers combinations : [59236, 5931, 5938, 5923, 23631, 23638, 23623,
> 3138, 3123, 3823]

