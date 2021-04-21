Python | Remove tuple from list of tuples if not containing any character



Given a list of tuples, the task is to remove all those tuples which do not
contain any character value.

 **Example:**

    
    
     **Input:** [(', ', 12), ('...', 55),
            ('-Geek', 115), ('Geeksfor', 115),]
    
    **Output:** [('-Geek', 115), ('Geeksfor', 115)]
    

**Method #1 : Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all those

# elements from list of tuple

# which does not contains any alphabet.

 

# List initialization

List = [(', ', 12), ('Paras', 5),

 ('jain.', 11), ('...', 55),

 ('-Geek', 115), ('Geeksfor', 115),

 (':', 63), ('Data', 3), ('-', 15),

 ('Structure', 32), ('Algo', 80),]

 

# Using list comprehension 

out = [(a, b) for a, b in List

 if any(c.isalpha() for c in a)]

 

# Printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

> [(‘Paras’, 5), (‘jain.’, 11), (‘-Geek’, 115), (‘Geeksfor’, 115), (‘Data’,
> 3), (‘Structure’, 32), (‘Algo’, 80)]
>
>  
>
>
>  
>

 **Method #2 : Using Regex**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all those

# elements from list of tuple

# which does not contains any alphabet.

 

# List initialization

List = [(', ', 12), ('Paras', 5),

 ('jain.', 11), ('...', 55),

 ('-Geek', 115), ('Geeksfor', 115),

 (':', 63), ('Data', 3), ('-', 15),

 ('Structure', 32), ('Algo', 80),]

 

# Importing

import re

 

# Using regex

out = [t for t in List if re.search(r'\w', t[0])]

 

# Printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

> [(‘Paras’, 5), (‘jain.’, 11), (‘-Geek’, 115), (‘Geeksfor’, 115), (‘Data’,
> 3), (‘Structure’, 32), (‘Algo’, 80)]

 **  
Method 3 : Using Filter and lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all those

# elements from list of tuple

# which does not contains any alphabet.

 

# List initialization

List = [(', ', 12), ('Paras', 5),

 ('jain.', 11), ('...', 55),

 ('-Geek', 115), ('Geeksfor', 115),

 (':', 63), ('Data', 3), ('-', 15),

 ('Structure', 32), ('Algo', 80),]

 

# Using filter

out = filter(lambda x:any(c.isalpha()

 for c in x[0]), List)

 

# Converting in list

out = list(out)

 

# Printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

> [(‘Paras’, 5), (‘jain.’, 11), (‘-Geek’, 115), (‘Geeksfor’, 115), (‘Data’,
> 3), (‘Structure’, 32), (‘Algo’, 80)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

