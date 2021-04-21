Python – Check for Key in Dictionary Value list



Sometimes, while working with data, we might have a problem we receive a
dictionary whole key has list of dictionaries as value. In this scenario, we
might need to find if a particular key exists in that. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingany()**  
This is simple and most recommended way in which this task can be performed.
In this, we just check for the key inside the values by iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Key in Dictionary Value list

# Using any()

 

# initializing dictionary 

test_dict = {'Gfg' : [{'CS' : 5}, {'GATE' : 6}],
'for' : 2, 'CS' : 3} 

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# initializing key

key = "GATE"

 

# Check for Key in Dictionary Value list

# Using any()

res = any(key in ele for ele in test_dict['Gfg'])

 

# printing result 

print("Is key present in nested dictionary list ? : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'Gfg': [{'CS': 5}, {'GATE': 6}], 'for': 2, 'CS': 3}
    Is key present in nested dictionary list ?  : True
    

**Method #2 : Using list comprehension + in operator**  
The combination of above functionalities can be used to perform this task. In
this, we iterate through the list using comprehension and perform key
flattening and store keys. Then we check for desired key using in operator.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for Key in Dictionary Value list

# Using list comprehension + in operator

 

# initializing dictionary 

test_dict = {'Gfg' : [{'CS' : 5}, {'GATE' : 6}],
'for' : 2, 'CS' : 3} 

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# initializing key

key = "GATE"

 

# Check for Key in Dictionary Value list

# Using list comprehension + in operator

res = key in [sub for ele in test_dict['Gfg'] for sub
in ele.keys()]

 

# printing result 

print("Is key present in nested dictionary list ? : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'Gfg': [{'CS': 5}, {'GATE': 6}], 'for': 2, 'CS': 3}
    Is key present in nested dictionary list ?  : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

