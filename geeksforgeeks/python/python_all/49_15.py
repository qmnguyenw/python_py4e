Python – Factors Frequency Dictionary



Given a list with elements, construct a dictionary with frequency of factors.

>  **Input** : test_list = [2, 4, 6, 8]  
>  **Output** : {1: 4, 2: 4, 3: 1, 4: 2, 5: 0, 6: 1, 7: 0, 8: 1}  
>  **Explanation** : All factors count mapped, e.g 2 is divisible by all 4
> values, hence mapped with 4.
>
>  **Input** : test_list = [1, 2]  
>  **Output** : {1: 2, 2 : 1}  
>  **Explanation** : Similar as above, 1 is factor of all.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, the elements
are iterated and required number is checked for being a factor, if yes, its
frequency is increased in dictionary corresponding to its key.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Factors Frequency Dictionary

# Using loop

 

# initializing list

test_list = [2, 4, 6, 8, 3, 9, 12, 15,
16, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

res = dict()

 

# iterating till max element 

for idx in range(1, max(test_list)):

 res[idx] = 0

 for key in test_list:

 

 # checking for factor 

 if key % idx == 0:

 res[idx] += 1

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
    The constructed dictionary : {1: 10, 2: 7, 3: 6, 4: 4, 5: 1, 6: 3, 7: 0, 8: 2, 9: 2, 10: 0, 11: 0, 12: 1, 13: 0, 14: 0, 15: 1, 16: 1, 17: 0}
    

**Method #2 : Using sum() + loop**

This is almost similar approach to above problem. The difference being sum()
is used for summation rather than a manual loop for solving problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Factors Frequency Dictionary

# Using sum() + loop

 

# initializing list

test_list = [2, 4, 6, 8, 3, 9, 12, 15,
16, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

res = dict()

for idx in range(1, max(test_list)):

 

 # using sum() instead of loop for sum computation

 res[idx] = sum(key % idx == 0 for key in
test_list)

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
    The constructed dictionary : {1: 10, 2: 7, 3: 6, 4: 4, 5: 1, 6: 3, 7: 0, 8: 2, 9: 2, 10: 0, 11: 0, 12: 1, 13: 0, 14: 0, 15: 1, 16: 1, 17: 0}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

