Python – Restrict Tuples by frequency of first element’s value



Given a Tuple list, the task is to write a Python program to restrict the
frequency of the 1st element of tuple values to at most K.

 **Examples:**

>  **Input :** test_list = [(2, 3), (3, 3), (1, 4), (2, 4), (2, 5), (3, 4),
> (1, 4), (3, 4), (4, 7)], K = 2
>
>  **Output :** [(2, 3), (3, 3), (1, 4), (2, 4), (3, 4), (1, 4), (4, 7)]
>
>  **Explanation :** 2 occurs 2 times in result list, (2, 5), the 3rd
> occurrence is omitted.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [(2, 3), (3, 3), (1, 4), (2, 4), (2, 5), (3, 4),
> (1, 4), (3, 4), (4, 7)], K = 3
>
>  **Output :** [(2, 3), (3, 3), (1, 4), (4, 7)]
>
>  **Explanation :** 2, 3, 1, 4 restricted to their 1st occurrence.

 **Method 1 : Using loop +** **keys()** **\+ conditional statements**

In this, we perform task of memorizing count of each element of 1st position
of tuples, and omit if its occurrences increases K.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Restrict Tuples by frequency of first element's value

# Using loop + keys() + conditional statements

 

# initializing list

test_list = [(2, 3), (3, 3), (1, 4), (2,
4), (2, 5),

 (3, 4), (1, 4), (3, 4), (4, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

res = []

mem = dict()

for sub in test_list:

 

 # check in memory

 if sub[0] not in mem.keys():

 mem[sub[0]] = 1

 else:

 mem[sub[0]] += 1

 

 # add if less than K frequency

 if mem[sub[0]] <= K:

 res.append(sub)

 

# printing result

print("Filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(2, 3), (3, 3), (1, 4), (2, 4), (2, 5), (3, 4), (1,
> 4), (3, 4), (4, 7)]
>
> Filtered tuples : [(2, 3), (3, 3), (1, 4), (2, 4), (3, 4), (1, 4), (4, 7)]
>
>  
>
>
>  
>

 **Method #2 : Using** **defaultdict()** **+** **filter()** **\+ lambda**

In this, we perform task of memorizing using defaultdict() and filter() and
lambda functions are used for the task of checking and adding to result upon
meeting of condition.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Restrict Tuples by frequency of first element's value

# Using defaultdict() + filter() + lambda

from collections import defaultdict

 

# initializing list

test_list = [(2, 3), (3, 3), (1, 4), (2,
4), (2, 5),

 (3, 4), (1, 4), (3, 4), (4, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 2

 

mem = defaultdict(list)

 

# filtering result using filter() and lambda function

res = list(filter(lambda sub: mem[sub[0]].append(

 sub[0]) or len(mem[sub[0]]) <= K, test_list))

 

# printing result

print("Filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(2, 3), (3, 3), (1, 4), (2, 4), (2, 5), (3, 4), (1,
> 4), (3, 4), (4, 7)]
>
> Filtered tuples : [(2, 3), (3, 3), (1, 4), (2, 4), (3, 4), (1, 4), (4, 7)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

