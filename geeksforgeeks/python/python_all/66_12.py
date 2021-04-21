Python – Mutiple Keys Grouped Summation



Sometimes, while working with Python records, we can have a problem in which,
we need to perform elements grouping based on multiple key equality, and also
summation of the grouped result of particular key. This kind of problem can
occur in application in data domains. Let’s discuss certain way in which this
task can be performed.

>  **Input** :  
> test_list = [(12, ‘M’, ‘Gfg’), (23, ‘H’, ‘Gfg’), (13, ‘M’, ‘Best’)]  
> grp_indx = [1, 2] [ Indices to group ]  
> sum_idx = [0] [ Index to sum ]  
>  **Output** : [(‘M’, ‘Gfg’, 12), (‘H’, ‘Gfg’, 23), (‘M’, ‘Best’, 13)]
>
>  **Input** :  
> test_list = [(12, ‘M’, ‘Gfg’), (23, ‘M’, ‘Gfg’), (13, ‘M’, ‘Best’)]  
> grp_indx = [1, 2] [ Indices to group ]  
> sum_idx = [0] [ Index to sum ]  
>  **Output** : [(‘M’, ‘Gfg’, 35), (‘M’, ‘Best’, 13)]

 **Method : Using loop +defaultdict() \+ list comprehension**  
The combination of above functionalities can be used to solve this problem. In
this, we perform grouping using loop and the task of performing summation of
key is done using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mutiple Keys Grouped Summation

# Using loop + defaultdict() + list comprehension

from collections import defaultdict

 

# initializing list

test_list = [(12, 'M', 'Gfg'), (23, 'H', 'Gfg'),

 (13, 'M', 'Best'), (18, 'M', 'Gfg'),

 (2, 'H', 'Gfg'), (23, 'M', 'Best')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing grouping indices

grp_indx = [1, 2]

 

# initializing sum index 

sum_idx = [0]

 

# Mutiple Keys Grouped Summation

# Using loop + defaultdict() + list comprehension

temp = defaultdict(int)

for sub in test_list:

 temp[(sub[grp_indx[0]], sub[grp_indx[1]])] +=
sub[sum_idx[0]]

res = [key + (val, ) for key, val in temp.items()]

 

# printing result 

print("The grouped summation : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [(12, ‘M’, ‘Gfg’), (23, ‘H’, ‘Gfg’), (13, ‘M’,
> ‘Best’), (18, ‘M’, ‘Gfg’), (2, ‘H’, ‘Gfg’), (23, ‘M’, ‘Best’)]  
> The grouped summation : [(‘M’, ‘Gfg’, 30), (‘H’, ‘Gfg’, 25), (‘M’, ‘Best’,
> 36)]

