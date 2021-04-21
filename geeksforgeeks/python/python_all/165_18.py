Python | Min and Max value in list of tuples



The computation of min and max value is a quite common utility in any
programming domain be it development or any other field that includes any
programming constructs. Sometimes, data can come in the format of tuples and
min and max operations have to be performed in them. Let’s discuss certain
ways in which this is handled.

 **Method #1 : Usingmin() and max()**  
In this method, we use the python inbuilt min and max functions to perform
the task of getting the minimum and maximum value of a particular element
position.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# min and max in list of tuples

# using min() and max()

 

# initializing list 

test_list = [(2, 3), (4, 7), (8, 11), (3,
6)]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using min() and max()

# to get min and max in list of tuples

res1 = min(test_list)[0], max(test_list)[0]

res2 = min(test_list)[1], max(test_list)[1]

 

# printing result 

print ("The min and max of index 1 : " + str(res1))

print ("The min and max of index 2 : " + str(res2))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [(2, 3), (4, 7), (8, 11), (3, 6)]
    The min and max of index 1 :  (2, 8)
    The min and max of index 2 :  (3, 11)
    

  
**Method #2 : Usingmap() + zip()**  
This is the more elegant way to perform this particular task. In this task we
use map function to link the elements to the zip functions that
accumulates to perform the functionality of min function or max function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# min and max in list of tuples

# using map() + zip()

 

# initializing list 

test_list = [(2, 3), (4, 7), (8, 11), (3,
6)]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using map() + zip()

# to get min and max in list of tuples

res1 = list(map(max, zip(*test_list)))

res2 = list(map(min, zip(*test_list)))

 

# printing result 

print ("The indices wise maximum number : " + str(res1))

print ("The indices wise minimum number : " + str(res2))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [(2, 3), (4, 7), (8, 11), (3, 6)]
    The indices wise maximum number : [8, 11]
    The indices wise minimum number : [2, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

