Python | Initialize common value to keys



Sometimes, while working with Python, we can be confronted with an issue in
which we need to assign each key of dictionary with a common value. This type
of problem in not occasional but can occur many times while programming. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingdefaultdict() \+ lambda**

The defaultdict can be initialized using a function which by default assigns
each new key with the common key. This is most recommended way to perform this
task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize common value to keys

# Using defaultdict()

from collections import defaultdict

 

# Initialize dictionary

test_dict = dict()

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Initialize common value to keys

# Using defaultdict()

res = defaultdict(lambda: 4, test_dict)

res_demo = res['Geeks']

 

# printing result

print("The value of key is : " + str(res_demo))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {}
    The value of key is :  4
    

  

  

**Method #2 : Usingget() \+ default value**

This method is just a display hack to perform this task. It doesn’t create the
actual list, but just prints the default value passed to get function and
hence the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize common value to keys

# Using get() + default value

 

# Initialize dictionary

test_dict = dict()

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Initialize common value to keys

# Using get() + default value

res_demo = test_dict.get('Geeks', 4)

 

# printing result

print("The value of key is : " + str(res_demo))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {}
    The value of key is :  4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

