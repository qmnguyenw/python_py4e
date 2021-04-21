Python – Extract dictionary items with List elements



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract all the items from dictionary that constitute all the
elements from a list. This kind of problem can occur in domains such as
competitive programming and web development. Let’s discuss certain ways in
which this task can be performed.

>  **Input** : test_dict = {‘gfg’ : [4, 6, 10], ‘is’ : [12]}  
>  **Output** : {‘gfg’: [4, 6, 10]}
>
>  **Input** : test_dict = {‘gfg’ : [4, 6, 10]}  
>  **Output** : {‘gfg’: [4, 6, 10]}

 **Method #1 : Usingset() + dictionary comprehension + items()**  
The combination of above functionalities can be used to solve this problem. In
this, we first reduce the list elements to remove duplicate, extract
dictionary items using items() and construction of required dictionary happens
using dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract dictionary items with List elements

# Using set() + dictionary comprehension + items()

 

# helpr_fnc

def hlper_fnc(req_list, test_dict):

 temp = set(req_list)

 temp2 = { key: set(val) for key, val in test_dict.items()
}

 return { key: val for key, val in test_dict.items() if
temp2[key].issubset(temp)}

 

# initializing dictionary

test_dict = {'gfg' : [4, 6], 'is' : [10], 'best'
: [4, 5, 7]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing req_list 

req_list = [4, 6, 10]

 

# Extract dictionary items with List elements

# Using set() + dictionary comprehension + items()

res = hlper_fnc(req_list, test_dict)

 

# printing result 

print("The extracted dictionary: " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘is’: [10], ‘best’: [4, 5, 7], ‘gfg’: [4, 6]}  
> The extracted dictionary: {‘is’: [10], ‘gfg’: [4, 6]}

