Python – Synchronized Sorting of Keys



Sometimes, while working with Python Dictionaries, we can have a problem in
which we need to perform the sort of one key of dictionary and which to
perform similar changes to corresponding keys as well. This kind has
application in web development and competitive programming. Let’s discuss
certain way in which this task can be performed.

>  **Input** : test_dict = {“Gfg” : [3, 2, 1], ‘best’ : [17, 10, 20]},
> sort_key = “Gfg”  
>  **Output** : {‘Gfg’: [1, 2, 3], ‘best’: [20, 10, 17]}
>
>  **Input** : test_dict = {“Gfg” : [3, 1], ‘best’ : [10, 20], ‘CS’ : [12,
> 43]}, sort_key = “Gfg”  
>  **Output** : {‘Gfg’: [1, 3], ‘best’: [20, 10], ‘CS’: [43, 12]}

 **Method #1 : Using dictionary comprehension +sorted() \+ list
comprehension**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the sorting using sorted() and replication to other
dictionaries is done using dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Synchronized Sorting 

# Using dictionary comprehension + sorted() + list comprehension

 

# initializing dictionary

test_dict = {"Gfg" : [4, 6, 7, 3, 10], 

 'is' : [7, 5, 9, 10, 11],

 'best' : [1, 2, 10, 21, 12]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing sort key

sort_key = "Gfg"

 

# Synchronized Sorting 

# Using dictionary comprehension + sorted() + list comprehension

temp = [ele for ele, idx in
sorted(enumerate(test_dict[sort_key]),

 key = lambda x : x[1])]

 

res = {key : [val[idx] for idx in temp] for key, val in
test_dict.items()}

 

# printing result 

print("The Synchronized sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘best’: [1, 2, 10, 21, 12], ‘Gfg’: [4, 6, 7, 3,
> 10], ‘is’: [7, 5, 9, 10, 11]}  
> The Synchronized sorted dictionary : {‘best’: [21, 1, 2, 10, 12], ‘Gfg’: [3,
> 4, 6, 7, 10], ‘is’: [10, 7, 5, 9, 11]}

