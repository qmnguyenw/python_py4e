Python – Cummulative Row Frequencies in List



Given Matrix, the task is to write a Python program to get total counts of
occurrences from the row.

>  **Input** : test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1,
> 1, 2, 2, 2]], ele_list = [1, 2, 7]  
> **Output** : [2, 2, 2, 5]  
> **Explanation** : 2 occurs 2 times in row 1 and so on.
>
>  **Input** : test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4]], ele_list =
> [1, 2, 7]  
> **Output** : [2, 2]  
> **Explanation** : 2 occurs 2 times in row 1 and so on.  
>

**Method #1 : Using** **Counter()** **+** **list comprehension**

In this, we perform the task of getting all the frequencies of all rows, and
then check in the list occurrence of the required element from the row, sum()
is used to get a summation of extracted frequencies in rows.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative Row Frequencies

# Using Counter() + list comprehension

from collections import Counter 

 

# initializing list

test_list = [[10, 2, 3, 2, 3], 

 [5, 5, 4, 7, 7, 4], 

 [1, 2], [1, 1, 2, 2, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing ele_list 

ele_list = [1, 2, 7]

 

# getting each rows counter 

freqs = [Counter(ele) for ele in test_list]

 

# getting summation of present values 

res = [sum([freq[wrd] for wrd in ele_list if wrd in
freq]) for freq in freqs]

 

# printing result 

print("Cummulative Frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1,
> 2, 2, 2]]  
> Cummulative Frequencies : [2, 2, 2, 5]

 **Method #2 : Using** **sum()** **\+ list comprehension**

In this, we perform the task of getting summation using sum(), and list
comprehension is used to check for elements in the check list and iterate
through rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative Row Frequencies

# Using sum() + list comprehension

 

# initializing list

test_list = [[10, 2, 3, 2, 3], 

 [5, 5, 4, 7, 7, 4],

 [1, 2], [1, 1, 2, 2, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing ele_list 

ele_list = [1, 2, 7]

 

# getting summation 

res = [sum(ele in ele_list for ele in sub) for sub
in test_list]

 

# printing result 

print("Cummulative Frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1,
> 2, 2, 2]]  
> Cummulative Frequencies : [2, 2, 2, 5]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

