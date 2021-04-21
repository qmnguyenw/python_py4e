Python – Store Function as dictionary value



Given a dictionary, assign its keys as function calls.

 **Case 1 : Without Params.**

The way that is employed to achieve this task is that, function name is kept
as dictionary values, and while calling with keys, brackets ‘()’ are added.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Functions as dictionary values

# Using Without params

 

# call Gfg fnc 

def print_key1():

 return "This is Gfg's value"

 

# initializing dictionary

# check for function name as key

test_dict = {"Gfg": print_key1, "is" : 5, "best" :
9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# calling function using brackets 

res = test_dict['Gfg']()

 

# printing result 

print("The required call result : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': <function print_key1 at 0x7f1c0445be18>, 'is': 5, 'best': 9}
    The required call result : This is Gfg's value
    

**Case 2 : With params**

  

  

The task of calling with params is similar to above case, the values are
passed during function call inside brackets as in usual function calls.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Functions as dictionary values

# Using With params 

 

# call Gfg fnc 

def sum_key(a, b):

 return a + b

 

# initializing dictionary

# check for function name as key

test_dict = {"Gfg": sum_key, "is" : 5, "best" : 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# calling function using brackets 

# params inside brackets

res = test_dict['Gfg'](10, 34)

 

# printing result 

print("The required call result : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': <function sum_key at 0x7f538d017e18>, 'is': 5, 'best': 9}
    The required call result : 44
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

