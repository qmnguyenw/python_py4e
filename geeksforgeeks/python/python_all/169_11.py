Python | Inserting item in sorted list maintaining order



Working with sorted list is essential because mostly the data we get is
ordered. Any query can come to insert the new data into its appropriate
position. Hence requires to know how to perform these dynamic queries. Lets
discuss certain ways in which this can be performed.  

 **Method #1 : Naive Method**  
In this method, we just simply test for the value and check if next element is
greater than the input element and store the index which is then used to slice
in that element at that position.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# insertion in sorted list

# using naive method 

 

# initializing list

test_list = [1, 2, 3, 6, 7]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# insert element

k = 5

 

# using naive method 

# insertion in sorted list

# using naive method 

for i in range(len(test_list)):

 if test_list[i] > k:

 index = i

 break

res = test_list[: i] + [k] + test_list[i :]

 

# printing result

print ("The list after insertion is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 2, 3, 6, 7]
    The list after insertion is : [1, 2, 3, 5, 6, 7]
    

  
**Method #2 : Usingbisect.insort()**  
This is more concise and recommended method to perform this particular task.
This method is designed for this particular task and performs this task in
most efficient manner.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# insertion in sorted list

# using bisect.insort()

import bisect

 

# initializing list

test_list = [1, 2, 3, 6, 7]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# insert element

k = 5

 

# using bisect.insort()

# insertion in sorted list

# using naive method 

bisect.insort(test_list, k) 

 

# printing result

print ("The list after insertion is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 2, 3, 6, 7]
    The list after insertion is : [1, 2, 3, 5, 6, 7]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

