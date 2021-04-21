Python program to Increment Suffix Number in String



Given a String, the task is to write a Python program to increment the number
which is at end of the string.

>  **Input** : test_str = ‘geeks006’  
> **Output** : geeks7  
> **Explanation** : Suffix 006 incremented to 7.
>
>  **Input** : test_str = ‘geeks007’  
> **Output** : geeks8  
> **Explanation** : Suffix 007 incremented to 8.  
>

**Method #1 : Using findall() +** **join()** **+** **replace()**

In this, strategy we perform the task of finding number using findall(), then
perform the task of separating numeric string and prefix string, then an
increment of a numeric string is performed. At last, the string is joined to
get a prefix followed by an incremented number.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Increment Suffix Number

# Using findall() + join() + replace()

import re

 

# initializing string

test_str = 'geeks006'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting suffix number 

reg = re.compile(r'[ 0 - 9]')

mtch = reg.findall(test_str)

 

# getting number 

num = ''.join(mtch[-3 : ])

pre_str = test_str.replace(num, '')

 

# Increment number 

add_val = int(num) + 1

 

# joining prefix str and added value 

res = pre_str + str(add_val)

 

# printing result 

print("Incremented numeric String : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : geeks006
    Incremented numeric String : geeks61

 **Method #2 : Using sub() + group() + zfill()**

In this, we perform the task of grouping numbers using group() and
incrementing, zfill() is used for task of filling the required leading values
in numerical. The sub() is used to find the numerical part of strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Increment Suffix Number

# Using sub() + group() + zfill()

import re

 

# initializing string

test_str = 'geeks006'

 

# printing original string

print("The original string is : " + str(test_str))

 

# fstring used to form string 

# zfill fills values post increment

res = re.sub(r'[0-9]+$',

 lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 

 test_str)

 

# printing result 

print("Incremented numeric String : " + str(res))   
  
---  
  
__

__

**Output:**

    
    
    The original string is : geeks006
    Incremented numeric String : geeks007

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

