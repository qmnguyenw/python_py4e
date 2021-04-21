Python – Matching Pairs of Brackets



Sometimes, while working with Python data, we can have a problem in which we
need to pair all the elements with the suitable closing brackets, and can have
data associated with pairing. This kind of problem is classic application of
Stack Data Structure and can have usage across many domains. Let’s discuss a
certain way in which this task can be done.

>  **Input** : test_list = [(‘(‘, 1), (‘(‘, 2), (‘)’, 3), (‘)’, 4)]  
>  **Output** : [(2, 3), (1, 4)]
>
>  **Input** : test_list = [(‘(‘, 1), (‘)’, 4)]  
>  **Output** : [(1, 4)]

 **Method : Using stack DS + loop**  
The combination above functionalities can be used to solve this problem. In
this, we make a new pair with each opening bracket and when the corresponding
closing bracket comes using LIFO technique, we form a pair with that closing
bracket.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matching Pairs of Brackets

# Using stack DS + loop

 

# initializing list

test_list = [('(', 7), ('(', 9), (')', 10),
(')', 11), ('(', 15), (')', 100)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Matching Pairs of Brackets

# Using stack DS + loop

stck = []

res = []

for ele1, ele2 in test_list:

 if '(' in ele1:

 stck.append((ele1, ele2))

 elif ')' in ele1:

 res.append((stck.pop()[1], ele2))

 

# printing result 

print("The paired elements : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [('(', 7), ('(', 9), (')', 10), (')', 11), ('(', 15), (')', 100)]
    The paired elements : [(9, 10), (7, 11), (15, 100)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

