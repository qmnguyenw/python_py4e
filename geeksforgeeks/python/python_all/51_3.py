Python – Multiplication across Like Keys Value list elements



Given two dictionaries with value lists, perform element wise like keys
multiplication.

>  **Input** : test_dict1 = {“Gfg” : [4, 6], “Best” : [8, 6], “is” : [9, 3]},  
> test_dict2 = {“Gfg”: [8, 4], “Best” : [6, 3], “is” : [9, 8]}  
>  **Output** : {‘Gfg’: [32, 24], ‘Best’: [48, 18], ‘is’: [81, 24]}  
>  **Explanation** : 4 * 8 = 32, 6 * 4 = 24 and so on, hence new list value.
>
>  **Input** : test_dict1 = {“Gfg” : [4, 6], “Best” : [8, 6]},  
> test_dict2 = {“Gfg”: [8, 4], “Best” : [6, 3]}  
>  **Output** : {‘Gfg’: [32, 24], ‘Best’: [48, 18]}  
>  **Explanation** : 4 * 8 = 32, 6 * 4 = 24 and so on, hence new list value.

 **Method : Using dictionary comprehension + zip()**

This is one of the ways in which this task can be performed. In this, we
perform the task of combining keys using zip() and use zip() again for
combining like values. The dictionary comprehension is used to perform
construction of new list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Multiplication across Like Keys Value list elements

# Using dictionary comprehension + zip()

 

# initializing dictionaries

test_dict1 = {"Gfg" : [4, 6, 7], "Best" : [8,
6, 4], "is" : [9, 3, 4]}

test_dict2 = {"Gfg": [8, 4, 3], "Best" : [6,
3, 1], "is" : [9, 8, 2]}

 

# printing original lists

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Using zip() to perform link keys and values 

res = {key: [ele1 * ele2 for (ele1, ele2) in
zip(test_dict1[key], val2)] 

 for (key, val2) in zip(test_dict1.keys(), test_dict2.values())}

 

# printing result 

print("The constructed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary 1 is : {'Gfg': [4, 6, 7], 'Best': [8, 6, 4], 'is': [9, 3, 4]}
    The original dictionary 2 is : {'Gfg': [8, 4, 3], 'Best': [6, 3, 1], 'is': [9, 8, 2]}
    The constructed dictionary : {'Gfg': [32, 24, 21], 'Best': [48, 18, 4], 'is': [81, 24, 8]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

