Python – Triple quote String concatenation



Sometimes, while working with Python Strings, we can have problem in which we
need to perform concatenation of Strings which are constructed by Triple
quotes. This happens in cases we have multiline strings. This can have
applications in many domains. Lets discuss certain way in which this task can
be performed.

    
    
    **Input** : test_str1 = """mango
    is"""
    test_str2 = """good
    for health
    """
    **Output** : mango good
     is for health
    
    **Input** : test_str1 = """Gold
    is"""
    test_str2 = """important
    for economy
    """
    **Output** : Gold important
     is for economy
    

**Method : Usingsplitlines() + strip() + join()**  
The combination of above functions can be used to perform this task. In this,
we perform the ask of line splitting using splitlines(). The task of
concatenation is done using strip() and join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Triple quote String concatenation

# Using splitlines() + join() + strip()

 

# initializing strings

test_str1 = """gfg

is"""

test_str2 = """best

for geeks

"""

 

# printing original strings

print("The original string 1 is : " + test_str1)

print("The original string 2 is : " + test_str2)

 

# Triple quote String concatenation

# Using splitlines() + join() + strip()

test_str1 = test_str1.splitlines()

test_str2 = test_str2.splitlines()

res = []

 

for i, j in zip(test_str1, test_str2):

 res.append(" " + i.strip() + " " + j.strip())

res = '\n'.join(res)

 

# printing result 

print("String after concatenation : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string 1 is : gfg
    is
    The original string 2 is : best
    for geeks
    
    String after concatenation :    gfg best
       is for geeks
    

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

