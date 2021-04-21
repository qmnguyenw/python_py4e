Python – Keys Values equal frequency



Given a dictionary, count instances where keys are equal to values.

>  **Input** : test_dict = {5:5, 8:9, 7:8, 1:2, 10:10, 4:8}  
> **Output** : 2  
> **Explanation** : At 2 instances, keys are equal to values.
>
>  **Input** : test_dict = {5:4, 8:9, 7:8, 1:2, 10:10, 4:8}  
> **Output** : 1  
> **Explanation** : At 1 instance, key is equal to value.

**Method #1 : Using loop**

In this, we count instances where keys are equal to values and increment the
counter accordingly.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys Values equal frequency

# Using loop

 

# initializing dictionary

test_dict = {5: 5, 8: 9, 7: 7, 1: 2,
10: 10, 4: 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = 0

for key in test_dict:

 

 # checking for equality and incrementing counter

 if key == test_dict[key]:

 res += 1

 

# printing result

print("The required frequency : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {5: 5, 8: 9, 7: 7, 1: 2, 10: 10, 4: 8}
    The required frequency : 3
    

**Method #2 : Using** **sum()** **+** **list comprehension**

In this, task of counting is performed using sum(), when equal key-values are
found, 1 is appending to list, and then at end, each value is summed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys Values equal frequency

# Using sum() + list comprehension

 

# initializing dictionary

test_dict = {5: 5, 8: 9, 7: 7, 1: 2,
10: 10, 4: 8}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# computing summation to get frequency

res = sum([1 for key in test_dict if key ==
test_dict[key]])

 

# printing result

print("The required frequency : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {5: 5, 8: 9, 7: 7, 1: 2, 10: 10, 4: 8}
    The required frequency : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

