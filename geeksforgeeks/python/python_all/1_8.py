Python – Split list into all possible tuple pairs



Given a list, the task is to write a python program that can split it into all
possible tuple pairs combinations.

> **Input :** test_list = [4, 7, 5, 1, 9]
>
>  **Output :** [[4, 7, 5, 1, 9], [4, 7, 5, (1, 9)], [4, 7, (5, 1), 9], [4, 7,
> (5, 9), 1], [4, (7, 5), 1, 9], [4, (7, 5), (1, 9)], [4, (7, 1), 5, 9], [4,
> (7, 1), (5, 9)], [4, (7, 9), 5, 1], [4, (7, 9), (5, 1)], [(4, 7), 5, 1, 9],
> [(4, 7), 5, (1, 9)], [(4, 7), (5, 1), 9], [(4, 7), (5, 9), 1], [(4, 5), 7,
> 1, 9], [(4, 5), 7, (1, 9)], [(4, 5), (7, 1), 9], [(4, 5), (7, 9), 1], [(4,
> 1), 7, 5, 9], [(4, 1), 7, (5, 9)], [(4, 1), (7, 5), 9], [(4, 1), (7, 9), 5],
> [(4, 9), 7, 5, 1], [(4, 9), 7, (5, 1)], [(4, 9), (7, 5), 1], [(4, 9), (7,
> 1), 5]]
>
>  **Explanation :** All pairs partitions are formed.
>
> I **nput :** test_list = [4, 7, 5, 1]
>
>  
>
>
>  
>
>
>  **Output :** [[4, 7, 5, 1], [4, 7, (5, 1)], [4, (7, 5), 1], [4, (7, 1), 5],
> [(4, 7), 5, 1], [(4, 7), (5, 1)], [(4, 5), 7, 1], [(4, 5), (7, 1)], [(4, 1),
> 7, 5], [(4, 1), (7, 5)]]
>
>  **Explanation :** All pairs partitions are formed.

 **Approach:** Using slicing and recursion

In this, we perform all pair creation from 1st element, and using recursion
multiple elements are converted into pairs by appropriate partitioning.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def pairings(test_list):

 if len(test_list) <= 1:

 return [test_list]

 

 # keeping 1st element and attaching every element with it

 parts = [[test_list[0]] + ele for ele in
pairings(test_list[1:])]

 for idx in range(1, len(test_list)):

 

 # pairing all possible from second element

 parts.extend([[(test_list[0], test_list[idx])] +

 ele for ele in pairings(test_list[1: idx]

 + test_list[idx + 1:])])

 

 return parts

 

 

# initializing list

test_list = [4, 7, 5, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling util. fnction

res = pairings(test_list)

 

# printing result

print("Created partitions : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [4, 7, 5, 1]
>
> Created partitions : [[4, 7, 5, 1], [4, 7, (5, 1)], [4, (7, 5), 1], [4, (7,
> 1), 5], [(4, 7), 5, 1], [(4, 7), (5, 1)], [(4, 5), 7, 1], [(4, 5), (7, 1)],
> [(4, 1), 7, 5], [(4, 1), (7, 5)]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

