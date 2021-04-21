Python Program to Re-assign a dictionary based on path relation



Given a dictionary, the task is to formulate a python program to re-assign it
using a path relation among its keys and values, i.e value of one key is key
to another.

**Example:**

>  **Input** : test_dict = {3 : 4, 5 : 6, 4 : 8, 6 : 9, 8 : 10}  
> **Output** : {3: 10, 5: 9, 4: 10, 6: 9, 8: 10}  
> **Explanation** : key 3 has value 4. key 4 has value 8. key 8 has value 10.
> there is no key 10 thus in the new dictionary key will have value 10.
>
> Similarly, key 5 has value 6. key 6 has value 9. There is no key 9 hence in
> the new dictionary key 5 will have value 9.

 **Approach:** _Using_ _loop_ _and_ _keys()_

  

  

In this, we iterate for each key and find its depth, by using external
function for repeated checking for each value being key of other item in
dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def find_depth(ele, dicti):

 

 # finding depth

 for idx in range(len(list(dicti.keys()))):

 

 # assigning value as key if found

 if ele in list(dicti.keys()):

 ele = dicti[ele]

 return ele

 

 

# initializing dictionary

test_dict = {3: 4, 5: 6, 4: 8, 6: 9,
8: 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = dict()

 

# iterating for each key

for key, val in list(test_dict.items()):

 test_dict.pop(key)

 res[key] = find_depth(val, test_dict)

 

# printing result

print("The reassigned dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {3: 4, 5: 6, 4: 8, 6: 9, 8: 10}
>
> The reassigned dictionary : {3: 10, 5: 9, 4: 10, 6: 9, 8: 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

