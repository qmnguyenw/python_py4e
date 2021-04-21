Python | Assign range of elements to List



Assigning elements to list is a common problem and many varieties of it have
been discussed in the previous articles. This particular article discusses the
insertion of range of elements in the list. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Usingextend()**  
This can be solved using the extend function in which the insertion of range
of numbers can be done on the rear end using the range function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Assigning range of elements to List

# using extend()

 

# initializing list

test_list = [3, 5, 6, 8]

 

# printing original list

print("The original list : " + str(test_list))

 

# using extend()

# Assigning range of elements to List

test_list.extend(range(6))

 

# print result

print("The list after adding range elements : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 5, 6, 8]
    The list after adding range elements : [3, 5, 6, 8, 0, 1, 2, 3, 4, 5]
    

**Method #2 Using* operator**  
This problem can also be solved using the * operator and with the advantage of
flexibility of addition of elements at any position.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Assigning range of elements to List

# using * operator

 

# initializing list

test_list = [3, 5, 6, 8]

 

# printing original list

print("The original list : " + str(test_list))

 

# using * operator

# Assigning range of elements to List

res = [3, 5, *range(6), 6, 8]

 

# print result

print("The list after adding range elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 5, 6, 8]
    The list after adding range elements : [3, 5, 0, 1, 2, 3, 4, 5, 6, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

