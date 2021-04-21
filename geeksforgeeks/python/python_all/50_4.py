Python – Test for Empty Dictionary Value List



Given a dictionary with list as values, check if all lists are empty.

>  **Input** : {“Gfg” : [], “Best” : []}  
>  **Output** : True  
>  **Explanation** : Both lists have no elements, hence True.
>
>  **Input** : {“Gfg” : [], “Best” : [4]}  
>  **Output** : False  
>  **Explanation** : “Best” contains element, Hence False.

 **Method #1 : Using any() + values()**

The combination of above functions can be used to solve this task. In this, we
check for any value present in values we extract using values(), if not found,
then list is empty.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Empty Dictionary Value List

# Using any() + values()

 

# initializing dictionary

test_dict = {"Gfg" : [], "Best" : [], "is" : []}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# checking if any value is found 

# using not to negate the result of any()

res = not any(test_dict.values())

 

# printing result 

print("Are value lists empty? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [], 'Best': [], 'is': []}
    Are value lists empty? : True
    

**Method #2 : Using all() + values()**

This is another way in which we can solve the problem. In this, we can check
for each key if all values are empty using all().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for Empty Dictionary Value List

# Using all() + values()

 

# initializing dictionary

test_dict = {"Gfg" : [], "Best" : [], "is" : []}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# checking if all keys have empty list 

res = all(ele == [] for ele in
list(test_dict.values()))

 

# printing result 

print("Are value lists empty? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [], 'Best': [], 'is': []}
    Are value lists empty? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

