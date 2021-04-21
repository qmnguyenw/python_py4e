Python – Remove duplicate values in dictionary



Sometimes, while working with Python dictionaries, we can have problem in
which we need to perform the removal of all the duplicate values of
dictionary, and we are not concerned if any key get removed in the process.
This kind of application can occur in school programming and day-day
programming. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is the brute force way in which we perform this task. In this, we keep
track of occurred value, and remove it if it repeats.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicate values in dictionary

# Using loop

 

# initializing dictionary

test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20,
'for' : 10, 'geeks' : 20}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove duplicate values in dictionary

# Using loop

temp = []

res = dict()

for key, val in test_dict.items():

 if val not in temp:

 temp.append(val)

 res[key] = val

 

# printing result 

print("The dictionary after values removal : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: 10, ‘for’: 10, ‘geeks’: 20, ‘is’: 15,
> ‘best’: 20}  
> The dictionary after values removal : {‘gfg’: 10, ‘geeks’: 20, ‘is’: 15}

  

  

**Method #2 : Using dictionary comprehension**  
The following problem can also be performed using dictionary comprehension. In
this, we perform task in similar way as above method, just as a shorthand.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicate values in dictionary

# Using dictionary comprehension

 

# initializing dictionary

test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20,
'for' : 10, 'geeks' : 20}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove duplicate values in dictionary

# Using dictionary comprehension

temp = {val : key for key, val in test_dict.items()}

res = {val : key for key, val in temp.items()}

 

# printing result 

print("The dictionary after values removal : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: 10, ‘for’: 10, ‘geeks’: 20, ‘is’: 15,
> ‘best’: 20}  
> The dictionary after values removal : {‘gfg’: 10, ‘geeks’: 20, ‘is’: 15}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

