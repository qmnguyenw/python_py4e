Python – Selectively Split in Strings



Sometimes, while working with Python strings, we may have to perform a split.
Not sometimes, normal one, depending on deliminator but something depending
upon programming constructs like elements, numbers, words etc and segregate
them. Lets discuss a way in which this task can be solved.

 **Method : Usingre.findall()**  
A specific regex can be employed to perform this task. In this we construct
regex using different elements like numbers, words punctuations etc.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective Split in Strings

# Using regex

import re

 

# initializing string

test_str = "print(\"geeks\");"

 

# printing original string

print("The original string is : " + test_str)

 

# Selective Split in Strings

# Using regex

res = re.findall('\d+\.\d+|\d+|\w+|[^a-zA-Z\s]', test_str)

 

# printing result 

print("The splitted string is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : print("geeks");
    The splitted string is : ['print', '(', '"', 'geeks', '"', ')', ';']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

