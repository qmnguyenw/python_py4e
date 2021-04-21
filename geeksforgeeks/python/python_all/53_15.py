Python – Replace dictionary value from other dictionary



Given two dictionaries, update the values from other dictionary if key is
present in other dictionary.

>  **Input** : test_dict = {“Gfg” : 5, “is” : 8, “Best” : 10, “for” : 8,
> “Geeks” : 9},  
> updict = {“Geeks” : 10, “Best” : 17}  
>  **Output** : {‘Gfg’: 5, ‘is’: 8, ‘Best’: 17, ‘for’: 8, ‘Geeks’: 10}  
>  **Explanation** : “Geeks” and “Best” values updated to 10 and 17.
>
>  **Input** : test_dict = {“Gfg” : 5, “is” : 8, “Best” : 10, “for” : 8,
> “Geeks” : 9},  
> updict = {“Geek” : 10, “Bet” : 17}  
>  **Output** : {‘Gfg’: 5, ‘is’: 8, ‘Best’: 10, ‘for’: 8, ‘Geeks’: 9}  
>  **Explanation** : No values matched, hence original dictionary.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we run a loop
for each key in target dictionary and update in case the value is present in
other dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace dictionary value from other dictionary

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10,
"for" : 8, "Geeks" : 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing updict

updict = {"Gfg" : 10, "Best" : 17}

 

for sub in test_dict:

 

 # checking if key present in other dictionary

 if sub in updict:

 test_dict[sub] = updict[sub]

 

# printing result 

print("The updated dictionary: " + str(test_dict))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: 5, ‘is’: 8, ‘Best’: 10, ‘for’: 8,
> ‘Geeks’: 9}  
> The updated dictionary: {‘Gfg’: 10, ‘is’: 8, ‘Best’: 17, ‘for’: 8, ‘Geeks’:
> 9}

 **Method #2 : Using dictionary comprehension**

This is one liner approach in which this task can be performed. In this, we
iterate for all the dictionary values and update in a one-liner manner in
dictionary comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace dictionary value from other dictionary

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10,
"for" : 8, "Geeks" : 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing updict

updict = {"Gfg" : 10, "Best" : 17}

 

res = {key: updict.get(key, test_dict[key]) for key in
test_dict}

 

# printing result 

print("The updated dictionary: " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: 5, ‘is’: 8, ‘Best’: 10, ‘for’: 8,
> ‘Geeks’: 9}  
> The updated dictionary: {‘Gfg’: 10, ‘is’: 8, ‘Best’: 17, ‘for’: 8, ‘Geeks’:
> 9}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

