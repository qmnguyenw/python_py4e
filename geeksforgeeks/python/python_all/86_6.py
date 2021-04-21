Python – Flatten Nested Dictionary to Matrix



Sometimes, while working with data, we can have a problem in which we need to
convert nested dictionary into Matrix, each nesting comprising of different
row in matrix. This can have applicaition in many data domains. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop + zip() + map()**  
The combination of above functions can be used to perform this task. In this,
we use brute force to flatten the dictionary keys and then use map() and zip()
to align them as rows of matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Nested Dictionary to Matrix

# using zip() + loop + map()

 

# initializing dictionary 

test_dict = {'Gfg1' : {'CS':1, 'GATE' : 2}, 

 'Gfg2' : {'CS':2, 'GATE' : 3},

 'Gfg3' : {'CS':4, 'GATE' : 5}} 

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# Flatten Nested Dictionary to Matrix

# using zip() + loop + map()

temp = list(test_dict.values())

sub = set()

for ele in temp:

 for idx in ele:

 sub.add(idx) 

res = []

res.append(sub)

for key, val in test_dict.items():

 temp2 = []

 for idx in sub:

 temp2.append(val.get(idx, 0))

 res.append(temp2)

 

res = [[idx for idx, val in test_dict.items()]] +
list(map(list, zip(*res)))

 

# printing result 

print("The Grouped dictionary list is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘Gfg3’: {‘GATE’: 5, ‘CS’: 4}, ‘Gfg1’: {‘GATE’:
> 2, ‘CS’: 1}, ‘Gfg2’: {‘GATE’: 3, ‘CS’: 2}}  
> The Grouped dictionary list is : [[‘Gfg3’, ‘Gfg1’, ‘Gfg2’], [‘GATE’, 5, 2,
> 3], [‘CS’, 4, 1, 2]]

  

  

**Method #2 : Usingunion() \+ list comprehension**  
The combination of above methods can be used to perform this task. In this, we
compute the union using union() rather than the nested loops. The result is
compiled using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Nested Dictionary to Matrix

# using union() + list comprehension

 

# initializing dictionary 

test_dict = {'Gfg1' : {'CS':1, 'GATE' : 2}, 

 'Gfg2' : {'CS':2, 'GATE' : 3},

 'Gfg3' : {'CS':4, 'GATE' : 5}} 

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# Flatten Nested Dictionary to Matrix

# using union() + list comprehension

temp = set().union(*test_dict.values())

res = [list(test_dict.keys())]

res += [[key] + [sub.get(key, 0) for sub in
test_dict.values()] for key in temp]

 

# printing result 

print("The Grouped dictionary list is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘Gfg3’: {‘GATE’: 5, ‘CS’: 4}, ‘Gfg1’: {‘GATE’:
> 2, ‘CS’: 1}, ‘Gfg2’: {‘GATE’: 3, ‘CS’: 2}}  
> The Grouped dictionary list is : [[‘Gfg3’, ‘Gfg1’, ‘Gfg2’], [‘GATE’, 5, 2,
> 3], [‘CS’, 4, 1, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

