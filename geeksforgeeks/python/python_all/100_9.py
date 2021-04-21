Python – Repeat Alternate Elements in list



Many times we have this particular use-case in which we need to repeat
alternate element of list K times. The problems of making a double clone has
been discussed but this problem extends to allow a flexible variable to define
the number of times the element has to be repeated. Let’s discuss certain ways
in which this can be performed.

 **Method #1 : Using list comprehension**  
This particular task requires generally 2 loops and list comprehension can
perform this particular task in a one line and hence reduce the lines of codes
and improving code readability.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate Element Repetition

# using list comprehension

 

# initializing list of lists

test_list = [4, 5, 6]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring magnitude of repetition

K = 3

 

# using list comprehension

# Alternate Element Repetition

res = [ele for idx, ele in enumerate(test_list) for i in
range(K) if idx % 2 == 0]

 

# printing result 

print("The list after alternate repeating elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 6]
    The list after alternate repeating elements : [4, 4, 4, 6, 6, 6]
    

**Method #2 : Usingitertools.chain.from_iterable() + itertools.repeat()**  
This particular problem can also be solved using python inbuilt functions of
itertools library. The repeat function, as name suggests does the task of
repetition and grouping into a list is done by the from_iterable function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate Element Repetition

# using itertools.chain.from_iterable() + itertools.repeat()

import itertools

 

# initializing list of lists

test_list = [4, 5, 6]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring magnitude of repetition

K = 3

 

# using itertools.chain.from_iterable() + itertools.repeat()

# Alternate Element Repetition

res = list(itertools.chain.from_iterable(itertools.repeat(ele, K)
for idx, ele in enumerate(test_list) if idx % 2 ==
0))

 

# printing result 

print("The list after alternate repetition elements : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 6]
    The list after alternate repeating elements : [4, 4, 4, 6, 6, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

