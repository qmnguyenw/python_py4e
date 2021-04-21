Python | Add comma between numbers



Sometimes, while working with currencies, we need to put commas between
numbers to represent a currency, hence given a string, we can have a problem
to insert commas into them. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Usingstr.format()**  
The string format function can be used by supplying the valid formatter to
perform the formatting. The string formatter is called with the value as
argument to perform this particular task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adding comma between numbers

# Using str.format()

 

# initializing number

test_num = 1234567

 

# printing original number 

print("The original number is : " + str(test_num))

 

# Using str.format()

# Adding comma between numbers

res = ('{:, }'.format(test_num))

 

# printing result 

print("The number after inserting commas : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original number is : 1234567
    The number after inserting commas : 1, 234, 567
    

**Method #2 : Usingformat()**  
This task can also be performed without taking the help of format library of
strings but the normal format library that can use the “d” notation of numbers
and simply insert the commas where required.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adding comma between numbers

# Using format()

 

# initializing number

test_num = 1234567

 

# printing original number 

print("The original number is : " + str(test_num))

 

# Using format()

# Adding comma between numbers

res = (format (test_num, ', d'))

 

# printing result 

print("The number after inserting commas : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original number is : 1234567
    The number after inserting commas : 1, 234, 567
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

