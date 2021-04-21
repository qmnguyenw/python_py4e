Python program to Convert Matrix to List of dictionaries



Given a Matrix, convert it to a list of dictionaries by mapping similar index
values.

>  **Input** : test_list = [[“Gfg”, [1, 2, 3]], [“best”, [9, 10, 11]]]  
> **Output** : [{‘Gfg’: 1, ‘best’: 9}, {‘Gfg’: 2, ‘best’: 10}, {‘Gfg’: 3,
> ‘best’: 11}]
>
> **Input** : test_list = [[“Gfg”, [1, 2, 3]]]  
> **Output** : [{‘Gfg’: 1}, {‘Gfg’: 2}, {‘Gfg’: 3}]

The brute way in which this task can be performed is using a loop. In this, we
iterate for all the elements in Matrix, and update dictionaries binding keys
to appropriate values in dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [["Gfg", [1, 2, 3]],

 ["is", [6, 5, 4]], ["best", [9, 10, 11]]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop to bind Matrix elements to dictionary

res = []

for key, val in test_list:

 

 for idx, val in enumerate(val):

 

 # append values according to rows structure

 if len(res) - 1 < idx:

 res.append({key: val})

 

 else:

 res[idx].update({key: val})

 

# printing result

print("Converted dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list : [[‘Gfg’, [1, 2, 3]], [‘is’, [6, 5, 4]], [‘best’, [9, 10,
> 11]]]  
> Converted dictionary : [{‘Gfg’: 1, ‘is’: 6, ‘best’: 9}, {‘Gfg’: 2, ‘is’: 5,
> ‘best’: 10}, {‘Gfg’: 3, ‘is’: 4, ‘best’: 11}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

