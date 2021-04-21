Python – Append Similar Values as Key



Sometimes, while working with data, we can have problems in which we need to
categorize a particular list and values to similar keys. This can be problem
in counting data. Like counting votes or counting coins. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we run a loop
to add values to dictionary value list, if not present we dynamically create
key and perform append.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Similar Values as Key

# Using loop

 

# initializing list

test_list = ['Manjeet', 'Nikhil', 'Akshat', 'Akash', 

 'Manjeet', 'Akash', 'Akshat', 'Manjeet']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Append Similar Values as Key

# Using loop

res = dict()

for ele in test_list:

 try:

 res[ele].append(ele)

 except KeyError:

 res[ele] = [ele]

 

# printing result 

print("The similar values dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [‘Manjeet’, ‘Nikhil’, ‘Akshat’, ‘Akash’, ‘Manjeet’,
> ‘Akash’, ‘Akshat’, ‘Manjeet’]  
> The similar values dictionary is : {‘Nikhil’: [‘Nikhil’], ‘Manjeet’:
> [‘Manjeet’, ‘Manjeet’, ‘Manjeet’], ‘Akash’: [‘Akash’, ‘Akash’], ‘Akshat’:
> [‘Akshat’, ‘Akshat’]}

  

  

**Method #2 : Usingdefaultdict() \+ loop**  
The combination of above functions can be used to solve this problem. In this,
we pre initialize the dictionary using defaultdict().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append Similar Values as Key

# Using defaultdict() + loop

from collections import defaultdict

 

# initializing list

test_list = ['Manjeet', 'Nikhil', 'Akshat', 'Akash', 

 'Manjeet', 'Akash', 'Akshat', 'Manjeet']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Append Similar Values as Key

# Using defaultdict() + loop

res = defaultdict(list)

for sub in test_list:

 res[sub].append(sub)

 

# printing result 

print("The similar values dictionary is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list is : [‘Manjeet’, ‘Nikhil’, ‘Akshat’, ‘Akash’, ‘Manjeet’,
> ‘Akash’, ‘Akshat’, ‘Manjeet’]  
> The similar values dictionary is : {‘Nikhil’: [‘Nikhil’], ‘Manjeet’:
> [‘Manjeet’, ‘Manjeet’, ‘Manjeet’], ‘Akash’: [‘Akash’, ‘Akash’], ‘Akshat’:
> [‘Akshat’, ‘Akshat’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

