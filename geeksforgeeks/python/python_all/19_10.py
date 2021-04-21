Python – Test if Values Sum is Greater than Keys Sum in dictionary



Given a Dictionary, check if the summation of values is greater than Keys sum.

>  **Input** : test_dict = {5:3, 1:3, 10:4, 7:3, 8:1, 9:5}  
> **Output** : False  
> **Explanation** : Values sum = 19 < 40, which is key sum, i.e false.
>
>  **Input** : test_dict = {5:3, 1:4}  
> **Output** : True  
> **Explanation** : Values sum = 7 > 6, which is key sum, i.e true.

**Method #1: Using loop**

In this, we compute keys and values sum in separate counter, and after the
loop equate the values, if values are greater than Keys summation, True is
returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Values Sum is Greater than Keys Sum in dictionary

# Using loop

 

# initializing dictionary

test_dict = {5: 3, 1: 3, 10: 4, 7: 3,
8: 1, 9: 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

key_sum = 0

val_sum = 0

 

for key in test_dict:

 

 # getting sum

 key_sum += key

 val_sum += test_dict[key]

 

# checking if val_sum greater than key sum

res = val_sum > key_sum

 

# printing result

print("The required result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}
    The required result : False
    

**Method #2 : Using sum() + values() + keys()**

In this way, keys sum and values sum is extracted using keys(), values() and
summation using sum(), the required condition is checked and verdict is
computed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Values Sum is Greater than Keys Sum in dictionary

# Using sum() + values() + keys()

 

# initializing dictionary

test_dict = {5: 3, 1: 3, 10: 4, 7: 3,
8: 1, 9: 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = sum(list(test_dict.keys())) <
sum(list(test_dict.values()))

 

# printing result

print("The required result : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}
    The required result : False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

