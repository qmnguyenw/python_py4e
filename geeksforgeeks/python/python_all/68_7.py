Python – Sort Dictionary key and values List



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform the sorting of it, wrt keys, but also can have a
variation in which we need to perform a sort on its values list as well. Let’s
discuss certain way in which this task can be performed.

>  **Input** : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]}  
>  **Output** : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]}
>
>  **Input** : test_dict = {‘c’: [10, 34, 3]}  
>  **Output** : {‘c’: [3, 10, 34]}

 **Method #1 : Usingsorted() \+ loop**  
The combination of above functions can be used to solve this problem. In this,
we initially sort all the values of keys, and then perform the keys sorting
after that, in brute manner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary key and values List

# Using loop + dictionary comprehension

 

# initializing dictionary

test_dict = {'gfg': [7, 6, 3], 

 'is': [2, 10, 3], 

 'best': [19, 4]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Sort Dictionary key and values List

# Using loop + dictionary comprehension

res = dict()

for key in sorted(test_dict):

 res[key] = sorted(test_dict[key])

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is : {‘gfg’: [7, 6, 3], ‘is’: [2, 10, 3], ‘best’:
> [19, 4]}  
> The sorted dictionary : {‘best’: [4, 19], ‘gfg’: [3, 6, 7], ‘is’: [2, 3,
> 10]}

