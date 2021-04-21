Python – Values frequencies of key



Sometimes, while working with Python dictionary lists, one can have a problem
in which we require to find the frequency of all the values occurring in a
specific key in dictionary list. This can have application across many domains
including web development. Let’s discuss certain ways in which this task can
be performed.

>  **Input** : test_list = [{‘gfg’: [1]}, {‘good’: [5, 78, 10], ‘gfg’: [5, 6,
> 7, 8]}]  
>  **Output** : {8: 1, 1: 1, 5: 1, 6: 1, 7: 1}
>
>  **Input** : test_list = [{‘gfg’: [1, 5, 6, 7]}]  
>  **Output** : {1: 1, 5: 1, 6: 1, 7: 1}

 **Method #1 : UsingCounter() \+ list comprehension**  
The combination of above functionalities is used to solve this problem. In
this, we perform the task of finding frequency using Counter() and computation
is done using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values frequencies of key

# Using Counter() + list comprehension

from collections import Counter

 

# initializing list

test_list = [{'gfg' : [1, 5, 6, 7], 'is' :
[9, 6, 2, 10]},

 {'gfg' : [5, 6, 7, 8], 'good' : [5, 7,
10]},

 {'gfg' : [7, 5], 'best' : [5, 7]}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# frequency key 

freq_key = "gfg"

 

# Values frequencies of key

# Using Counter() + list comprehension

res = Counter([idx for val in test_list for idx in
val[freq_key]])

 

# printing result 

print("The frequency dictionary : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘gfg’: [1, 5, 6, 7], ‘is’: [9, 6, 2, 10]}, {‘gfg’:
> [5, 6, 7, 8], ‘good’: [5, 7, 10]}, {‘gfg’: [7, 5], ‘best’: [5, 7]}]
>
> The frequency dictionary : {8: 1, 1: 1, 5: 3, 6: 2, 7: 3}

