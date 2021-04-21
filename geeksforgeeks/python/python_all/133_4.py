Python | Merge Python key values to list



Sometimes, while working with Python, we might have a problem in which we need
to get the values of dictionary from several dictionaries to be encapsulated
into one dictionary. This type of problem can be common in domains in which we
work with relational data like in web developments. Let’s discuss certain ways
in which this problem can be solved.

 **Method #1 : Usingsetdefault() \+ loop**  
This task can be performed using a nested loop and fetching each element of
dictionary and creating a new list to new key or appending the values in case
of similar key occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge Python key values to list

# Using setdefault() + loop

 

# Initialize list

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6}, 

 {'it' : 5, 'is' : 7, 'best' : 8},

 {'CS' : 10}]

 

# Printing original list

print("The original list is : " + str(test_list))

 

# using setdefault() + loop

# Merge Python key values to list

res = {}

for sub in test_list:

 for key, val in sub.items(): 

 res.setdefault(key, []).append(val)

 

# printing result 

print("The merged values encapsulated dictionary is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [{‘is’: 4, ‘gfg’: 2, ‘best’: 6}, {‘it’: 5, ‘is’: 7,
> ‘best’: 8}, {‘CS’: 10}]  
> The merged values encapsulated dictionary is : {‘is’: [4, 7], ‘it’: [5],
> ‘gfg’: [2], ‘CS’: [10], ‘best’: [6, 8]}

  

  

**Method #2 : Using list comprehension + dictionary comprehension**  
The combination of above can be used to perform this particular task. This
offers a one liner that can be employed for this task. Even though it might be
efficient on performance domain.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge Python key values to list

# Using list comprehension + dictionary comprehension

 

# Initialize list

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6}, 

 {'it' : 5, 'is' : 7, 'best' : 8},

 {'CS' : 10}]

 

# Printing original list

print("The original list is : " + str(test_list))

 

# using list comprehension + dictionary comprehension

# Merge Python key values to list

res = {key: list({sub[key] for sub in test_list if key
in sub})

 for key in {key for sub in test_list for key in
sub}}

 

# printing result 

print("The merged values encapsulated dictionary is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [{‘is’: 4, ‘gfg’: 2, ‘best’: 6}, {‘it’: 5, ‘is’: 7,
> ‘best’: 8}, {‘CS’: 10}]  
> The merged values encapsulated dictionary is : {‘is’: [4, 7], ‘it’: [5],
> ‘gfg’: [2], ‘CS’: [10], ‘best’: [6, 8]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

