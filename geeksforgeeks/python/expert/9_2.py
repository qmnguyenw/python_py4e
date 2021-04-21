Python | assert keyword



Assertions in any programming language are the debugging tools which help in
smooth flow of code. Assertions are mainly assumptions that a programmer knows
always wants to be true and hence puts them in code so that failure of them
doesn’t allow the code to execute further.

In python assert keyword helps in achieving this task. This statement simply
takes input a boolean condition, which when returns true doesn’t return
anything, but if it is computed to be false, then it raises an
AssertionError along with the optional message provided.  

> Syntax : **assert condition, error_message(optional)**
>
>  **Parameters :**  
>  **condition :** The boolean condition returning true or false.  
>  **error_message :** The optional argument to be printed in console in case
> of AssertionError
>
>  **Returns :**  
>  Returns AssertionError, in case the condition evaluates to false along
> with the error message which when provided.
>
>  
>
>
>  
>

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# working of assert 

 

# initializing number

a = 4

b = 0

 

# using assert to check for 0

print ("The value of a / b is : ")

assert b != 0, "Divide by 0 error"

print (a / b)  
  
---  
  
 __

 __

 **Output :**

    
    
    The value of a/b is : 
    

**Runtime Exception :**

    
    
    Traceback (most recent call last):
      File "/home/40545678b342ce3b70beb1224bed345f.py", line 10, in 
        assert b != 0, "Divide by 0 error"
    AssertionError: Divide by 0 error
    

**Practical Application :** This has a much greater utility in testing and
Quality assurance role in any development domain. Different types of
assertions are used depending upon the application. Below is the simpler
demonstration of program that only allows only the batch with all hot food to
be dispatched, else rejects whole batch.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# working of assert 

# Application

 

# initializing list of foods temperatures

batch = [ 40, 26, 39, 30, 25, 21]

 

# initializing cut temperature

cut = 26

 

# using assert to check for temperature greater than cut

for i in batch:

 assert i >= 26, "Batch is Rejected"

 print (str(i) + " is O.K" )  
  
---  
  
 __

 __

 **Output :**

    
    
    40 is O.K
    26 is O.K
    39 is O.K
    30 is O.K
    

**Runtime Exception :**

    
    
    Traceback (most recent call last):
      File "/home/bd45fb65343814a85b6c19bbe366b419.py", line 13, in 
        assert i >= 26, "Batch is Rejected"
    AssertionError: Batch is Rejected
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

