Python – Conditional Prefix in List



Given a list of elements, attach different prefix according to condition.

>  **Input** : test_list = [45, 53, 76, 86, 3, 49], pref_1 = “LOSE-“, pref_2 =
> “WIN-”  
>  **Output** : [‘LOSE-45’, ‘WIN-53’, ‘WIN-76’, ‘WIN-86’, ‘LOSE-3’, ‘LOSE-49’]  
>  **Explanation** : All 50+ are prefixed as “WIN-” and others as “LOSE-“.
>
>  **Input** : test_list = [78, 53, 76, 86, 83, 69], pref_1 = “LOSE-“, pref_2
> = “WIN-”  
>  **Output** : [‘WIN-78’, ‘WIN-53’, ‘WIN-76’, ‘WIN-86’, ‘WIN-83’, ‘WIN-69’]  
>  **Explanation** : All are 50+ hence prefixed “WIN-“.

 **Method #1 : Using loop**

This brute way in which this task can be performed. In this, we perform the
task of attatching the prefix by using conditionary operator and loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Conditional Prefix in List

# Using loop

 

# initializing list

test_list = [45, 53, 76, 86, 3, 49]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing pref 1

pref_1 = "LOW-"

 

# initializing pref 2

pref_2 = "HIGH-"

 

res = []

for ele in test_list:

 

 # appending prefix on greater than 50 check

 if ele >= 50:

 res.append(pref_2 + str(ele))

 else :

 res.append(pref_1 + str(ele))

 

# printing result 

print("The prefixed elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [45, 53, 76, 86, 3, 49]
    The prefixed elements : ['LOW-45', 'HIGH-53', 'HIGH-76', 'HIGH-86', 'LOW-3', 'LOW-49']
    

**Method #2 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
perform the similar task as above as one liner using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Conditional Prefix in List

# Using list comprehension

 

# initializing list

test_list = [45, 53, 76, 86, 3, 49]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing pref 1

pref_1 = "LOW-"

 

# initializing pref 2

pref_2 = "HIGH-"

 

# solution encapsulated as one-liner and conditional checks

res = [pref_2 + str(ele) if ele >= 50 else pref_1 +
str(ele) for ele in test_list]

 

# printing result 

print("The prefixed elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [45, 53, 76, 86, 3, 49]
    The prefixed elements : ['LOW-45', 'HIGH-53', 'HIGH-76', 'HIGH-86', 'LOW-3', 'LOW-49']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

