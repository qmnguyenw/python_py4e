Python – Remove K value items from dictionary nesting



Given dictionary with multiple nestings, remove all the keys with value K.

>  **Input** : [{“Gfg” : {“a” : 5, “b” : 8, “c” : 9}}, {“is” : {“j” : 8, “k” :
> 10}}, {“Best” : {“i” : 16}}], K = 8  
>  **Output** : [{‘a’: 5}, {‘c’: 9}, {‘k’: 10}, {‘i’: 16}]  
>  **Explanation** : All the keys with value 8, (“b”, “j”) has been removed.
>
>  **Input** : [{“Gfg” : {“a” : 5, “b” : 8, “c” : 9}}, {“is” : {“j” : 8, “k” :
> 10}}, {“Best” : {“i” : 16}}], K = 5  
>  **Output** : [{‘c’: 9}, {‘k’: 10}, {‘i’: 16}, {“j” : 8}, {“b” : 8}]  
>  **Explanation** : “a” with 5 as value removed.

 **Method #1 : Using loop + dictionary comprehension**

The combination of above functions can be used to solve this problem. In this,
we iterate for all the nesting keys using loop. and remove values. This
approach is for single level nesting of dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K value items from dictionary nestings

# Using dictionary comprehension + loop

 

# initializing list

test_list = [{"Gfg" : {"a" : 5, "b" : 8, "c" :
9}},

 {"is" : {"f" : 8, "j" : 8, "k" : 10}},

 {"Best" : {"i" : 16}}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 8

 

res = list()

 

for sub in test_list:

 for key, val in sub.items():

 

 # iterating for 1st nesting only

 for key1, val1 in val.items():

 if val1 != K:

 res.append({key1 : val1})

 

# printing result 

print("The dictionary after value removal : " + str(res))   
  
---  
  
__

__

**Output**

> The original list is : [{‘Gfg’: {‘a’: 5, ‘b’: 8, ‘c’: 9}}, {‘is’: {‘f’: 8,
> ‘j’: 8, ‘k’: 10}}, {‘Best’: {‘i’: 16}}]  
> The dictionary after value removal : [{‘a’: 5}, {‘c’: 9}, {‘k’: 10}, {‘i’:
> 16}]

 **Method #2 : Using recursion + loop (For multiple nesting)**

This is yet another way in which this task can be performed. In this we solve
a more generic problem of catering to inner dictionary elements as well using
recursion.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K value items from dictionary nestings

# Using recursion + loop (For multiple nesting)

 

res = []

 

# helper function to solve problem

def hlper_fnc(test_dict):

 for key in test_dict:

 if type(test_dict[key]) == dict:

 hlper_fnc(test_dict[key])

 else:

 if test_dict[key] != K:

 res.append({key : test_dict[key]})

 

# initializing dictionary

test_dict = {"Gfg" : {"a" : 5, "b" : 8, "c" :
9},

 "is" : {"f" : 8, "l" : { "j" : 8, "k" :
10}},

 "Best" : {"i" : {"k" : { "o" : 8}}}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 8

 

# computing result

hlper_fnc(test_dict)

 

# printing result 

print("The dictionary after value removal : " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: {‘a’: 5, ‘b’: 8, ‘c’: 9}, ‘is’: {‘f’:
> 8, ‘l’: {‘j’: 8, ‘k’: 10}}, ‘Best’: {‘i’: {‘k’: {‘o’: 8}}}}  
> The dictionary after value removal : [{‘a’: 5}, {‘c’: 9}, {‘k’: 10}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

