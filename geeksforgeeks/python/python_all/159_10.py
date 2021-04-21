Python | Maximum and Minimum value from two lists



The problem of finding a maximum and minimum values in a list is quite common.
But sometimes this problem can be extended in two lists and hence becomes a
modified problem. This article discusses shorthands by which this task can be
performed easily. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Using max() + min() + “+” operator**  
The maximum and minimum values can be determined by the conventional max and
min function of python and the extension of one to two lists can be dealt
using the “+” operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# maximum and minimum values in two lists 

# using max() + min() + "+" operator

 

# initializing lists

test_list1 = [1, 3, 4, 5, 2, 6]

test_list2 = [3, 4, 8, 3, 10, 1]

 

# printing the original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using max() + min() + "+" operator

# maximum and minimum values in two lists 

max_all = max(test_list1 + test_list2)

min_all = min(test_list1 + test_list2)

 

# printing result

print ("The maximum of both lists is : " + str(max_all))

print ("The minimum of both lists is : " + str(min_all))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [1, 3, 4, 5, 2, 6]
    The original list 2 is : [3, 4, 8, 3, 10, 1]
    The maximum of both lists is : 10
    The minimum of both lists is : 1
    

  
**Method #2 : Usingmax() + min() + chain()**  
Another method to perform this particular task is by using the chain function
which performs the task similar to the “+” operator but using an iterator,
hence faster.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# maximum and minimum values in two lists 

# using max() + min() + "+" operator

from itertools import chain

 

# initializing lists

test_list1 = [1, 3, 4, 5, 2, 6]

test_list2 = [3, 4, 8, 3, 10, 1]

 

# printing the original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using max() + min() + "+" operator

# maximum and minimum values in two lists 

max_all = max(chain(test_list1, test_list2))

min_all = min(chain(test_list1, test_list2))

 

# printing result

print ("The maximum of both lists is : " + str(max_all))

print ("The minimum of both lists is : " + str(min_all))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [1, 3, 4, 5, 2, 6]
    The original list 2 is : [3, 4, 8, 3, 10, 1]
    The maximum of both lists is : 10
    The minimum of both lists is : 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

