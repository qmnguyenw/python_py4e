Python – Change Datatype of Tuple Values



Sometimes, while working with set of records, we can have a problem in which
we need to perform a data type change of values of tuples, which are in its
2nd position, i.e value position. This kind of problem can occur in all
domains that include data manipulations. Let’s discuss certain ways in which
this task can be performed.

    
    
    **Input** : test_list = [(44, 5.6), (16, 10)]
    **Output** : [(44, '5.6'), (16, '10')]
    
    **Input** : test_list = [(44, 5.8)]
    **Output** : [(44, '5.8')]
    

**Method #1 : Usingenumerate() \+ loop**  
This is brute force way in which this problem can be solved. In this, we
reassign the tuple values, by changing required index of tuple to type cast
using appropriate datatype conversion functions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Change Datatype of Tuple Values

# Using enumerate() + loop

 

# initializing list

test_list = [(4, 5), (6, 7), (1, 4), (8,
10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Change Datatype of Tuple Values

# Using enumerate() + loop

# converting to string using str()

for idx, (x, y) in enumerate(test_list):

 test_list[idx] = (x, str(y))

 

# printing result 

print("The converted records : " + str(test_list))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(4, 5), (6, 7), (1, 4), (8, 10)]
    The converted records : [(4, '5'), (6, '7'), (1, '4'), (8, '10')]
    

**Method #2 : Using list comprehension**  
The above functionality can also be used to solve this problem. In this, we
perform similar task as above method, just in one liner way using list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Change Datatype of Tuple Values

# Using list comprehension

 

# initializing list

test_list = [(4, 5), (6, 7), (1, 4), (8,
10)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Change Datatype of Tuple Values

# Using list comprehension

# converting to string using str()

res = [(x, str(y)) for x, y in test_list]

 

# printing result 

print("The converted records : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(4, 5), (6, 7), (1, 4), (8, 10)]
    The converted records : [(4, '5'), (6, '7'), (1, '4'), (8, '10')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

