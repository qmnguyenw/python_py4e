Python | Index specific cyclic iteration in list



The problem of cyclic iteration is quite common, but sometimes, we come
through the issue in which we require to process the list in a way in which it
is cyclic iterated that too starting from a specific index. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using% operator + loop**  
The % operator can be used to cycle the out of bound index value to begin from
the beginning of list to form a cycle and hence help in the cyclic iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# cyclic iteration in list 

# using % operator and loop

 

# initializing tuple list 

test_list = [5, 4, 2, 3, 7]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# starting index 

K = 3

 

# using % operator and loop

# cyclic iteration in list 

res = []

for i in range(len(test_list)):

 res.append(test_list[K % len(test_list)])

 K = K + 1

 

# printing result 

print ("The cycled list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 4, 2, 3, 7]
    The cycled list is : [3, 7, 5, 4, 2]
    

  
**Method #2 : Usingitertools.cycle() + itertools.islice() +
itertools.dropwhile()**  
The itertools library has built in functions that can help achieve to the
solution of this particular problem. The cycle function performs the cycling
part, dropwhile function brings the cycle to begin of list and islice function
specifies the cycle size.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# cyclic iteration in list using itertools

from itertools import cycle, islice, dropwhile

 

# initializing tuple list 

test_list = [5, 4, 2, 3, 7]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# starting index 

K = 3

 

# using itertools methods for

# cyclic iteration in list 

cycling = cycle(test_list) 

skipping = dropwhile(lambda x: x != K, cycling) 

slicing = islice(skipping, None, len(test_list))

slicing = list(slicing)

 

# printing result 

print ("The cycled list is : " + str(slicing))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 4, 2, 3, 7]
    The cycled list is : [3, 7, 5, 4, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

