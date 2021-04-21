Python – Convert list of dictionaries to Dictionary Value list



Given a list of dictionary, convert to dictionary with same key mapped with
all values in as value list.

>  **Input** : test_list = [{“Gfg” : 6, “is” : 9, “best” : 10},  
> {“Gfg” : 8, “is” : 11, “best” : 19}]  
>  **Output** : {‘Gfg’: [6, 8], ‘is’: [9, 11], ‘best’: [10, 19]}  
>  **Explanation** : 6, 8 of “Gfg” mapped as value list, similarly every
> other.
>
>  **Input** : test_list = [{“Gfg” : 6, “best” : 10},  
> {“Gfg” : 8, “best” : 19}]  
>  **Output** : {‘Gfg’: [6, 8], ‘best’: [10, 19]}  
>  **Explanation** : Same as above, conversion.

 **Method #1 : Using loop**

This is brute way to solve this problem. In this, we iterate through all the
dictionaries, and extract each key and convert to required dictionary in
nested loops.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list of dictionaries to Dictionary Value list

# Using loop

from collections import defaultdict

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop to get dictionaries

# defaultdict used to make default empty list 

# for each key

res = defaultdict(list)

for sub in test_list:

 for key in sub:

 res[key].append(sub[key])

 

# printing result 

print("The extracted dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 6, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 2, 'is': 16, 'best': 10}, {'Gfg': 12, 'is': 1, 'best': 8}, {'Gfg': 22, 'is': 6, 'best': 8}]
    The extracted dictionary : {'Gfg': [6, 8, 2, 12, 22], 'is': [9, 11, 16, 1, 6], 'best': [10, 19, 10, 8, 8]}
    

**Method #2 : Using list comprehension + dictionary comprehension**

The combination of above functionalities can be used to solve this problem. In
this, we use dictionary comprehension to construct dictionary and list
comprehension is used to extract values from original list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list of dictionaries to Dictionary Value list

# Using list comprehension + dictionary comprehension

from collections import defaultdict

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

# dictionary and list comprehension 

# for shorthand to solution of problem

res = defaultdict(list)

{res[key].append(sub[key]) for sub in test_list for key in
sub} 

 

# printing result 

print("The extracted dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 6, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 2, 'is': 16, 'best': 10}, {'Gfg': 12, 'is': 1, 'best': 8}, {'Gfg': 22, 'is': 6, 'best': 8}]
    The extracted dictionary : {'Gfg': [6, 8, 2, 12, 22], 'is': [9, 11, 16, 1, 6], 'best': [10, 19, 10, 8, 8]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

