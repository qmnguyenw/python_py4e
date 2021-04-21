Python – Column Mapped Tuples to dictionary items



Given Tuple Matrix of length 2, map each column’s element value with next
column and construct dictionary keys.

>  **Input** : test_list = [[(1, 4), (6, 3), (4, 7)], [(7, 3), (10, 14), (11,
> 22)]]  
>  **Output** : {1: 7, 4: 3, 6: 10, 3: 14, 4: 11, 7: 22}  
>  **Explanation** : 1 -> 7, 4 -> 3.., as in same column and indices.
>
>  **Input** : test_list = [[(1, 4), (6, 3)], [(7, 3), (10, 14)]]  
>  **Output** : {1: 7, 4: 3, 6: 10, 3: 14}  
>  **Explanation** : Self explanatory column wise pairing.

 **Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate for all the elements with their next column elements and construct
dictionary key-value pair.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column Mapped Tuples to dictionary items

# Using loop

 

# initializing list

test_list = [[(5, 6), (7, 4), (1, 2)], 

 [(7, 3), (10, 14), (11, 22)] ]

 

# printing original list

print("The original list : " + str(test_list))

 

res = dict()

 

# loop for tuple lists

for idx in range(len(test_list) - 1):

 for idx2 in range(len(test_list[idx])):

 

 # column wise dictionary pairing 

 res[test_list[idx][idx2][0]] = test_list[idx +
1][idx2][0]

 res[test_list[idx][idx2][1]] = test_list[idx +
1][idx2][1]

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [[(5, 6), (7, 4), (1, 2)], [(7, 3), (10, 14), (11, 22)]]  
> The constructed dictionary : {5: 7, 6: 3, 7: 10, 4: 14, 1: 11, 2: 22}

 **Method #2 : Using dictionary comprehension + zip()**

The combination of above functions provides one-liner to solve this problem.
In this, we perform the task of zipping all the columns using zip() and
dictionary comprehension is used to key-value pairs.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column Mapped Tuples to dictionary items

# Using dictionary comprehension + zip()

 

# initializing list

test_list = [[(5, 6), (7, 4), (1, 2)], 

 [(7, 3), (10, 14), (11, 22)] ]

 

# printing original list

print("The original list : " + str(test_list))

 

# nested dictionary comprehension to form pairing 

# paired using zip()

res = {key[idx] : val[idx] for key, val in zip(

 *tuple(test_list)) for idx in range(len(key))}

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original list : [[(5, 6), (7, 4), (1, 2)], [(7, 3), (10, 14), (11, 22)]]  
> The constructed dictionary : {5: 7, 6: 3, 7: 10, 4: 14, 1: 11, 2: 22}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

