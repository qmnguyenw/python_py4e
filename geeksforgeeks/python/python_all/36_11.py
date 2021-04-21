Python – Concatenate Tuple to Dictionary Key



Given Tuples, convert them to dictionary with key being concatenated string.

>  **Input** : test_list = [((“gfg”, “is”, “best”), 10), ((“gfg”, “for”,
> “cs”), 15)]  
>  **Output** : {‘gfg is best’: 10, ‘gfg for cs’: 15}  
>  **Explanation** : Tuple strings concatenated as strings.
>
>  **Input** : test_list = [((“gfg”, “is”, “best”), 10)]  
>  **Output** : {‘gfg is best’: 10}  
>  **Explanation** : Tuple strings concatenated as strings.

 **Method #1 : Using loop + join()**

In this, we perform the task of concatenation for dictionary key using join()
and loop is used to render the required dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Tuple to Dictionary Key

# Using loop + join()

 

# initializing list

test_list = [(("gfg", "is", "best"), 10), (("gfg",
"good"), 1), (("gfg", "for", "cs"), 15)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = {}

for sub in test_list:

 

 # joining for making key

 res[" ".join(sub[0])] = sub[1]

 

# printing result 

print("The computed Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(('gfg', 'is', 'best'), 10), (('gfg', 'good'), 1), (('gfg', 'for', 'cs'), 15)]
    The computed Dictionary : {'gfg is best': 10, 'gfg good': 1, 'gfg for cs': 15}
    

**Method #2 : Using dictionary comprehension**

This is shorthand to above method, similar functionality, just one-liner on
paper for compact solution.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Tuple to Dictionary Key

# Using dictionary comprehension

 

# initializing list

test_list = [(("gfg", "is", "best"), 10), (("gfg",
"good"), 1), (("gfg", "for", "cs"), 15)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# one liner to solve problem 

res = {' '.join(key): val for key, val in test_list}

 

# printing result 

print("The computed Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(('gfg', 'is', 'best'), 10), (('gfg', 'good'), 1), (('gfg', 'for', 'cs'), 15)]
    The computed Dictionary : {'gfg is best': 10, 'gfg good': 1, 'gfg for cs': 15}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

