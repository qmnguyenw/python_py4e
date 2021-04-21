Python | Optional padding in list elements



In real world problems, we sometimes require to pad the element of list
according to a condition that maximum characters have reached. Padding a
number with 0 if it’s length is less than required by any field is one of the
basic issues that occur in web forms in Web Development. Let’s discuss certain
ways in which this issue can be solved.  

 **Method #1 : Using list comprehension**  
This problem can be solved easily using the basic list comprehension in which
we just need to use string formatting to perform the optional padding with 0
if size of each element is less than the specified size.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform list element padding

# using list comprehension

 

# initializing list 

test_list = [3, 54, 4, 1, 10]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list comprehension

# to perform list element padding

res = ["%02d" %i for i in test_list]

 

# printing result 

print ("The list after element padding " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 54, 4, 1, 10]
    The list after element padding ['03', '54', '04', '01', '10']
    

  
**Method #2 : Usingstr.rjust()**  
There is a function dedicated in python to do this job. rjust() function
does the task of specifying the size of the string and also takes the
character in which the character has to be padded.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to perform list element padding

# using str.rjust()

 

# initializing list 

test_list = [3, 54, 4, 1, 10]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using str.rjust()

# to perform list element padding

res = [str(i).rjust(2, '0') for i in test_list]

 

# printing result 

print ("The list after element padding " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 54, 4, 1, 10]
    The list after element padding ['03', '54', '04', '01', '10']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

