Python – Detect loop in Dictionaries



Sometimes, while working with Python dictionaries, we can have problem in
which we need to check if values of dictionaries don’t form a loop when they
are mapped through key of other dictionaries. This kind of problem can have
applications in many domains including competitive programming and brute
force.

>  **Input** : test_dict1 = {9 : [1, 5], 8 : [1, 4], 10 : [4, 2]}  
> test_dict2 = {2 : [1, 8]}  
>  **Output** : True
>
>  **Input** : test_dict1 = {15 : [1, 5]}  
> test_dict2 = {2 : [1, 10]}  
>  **Output** : False

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we iterate for
all the values of particular dictionary’s keys’ and map with values of similar
keys in dictionary keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Detect loop in Dictionaries

# Using loop

 

# initializing dictionaries

test_dict1 = {7 : [1, 2], 8 : [1, 4], 9 :
[4, 2]} 

test_dict2 = {2 : [1, 7], 10 : [1, 6], 11 :
[24, 20]} 

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Detect loop in Dictionaries

# Using loop

res = False

for idx1 in test_dict1.values():

 temp1 = (idx for idx in idx1 if idx in test_dict2)

 for idx in temp1:

 for idx2 in test_dict2[idx]:

 if idx2 in test_dict1:

 res = True

 

# printing result 

print("Does dictionaries contain loop : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary 1 is : {8: [1, 4], 9: [4, 2], 7: [1, 2]}
    The original dictionary 2 is : {2: [1, 7], 11: [24, 20], 10: [1, 6]}
    Does dictionaries contain loop : True
    

