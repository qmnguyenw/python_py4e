Python | Add Logging to a Python Script



In this article, we will learn how to have scripts and simple programs to
write diagnostic information to log files.

 **Code #1 : Using the logging module to add logging to a simple program**

 __

 __  
 __

 __

 __  
 __  
 __

import logging

 

def main():

 # Configure the logging system

 logging.basicConfig(filename ='app.log',

 level = logging.ERROR)

 

 # Variables (to make the calls that follow work)

 hostname = 'www.python.org'

 item = 'spam'

 filename = 'data.csv'

 mode = 'r'

 

 # Example logging calls (insert into your program)

 logging.critical('Host %s unknown', hostname)

 logging.error("Couldn't find %r", item)

 logging.warning('Feature is deprecated')

 logging.info('Opening file %r, mode = %r', filename, mode)

 logging.debug('Got here')

 

if __name__ == '__main__':

main()  
  
---  
  
 __

 __

  * The five logging calls ( **critical(), error(), warning(), info(), debug()** ) represent different severity levels in decreasing order.
  * The level argument to **basicConfig()** is a filter. All messages issued at a level lower than this setting will be ignored.
  * The argument to each logging operation is a message string followed by zero or more arguments. When making the final log message, the % operator is used to format the message string using the supplied arguments.

If you run the code above, the contents of the file **app.log** will be as
follow –

    
    
    CRITICAL:root:Host www.python.org unknown
    ERROR:root:Could not find 'spam'

To change the output or level of output, change the parameters to the
**basicConfig()** call as in the code given below –

 **Code #2 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

logging.basicConfig(

 filename = 'app.log', 

 level = logging.WARNING, 

 format = '%(levelname)s:%(asctime)s:%(message)s')  
  
---  
  
 __

 __

 **Output :**

    
    
    CRITICAL:2012-11-20 12:27:13, 595:Host www.python.org unknown
    ERROR:2012-11-20 12:27:13, 595:Could not find 'spam'
    WARNING:2012-11-20 12:27:13, 595:Feature is deprecated

The logging configuration is hardcoded directly into the program. To configure
it from a configuration file, change the **basicConfig()** call to the
following.

 **Code #3 :**

 __

 __  
 __

 __

 __  
 __  
 __

import logging

import logging.config

 

def main():

 # Configure the logging system

 logging.config.fileConfig('logconfig.ini')

 ...  
  
---  
  
 __

 __

Now make a configuration file that looks like this –

    
    
    [loggers]
    keys=root
    
    [handlers]
    keys=defaultHandler
    
    [formatters]
    keys=defaultFormatter
    
    [logger_root]
    level=INFO
    handlers=defaultHandler
    qualname=root
    
    [handler_defaultHandler]
    class=FileHandler
    formatter=defaultFormatter
    args=('app.log', 'a')
    
    [formatter_defaultFormatter]
    format=%(levelname)s:%(name)s:%(message)s
    

If you want to make changes to the configuration, you can simply edit the file
as appropriate.

Ignoring for the moment that there are about a million advanced configuration
options for the logging module, this solution is quite sufficient for simple
programs and scripts. Simply make sure to execute the basicConfig() call
prior to making any logging calls, and the program will generate logging
output.

  
**Reference:** https://docs.python.org/3/howto/logging-cookbook.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

