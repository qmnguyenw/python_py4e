Python – Assign Reversed Values in Dictionary



Given a dictionary, assign each key, values after reverting the values of
dictionary.

>  **Input** : {1 : 4, 2 : 5, 3 : 6}  
>  **Output** : {1 : 6, 2 : 5, 3 : 4}  
>  **Explanation** : Value order changed, 4, 5, 6 to 6, 5, 4.
>
>  **Input** : {1 : 5, 2 : 5, 3 : 5}  
>  **Output** : {1 : 5, 2 : 5, 3 : 5}  
>  **Explanation** : Same values, no visible change.

 **Method #1 : Using values() + loop + reversed()**

This is one of the ways in which this task can be performed. In this, we
reverse all the values in dictionary using reversed() and reassign to keys.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign Reversed Values in Dictionary

# Using reversed() + loop + values()

 

# initializing dictionary

test_dict = {1 : "Gfg", 2 : "is", 3 : "Best"}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# extract values using values()

new_val = list(reversed(list(test_dict.values())))

 

# reassign new values

res = dict()

cnt = 0

for key in test_dict:

 res[key] = new_val[cnt]

 cnt += 1

 

# printing result 

print("Reassigned reverse values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {1: 'Gfg', 2: 'is', 3: 'Best'}
    Reassigned reverse values : {1: 'Best', 2: 'is', 3: 'Gfg'}
    

**Method #2 : Using dictionary comprehension + reversed() + values()**

The combination of above functions can be used to solve this problem. In this,
we perform the task of remaking reversed dictionary using dictionary
comprehension recipe for one-liner solution.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign Reversed Values in Dictionary

# Using dictionary comprehension + reversed() + values()

 

# initializing dictionary

test_dict = {1 : "Gfg", 2 : "is", 3 : "Best"}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# extract values using values()

new_val = list(reversed(list(test_dict.values())))

 

# one-liner dictionary comprehension approach

# enumerate for counter

res = {key : new_val[idx] for idx, key in
enumerate(list(test_dict.keys()))}

 

# printing result 

print("Reassigned reverse values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {1: 'Gfg', 2: 'is', 3: 'Best'}
    Reassigned reverse values : {1: 'Best', 2: 'is', 3: 'Gfg'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

