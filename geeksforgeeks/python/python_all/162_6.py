Python | Largest number possible from list of given numbers



Given a list of numbers, the task is to find the largest number possible from
the elements given in the list.

This is one of the problems that is essential in competitive point of view and
this article discusses various shorthands to solve this problem in Python.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using sorted() + lambda**  
The combination of the above function can be used to perform this task. The
sorted function performs the reverse sort of list indices converted into
string and lambda functions handles the conversion and iteration operation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# largest possible number in list

# using sorted() + lambda

from functools import cmp_to_key

 

# initializing list 

test_list = [23, 65, 98, 3, 4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using sorted() + lambda

# largest possible number in list 

res = sorted(test_list, key = cmp_to_key(lambda i, j: -1

 if str(j) + str(i) < str(i) + str(j) else 1))

 

# printing result 

print ("The largest possible number : " +
''.join(map(str,res)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [23, 65, 98, 3, 4]
    The largest possible number : 98654323
    

  
**Method #2 : Usingitertools.permutation() \+ join() + max()**  
The itertools.permutation can be used to get possible permutation and max
function chooses the maximum of it after being converted to integer as a
result of joined output as given by join function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# largest possible number in list

# using itertools.permutation() + join() + max()

from itertools import permutations

 

# initializing list 

test_list = [23, 65, 98, 3, 4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using itertools.permutation() + join() + max()

# largest possible number in list 

res = int(max((''.join(i) for i in permutations(str(i)


 for i in test_list)), key = int))

 

# printing result 

print ("The largest possible number : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [23, 65, 98, 3, 4]
    The largest possible number : 98654323
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

