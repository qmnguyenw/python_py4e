Python | Initialize dictionary with multiple keys



Sometimes, while working with dictionaries, we might have a problem in which
we need to initialize the dictionary with more than one keys with same value.
This application requirement can be in domains of web development in which we
might want to declare and initialize at the same time. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingloop**  
We can have a loop which performs this particular task. But this just
partially solves our problem of multiple addition but the dictionary has to be
declared beforehand for this.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary with multiple keys

# Using loop

 

# declare dictionary

test_dict = {}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize keys 

test_keys = ['gfg', 'is', 'best']

 

# Using loop

# Initialize dictionary with multiple keys

for keys in test_keys:

 test_dict[keys] = 4

 

# printing result 

print("Dictionary after updating multiple key-value : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {}  
> Dictionary after updating multiple key-value : {‘is’: 4, ‘gfg’: 4, ‘best’:
> 4}

  

  

**Method #2 : Usingfromkeys()**  
This function is used to actually perform both task of multiple assignment and
declaration with a single statement. We also use * operator to pack the values
together into a dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary with multiple keys

# Using fromkeys()

 

# Initialize keys 

test_keys = ['gfg', 'is', 'best']

 

# Using fromkeys()

# Initialize dictionary with multiple keys

res ={ **dict.fromkeys(test_keys, 4)} 

 

# printing result 

print("Dictionary after Initializing multiple key-value : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> Dictionary after Initializing multiple key-value : {‘gfg’: 4, ‘is’: 4,
> ‘best’: 4}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

