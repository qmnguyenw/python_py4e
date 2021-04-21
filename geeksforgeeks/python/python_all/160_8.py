Python | Ways to merge strings into list



Given n strings, the task is to merge all strings into a single list.

While developing an application, there come many scenarios when we need to
operate on the string and convert it as some mutable data structure, say
_list_. There are multiple ways we can convert strings into list based on the
requirement. Let’s understand it better with help of examples.

 **  
Method #1: Using ** _ast_****

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge all strings into a single list.

 

# Importing

import ast

 

# Initialization of strings

str1 ="'Geeks', 'for', 'Geeks'"

str2 ="'paras.j', 'jain.l'"

str3 ="'india'"

 

 

# Initialization of list

list = []

 

# Extending into single list

for x in (str1, str2, str3):

 list.extend(ast.literal_eval(x))

 

# printing output

print(list)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geeks', 'for', 'Geeks', 'paras.j', 'jain.l', 'i', 'n', 'd', 'i', 'a']
    

**  
Method #2: Using ** _eval_****

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge all strings into a single list.

 

# Initialization of strings

str1 ="['Geeks', 'for', 'Geeks']"

str2 ="['paras.j', 'jain.l']"

str3 ="['india']"

 

 

out = [str1, str2, str3]

 

out = eval('+'.join(out))

 

# printing output

print(out)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geeks', 'for', 'Geeks', 'paras.j', 'jain.l', 'india']
    

__

__  
__

__

__  
__  
__

# Python code to merge all strings into a single list.

 

# Initialization of strings

str1 ="'Geeks', 'for', 'Geeks'"

str2 = "'121', '142'"

str3 ="'extend', 'India'"

 

 

out = [str1, str2, str3]

 

out = eval('+'.join(out))

 

# printing output

print(list(out))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Geeks', 'for', 'Geeks121', '142extend', 'India']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

