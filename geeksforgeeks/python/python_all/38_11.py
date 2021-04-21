Python – Convert String to unicode characters



Given a String, convert its characters to unicode characters.

>  **Input** : test_str = ‘gfg’  
>  **Output** : \u0067\u0066\u0067  
>  **Explanation** : Result changed to unicoded string.
>
>  **Input** : test_str = ‘himani’  
>  **Output** : \u0068\u0069\u006D\u0061\u006E\u0069  
>  **Explanation** : Result changed to unicoded string.

 **Method #1 : Using re.sub() + ord() + lambda**

In this, we perform the task of substitution using re.sub() and lambda
function is used to perform the task of conversion of each characters using
ord().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to unicode characters

# using re.sub() + ord() + lambda

import re

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# using sub() to perform substitutions

# ord() for conversion.

res = (re.sub('.', lambda x: r'\u % 04X' %
ord(x.group()), test_str))

 

# printing result 

print("The unicode converted String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The unicode converted String : \u0067\u0065\u0065\u006B\u0073\u0066\u006F\u0072\u0067\u0065\u0065\u006B\u0073
    

**Method #2 : Using join() + format() + ord()**

In this, task of substitution in unicode formatted string is done using
format() and ord() is used for conversion.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to unicode characters

# using join() + format() + ord()

import re

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original String

print("The original string is : " + str(test_str))

 

# using format to perform required formatting 

res = ''.join(r'\u{:04X}'.format(ord(chr)) for
chr in test_str)

 

# printing result 

print("The unicode converted String : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The unicode converted String : \u0067\u0065\u0065\u006B\u0073\u0066\u006F\u0072\u0067\u0065\u0065\u006B\u0073
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

