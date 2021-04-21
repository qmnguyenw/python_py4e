Python – Round Off Dictionary Values to K decimals



Given Dictionary with float values perform round off to K of all the values.

>  **Input** : {“Gfg” : 54.684034, “is” : 76.324334, “Best” : 28.43524}, K = 2  
>  **Output** : {“Gfg” : 54.68, “is” : 76.32, “Best” : 28.43}  
>  **Explanation** : Values rounded till 2.
>
>  **Input** : {“Gfg” : 54.684034, “is” : 76.324334, “Best” : 28.43524}, K = 1  
>  **Output** : {“Gfg” : 54.6, “is” : 76.3, “Best” : 28.4}  
>  **Explanation** : Values rounded till 1.

 **Method #1 : Using loop + round()**

This is one of the ways in which this task can be performed. In this, we
iterate for all the values, and perform round off to nearest K values using
round().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Round Off Dictionary Values to K decimals

# Using loop + round()

 

# initializing dictionary

test_dict = {"Gfg" : 54.684034, "is" : 76.324334,
"Best" : 28.43524}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 3

 

# loop to iterate for values 

res = dict()

for key in test_dict:

 

 # rounding to K using round()

 res[key] = round(test_dict[key], K)

 

# printing result 

print("Values after round off : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 54.684034, 'is': 76.324334, 'Best': 28.43524}
    Values after round off : {'Gfg': 54.684, 'is': 76.324, 'Best': 28.435}
    
    

**Method #2 : Using dictionary comprehension + round()**

This is yet another way in which this task can be performed. In this we
performed similar task using above functionality, the difference being usage
of dictionary comprehension to provide one-line solution.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Round Off Dictionary Values to K decimals

# Using dictionary comprehension + round()

 

# initializing dictionary

test_dict = {"Gfg" : 54.684034, "is" : 76.324334,
"Best" : 28.43524}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 3

 

# Encapsulating solution using single comprehension

res = {key : round(test_dict[key], K) for key in test_dict}

 

# printing result 

print("Values after round off : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 54.684034, 'is': 76.324334, 'Best': 28.43524}
    Values after round off : {'Gfg': 54.684, 'is': 76.324, 'Best': 28.435}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

