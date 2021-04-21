Python – Leaf and Non-Leaf Nodes Dictionary



Sometimes, while working with Python, we can have a problem in which we need
to work with Graph data represented in form of a Dictionary. In this, we may
need to check for all the leaf and non-lead nodes. This kind of problem has
direct applications in algorithms of Machine Learning. Let’s discuss a way in
which this task can be performed.  

> **Input** : test_dict = {‘Gfg’: {‘is’: 2, ‘best’: 1}}  
> **Output** : {‘leaf’: 2, ‘non-leaf’: 1}  
>  **Input** : test_dict = {‘Gfg’: {‘best’: 2}}  
> **Output** : {‘non-leaf’: 1, ‘leaf’: 1}  
>

**Method : Using recursion + isinstance() + loop**  
The combination of the above functionalities can be used to solve this
problem. In this, we recur for the inner nesting using recursion and check for
leaves or non-leaves by value types using isinstance().  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Leaf and Non-Leaf Nodes Dictionary

# Using recursion + isinstance() + loop

def hlpr_fnc(dict1, res = {'non-leaf':0, 'leaf':0}):

 

 #res['non-leaf'] += 1 

 nodes = dict1.keys()

 for node in nodes:

 subnode = dict1[node]

 if isinstance(subnode, dict):

 res['non-leaf'] += 1

 hlpr_fnc(subnode, res)

 else:

 res['leaf'] += 1

 return res

# initializing dictionary

test_dict = {'a': {'b': 1, 'c': {'d': {'e':
2, 'f': 1}}, 'g': {'h': {'i': 2, 'j':
1}}}}

# printing original dictionary

print("The original dictionary : " + str(test_dict))

# Leaf and Non-Leaf Nodes Dictionary

# Using recursion + isinstance() + loop

res = hlpr_fnc(test_dict)

 

# printing result

print("The leaf and Non-Leaf nodes : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original dictionary : {'a': {'b': 1, 'c': {'d': {'e': 2, 'f': 1}}, 'g': {'h': {'i': 2, 'j': 1}}}}
    The leaf and Non-Leaf nodes : {'non-leaf': 5, 'leaf': 5}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

