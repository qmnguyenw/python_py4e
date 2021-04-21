Python – Count if dictionary position equals key or value



Given a dictionary, count instances where dictionary item position equals key
or value. Valid for Py >= 3.6 [ Introduction of dictionary ordering ].

>  **Input** : test_dict = {5:3, 2:3, 10:4, 7:3, 8:1, 9:5}  
> **Output** : 2  
> **Explanation** : At 3 and 5th position, values are 3 and 5.
>
>  **Input** : test_dict = {5:3, 2:3, 10:4, 8:1, 9:5}  
> **Output** : 1  
> **Explanation** : At 5th position, value is 5.  
>

**Method #1 : Using loop**

In this we iterate for each dictionary item and test for each item to check if
any position is equal to key or value of dictionary, if found, we iterate the
counter.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count if dictionary position equals key or value

# Using loop

 

# initializing dictionary

test_dict = {5: 3, 1: 3, 10: 4, 7: 3,
8: 1, 9: 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = 0

test_dict = list(test_dict.items())

for idx in range(0, len(test_dict)):

 

 # checking for key or value equality

 if idx == test_dict[idx][0] or idx ==
test_dict[idx][1]:

 res += 1

 

# printing result

print("The required frequency : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}
    The required frequency : 3
    

**Method #2 : Using** **sum()** **+** **list comprehension**

In this, we assign 1 to each case in which dictionary index is found equal to
any of its items, then perform list summation using sum().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count if dictionary position equals key or value

# Using sum() + list comprehension

 

# initializing dictionary

test_dict = {5: 3, 1: 3, 10: 4, 7: 3,
8: 1, 9: 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

test_dict = list(test_dict.items())

 

# sum() computing sum for filtered cases

res = sum([1 for idx in range(0, len(test_dict))
if idx ==

 test_dict[idx][0] or idx == test_dict[idx][1]])

 

# printing result

print("The required frequency : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original dictionary is : {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}
    The required frequency : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

