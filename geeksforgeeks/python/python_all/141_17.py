Python | Convert key-value pair comma separated string into dictionary



Given a string, with different key-value pairs separated with commas, the task
is to convert that string into the dictionary. These types of problems are
common in web development where we fetch arguments from queries or get a
response in the form of strings. Given below are a few methods to solve the
task.

 **Method #1: Using dictionary comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting comma separated string

# into dictionary

 

# Initialising string

ini_string1 = 'name = akshat, course = btech, branch = computer'

 

# Printing initial string

print ("Initial String", ini_string1)

 

# Converting string into dictionary

# using dict comprehension

res = dict(item.split("=") for item in
ini_string1.split(", "))

 

# Printing resultant string

print ("Resultant dictionary", str(res))

   
  
---  
  
__

__

**Output:**

> Initial String name = akshat, course = btech, branch = computer  
> Resultant dictionary {‘branch ‘: ‘ computer’, ‘name ‘: ‘ akshat’, ‘course ‘:
> ‘ btech’}

  
**Method #2: Using Map and lambda**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting comma separated string

# into dictionary

 

# Initialising string

ini_string1 = 'name = akshat, course = btech, branch = computer'

 

# Printing initial string

print ("Initial String", ini_string1)

 

# Converting string into dictionary

# using map and lambda

res = dict(map(lambda x: x.split('='),
ini_string1.split(', ')))

 

# Printing resultant string

print ("Resultant dictionary", str(res))

   
  
---  
  
__

__

**Output:**

> Initial String name = akshat, course = btech, branch = computer  
> Resultant dictionary {‘course ‘: ‘ btech’, ‘name ‘: ‘ akshat’, ‘branch ‘: ‘
> computer’}

  
**Method #3: Usingeval() function**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting comma separated string

# into dictionary

 

# Initialising string

ini_string1 = 'name ="akshat", course ="btech", branch ="computer"'

 

# Printing initial string

print ("Initial String", ini_string1)

 

# Converting string into dictionary

# using eval

res = eval('dict('+ini_string1+')')

 

# Printing resultant string

print ("Resultant dictionary", str(res))

   
  
---  
  
__

__

**Output:**

> Initial String name =”akshat”, course =”btech”, branch =”computer”  
> Resultant dictionary {‘course’: ‘btech’, ‘name’: ‘akshat’, ‘branch’:
> ‘computer’}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

