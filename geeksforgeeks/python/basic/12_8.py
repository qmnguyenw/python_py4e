Python | Add Logging to Python Libraries



In this article, we will learn how to add a logging capability to a library,
but don’t want it to interfere with programs that don’t use logging.

For libraries that want to perform logging, create a dedicated logger object,
and initially configure it as shown in the code below –

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# abc.py

import logging

 

log = logging.getLogger(__name__)

log.addHandler(logging.NullHandler())

 

# Example function (for testing)

def func():

 log.critical('A Critical Error !')

 log.debug('A debug message')  
  
---  
  
 __

 __

With this configuration, no logging will occur by default.

 __

 __  
 __

 __

 __  
 __  
 __

import somelib

abc.func()  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    NO OUTPUT

If the logging system gets configured, log messages will start to appear.

 **Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

import logging

 

logging.basicConfig()

somelib.func()  
  
---  
  
 __

 __

 **Output :**

    
    
    CRITICAL:somelib:A Critical Error!

 **How does it work ?**

  * Libraries present a special problem for logging, since information about the environment in which they are used isn’t known.
  * As a general rule, never write library code that tries to configure the logging system on its own or which makes assumptions about an already existing logging configuration.
  * Thus, one needs to take great care to provide isolation.
  * The call to getLogger(__name__) creates a logger module that has the same name as the calling module.
  * Since all modules are unique, this creates a dedicated logger that is likely to be separate from other loggers.
  * The log.addHandler(logging.NullHandler()) operation attaches a null handler to the just created logger object. A null handler ignores all logging messages by default.
  * Thus, if the library is used and logging is never configured, no messages or warnings will appear.

Logging of individual libraries can be independently configured, regardless of
other logging settings as shown in the code given below –

 **Code #3:**

 __

 __  
 __

 __

 __  
 __  
 __

import logging

 

logging.basicConfig(level = logging.ERROR)

 

import abc

print (abc.func())

 

Change the logging level for 'abc' only

logging.getLogger('abc').level = logging.DEBUG

print (abc.func())  
  
---  
  
 __

 __

 **Output :**

    
    
    CRITICAL:abc:A Critical Error!
    DEBUG:abc:A debug message

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

