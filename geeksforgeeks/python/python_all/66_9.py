Python – Sort Records by Kth Index List



Sometimes, while working with Python Records, we can have a problem in which
we need to perform Sorting of Records by some element in Tuple, this can again
be somtimes, a list and sorting has to performed by Kth index of that list.
This is uncommon problem, but can have usecase in domains such as web
development. Let’s discuss certain way in which this task can be performed.

>  **Input** :  
> test_list = [([4, 5], ‘Gfg’), ([8, 4], ‘is’), ([2, 3], ‘best’)]  
> K = 0  
>  **Output** : [([2, 3], ‘best’), ([4, 5], ‘Gfg’), ([8, 4], ‘is’)]
>
>  **Input** :  
> test_list = [([4, 5], ‘Gfg’), ([8, 4], ‘is’), ([2, 3], ‘best’)]  
> K = 1  
>  **Output** : [([2, 3], ‘best’), ([8, 4], ‘is’), ([4, 5], ‘Gfg’)]

 **Method : Usingsort() \+ lambda**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of sorting using sort, the parameter and index by which
sorting has to be performed is provided using lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Records by Kth Index List

# Using sort() + lambda

 

# initializing list

test_list = [([4, 5, 7, 3], 'Gfg'), ([8, 6,
3, 1], 'is'),

 ([2, 3, 5, 2], 'best')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# Sort Records by Kth Index List

# Using sort() + lambda

test_list.sort(key = lambda sub: sub[0][K])

 

# printing result 

print("The records after sorting : " + str(test_list))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [([4, 5, 7, 3], ‘Gfg’), ([8, 6, 3, 1], ‘is’), ([2, 3,
> 5, 2], ‘best’)]  
> The records after sorting : [([2, 3, 5, 2], ‘best’), ([4, 5, 7, 3], ‘Gfg’),
> ([8, 6, 3, 1], ‘is’)]

