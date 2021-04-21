Python – Convert Values into proportions



Sometimes, while working with Python dictionaries, we can have problem in
which we need to convert the values into proportions with respect to total.
This can have applications in Data Science and Machine Learning domain. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingsum() \+ loop**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of finding sum using sum(). And the task of division
is done inside a loop using division with sum of each value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Values into proportions

# Using sum() + loop

 

# initializing dictionary

test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20
}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Values into proportions

# Using sum() + loop

temp = sum(test_dict.values())

for key, val in test_dict.items():

 test_dict[key] = val / temp

 

# printing result 

print("The proportions divided values : " + str(test_dict))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: 15, ‘best’: 20, ‘gfg’: 10}  
> The proportions divided values : {‘is’: 0.3333333333333333, ‘best’:
> 0.4444444444444444, ‘gfg’: 0.2222222222222222}

  

  

**Method #2 : Using dictionary comprehension +sum()**  
The combination of above functions can be used to perform this task. In this,
we calculate sum in similar manner as above method, and dictionary
comprehension is used to perform the task of looping in one liner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Values into proportions

# Using dictionary comprehension + sum()

 

# initializing dictionary

test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20
}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Values into proportions

# Using dictionary comprehension + sum()

temp = sum(test_dict.values())

res = {key: val / temp for key, val in test_dict.items()}

 

# printing result 

print("The proportions divided values : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: 15, ‘best’: 20, ‘gfg’: 10}  
> The proportions divided values : {‘is’: 0.3333333333333333, ‘best’:
> 0.4444444444444444, ‘gfg’: 0.2222222222222222}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

