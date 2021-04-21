Python – Test if custom keys equal to K in dictionary



Given dictionary and custom keys list, check if all those custom keys equals
K.

>  **Input** : test_dict = {“Gfg” : 5, “is” : 8, “Best” : 10, “for” : 10,
> “Geeks” : 10}, cust_keys = [“is”, “for”, “Geeks”], K = 10
>
>  **Output** : False
>
>  **Explanation** : “is” is having 8 as value not 10, hence False
>
>  **Input** : test_dict = {“Gfg” : 5, “is” : 10, “Best” : 10, “for” : 10,
> “Geeks” : 10}, cust_keys = [“is”, “for”, “Geeks”], K = 10
>
>  
>
>
>  
>
>
>  **Output** : True
>
>  **Explanation** : All keys have 10 as values.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this we iterate each
custom key and check if all are equal to K by keeping track using boolean
variable.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if custom keys equal to K in dictionary

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10,
"for" : 8, "Geeks" : 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing custom keys list 

cust_keys = ["is", "for", "Geeks"]

 

# initializing K 

K = 8

 

# using loop to check for all keys 

res = True

for key in cust_keys:

 if test_dict[key] != K:

 

 # break even if 1 value is not equal to K

 res = False

 break

 

# printing result 

print("Are all custom keys equal to K : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 8, 'Best': 10, 'for': 8, 'Geeks': 8}
    Are all custom keys equal to K : True
    
    

**Method #2 : Using all() + generator expression**

The combination of above functionalities can be used to solve this problem. In
this, we use all() to check for all the values and generator expression
performs required iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if custom keys equal to K in dictionary

# Using all() + generator expression

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10,
"for" : 8, "Geeks" : 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing custom keys list 

cust_keys = ["is", "for", "Geeks"]

 

# initializing K 

K = 8

 

# returns true if all elements match K 

res = all(test_dict[key] == K for key in cust_keys)

 

# printing result 

print("Are all custom keys equal to K : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 8, 'Best': 10, 'for': 8, 'Geeks': 8}
    Are all custom keys equal to K : True
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

