Python – Consecutive Ranges of K greater than N



Given a list of elements, the task is to write a Python program to get all
ranges of K greater than N.

>  **Input :** [2, 6, 6, 6, 6, 5, 4, 6, 6, 8, 4, 6, 6, 6, 2, 6], K = 6, N = 3
>
>  **Output :** [(1, 4), (11, 13)]
>
>  **Explanation :** 6 is consecutive from index 1 to 4, hence 1-4 in result.
> 7-8 also has 6, but its less than 3 size range, hence not included in
> result.
>
>  **Input :** [2, 1, 1, 1, 1, 5, 4, 1, 1], K = 1, N = 3
>
>  
>
>
>  
>
>
>  **Output :** [(1, 4)]
>
>  **Explanation :** 1 is consecutive from index 1 to 4, hence 1-4 in result.
> 7-8 also has 1, but its less than 3 size range, hence not included in
> result.

 **Method #1: Using** **loop**

In this, each occurrence of K is traced and a nested loop is employed to get
the size of the range. If the range size is greater than N, the range is
recorded in the result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Ranges of K greater than N

# Using loop

 

# initializing list

test_list = [2, 6, 6, 6, 6, 5, 4, 6, 

 6, 8, 4, 6, 6, 6, 2, 6]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

# initializing N

N = 3

 

res = []

strt, end = 0, 0

prev = 1

for idx, ele in enumerate(test_list):

 

 # if ele K assign end

 if ele == K:

 end = idx

 

 # if prev ele not K, reassign start

 if prev != K: # previous item one

 strt = idx

 else:

 

 # if range is greater than N, append to result

 if prev == K and end - strt + 1 >= N:

 res.append((strt, end))

 prev = ele

 

# printing result

print("The extracted ranges : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [2, 6, 6, 6, 6, 5, 4, 6, 6, 8, 4, 6, 6, 6, 2, 6]
>
> The extracted ranges : [(1, 4), (11, 13)]

 **Method #2 : Using** **enumerate()** **+** **zip()** **+** **list slicing**
**+** **list comprehension**

In this, all the pairs of ending and starting of K are extracted with previous
and next element respectively. The pairs index are then checked to have
required ranges in between to add to the result in the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Ranges of K greater than N

# Using enumerate() + zip() + list slice + list comprehension

 

# initializing list

test_list = [2, 6, 6, 6, 6, 5, 4, 6, 

 6, 8, 4, 6, 6, 6, 2, 6]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 6

 

# initializing N

N = 3

 

# getting break pairs indices

brk_pairs = [idx for idx, (x, y) in enumerate(

 zip(test_list, test_list[1:]), 

 1) if (x == K) != (y == K)]

 

# The ranges are checked for size required

res = [(idx, ele - 1) for idx, ele in zip([K] +
brk_pairs, 

 brk_pairs + [len(test_list)])

 if ele - idx >= N and test_list[idx] == K]

 

# printing result

print("The extracted ranges : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [2, 6, 6, 6, 6, 5, 4, 6, 6, 8, 4, 6, 6, 6, 2, 6]
>
> The extracted ranges : [(1, 4), (11, 13)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

