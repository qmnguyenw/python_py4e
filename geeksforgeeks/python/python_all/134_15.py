Python | Perform operation on each key dictionary



Sometimes, while working with dictionaries, we might come across a problem in
which we require to perform a particular operation on each value of keys. This
type of problem can occur in web development domain. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop**  
This is the naive method in which this task can be performed. In this we
simply run a loop to traverse each key in dictionary and perform the desired
operation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Perform operation on each key dictionary

# Using loop

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using loop

# Perform operation on each key dictionary

for key in test_dict: 

 test_dict[key] *= 3

 

# printing result 

print("The dictionary after triple each key's value : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 4, ‘gfg’: 6, ‘best’: 7}  
> The dictionary after triple each key’s value : {‘is’: 12, ‘gfg’: 18, ‘best’:
> 21}

  

  

**Method #2 : Usingupdate() \+ dictionary comprehension**  
An alternate one-liner to perform this task, the combination of above
functions can be used to perform this particular task. The update function
is used to perform the necessary operation over the dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Perform operation on each key dictionary

# Using update() + dictionary comprehension

 

# Initialize dictionary

test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using update() + dictionary comprehension

# Perform operation on each key dictionary

test_dict.update((x, y * 3) for x, y in test_dict.items())

 

# printing result 

print("The dictionary after triple each key's value : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘is’: 4, ‘gfg’: 6, ‘best’: 7}  
> The dictionary after triple each key’s value : {‘is’: 12, ‘gfg’: 18, ‘best’:
> 21}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

