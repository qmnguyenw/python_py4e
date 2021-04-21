Python | Type conversion of dictionary items



The interconversion of data types is quite common, and we may have this
problem while working with dictionaries as well. We might have a key and
corresponding list with numeric alphabets, and we with to transform the whole
dictionary to integers rather than string numerics. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using loop**  
This problem can be solved using naive method by the use of loops. In this, we
loop for each key and value and then typecast keys and value’s separately and
returning the desired integral container.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Type conversion of dictionary items

# Using loop

 

# Initialize dictionary

test_dict = {'1' : ['4', '5'], '4' : ['6', '7'],
'10' : ['8']}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using loop

# Type conversion of dictionary items

res = {}

for key, value in test_dict.items():

 res[int(key)] = [int(item) for item in value]

 

# printing result 

print("Dictionary after type conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {’10’: [‘8’], ‘4’: [‘6’, ‘7’], ‘1’: [‘4’, ‘5’]}  
> Dictionary after type conversion : {1: [4, 5], 10: [8], 4: [6, 7]}

  

  

**Method #2 : Using dictionary comprehension**  
This task can be easily performed using single line shorthand using dictionary
comprehension. This offers a shorter alternative to the loop method discussed
above and hence recommended.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Type conversion of dictionary items

# Using dictionary comprehension

 

# Initialize dictionary

test_dict = {'1' : ['4', '5'], '4' : ['6', '7'],
'10' : ['8']}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using dictionary comprehension

# Type conversion of dictionary items

res = {int(key):[int(i) for i in val]

 for key, val in test_dict.items()}

 

# printing result 

print("Dictionary after type conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {’10’: [‘8’], ‘4’: [‘6’, ‘7’], ‘1’: [‘4’, ‘5’]}  
> Dictionary after type conversion : {1: [4, 5], 10: [8], 4: [6, 7]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

