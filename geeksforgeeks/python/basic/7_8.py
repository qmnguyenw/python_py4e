Difference between Yield and Return in Python



 **Python Yield**  
It is generally used to convert a regular Python function into a generator. A
generator is a special function in Python that returns a generator object to
the caller. Since it stores the local variable states, hence overhead of
memory allocation is controlled.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate yield keyword

 

# Use of yield

def printresult(String) : 

 for i in String: 

 if i == "e": 

 yield i 

 

# initializing string 

String = "GeeksforGeeks"

ans = 0

print ("The number of 'e' in word is : ", end = "" ) 

String = String.strip() 

 

for j in printresult(String): 

 ans = ans + 1

 

print (ans)   
  
---  
  
__

__

**Output:**

    
    
    The number of 'e' in word is : 4

 **Python Return**  
It is generally used for the end of the execution and “returns” the result to
the caller statement. It can return all type of values and it returns None
when there is no expression with the statement “return”.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to show return statement

class Test: 

 def __init__(self): 

 self.str = "GeeksForGeeks"

 self.x = "Shubham Singh"

 

# This function returns an object of Test 

def fun(): 

 return Test() 

 

# Driver code to test above method 

t = fun() 

print(t.str) 

print(t.x)   
  
---  
  
__

__

**Output:**

    
    
    GeeksForGeeks
    Shubham Singh

## Difference between Python yield and Return

S.NO.| YIELD| RETURN| 1| Yield is generally used to convert a regular Python
function into a generator.| Return is generally used for the end of the
execution and “returns” the result to the caller statement.| 2| It replace the
return of a function to suspend its execution without destroying local
variables.| It exits from a function and handing back a value to its caller.|
3| It is used when the generator returns an intermediate result to the
caller.| It is used when a function is ready to send a value.| 4| Code written
after yield statement execute in next function call.| while, code written
after return statement wont execute.| 5| It can run multiple times.| It only
runs single time.| 6| Yield statement function is executed from the last state
from where the function get paused.| Every function calls run the function
from the start.  
---|---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

