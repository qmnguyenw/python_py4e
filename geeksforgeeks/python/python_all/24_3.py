Python – Remove double quotes from dictionary keys



Given dictionary with string keys, remove double quotes from it.

>  **Input** : test_dict = {‘”Geeks”‘ : 3, ‘”g”eeks’ : 9}  
>  **Output** : {‘Geeks’: 3, ‘geeks’: 9}  
>  **Explanation** : Double qoutes removed from keys.
>
>  **Input** : test_dict = {‘”Geeks”‘ : 3}  
>  **Output** : {‘Geeks’: 3}  
>  **Explanation** : Double qoutes removed from keys.

 **Method #1 : Using dictionary comprehension + replace()**

The combination of above functionalities can be used to solve this problem. In
this, we perform removal of double quotes using replace() with empty string.
The dictionary comprehension is used for remaking dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove double quotes from dictionary keys

# Using dictionary comprehension + replace()

 

# initializing dictionary

test_dict = {'"Geeks"' : 3, '"is" for' : 5, '"g"eeks'
: 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# dictionary comprehension to make double quotes free

# dictionary

res = {key.replace('"', ''):val for key, val in
test_dict.items()}

 

# printing result 

print("The dictionary after removal of double quotes : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'"Geeks"': 3, '"is" for': 5, '"g"eeks': 9}
    The dictionary after removal of double quotes : {'Geeks': 3, 'is for': 5, 'geeks': 9}
    
    

**Method #2 : Using re.sub() + dictionary comprehension**

The combination of above functions is also an alternative to solve this task.
In this, we employ regex to solve the problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove double quotes from dictionary keys

# Using re.sub() + dictionary comprehension

import re

 

# initializing dictionary

test_dict = {'"Geeks"' : 3, '"is" for' : 5, '"g"eeks'
: 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# regex making replacement of double quotes with empty string 

res = {re.sub(r'"', '', key): val for key, val in
test_dict.items()}

 

# printing result 

print("The dictionary after removal of double quotes : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'"Geeks"': 3, '"is" for': 5, '"g"eeks': 9}
    The dictionary after removal of double quotes : {'Geeks': 3, 'is for': 5, 'geeks': 9}
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

