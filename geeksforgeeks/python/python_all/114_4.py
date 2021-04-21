Python | Multiply Integer in Mixed List of string and numbers



Sometimes, while working with Python, we can come across a problem in which we
require to find the product of list. This problem is easier to solve. But this
can get complex in case we have mixture of data types to go along with it.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using Type casting + Exception Handling**  
We can employ a brute force method to type caste each element and catch the
exception if any occurs. This can ensure that only integers are multiplied to
product and hence can solve the problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mixed List Integer Multiplication

# using type caste and exception handling

 

# initializing list

test_list = [5, 8, "gfg", 8, (5, 7), 'is',
2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Mixed List Integer Multiplication

# using type caste and exception handling

res = 1

for ele in test_list:

 try:

 res *= int(ele)

 except :

 pass

 

# printing result 

print("Product of integers in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 8, 'gfg', 8, (5, 7), 'is', 2]
    Product of integers in list : 640
    

**Method #2 : Using loop +isinstance()**  
This is brute force way in which this task can be performed. In this, we run a
loop over all the elements and perform multiplication only when we find an
integer using isinstance().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mixed List Integer Multiplication

# using loop + isinstance()

 

# initializing list

test_list = [5, 8, "gfg", 8, (5, 7), 'is',
2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Mixed List Integer Multiplication

# using loop + isinstance()

res = 1

for ele in test_list:

 if(isinstance(ele, int)):

 res *= ele

 

# printing result 

print("Product of integers in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 8, 'gfg', 8, (5, 7), 'is', 2]
    Product of integers in list : 640
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

