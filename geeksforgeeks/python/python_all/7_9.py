Python program to randomly create N Lists of K size



Given a List, the task is to write a Python program to randomly generate N
lists of size K.

 **Examples:**

>  **Input :** test_list = [6, 9, 1, 8, 4, 7], K, N = 3, 4
>
>  **Output :** [[8, 7, 6], [8, 6, 9], [8, 1, 6], [7, 8, 9]]
>
>  **Explanation :** 4 rows of 3 length are randomly extracted.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [6, 9, 1, 8, 4, 7], K, N = 2, 3
>
>  **Output :** [[7, 6], [7, 9], [1, 9]]
>
>  **Explanation :** 3 rows of 2 length are randomly extracted.

 **Method 1 : Using** **generator** **+** **shuffle()**

In this, getting random elements is done using shuffle(), and yield with
slicing is used to get K size of shuffled list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K sized N random elements

# Using generator + shuffle()

from random import shuffle

 

# get random list 

def random_list(sub, K):

 while True:

 shuffle(sub)

 yield sub[:K]

 

# initializing list

test_list = [6, 9, 1, 8, 4, 7]

 

# initializing K, N 

K, N = 3, 4

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

# getting N random elements 

for idx in range(0, N):

 res.append(next(random_list(test_list, K)))

 

# printing result

print("K sized N random lists : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [6, 9, 1, 8, 4, 7]
    K sized N random lists : [[7, 1, 8], [8, 6, 1], [4, 9, 6], [6, 9, 1]]

 **Method 2 : Using** **product()** **+** **sample()**

In this, all the possible permutations of K elements are extracted using
product(), and from that random sampling of N lists are done.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K sized N random elements

# Using product() + sample()

from random import sample

import itertools

 

# initializing list

test_list = [6, 9, 1, 8, 4, 7]

 

# initializing K, N 

K, N = 3, 4

 

# printing original list

print("The original list is : " + str(test_list))

 

# get all permutations

temp = (idx for idx in itertools.product(test_list, repeat =
K))

 

# get Random N from them

res = sample(list(temp), N)

res = list(map(list, res))

 

# printing result

print("K sized N random lists : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [6, 9, 1, 8, 4, 7]
    K sized N random lists : [[1, 1, 1], [6, 9, 4], [8, 7, 6], [4, 8, 8]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

