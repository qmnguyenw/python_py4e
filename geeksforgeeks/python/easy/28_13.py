Defining Clean Up Actions in Python



Think of a task you will always want your program to do, whether it runs
perfectly or raise any kind of error. For example, We use of **try** statement
which has an optional clause – **“finally”** to perform clean up actions, that
must be executed under all conditions.  
 **Cleanup actions:** Before leaving the **try** statement, **“finally”**
clause is always executed, whether any exception is raised or not. These are
clauses which are intended to define clean-up actions that must be executed
under all circumstances.  
Whenever an exception occurs and is not being handled by the **except**
clause, first **finally** will occur and then the error is raised as default
[Code 3].

 **Python Programs illustrating “Defining Clean Up Actions”**

 **Code 1 :** Code works normally and clean-up action is taken at the end

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# clean up actions

def divide(x, y):

 try:

 # Floor Division : Gives only Fractional Part as Answer

 result = x // y

 except ZeroDivisionError:

 print("Sorry ! You are dividing by zero ")

 else:

 print("Yeah ! Your answer is :", result)

 finally:

 print("I'm finally clause, always raised !! ")

 

# Look at parameters and note the working of Program

divide(3, 2)  
  
---  
  
 __

 __

 **Output :**

    
    
    Yeah ! Your answer is : 1
    I'm finally clause, always raised !! 
    

  
**Code 2 :** Code raise error and is carefully handled in the **except**
clause. Note that Clean-up action is taken at the end.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# clean up actions

def divide(x, y):

 try:

 # Floor Division : Gives only Fractional Part as Answer

 result = x // y

 except ZeroDivisionError:

 print("Sorry ! You are dividing by zero ")

 else:

 print("Yeah ! Your answer is :", result)

 finally:

 print("I'm finally clause, always raised !! ")

 

# Look at parameters and note the working of Program

divide(3, 0)  
  
---  
  
 __

 __

 **Output :**

    
    
    Sorry ! You are dividing by zero 
    I'm finally clause, always raised !!
    

**Code 3 :** Code, raise error but we don’t have any **except** clause to
handle it. So, clean-up action is taken first and then the **error(by default)
is raised** by the compiler.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate

# clean up actions

def divide(x, y):

 try:

 # Floor Division : Gives only Fractional Part as Answer

 result = x // y

 except ZeroDivisionError:

 print("Sorry ! You are dividing by zero ")

 else:

 print("Yeah ! Your answer is :", result)

 finally:

 print("I'm finally clause, always raised !! ")

 

# Look at parameters and note the working of Program

divide(3, "3")  
  
---  
  
 __

 __

 **Output :**

    
    
    I'm finally clause, always raised !! 

**Error:**

    
    
    Traceback (most recent call last):
      File "C:/Users/DELL/Desktop/Code.py", line 15, in 
        divide(3, "3")
      File "C:/Users/DELL/Desktop/Code.py", line 7, in divide
        result = x // y
    TypeError: unsupported operand type(s) for //: 'int' and 'str'
    

This article is contributed by **Mohit Gupta_OMG 😀**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

