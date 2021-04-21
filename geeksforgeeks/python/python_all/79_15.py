Python – Group Similar keys in dictionary



Sometimes while working with dictionary data, we can have problems in which we
need to perform grouping based on substring of keys and reform the data
grouped on similar keys. This can have application in data preprocessing. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which we perform this task. In this, we check for element
using conditional statement and insert the keys according to substring
presence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Similar keys in dictionary

# Using loop

 

# initializing Dictionary

test_dict = {'gfg1' : 1, 'is1' : 2, 'best1' : 3,


 'gfg2' : 9, 'is2' : 8, 'best2' : 7,

 'gfg3' : 10, 'is3' : 5, 'best3' : 6}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Group Similar keys in dictionary

# Using loop

res = []

res1, res2, res3 = {}, {}, {}

for key, value in test_dict.items():

 if 'gfg' in key:

 res1[key] = value

 elif 'is' in key:

 res2[key] = value

 elif 'best' in key:

 res3[key] = value

 

res.append(res1)

res.append(res2)

res.append(res3)

 

# printing result 

print("The grouped similar keys are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘best2’: 7, ‘best3’: 6, ‘is2’: 8, ‘is3’: 5,
> ‘best1’: 3, ‘gfg1’: 1, ‘gfg3’: 10, ‘is1’: 2, ‘gfg2’: 9}  
> The grouped similar keys are : [{‘gfg3’: 10, ‘gfg2’: 9, ‘gfg1’: 1}, {‘is2’:
> 8, ‘is3’: 5, ‘is1’: 2}, {‘best3’: 6, ‘best1’: 3, ‘best2’: 7}]

  

  

**Method #2 : Using dictionary comprehension**  
This is yet another way in which this task can be performed. In this, we group
the substring to keys using dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Similar keys in dictionary

# Using dictionary comprehension

 

# initializing Dictionary

test_dict = {'gfg1' : 1, 'is1' : 2, 'best1' : 3,


 'gfg2' : 9, 'is2' : 8, 'best2' : 7,

 'gfg3' : 10, 'is3' : 5, 'best3' : 6}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Group Similar keys in dictionary

# Using dictionary

res = []

res1 = {key : val for key, val in test_dict.items() if 'gfg'
in key}

res2 = {key : val for key, val in test_dict.items() if 'is'
in key}

res3 = {key : val for key, val in test_dict.items() if
'best' in key}

res.append(res1)

res.append(res2)

res.append(res3)

 

# printing result 

print("The grouped similar keys are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘best2’: 7, ‘best3’: 6, ‘is2’: 8, ‘is3’: 5,
> ‘best1’: 3, ‘gfg1’: 1, ‘gfg3’: 10, ‘is1’: 2, ‘gfg2’: 9}  
> The grouped similar keys are : [{‘gfg3’: 10, ‘gfg2’: 9, ‘gfg1’: 1}, {‘is2’:
> 8, ‘is3’: 5, ‘is1’: 2}, {‘best3’: 6, ‘best1’: 3, ‘best2’: 7}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

