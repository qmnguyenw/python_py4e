Python – Convert Strings to Uppercase in Dictionary value lists



Given dictionary with values list, convert all the strings to upper case.

>  **Input** : {“Gfg” : [“ab”, “cd”], “Best” : [“gh”], “is” : [“kl”]}  
>  **Output** : {‘Gfg’: [‘AB’, ‘CD’], ‘Best’: [‘GH’], ‘is’: [‘KL’]}  
>  **Explanation** : All value lists strings are converted to upper case.
>
>  **Input** : {“Gfg” : [“ab”, “cd”, “Ef”]}  
>  **Output** : {‘Gfg’: [‘AB’, ‘CD’, “EF”]}  
>  **Explanation** : All value lists strings are converted to upper case,
> already upper case have no effect.

 **Method #1 : Using dictionary comprehension + upper() + list comprehension**

The combination of above functions can be used to solve this problem. In this,
we perform upper case using upper(), list comprehension is used to iterate
through all strings, dictionary comprehension is used to remake dictionary
with upper case values.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Strings to Uppercase in Dictionary value lists

# Using dictionary comprehension + upper() + list comprehension

 

# initializing dictionary

test_dict = {"Gfg" : ["ab", "cd", "ef"],

 "Best" : ["gh", "ij"], "is" : ["kl"]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using upper to convert to upper case 

res = {key: [ele.upper() for ele in test_dict[key] ] for key
in test_dict }

 

# printing result 

print("The dictionary after conversion " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [‘ab’, ‘cd’, ‘ef’], ‘Best’: [‘gh’,
> ‘ij’], ‘is’: [‘kl’]}  
> The dictionary after conversion {‘Gfg’: [‘AB’, ‘CD’, ‘EF’], ‘Best’: [‘GH’,
> ‘IJ’], ‘is’: [‘KL’]}

 **Method #2 : Using map() + upper() + dictionary comprehension**

The combination of above functions can be used to solve this problem. In this,
we perform the task of extending logic of upper case using map() instead of
list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Strings to Uppercase in Dictionary value lists

# Using map() + upper() + dictionary comprehension

 

# initializing dictionary

test_dict = {"Gfg" : ["ab", "cd", "ef"],

 "Best" : ["gh", "ij"], "is" : ["kl"]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using map() to extend logic to all inner list 

res = {key: list(map(str.upper, test_dict[key])) for key
in test_dict}

 

# printing result 

print("The dictionary after conversion " + str(res))   
  
---  
  
__

__

**Output**

> The original dictionary is : {‘Gfg’: [‘ab’, ‘cd’, ‘ef’], ‘Best’: [‘gh’,
> ‘ij’], ‘is’: [‘kl’]}  
> The dictionary after conversion {‘Gfg’: [‘AB’, ‘CD’, ‘EF’], ‘Best’: [‘GH’,
> ‘IJ’], ‘is’: [‘KL’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

