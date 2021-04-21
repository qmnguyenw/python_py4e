Python – Element frequencies in percent range



Given a list of elements, and percent ranges, the task is to write a python
program to extract all the elements whose frequency is present in a given
range.

> **Input :** test_list = [4, 6, 2, 4, 6, 7, 8, 4, 9, 1, 4, 6, 7, 8], strt,
> end = 13, 25
>
>  **Output :** [6, 7, 8]
>
>  **Explanation :** 21.4, 14.2, 14.2 is percentage presence of 6, 7, 8
> respectively.
>
>  **Input :** test_list = [4, 6, 2, 4, 6, 7, 8, 4, 9, 1, 4, 6, 7, 8], strt,
> end = 13, 20
>
>  
>
>
>  
>
>
>  **Output :** [7, 8]
>
>  **Explanation :** 14.2, 14.2 is percentage presence of 7, 8 respectively.

Presence percentage can be simply computed by the below formula:

    
    
    Frequency of the element present in the list/ total no. of elements in the list

 **Method #1 : Using** **Counter()** **+** **set()** **+** **loop** **+**
**len()**

In this, frequencies of all the elements are extracted using loop. Next step
is to get the set of elements of list and check if frequencies are between
range specified.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Element frequencies in percent range

# Using Counter() + set() + loop + len()

from collections import Counter

 

# initializing list

test_list = [4, 6, 2, 4, 6, 7, 8, 4,
9, 1, 4, 6, 7, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing percent ranges

strt, end = 13, 25

 

# getting frequencies

freqs = dict(Counter(test_list))

 

# computing percents and assiging

res = []

for ele in set(test_list):

 percent = (freqs[ele] / len(test_list)) * 100

 if percent >= strt and percent <= end:

 res.append(ele)

 

# printing result

print("Elements within range of frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 6, 2, 4, 6, 7, 8, 4, 9, 1, 4, 6, 7, 8]
    Elements within range of frequencies : [6, 7, 8]

 **Method #2 : Using** **Counter()** **+** **loop** **+** **len()**  
This performs tasks in an almost similar manner, the key difference being the
Counter keys are iterated rather than the list elements, as they’d provide
similar output.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Element frequencies in percent range

# Using Counter() + loop + len()

from collections import Counter

 

# initializing list

test_list = [4, 6, 2, 4, 6, 7, 8, 4,
9, 1, 4, 6, 7, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing percent ranges

strt, end = 13, 25

 

# getting frequencies

freqs = dict(Counter(test_list))

 

# computing percents and assiging

# iterating from dictionary

res = []

for ele in freqs:

 percent = (freqs[ele] / len(test_list)) * 100

 if percent >= strt and percent <= end:

 res.append(ele)

 

# printing result

print("Elements within range of frequencies : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 6, 2, 4, 6, 7, 8, 4, 9, 1, 4, 6, 7, 8]
    Elements within range of frequencies : [6, 7, 8]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

