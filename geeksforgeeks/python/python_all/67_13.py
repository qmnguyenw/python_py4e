Python – Convert dictionary items to values



Sometimes, while working with Python dictionary, we can have a problem in
which we need to convert all the items of dictionary to a separate value
dictionary. This problem can occur in applications in which we receive
dictionary in which both keys and values need to be mapped as separate values.
Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_dict = {‘Gfg’: 1}  
>  **Output** : [{‘key’: ‘Gfg’, ‘value’: 1}]
>
>  **Input** : test_dict = {‘Gfg’: 1, ‘best’: 5}  
>  **Output** : [{‘key’: ‘Gfg’, ‘value’: 1}, {‘key’: ‘best’, ‘value’: 5}]

 **Method #1 : Using loop**  
This is brute force way to solve this problem. In this, we need to run a loop
to assign each item of dictionary a different value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert dictionary items to values

# Using loop

 

# initializing dictionary

test_dict = {'Gfg': 1, 'is': 2, 'best': 3}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Convert dictionary items to values

# Using loop

res = []

for key, val in test_dict.items():

 res.append({"key": key, "value": val})

 

# printing result 

print("Converted Dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘Gfg’: 1, ‘is’: 2, ‘best’: 3}  
> Converted Dictionary : [{‘key’: ‘Gfg’, ‘value’: 1}, {‘key’: ‘is’, ‘value’:
> 2}, {‘key’: ‘best’, ‘value’: 3}]

