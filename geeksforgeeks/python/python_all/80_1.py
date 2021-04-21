Python – Extracting keys not in values



Sometimes, while working with Python dictionaries, we can have a problem in
which we require to get all the keys that do not occur in values lists. This
can have applications in the domains such as day-day programming. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Usingset() + values() + keys() \+ loop**  
This is brute way to approach this task. In this, we test for elements in
value lists, and keep adding them in separate list. Then we subtract this from
extracted keys using keys().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting keys not in values

# Using set() + keys() + values() + loop

 

# initializing Dictionary

test_dict = {3 : [1, 3, 4], 5 : [1, 2], 6
: [4, 3], 4 : [1, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extracting keys not in values

# Using set() + keys() + values() + loop

temp1 = set(test_dict.keys())

temp2 = set()

for ele in test_dict.values():

 temp2.update(ele)

res = list(temp1 - temp2)

 

# printing result 

print("The extracted keys are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {3: [1, 3, 4], 4: [1, 3], 5: [1, 2], 6: [4, 3]}  
> The extracted keys are : [5, 6]

  

  

**Method #2 : Using generator expression +set()**  
This method is similar to above method. The difference is that it is performed
as one liner way in compact format using generator expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting keys not in values

# Using generator expression + set()

 

# initializing Dictionary

test_dict = {3 : [1, 3, 4], 5 : [1, 2], 6
: [4, 3], 4 : [1, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extracting keys not in values

# Using generator expression + set()

res = list(set(test_dict) - set(ele for sub in
test_dict.values() for ele in sub))

 

# printing result 

print("The extracted keys are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {3: [1, 3, 4], 4: [1, 3], 5: [1, 2], 6: [4, 3]}  
> The extracted keys are : [5, 6]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

