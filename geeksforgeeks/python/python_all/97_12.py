Python | Average of two lists



The problem of finding a average values in a list is quite common. But
sometimes this problem can be extended in two lists and hence becomes a
modified problem. This article discusses shorthands by which this task can be
performed easily. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Usingsum() + len() + “+” operator**  
The average value can be determined by the conventional sum() and len function
of python and the extension of one to two lists can be dealt using the “+”
operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Average of two lists

# using sum() + len() + "+" operator

 

# initializing lists

test_list1 = [1, 3, 4, 5, 2, 6]

test_list2 = [3, 4, 8, 3, 10, 1]

 

# printing the original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# Average of two lists

# using sum() + len() + "+" operator

res = sum(test_list1 + test_list2) / len(test_list1 +
test_list2)

 

# printing result

print ("The Average of both lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 4, 5, 2, 6]
    The original list 2 is : [3, 4, 8, 3, 10, 1]
    The Average of both lists is : 4.166666666666667
    

**Method #2 : Usingsum() + len() + chain()**  
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

# Average of two lists

# using sum() + len() + "+" operator

from itertools import chain

 

# initializing lists

test_list1 = [1, 3, 4, 5, 2, 6]

test_list2 = [3, 4, 8, 3, 10, 1]

 

# printing the original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# Average of two lists

# using sum() + len() + "+" operator

res = sum(chain(test_list1, test_list2)) /
len(list(chain(test_list1, test_list2)))

 

# printing result

print ("The Average of both lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 4, 5, 2, 6]
    The original list 2 is : [3, 4, 8, 3, 10, 1]
    The Average of both lists is : 4.166666666666667
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

