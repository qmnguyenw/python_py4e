Handling EOFError Exception in Python



 **EOFError** is raised when one of the built-in functions input() or
raw_input() hits an end-of-file condition (EOF) without reading any data. This
error is sometimes experienced while using online IDEs. This occurs when we
have asked the user for input but have not provided any input in the input
box. We can overcome this issue by using **try** and **except** keywords in
Python. This is called as Exception Handling.

 **Example:** This code will generate an EOFError when there is no input given
to the online IDE.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

n= int(input())

print(n * 10)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200826203022/codechef-200x145.PNG)

This exception can be handled as:

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

try:

 n = int(input())

 print(n * 10)

 

except EOFError as e:

 print(e)  
  
---  
  
 __

 __

 **Output:**

    
    
    EOF when reading a line

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

