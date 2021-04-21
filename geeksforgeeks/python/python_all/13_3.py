Python Program to display keys with same values in a dictionary List



Given a list with all dictionary elements, the task is to write a Python
program to extract keys having similar values across all dictionaries.

 **Examples:**

>  **Input** : test_list = [{“Gfg”: 5, “is” : 8, “best” : 0}, {“Gfg”: 5, “is”
> : 1, “best” : 0}, {“Gfg”: 5, “is” : 0, “best” : 0}]  
> **Output** : [‘Gfg’, ‘best’]  
> **Explanation** : All Gfg values are 5 and best has 0 as all its values in
> all dictionaries.
>
>  **Input** : test_list = [{“Gfg”: 5, “is” : 8, “best” : 1}, {“Gfg”: 5, “is”
> : 1, “best” : 0}, {“Gfg”: 5, “is” : 0, “best” : 0}]  
> **Output** : [‘Gfg’]  
> **Explanation** : All Gfg values are 5.  
>

**Method 1 :** _Using_ _keys()_ _and_ _loop_

  

  

In this, we iterate through all the elements in the list using loop and
extract keys using keys(). For each key, each dictionary’s key is compared, if
found similar, key is added to result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = [{"Gfg": 5, "is": 8, "best": 0},

 {"Gfg": 5, "is": 1, "best": 0},

 {"Gfg": 5, "is": 0, "best": 0}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting keys

keys = list(test_list[0].keys())

 

res = []

# iterating each dictionary for similar key's value

for key in keys:

 flag = 1

 for ele in test_list:

 

 # checking for similar values

 if test_list[0][key] != ele[key]:

 flag = 0

 break

 

 if flag:

 res.append(key)

 

# printing result

print("Similar values keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 5, ‘is’: 8, ‘best’: 0}, {‘Gfg’: 5, ‘is’: 1,
> ‘best’: 0}, {‘Gfg’: 5, ‘is’: 0, ‘best’: 0}]
>
> Similar values keys : [‘Gfg’, ‘best’]

 **Method 2 :** _Using_ _all()_ _,_ _loop_ _and_ _keys()_

In this, inner loop is avoided and replaced by all() which checks for all the
keys having similar values and then the key is extracted.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing Matrix

test_list = [{"Gfg": 5, "is": 8, "best": 0},

 {"Gfg": 5, "is": 1, "best": 0},

 {"Gfg": 5, "is": 0, "best": 0}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting keys

keys = list(test_list[0].keys())

 

res = []

 

# iterating each dictionary for similar key's value

for key in keys:

 

 # using all to check all keys with similar values

 flag = all(test_list[0][key] == ele[key] for ele in
test_list)

 

 if flag:

 res.append(key)

 

# printing result

print("Similar values keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 5, ‘is’: 8, ‘best’: 0}, {‘Gfg’: 5, ‘is’: 1,
> ‘best’: 0}, {‘Gfg’: 5, ‘is’: 0, ‘best’: 0}]
>
> Similar values keys : [‘Gfg’, ‘best’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

