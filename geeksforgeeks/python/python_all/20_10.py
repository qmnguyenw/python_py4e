Python program to count Bidirectional Tuple Pairs



Given Tuple list, compute bidirectional tuples.

>  **Input** : test_list = [(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]  
> **Output** : 3  
> **Explanation** : (1, 2), (2, 1); (5, 6) -> [(6, 5), (6, 5)], total 3 pairs.
>
>  **Input** : test_list = [(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)]  
> **Output** : 2  
> **Explanation** : (5, 6) -> [(6, 5), (6, 5)], total 2 pairs.  
>

**Method : Using loop**

In this we check for each element if we have any other element which is
bidirectional, Once the pair is found, counter is incremented.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Count Bidirectional Tuple Pairs

# Using loop

 

# initializing list

test_list = [(5, 6), (1, 2), (6, 5), (9,
1), (6, 5), (2, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = 0

for idx in range(0, len(test_list)):

 for iidx in range(idx + 1, len(test_list)):

 

 # checking bidirection

 if test_list[iidx][0] == test_list[idx][1] and
test_list[idx][1] == test_list[iidx][0]:

 res += 1

 

# printing result

print("Bidirectional pairs count : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]  
> Bidirectional pairs count : 3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

