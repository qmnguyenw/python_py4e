Multiple Exception Handling in Python



Given a piece of code that can throw any of several different exceptions, and
one needs to account for all of the potential exceptions that could be raised
without creating duplicate code or long, meandering code passages.

If you can handle different exceptions all using a single block of code, they
can be grouped together in a tuple as shown in the code given below :

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 client_obj.get_url(url)

except (URLError, ValueError, SocketTimeout):

 client_obj.remove_url(url)  
  
---  
  
 __

 __

Theremove_url() method will be called if any of the listed exceptions
occurs. If, on the other hand, if one of the exceptions has to be handled
differently, then put it into its own except clause as shown in the code given
below :

 **Code #2 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

try:

 client_obj.get_url(url)

except (URLError, ValueError):

 client_obj.remove_url(url)

except SocketTimeout:

 client_obj.handle_url_timeout(url)  
  
---  
  
 __

 __

Many exceptions are grouped into an inheritance hierarchy. For such
exceptions, all of the exceptions can be caught by simply specifying a base
class. For example, instead of writing code as shown in the code given below –

 **Code #3 :**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 f = open(filename)

except (FileNotFoundError, PermissionError):

 ...  
  
---  
  
 __

 __

Except statement can be re-written as in the code given below. This works
becauseOSError is a base class that’s common to both the FileNotFoundError
and **PermissionError** exceptions.

 **Code #4 :**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 f = open(filename)

except OSError:

 ...  
  
---  
  
 __

 __

Although it’s not specific to handle multiple exceptions per **se** , it is
worth noting that one can get a handle to the thrown exception using them as a
keyword as shown in the code given below.

 **Code #5 :**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 f = open(filename)

 

except OSError as e:

 if e.errno == errno.ENOENT:

 logger.error('File not found')

 elif e.errno == errno.EACCES:

 logger.error('Permission denied')

 else:

 logger.error('Unexpected error: % d', e.errno)  
  
---  
  
 __

 __

The **e** variable holds an instance of the raised OSError. This is useful if
the exception has to be invested further, such as processing it based on the
value of the additional status code. The except clauses are checked in the
order listed and the first match executes.

 **Code #6 : Create situations where multiple except clauses might match**

 __

 __  
 __

 __

 __  
 __  
 __

f= open('missing')  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
    File "", line 1, in 
    FileNotFoundError: [Errno 2] No such file or directory: 'miss
    

__

__  
__

__

__  
__  
__

try:

 f = open('missing')

 except OSError:

 print('It failed')

 except FileNotFoundError:

 print('File not found')  
  
---  
  
 __

 __

 **Output :**

    
    
    Failed
    

Here the except FileNotFoundError clause doesn’t execute because the
OSError is more general, matches the FileNotFoundError exception, and was
listed first.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

