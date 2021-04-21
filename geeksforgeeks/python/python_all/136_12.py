Python | Check for None values in given dictionary



Many times, while working with dictionaries, we wish to check for a non-null
dictionary, i.e check for None values in given dictionary. This finds
application in Machine Learning in which we have to feed data with no none
values. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingall() + not operator + values()**

The combination of above functions can be used to perform this particular
task. In this, we check for all the values using all function extracted
using values function. The not operator is used to inverse the result to
check for any of None value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Non None Dictionary values

# Using all() + not operator + values()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using all() + not operator + values()

# Check for Non None Dictionary values

res = not all(test_dict.values())

 

# printing result 

print("Does Dictionary contain None value ? " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': 1, 'CS': None, 'for': 2}
    Does Dictionary contain None value ? True
    

  

  

**Method #2 : Usingin operator + values()**

This task can also be performed using the in operator and values function. We
just check for None in all the values extracted using the values function
and check for existence using the in operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Non None Dictionary values

# Using in operator + values()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using in operator + values()

# Check for Non None Dictionary values

res = None in test_dict.values()

 

# printing result 

print("Does Dictionary contain None value ? " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': 1, 'CS': None, 'for': 2}
    Does Dictionary contain None value ? True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

