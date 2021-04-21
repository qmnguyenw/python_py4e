Python | Convert list of tuples into digits



Given a list of tuples, the task is to convert it into list of all digits
which exists in elements of list.

Let’s discuss certain ways in which this task is performed.

 **Method #1: Usingre**

The most concise and readable way to convert list of tuple into list of all
digits which exists in elements of list is by using _re_.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert list of tuples into

# list of all digits which exists

# in elements of list.

 

# Importing

import re

 

# Input list initialization

lst = [(11, 100), (22, 200), (33, 300), (44,
400), (88, 800)]

 

# Using re

temp = re.sub(r'[\[\]\(\), ]', '', str(lst))

 

# Using set

Output = [int(i) for i in set(temp)]

 

# Printing output

print("Initial List is :", lst)

print("Output list is :", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

> Initial List is : [(11, 100), (22, 200), (33, 300), (44, 400), (88, 800)]  
> Output list is : [1, 4, 8, 0, 3, 2]

