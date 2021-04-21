How to write an empty function in Python – pass statement?



In C/C++ and Java, we can write empty function as following

    
    
    // An empty function in C/C++/Java
    void fun() {  }
    

In Python, if we write something like following in Python, it would produce
compiler error.

 __

 __  
 __

 __

 __  
 __  
 __

# Incorrect empty function in Python

def fun():   
  
---  
  
__

__

Output :

    
    
    IndentationError: expected an indented block

In Python, to write empty functions, we use **pass** statement. pass is a
special statement in Python that does nothing. It only works as a dummy
statement.

 __

 __  
 __

 __

 __  
 __  
 __

# Correct way of writing empty function

# in Python

def fun(): 

 pass  
  
---  
  
 __

 __

We can use pass in empty while statement also.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Empty loop in Python

mutex = True

while (mutex == True) :

 pass  
  
---  
  
 __

 __

We can use pass in empty if else statements.

 __

 __  
 __

 __

 __  
 __  
 __

# Empty in if/else in Python

mutex = True

if (mutex == True) :

 pass

else :

 print("False")  
  
---  
  
 __

 __

This article is contributed by **Shivam Gupta**. Please write comments if you
find anything incorrect, or you want to share more information about the topic
discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

