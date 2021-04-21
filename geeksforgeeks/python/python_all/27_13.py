Python – Cross Pattern Pairs in List



Given two lists, pair them diagonally, in cross pattern [works for even and
equi-length lists].

>  **Input** : test_list1 = [4, 5, 6, 2], test_list2 = [9, 1, 4, 7]  
> **Output** : [(4, 1), (5, 9), (6, 7), (2, 4)]  
> **Explanation** : Crosslinked diagonally, 4->1, 5->9.
>
>  **Input** : test_list1 = [4, 5], test_list2 = [9, 1]  
> **Output** : [(4, 1), (5, 9)]  
> **Explanation** : Crosslinked diagonally, 4->1, 5->9\.  
>

**Method #1 : Using loop**

In this, we iterate through list and test for even or odd index, in case of
even index, we pair with next element of other list, or else we pair with
previous element of other list. This way cross pattern tuples are formed.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Pattern Pairs in List

# Using loop

 

 

# function to generate cross pattern pairs

def crossPair(test_list1, test_list2):

 

 # lengths of both lists should be equal

 if len(test_list1) != len(test_list2):

 return -1

 

 res = []

 for idx in range(len(test_list1)):

 

 # checking for conditions

 if idx % 2 == 0:

 res.append((test_list1[idx], test_list2[idx + 1]))

 else:

 res.append((test_list1[idx], test_list2[idx - 1]))

 return res

 

 

# initializing lists

input_list1 = [4, 5, 6, 2, 8, 9]

input_list2 = [9, 1, 4, 7, 9, 2]

 

# printing original lists

print("The original list 1 is : " + str(input_list1))

print("The original list 2 is : " + str(input_list2))

 

# printing result

print("Paired List elements : ", crossPair(input_list1, input_list2))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [4, 5, 6, 2, 8, 9]  
> The original list 2 is : [9, 1, 4, 7, 9, 2]  
> Paired List elements : [(4, 1), (5, 9), (6, 7), (2, 4), (8, 2), (9, 9)]

 **Method #2 : Using list comprehension**

Uses similar approach as above method, difference being list comprehension is
used as a single linear alternative to solve this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Pattern Pairs in List

# Using list comprehension

 

 

# function to generate cross pattern pairs

def crossPair(test_list1, test_list2):

 

 # lengths of both lists should be equal

 if len(test_list1) != len(test_list2):

 return -1

 

 # list comprehension used as one liner alternative

 res = [(test_list1[idx], test_list2[idx + 1]) if idx %
2 ==

 0 else (test_list1[idx], test_list2[idx - 1]) for idx in
range(len(test_list1))]

 return res

 

 

# initializing lists

input_list1 = [4, 5, 6, 2, 8, 9]

input_list2 = [9, 1, 4, 7, 9, 2]

 

# printing original lists

print("The original list 1 is : " + str(input_list1))

print("The original list 2 is : " + str(input_list2))

 

# printing result

print("Paired List elements : ", crossPair(input_list1, input_list2))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [4, 5, 6, 2, 8, 9]  
> The original list 2 is : [9, 1, 4, 7, 9, 2]  
> Paired List elements : [(4, 1), (5, 9), (6, 7), (2, 4), (8, 2), (9, 9)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

