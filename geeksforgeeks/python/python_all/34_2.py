Python program to change the value of a dictionary if it equals K



Given a dictionary, change the value if it is equal to K.

> **Input** : test_dict = {“Gfg”: 4, “is”: 8, “best”: 10, “for”: 8, “geeks”:
> 19}, K = 8, repl_val = 25  
> **Output** : {‘Gfg’: 4, ‘is’: 25, ‘best’: 10, ‘for’: 25, ‘geeks’: 19}  
> **Explanation** : All values with 8 converted to 25.
>
>  **Input** : test_dict = {“Gfg”: 6, “is”: 8, “best”: 10, “for”: 8, “geeks”:
> 19}, K = 6, repl_val = 25  
> **Output** : {‘Gfg’: 25, ‘is’: 8, ‘best’: 10, ‘for’: 8, ‘geeks’: 19}  
> **Explanation** : All values with 6 converted to 25.

**Method #1 : Using** a **loop**

This is a brute way in which this task can be performed. In this, we iterate
for all the keys and values of dictionaries, and if found a match, then the
required conversion is carried out.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Change value if value equals K in dictionary

# Using loop

 

# initializing dictionary

test_dict = {"Gfg": 4, "is": 8, "best": 10,
"for": 8, "geeks": 19}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 8

 

# initializing repl_val 

repl_val = 20

 

# iterating dictionary

for key, val in test_dict.items():

 

 # checking for required value

 if val == K:

 test_dict[key] = repl_val

 

# printing result 

print("The dictionary after values replacement : " +
str(test_dict))  
  
---  
  
 __

 __

 **Output**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 8, ‘best’: 10, ‘for’: 8,
> ‘geeks’: 19}  
> The dictionary after values replacement : {‘Gfg’: 4, ‘is’: 20, ‘best’: 10,
> ‘for’: 20, ‘geeks’: 19}

 **Method #2 : Using dictionary comprehension**

This is a one-liner alternative to solve this problem. In this, we iterate and
assign creating a new dictionary rather than doing in-place replacement as in
the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Change value if value equals K in dictionary

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {"Gfg": 4, "is": 8, "best": 10,
"for": 8, "geeks": 19}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 8

 

# initializing repl_val 

repl_val = 20

 

# one-liner to solve for dictionary

res = {key : repl_val if val == K else val for key, val
in test_dict.items()}

 

# printing result 

print("The dictionary after values replacement : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 8, ‘best’: 10, ‘for’: 8,
> ‘geeks’: 19}  
> The dictionary after values replacement : {‘Gfg’: 4, ‘is’: 20, ‘best’: 10,
> ‘for’: 20, ‘geeks’: 19}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

