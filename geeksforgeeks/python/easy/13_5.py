Python | Catching and Creating Exceptions



Catching all exceptions is sometimes used as a crutch by programmers who can’t
remember all of the possible exceptions that might occur in complicated
operations. As such, it is also a very good way to write undebuggable code.  
Because of this, if one catches all exceptions, it is absolutely critical to
log or reports the actual reason for the exception somewhere (e.g., log file,
error message printed to screen, etc.).

 **Problem –** Code that catches all the exceptions

 **Code #1 : Writing an exception handler for Exception to catch all the
exceptions.**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 ...

except Exception as e:

 ...

 # Important 

 log('Reason:', e)  
  
---  
  
 __

 __

This will catch all exceptions save **SystemExit**, **KeyboardInterrupt**,
and **GeneratorExit**.

 **Code #2 : Considering the example.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

def parse_int(s):

 try:

 n = int(v)

 except Exception:

 print("Couldn't parse")  
  
---  
  
 __

 __

 **Code #3 : Using the above function**

 __

 __  
 __

 __

 __  
 __  
 __

print (parse_int('n / a'), "\n")

 

print (parse_int('42'))  
  
---  
  
 __

 __

 **Output :**

    
    
    Couldn't parse
    
    Couldn't parse
    

At this point, the question arises how it doesn’t work. Now if the function
had been written as:

 **Code #4 :**

 __

 __  
 __

 __

 __  
 __  
 __

def parse_int(s):

 try:

 n = int(v)

 except Exception as e:

 print("Couldn't parse")

 print('Reason:', e)  
  
---  
  
 __

 __

In this case, the following output will be received, which indicates that a
programming mistake has been made.

 __

 __  
 __

 __

 __  
 __  
 __

parse_int('42')  
  
---  
  
 __

 __

 **Output :**

    
    
    Couldn't parse
    Reason: global name 'v' is not defined
    

  
**Problem –** To wrap lower-level exceptions with custom ones that have more
meaning in the context of the application (one is working on).

To create new exceptions just define them as classes that inherit from
**Exception** (or one of the other existing exception types if it makes more
sense).

 **Code #5 : Defining some custom exceptions**

 __

 __  
 __

 __

 __  
 __  
 __

class NetworkError(Exception):

 pass

class HostnameError(NetworkError):

 pass

class TimeoutError(NetworkError):

 pass

class ProtocolError(NetworkError):

 pass  
  
---  
  
 __

 __

 **Code #6 : Using these exceptions in the normal way.**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 msg = s.recv()

except TimeoutError as e:

 ...

except ProtocolError as e:

 ...  
  
---  
  
 __

 __

  * Custom exception classes should almost always inherit from the built-in Exception class, or inherit from some locally defined base exception that itself inherits from Exception.
  * BaseException is reserved for system-exiting exceptions, such as KeyboardInterrupt or SystemExit, and other exceptions that should signal the application to exit. Therefore, catching these exceptions is not the intended use case.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

