Python – Alternate list elements as key-value pairs



Given a list, convert it into dictionary by mapping alternate elements as key-
value pairs.

>  **Input** : test_list = [2, 3, 5, 6, 7, 8]  
>  **Output** : {3: 6, 6: 8, 2: 5, 5: 7}  
>  **Explanation** : Alternate elements mapped to get key-value pairs. 3 -> 6
> [ alternate]
>
>  **Input** : test_list = [2, 3, 5, 6]  
>  **Output** : {3: 6, 2: 5}  
>  **Explanation** : Alternate elements mapped to get key-value pairs. 3 -> 6
> [ alternate]

 **Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate twice to get both the alternate elements to get desired all alternate
key-value dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate Elements Dictionary

# Using loop

 

# initializing list

test_list = [2, 3, 5, 6, 7, 8, 9, 10] 

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

 

# pairing first set of Alternate elements 

for idx in range(len(test_list) - 2):

 if idx % 2:

 res[test_list[idx]] = test_list[idx + 2]

 

# pairing other set

for idx in range(len(test_list) - 2):

 if not idx % 2:

 res[test_list[idx]] = test_list[idx + 2]

 

# printing result 

print("The extracted dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 5, 6, 7, 8, 9, 10]
    The extracted dictionary : {3: 6, 6: 8, 8: 10, 2: 5, 5: 7, 7: 9}
    

**Method #2 : Using dictionary comprehension + list slicing**

This is yet another way in which this task can be performed. In this, we slice
out both alternate elements lists and use dictionary comprehension for
pairing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate Elements Dictionary

# Using dictionary comprehension + list slicing 

 

# initializing list

test_list = [2, 3, 5, 6, 7, 8, 9, 10] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# extracting lists

list1 = test_list[1::2]

list2 = test_list[::2]

 

# constructing pairs using dictionary comprehension

res = {list1[idx] : list1[idx + 1] for idx in
range(len(list1) - 1)}

res.update({list2[idx] : list2[idx + 1] for idx in
range(len(list2) - 1)})

 

# printing result 

print("The extracted dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [2, 3, 5, 6, 7, 8, 9, 10]
    The extracted dictionary : {3: 6, 6: 8, 8: 10, 2: 5, 5: 7, 7: 9}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

