Python – Test if all Values are Same in Dictionary



Given a dictionary, test if all its values are same.

>  **Input** : test_dict = {“Gfg” : 8, “is” : 8, “Best” : 8}  
>  **Output** : True  
>  **Explanation** : All element values are same, 8.
>
>  **Input** : test_dict = {“Gfg” : 8, “is” : 8, “Best” : 9}  
>  **Output** : False  
>  **Explanation** : All element values not same.

 **Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate for all the values and compare with value in dictionary, if any one is
different, then False is returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all Values are Same in Dictionary 

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 5, "Best" : 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Flag to check if all elements are same 

res = True

 

# extracting value to compare

test_val = list(test_dict.values())[0]

 

for ele in test_dict:

 if test_dict[ele] != test_val:

 res = False

 break

 

# printing result 

print("Are all values similar in dictionary? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 5, 'Best': 5}
    Are all values similar in dictionary? : True
    

**Method #2 : Using set() + values() + len()**

This is yet another way in which this task can be performed. In this, we
extract all the values using values() and set() is used to remove duplicates.
If length of the extracted set is 1, then all the values are assumed to be
similar.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if all Values are Same in Dictionary 

# Using set() + values() + len()

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 5, "Best" : 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using set() to remove duplicates and check for values count

res = len(list(set(list(test_dict.values())))) == 1

 

# printing result 

print("Are all values similar in dictionary? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 5, 'Best': 5}
    Are all values similar in dictionary? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

