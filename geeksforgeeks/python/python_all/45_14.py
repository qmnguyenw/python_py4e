Python – Convert Dictionary values to Absolute Magnitude



Given a dictionary, convert its values to absolute.

>  **Input** : test_dict = {“Gfg” : -5, “is” : -7, “Best” : -2}  
>  **Output** : {“Gfg” : 5, “is” : 7, “Best” : 2}  
>  **Explanation** : All negative elements changed to positive with same
> magnitude
>
>  **Input** : test_dict = {“Gfg” : -8, “is” : 7, “Best” : -2}  
>  **Output** : {“Gfg” : 8, “is” : 7, “Best” : 2}  
>  **Explanation** : All negative elements changed to positive with same
> magnitude

 **Method #1 : Using loop + abs()**

This is one of the ways in which this task can be performed. In this, we
iterate for each value of dictionary using loop and perform the absolute
magnitude conversion using abs().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Dictionary values to Absolute Magnitude

# Using loop + abs()

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : -7, "Best" : 2,
"for" : -9, "geeks" : -8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using abs() to perform conversion 

# from negative to positive values 

for ele in test_dict:

 test_dict[ele] = abs(test_dict[ele])

 

# printing result 

print("Dictionary after absulute conversion : " + str(test_dict))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': -7, 'Best': 2, 'for': -9, 'geeks': -8}
    Dictionary after absulute conversion : {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    

**Method #2 : Using dictionary comprehension + abs()**

This task is similar to above method. The difference being dictionary
comprehension is used instead of loop to perform the task of iteration through
keys.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Dictionary values to Absolute Magnitude

# Using dictionary comprehension + abs()

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : -7, "Best" : 2,
"for" : -9, "geeks" : -8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# dictionary comprehension using to compile result

# items() used to extract dictionary keys and values.

res = {key : abs(val) for key, val in test_dict.items()}

 

# printing result 

print("Dictionary after absulute conversion : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': -7, 'Best': 2, 'for': -9, 'geeks': -8}
    Dictionary after absulute conversion : {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

