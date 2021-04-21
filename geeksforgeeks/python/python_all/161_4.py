Python | Swapping sublists over given range



The problem of swapping a single number can be extended to the issue of having
the list and perform the swap over an entire range which can be a useful
utility over a time. This has its application in any kind of data manipulation
in various domains. Let’s discuss certain ways in which this can be performed.  

 **Method #1 : Using list slicing and swapping**  
The lists can be swapped the same ways a variable can be swapped in python but
the difference is that instead of variable, we pass a sliced list to be
swapped.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# swapping sublist

# using list swapping and slicing

 

# initializing list 

test_list = [1, 4, 5, 8, 3, 10, 6, 7,
11, 14, 15, 2]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using list swapping and slicing 

# swapping sublist

test_list[1 : 3], test_list[6 : 8] = test_list[6 :
8], test_list[1 : 3]

 

# printing result

print ("The list after sublist swapping : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 8, 3, 10, 6, 7, 11, 14, 15, 2]
    The list after sublist swapping : [1, 6, 7, 8, 3, 10, 4, 5, 11, 14, 15, 2]
    

  
**Method #2 : Usingslice() + itertools.chain.from_iterable()**  
The slice function can perform the slice functionality to extract a sublist
from a list and from_iterable function helps to perform the swap
functionality.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate swapping

# sublist using slice() + itertools.chain.from_iterable()

import itertools

 

# initializing list 

test_list = [1, 4, 5, 8, 3, 10, 6, 7,
11, 14, 15, 2]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using slice() + itertools.chain.from_iterable()

# swapping sublist

slice_1 = test_list[1 : 3]

slice_2 = test_list[6 : 8]

slice_temp = [slice(0, 1), slice(6, 8),
slice(3, 6),

 slice(1, 3), slice(8, len(test_list))]

 

res = list(itertools.chain.from_iterable([test_list[i]

 for i in slice_temp]))

 

# printing result

print ("The list after sublist swapping : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 8, 3, 10, 6, 7, 11, 14, 15, 2]
    The list after sublist swapping : [1, 6, 7, 8, 3, 10, 4, 5, 11, 14, 15, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

