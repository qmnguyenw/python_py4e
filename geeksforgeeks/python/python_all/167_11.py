Python | Pair iteration in list



List iteration is common in programming, but sometimes one requires to print
the elements in consecutive pairs. This particular problem is quite common and
having a solution to it always turns out to be handy. Let’s discuss certain
ways in which this problem can be solved.  

 **Method #1 : Using list comprehension**  
List comprehension can be used to print the pairs by accessing current and
next element in the list and then printing the same. Care has to be taken
while pairing the last element with the first one to form a cyclic pair.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# pair iteration in list 

# using list comprehension

from itertools import compress

 

# initializing list 

test_list = [0, 1, 2, 3, 4, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list comprehension

# to perform pair iteration in list 

res = [((i), (i + 1) % len(test_list)) 

 for i in range(len(test_list))]

 

# printing result

print ("The pair list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [0, 1, 2, 3, 4, 5]
    The pair list is : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
    

  
**Method #2 : Usingzip() \+ list slicing**

zip function can be used to extract pairs over the list and slicing can be
used to successively pair the current element with the next one for the
efficient pairing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# pair iteration in list 

# using zip() + list slicing 

from itertools import compress

 

# initializing list 

test_list = [0, 1, 2, 3, 4, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using zip() + list slicing 

# to perform pair iteration in list 

res = list(zip(test_list, test_list[1:] +
test_list[:1]))

 

# printing result

print ("The pair list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [0, 1, 2, 3, 4, 5]
    The pair list is : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

