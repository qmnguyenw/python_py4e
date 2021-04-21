Python – Convert Dictionaries List to Order Key Nested dictionaries



Given list of dictionaries, convert to ordered key dictionary with each key
contained dictionary as its nested value.

>  **Input** : test_list = [{“Gfg” : 3, 4 : 9}, {“is”: 8, “Good” : 2}]  
>  **Output** : {0: {‘Gfg’: 3, 4: 9}, 1: {‘is’: 8, ‘Good’: 2}}  
>  **Explanation** : List converted to dictionary with index keys.
>
>  **Input** : test_list = [{“is”: 8, “Good” : 2}]  
>  **Output** : {1: {‘is’: 8, ‘Good’: 2}}  
>  **Explanation** : List converted to dictionary with index keys, just one
> row.

 **Method #1 : Using loop + enumerate()**

This is brute way in which this task can be performed. In this, we iterate
through the index and value together using enumerate and create custom
required dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Dictionaries List to Order Key Nested dictionaries

# Using loop + enumerate()

 

# initializing lists

test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8,
"Good" : 2}, {"Best": 10, "CS" : 1}]

 

# printing original list

print("The original list : " + str(test_list))

 

# using enumerate() to extract key to map with dict values 

res = dict()

for idx, val in enumerate(test_list):

 res[idx] = val

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 4: 9}, {'is': 8, 'Good': 2}, {'Best': 10, 'CS': 1}]
    The constructed dictionary : {0: {'Gfg': 3, 4: 9}, 1: {'is': 8, 'Good': 2}, 2: {'Best': 10, 'CS': 1}}
    

**Method #2 : Using dictionary comprehension + enumerate()**

This is similar to above method, the only difference is that dictionary
comprehension is used instead of loop to perform task of encapsulation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Dictionaries List to Order Key Nested dictionaries

# Using dictionary comprehension + enumerate() 

 

# initializing lists

test_list = [{"Gfg" : 3, 4 : 9}, {"is": 8,
"Good" : 2}, {"Best": 10, "CS" : 1}]

 

# printing original list

print("The original list : " + str(test_list))

 

# dictionary comprehension encapsulating result as one liner

res = {idx : val for idx, val in enumerate(test_list)}

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3, 4: 9}, {'is': 8, 'Good': 2}, {'Best': 10, 'CS': 1}]
    The constructed dictionary : {0: {'Gfg': 3, 4: 9}, 1: {'is': 8, 'Good': 2}, 2: {'Best': 10, 'CS': 1}}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

