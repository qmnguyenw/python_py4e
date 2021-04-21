Python | Check if key has Non-None value in dictionary



Sometimes, while working with Python dictionaries, we might come across a
problem in which we need to find if a particular key of dictionary is valid
i.e it is not False or has a non None value. This kind of problem can occur in
Machine Learning domain. Let’s discuss certain ways in which this problem can
be solved.

 **Method #1 : Using if**  
This task can simply be solved using the conditional operator "if". The if
statement autochecks for the truthness of any statement and hence with the
key’s value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if key has Non-None value in dictionary

# Using if

 

# Initialize dictionary

test_dict = {'gfg' : None, 'is' : 4, 'for' : 2,
'CS' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using if

# Check if key has Non-None value in dictionary

res = False

if test_dict['gfg']:

 res = True

 

# printing result 

print("Does gfg have a Non-None value? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘gfg’: None, ‘is’: 4, ‘for’: 2, ‘CS’: 10}  
> Does gfg have a Non-None value? : False

  

  

**Method #2 : Usingbool() + get()**  
The above functions together can be used to perform this particular task. The
get performs the task of getting the value corresponding a key and bool
function checks for truthfulness.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if key has Non-None value in dictionary

# Using bool() + get()

 

# Initialize dictionary

test_dict = {'gfg' : None, 'is' : 4, 'for' : 2,
'CS' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using bool() + get()

# Check if key has Non-None value in dictionary

res = bool(test_dict.get('gfg'))

 

# printing result 

print("Does gfg have a Non-None value? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘gfg’: None, ‘is’: 4, ‘for’: 2, ‘CS’: 10}  
> Does gfg have a Non-None value? : False

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

