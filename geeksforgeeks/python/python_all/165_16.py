Python | Zip different sized list



In Python, zipping is a utility where we pair one list with the other.
Usually, this task is successful only in the cases when the sizes of both the
lists to be zipped are of the same size. But sometimes we require that
different sized lists also to be zipped. Let’s discuss certain ways in which
this problem can be solved if it occurs.

 **Method #1 : Usingenumerate() \+ loop**  
This is the way in which we use the brute force method to achieve this
particular task. In this process, we loop both the list and when one becomes
larger than other we cycle the elements to begin them from the beginning.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# zipping of two different size list 

# using enumerate() + loop

 

# initializing lists

test_list1 = [7, 8, 4, 5, 9, 10]

test_list2 = [1, 5, 6]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using enumerate() + loop

# zipping of two different size list 

res = []

for i, j in enumerate(test_list1):

 res.append((j, test_list2[i % len(test_list2)]))

 

# printing result 

print ("The zipped list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [7, 8, 4, 5, 9, 10]
    The original list 2 is : [1, 5, 6]
    The zipped list is : [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
    

  
**Method #2 : Usingitertools.cycle()**  
This is yet another way to perform this particular task, in this we cycle the
smaller list so that it can begin zipping from beginning in case the smaller
list gets exhausted using a zip function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# zipping of two different size list 

# using itertools.cycle()

from itertools import cycle

 

# initializing lists

test_list1 = [7, 8, 4, 5, 9, 10]

test_list2 = [1, 5, 6]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using itertools.cycle()

# zipping of two different size list 

res = list(zip(test_list1, cycle(test_list2))

 if len(test_list1) > len(test_list2)

 else zip(cycle(test_list1), test_list2))

 

# printing result 

print ("The zipped list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [7, 8, 4, 5, 9, 10]
    The original list 2 is : [1, 5, 6]
    The zipped list is : [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

