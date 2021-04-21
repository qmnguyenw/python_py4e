Python | Remove first K elements matching some condition



Removal of elements in list can be performed using many inbuilt functions.
Removing all or just a single occurrence removal both functions are present in
Python library. This article discusses to remove just the first _K_
occurrences of elements matching particular condition.

 **Method #1 : Naive Method**  
We can append the elements that are matching condition after _K_ occurrences
of elements have been done and hence would perform the task similar to the
removal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to remove first K elements matching condition

# using Naive Method 

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9, 8, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using Naive Method 

# to remove first K elements matching condition 

# removes first 4 odd occurrences

counter = 1

res = []

for i in test_list:

 if counter > 4 or not (i % 2 != 0):

 res.append(i)

 else:

 counter += 1

 

# printing result

print ("The filtered list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 5, 1, 6, 7, 9, 8, 5]
    The filtered list is : [6, 9, 8, 5]
    

  
**Method #2 : Usingitertools.filterfalse() + itertools.count()**  
This is different and elegant way to perform this particular task. It filters
out all the numbers that become greater than K as counter reaches K and
matches against the condition. This is one-liner and preferred method to
achieve this task.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to remove first K elements matching condition

# using itertools.filterfalse() + itertools.count()

from itertools import filterfalse, count

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9, 8, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using itertools.filterfalse() + itertools.count()

# to remove first K elements matching condition 

# removes first 4 odd occurrences

res = filterfalse(lambda i, counter = count(): i % 2 !=
0 and

 next(counter) < 4, test_list)

 

# printing result

print ("The filtered list is : " + str(list(res)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 5, 1, 6, 7, 9, 8, 5]
    The filtered list is : [6, 9, 8, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

