Python | List Initialization with alternate 0s and 1s



The initialization of list with a single number is a generic problem whose
solution has been dealt many number of times. But sometimes we require to
initialize the list with elements alternatively repeating K no. of times. This
has use cases in M.L or A.I algorithms which require presetting of data in
lists. Let’s discuss certain ways in which this problem is solved.

 **Method #1 : Using list comprehension**  
In this method, we insert elements in the list alternatively for the specific
number of times of each elements’ occurrence. It takes the remainder of sum of
counts of both occurrences of elements with particular occurrence of element
for cycle computation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform cyclic initialization

# using list comprehension

 

# count of 1 

count_1 = 4

 

# count of 0

count_0 = 3

 

# total length of list 

size = 14

 

# initializing list cyclically

# using list comprehension

test_list = [ 1 if i % (count_1 + count_0) < count_1 

 else 0 for i in range(size) ]

 

# printing list after change

print ("The list after initializing : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The list after initializing : [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    

  
**Method #2 : Usingitertools.cycle() + itertools.islice()**  
This is the most pythonic way in which we can perform the cyclic
initialization. Slice each of the part of list into the allotted element size
in a cyclic manner using cycle function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform cyclic initialization

# using itertools.cycle() + itertools.islice()

import itertools

 

# count of 1 

count_1 = 4

 

# count of 0

count_0 = 3

 

# total length of list 

size = 16

 

# getting pattern

pattern = [1] * count_1 + [0] * count_0

 

# initializing list cyclically

# using itertools.cycle() + itertools.islice()

test_list = list(itertools.islice(itertools.cycle(pattern), size))

 

# printing list after change

print ("The list after initializing : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The list after initializing : [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

