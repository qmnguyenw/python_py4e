Python Program to calculate Dictionaries frequencies



Given a list of dictionaries, the task here is to write a python program to
extract dictionary frequencies of each dictionary.

>  **Input :** test_list = [{‘gfg’ : 1, ‘is’ : 4, ‘best’ : 9},
>
> {‘gfg’ : 6, ‘is’ : 3, ‘best’ : 8},
>
> {‘gfg’ : 1, ‘is’ : 4, ‘best’ : 9},
>
> {‘gfg’ : 1, ‘is’ : 1, ‘best’ : 9},
>
>  
>
>
>  
>
>
> {‘gfg’ : 6, ‘is’ : 3, ‘best’ : 8}]
>
>  **Output :** [({‘gfg’: 1, ‘is’: 4, ‘best’: 9}, 2), ({‘gfg’: 6, ‘is’: 3,
> ‘best’: 8}, 2), ({‘gfg’: 1, ‘is’: 1, ‘best’: 9}, 1)]
>
>  **Explanation :** Dictionaries with their frequency appended as result in
> list.
>
>  **Input :** test_list = [{‘gfg’ : 1, ‘is’ : 4, ‘best’ : 9},
>
> {‘gfg’ : 6, ‘is’ : 3, ‘best’ : 8},
>
> {‘gfg’ : 1, ‘is’ : 4, ‘best’ : 9},
>
> {‘gfg’ : 1, ‘is’ : 1, ‘best’ : 9}]
>
>  **Output :** [({‘gfg’: 1, ‘is’: 4, ‘best’: 9}, 2), ({‘gfg’: 6, ‘is’: 3,
> ‘best’: 8}, 1), ({‘gfg’: 1, ‘is’: 1, ‘best’: 9}, 1)]
>
>  
>
>
>  
>
>
>  **Explanation :** Dictionaries with their frequency appended as result in
> list.

 **Method 1 :** _Using_ _index()_ _and_ _loop_

In this, each dictionary is iterated and index() is used to get the index of
dictionary mapped with its increasing frequencies, and increment counter in
case of repeated dictionary.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [{'gfg': 1, 'is': 4, 'best': 9},

 {'gfg': 6, 'is': 3, 'best': 8},

 {'gfg': 1, 'is': 4, 'best': 9},

 {'gfg': 1, 'is': 1, 'best': 9},

 {'gfg': 6, 'is': 3, 'best': 8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub in test_list:

 

 flag = 0

 for ele in res:

 

 # checking for presence and incrementing frequency

 if sub == ele[0]:

 res[res.index(ele)] = (sub, ele[1] + 1)

 flag = 1

 

 if not flag:

 res.append((sub, 1))

 

# printing result

print("Dictionaries frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 1, ‘is’: 4, ‘best’: 9}, {‘gfg’: 6, ‘is’: 3,
> ‘best’: 8}, {‘gfg’: 1, ‘is’: 4, ‘best’: 9}, {‘gfg’: 1, ‘is’: 1, ‘best’: 9},
> {‘gfg’: 6, ‘is’: 3, ‘best’: 8}]
>
> Dictionaries frequencies : [({‘best’: 9, ‘gfg’: 1, ‘is’: 4}, 2), ({‘best’:
> 8, ‘gfg’: 6, ‘is’: 3}, 2), ({‘best’: 9, ‘gfg’: 1, ‘is’: 1}, 1)]

 **Method 2 :** _Using_ _Counter()_ _and_ _sorted()_

In this, dictionary elements are converted to tuple pairs and then Counter is
used to get frequency of each. At last step, each dictionary is reconverted to
its original form.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

# initializing list

test_list = [{'gfg': 1, 'is': 4, 'best': 9},

 {'gfg': 6, 'is': 3, 'best': 8},

 {'gfg': 1, 'is': 4, 'best': 9},

 {'gfg': 1, 'is': 1, 'best': 9},

 {'gfg': 6, 'is': 3, 'best': 8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting frequencies

temp = Counter(tuple(sorted(sub.items())) for sub in
test_list)

 

# converting back to Dictionaries

res = [(dict([tuple(ele) for ele in sub]), temp[sub])
for sub in temp]

 

# printing result

print("Dictionaries frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 1, ‘is’: 4, ‘best’: 9}, {‘gfg’: 6, ‘is’: 3,
> ‘best’: 8}, {‘gfg’: 1, ‘is’: 4, ‘best’: 9}, {‘gfg’: 1, ‘is’: 1, ‘best’: 9},
> {‘gfg’: 6, ‘is’: 3, ‘best’: 8}]
>
> Dictionaries frequencies : [({‘best’: 9, ‘gfg’: 1, ‘is’: 4}, 2), ({‘best’:
> 8, ‘gfg’: 6, ‘is’: 3}, 2), ({‘best’: 9, ‘gfg’: 1, ‘is’: 1}, 1)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

