Python | Keys with Maximum value



Many times, we may have problem in which we require to find not just the
value, but the corresponding keys to the maximum value in the entire
dictionary. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingmax() + list comprehension + values()**  
The combination of above functions can be used to perform this particular
task. In this, maximum value is extracted using the max function, while values
of dictionary is extracted using values(). The list comprehension is used to
iterate through the dictionary for matching keys with max value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys with Maximum value

# Using max() + list comprehension + values()

 

# initializing dictionary

test_dict = {'Gfg' : 2, 'for' : 1, 'CS' : 2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using max() + list comprehension + values()

# Keys with Maximum value

temp = max(test_dict.values())

res = [key for key in test_dict if test_dict[key] ==
temp]

 

# printing result 

print("Keys with maximum values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'CS': 2, 'Gfg': 2, 'for': 1}
    Keys with maximum values are : ['CS', 'Gfg']
    

**Method #2 : Usingall() \+ list comprehension**  
This task can also be performed using list comprehension and all function. In
this, we take all the elements values, using all function that are smaller
than values with keys and return the keys with largest values using list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys with Maximum value

# Using all() + list comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 2, 'for' : 1, 'CS' : 2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using all() + list comprehension

# Keys with Maximum value

res = [key for key in test_dict if all(test_dict[temp]
<= test_dict[key] for temp in test_dict)]

 

# printing result 

print("Keys with maximum values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'CS': 2, 'Gfg': 2, 'for': 1}
    Keys with maximum values are : ['CS', 'Gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

