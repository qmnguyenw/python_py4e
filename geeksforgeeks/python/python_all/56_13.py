Python – Extract digits from Tuple list



Sometimes, while working with Python lists, we can have a problem in which we
need to perform extraction of all the digits from tuple list. This kind of
problem can find its application in data domains and day-day programming.
Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(15, 3), (3, 9)]  
>  **Output** : [9, 5, 3, 1]
>
>  **Input** : test_list = [(15, 3)]  
>  **Output** : [5, 3, 1]

 **Method #1 : Usingmap() + chain.from_iterable() + set() + loop**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of flattening list using chain.from_iterable(), and then
the digits are extracted using brute method. set() is used to remove duplicate
digits.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract digits from Tuple list

# Using map() + chain.from_iterable() + set() + loop

from itertools import chain

 

# initializing list

test_list = [(15, 3), (3, 9), (1, 10), (99,
2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Extract digits from Tuple list

# Using map() + chain.from_iterable() + set() + loop

temp = map(lambda ele: str(ele),
chain.from_iterable(test_list))

res = set()

for sub in temp:

 for ele in sub:

 res.add(ele)

 

# printing result 

print("The extrated digits : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(15, 3), (3, 9), (1, 10), (99, 2)]
    The extrated digits : {'0', '5', '3', '1', '2', '9'}
    

