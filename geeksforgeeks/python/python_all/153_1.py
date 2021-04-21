Python | Convert given list into nested list



Some times, we come over the data that is in string format in a list and it is
required to convert it into a list of the list. This kind of problem of
converting a list of strings to nested list is quite common in web
development. Let’s discuss certain ways in which this can be performed.

 **Method #1: Using iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert list

# of string into list of list

 

# List initialization

Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',

 'Geeks, 123', '555.7492, 152.5406']

 

temp = []

 

# Getting elem in list of list format

for elem in Input:

 temp2 = elem.split(', ')

 temp.append((temp2))

 

# List initialization

Output = [] 

 

# Using Iteration to convert 

# element into list of list

for elem in temp:

 temp3 = []

 for elem2 in elem:

 temp3.append(elem2)

 Output.append(temp3)

 

# printing

print(Output)  
  
---  
  
 __

 __

 **Output:**

> [[‘Geeeks’, ‘Forgeeks’], [‘65.7492’, ‘62.5405’], [‘Geeks’, ‘123’],
> [‘555.7492’, ‘152.5406’]]

  
**Method #2 :** Using ast [list with numeric values]

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert list

# of string into list of list

 

# importing

import ast

 

# List Initialization

Input = ['12, 454', '15.72, 82.85', '52.236, 25256',
'95.9492, 72.906']

 

# using ast to convert

Output = [list(ast.literal_eval(x)) for x in Input]

 

# printing

print(Output)  
  
---  
  
 __

 __

 **Output:**

> [[12, 454], [15.72, 82.85], [52.236, 25256], [95.9492, 72.906]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

