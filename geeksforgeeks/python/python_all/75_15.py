Python – Convert key-value String to dictionary



Sometimes, while working with Python strings, we can have problem in which we
need to convert a string key-value pairs to dictionary. This can have
applications in which we are working with string data and needs to be
converted. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingmap() + split() \+ loop**  
The combination of above functionalities can be used to perform this task. In
this, we perform the conversion of key-value pair to dictionary using map and
splitting key-value pairs is done using split().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert key-value String to dictionary

# Using map() + split() + loop

 

# initializing string

test_str = 'gfg:1, is:2, best:3'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Convert key-value String to dictionary

# Using map() + split() + loop

res = []

for sub in test_str.split(', '):

 if ':' in sub:

 res.append(map(str.strip, sub.split(':', 1)))

res = dict(res)

 

# printing result 

print("The converted dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg:1, is:2, best:3
    The converted dictionary is : {'gfg': '1', 'is': '2', 'best': '3'}
    

**Method #2 : Usingdict() + generator expression + split() + map()**  
This is yet another way in which this problem can be solved. In this, we
perform the task in similar way as above but in 1 liner way using dict() and
generator expression.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert key-value String to dictionary

# Using dict() + generator expression + split() + map()

 

# initializing string

test_str = 'gfg:1, is:2, best:3'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Convert key-value String to dictionary

# Using dict() + generator expression + split() + map()

res = dict(map(str.strip, sub.split(':', 1)) for
sub in test_str.split(', ') if ':' in sub)

 

# printing result 

print("The converted dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfg:1, is:2, best:3
    The converted dictionary is : {'gfg': '1', 'is': '2', 'best': '3'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

