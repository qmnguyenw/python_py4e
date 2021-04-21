Python | Repeat each element K times in list



Many times we have this particular use-case in which we need to repeat each
element of list K times. The problems of making a double clone have been
discussed but this problem extends to allow a flexible variable to define the
number of times the element has to be repeated. Let’s discuss certain ways in
which this can be performed.

 **Method #1 : Using list comprehension**  
This particular task requires generally 2 loops and list comprehension can
perform this particular task in one line and hence reduce the lines of codes
and improving code readability.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# repeat element K times

# using list comprehension

 

# initializing list of lists

test_list = [4, 5, 6]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring magnitude of repetition

K = 3

 

# using list comprehension

# repeat elements K times

res = [ele for ele in test_list for i in range(K)]

 

# printing result 

print("The list after adding elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 6]
    The list after adding elements :  [4, 4, 4, 5, 5, 5, 6, 6, 6]
    

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

# repeat element K times

# using itertools.chain.from_iterable() + itertools.repeat()

import itertools

 

# initializing list of lists

test_list = [4, 5, 6]

 

# printing original list 

print("The original list : " + str(test_list))

 

# declaring magnitude of repetition

K = 3

 

# using itertools.chain.from_iterable() 

# + itertools.repeat() repeat elements K times

res = list(itertools.chain.from_iterable(itertools.repeat(i, K)

 for i in test_list))

 

# printing result 

print("The list after adding elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 6]
    The list after adding elements :  [4, 4, 4, 5, 5, 5, 6, 6, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

