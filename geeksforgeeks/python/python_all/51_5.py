Python – Convert String to List of dictionaries



Given List of dictionaries in String format, Convert into actual List of
Dictionaries.

>  **Input** : test_str = [“[{‘Gfg’ : 3, ‘Best’ : 8}, {‘Gfg’ : 4, ‘Best’ :
> 8}]”]  
>  **Output** : [[{‘Gfg’: 3, ‘Best’: 8}, {‘Gfg’: 4, ‘Best’: 8}]]  
>  **Explanation** : String converted to list of dictionaries.
>
>  **Input** : test_str = [“[{‘Gfg’ : 3, ‘Best’ : 8}]”]  
>  **Output** : [[{‘Gfg’: 3, ‘Best’: 8}]]  
>  **Explanation** : String converted to list of dictionaries.

 **Method #1 : Using json.loads() + replace()**

The combination of above functions can be used to solve this problem. In this,
we replace the internal Strings using replace() and dictionary list is made
using loads().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to List of dictionaries

# Using json.loads + replace()

import json

 

# initializing string

test_str = ["[{'Gfg' : 3, 'Best' : 8}, {'Gfg' : 4, 'Best' : 9}]"]

 

# printing original string

print("The original string is : " + str(test_str))

 

# replace() used to replace strings 

# loads() used to convert 

res = [json.loads(idx.replace("'", '"')) for idx in
test_str]

 

# printing result 

print("Converted list of dictionaries : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : ["[{'Gfg' : 3, 'Best' : 8}, {'Gfg' : 4, 'Best' : 9}]"]
    Converted list of dictionaries : [[{'Gfg': 3, 'Best': 8}, {'Gfg': 4, 'Best': 9}]]
    

**Method #2 : Using eval()**

This is one of the ways in which this task can be performed. The eval(),
internally evaluates the data type and returns required result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to List of dictionaries

# Using json.loads + replace()

 

# initializing string

test_str = "[{'Gfg' : 3, 'Best' : 8}, {'Gfg' : 9, 'Best' : 9}]"

 

# printing original string

print("The original string is : " + str(test_str))

 

# eval() used to convert 

res = list(eval(test_str))

 

# printing result 

print("Converted list of dictionaries : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : [{'Gfg' : 3, 'Best' : 8}, {'Gfg' : 9, 'Best' : 9}]
    Converted list of dictionaries : [{'Gfg': 3, 'Best': 8}, {'Gfg': 9, 'Best': 9}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

