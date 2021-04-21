Python Program that displays the key of list value with maximum range



Given a Dictionary with keys and values that are lists, the following program
displays key of the value whose range in maximum.

    
    
    Range = Maximum number-Minimum number
    

> **Input** : test_dict = {“Gfg” : [6, 2, 4, 1], “is” : [4, 7, 3, 3, 8],
> “Best” : [1, 0, 9, 3]}  
> **Output** : Best  
> **Explanation** : 9 – 0 = 9, Maximum range compared to all other list given
> as values  
>  **Input** : test_dict = {“Gfg” : [16, 2, 4, 1], “Best” : [1, 0, 9, 3]}  
> **Output** : Gfg  
> **Explanation** : 16 – 1 = 15, Maximum range compared to all other list
> given as values  
>

**Method 1 :** _ **** Using __max()_ _,_ _min()_ _and_ _loop_

In this, we get max() and min() of each list and perform difference to find
range. This value is then stored and max difference of all such values is
computed by applying max() at the result list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {"Gfg" : [6, 2, 4, 1], "is" : [4,
7, 3, 3, 8], "Best" : [1, 0, 9, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

max_res = 0

for sub, vals in test_dict.items():

 

 # storing maximum of difference

 max_res = max(max_res, max(vals) - min(vals)) 

 if max_res == max(vals) - min(vals):

 res = sub

 

# printing result 

print("The maximum element key : " + str(res))   
  
---  
  
__

__

**Output:**

  

  

> The original dictionary is : {‘Gfg’: [6, 2, 4, 1], ‘is’: [4, 7, 3, 3, 8],
> ‘Best’: [1, 0, 9, 3]}
>
> The maximum element key : Best

 **Method 2 :** _Using_ _list comprehension_ _,_ _max()_ _and_ _min()_

In this, we compute the maximum range, and then extract the key which matches
that difference using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {"Gfg" : [6, 2, 4, 1], "is" : [4,
7, 3, 3, 8], "Best" : [1, 0, 9, 3]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# getting max value 

max_res = max([max(vals) - min(vals) for sub, vals in
test_dict.items()])

 

# getting key matching with maximum value 

res = [sub for sub in test_dict if max(test_dict[sub]) -
min(test_dict[sub]) == max_res][0]

 

# printing result 

print("The maximum element key : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: [6, 2, 4, 1], ‘is’: [4, 7, 3, 3, 8],
> ‘Best’: [1, 0, 9, 3]}
>
> The maximum element key : Best

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

