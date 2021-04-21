Python program to find the sum of dictionary keys



Given a dictionary with integer keys. The task is to find the sum of all the
keys.

 **Examples:**

    
    
     **Input** : test_dict = {3 : 4, 9 : 10, 15 : 10, 5 : 7} 
    **Output** : 32 
    **Explanation** : 3 + 9 + 15 + 5 = 32, sum of keys.
    
    **Input** : test_dict = {3 : 4, 9 : 10, 15 : 10} 
    **Output** : 27 
    **Explanation** : 3 + 9 + 15 = 27, sum of keys. 

**Method #1: Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate all the keys in the dictionary and compute summation using a counter.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Keys Summation

# Using loop

 

# initializing dictionary

test_dict = {3: 4, 9: 10, 15: 10, 5: 7,
6: 7}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = 0

for key in test_dict:

 

 # adding keys

 res += key

 

# printing result

print("The dictionary keys summation : " + str(res))  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    The original dictionary is : {3: 4, 9: 10, 15: 10, 5: 7, 6: 7}
    The dictionary keys summation : 38
    

