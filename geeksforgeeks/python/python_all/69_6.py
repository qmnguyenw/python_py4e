Python – Convert Value list elements to List records



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to convert the nested list values to individual records to
include another level of nesting to accommodate data. This kind of problem can
have applications in data domains such as web development and Machine
Learning. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_dict = {‘gfg’ : [4, 5], ‘best’ : [8, 10, 7, 9]}  
>  **Output** : {‘best’: [{8: []}, {10: []}, {7: []}, {9: []}], ‘gfg’: [{4:
> []}, {5: []}]}
>
>  **Input** : test_dict = {‘gfg’ : [7]}  
>  **Output** : {‘gfg’: [{7: []}]}

 **Method #1 : Using loop +enumerate()**  
The combination of above functions can be used to solve this problem. This is
brute force approach to this in which we iterate for all list and create
records list for each value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Value list elements to List records

# Using loop + enumerate()

 

# initializing dictionary

test_dict = {'gfg' : [4, 5], 'is' : [8], 'best' :
[10]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Convert Value list elements to List records

# Using loop + enumerate()

for ele in test_dict.values():

 for idx, val in enumerate(ele):

 ele[idx] = {val: []}

 

# printing result 

print("The converted dictionary is : " + str(test_dict))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘best’: [10], ‘is’: [8], ‘gfg’: [4, 5]}  
> The converted dictionary is : {‘best’: [{10: []}], ‘is’: [{8: []}], ‘gfg’:
> [{4: []}, {5: []}]}

