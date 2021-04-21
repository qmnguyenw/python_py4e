Python | Initialize dictionary with common value



While working with Python, sometimes, we might have a problem in which we
require the initialize the static list into a dictionary with a constant
value. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingdict() \+ list comprehension**

The combination of above functions can be used to perform this particular
task. In this, we just convert the elements extracted from list as keys and
assign the common value using list comprehension and conversion done by
dict().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary with common value

# Using list comprehension + dict()

 

# Initialize list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initialize dictionary with common value

# Using list comprehension + dict()

res = dict((sub, 4) for sub in test_list)

 

# printing result

print("The constructed dictionary with common value : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    The constructed dictionary with common value : {'is': 4, 'gfg': 4, 'best': 4}
    

  

  

**Method #2 : Usingfromkeys()**

The inbuilt function of fromkeys() can also be used to perform this particular
task which is made to perform this particular task itself and is more Pythonic
way to perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary with common value

# Using fromkeys()

 

# Initialize list

test_list = ['gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initialize dictionary with common value

# Using fromkeys()

res = dict.fromkeys(test_list, 4)

 

# printing result

print("The constructed dictionary with common value : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    The constructed dictionary with common value : {'is': 4, 'gfg': 4, 'best': 4}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

