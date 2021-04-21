str() vs repr() in Python



str() and repr() both are used to get a string representation of object.

  1.  **Example of str():**

 __

 __  
 __

 __

 __  
 __  
 __

s= 'Hello, Geeks.'

print (str(s))

print (str(2.0/11.0))  
  
---  
  
 __

 __

Output:

    
        Hello, Geeks.
    0.181818181818

.

  2.  **Example of repr():**

 __

 __  
 __

 __

 __  
 __  
 __

s= 'Hello, Geeks.'

print (repr(s))

print (repr(2.0/11.0))  
  
---  
  
 __

 __

Output:

    
        'Hello, Geeks.'
    0.18181818181818182

From above output, we can see if we print string using repr() function then it
prints with a pair of quotes and if we calculate a value we get more precise
value than str() function.

  

  

Following are differences:

  *  _ **str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable**_. For example, if we suspect a float has a small rounding error, repr will show us while str may not.
  * repr() compute the “official” string representation of an object (a representation that has all information about the object) and str() is used to compute the “informal” string representation of an object (a representation that is useful for printing the object).
  * The print statement and str() built-in function uses __str__ to display the string representation of the object while the repr() built-in function uses __repr__ to display the object.

Let understand this by an example:-

 __

 __  
 __

 __

 __  
 __  
 __

import datetime

today = datetime.datetime.now()

 

# Prints readable format for date-time object

print (str(today))

 

# prints the official format of date-time object

print (repr(today))   
  
---  
  
__

__

Output:

    
    
    2016-02-22 19:32:04.078030
    datetime.datetime(2016, 2, 22, 19, 32, 4, 78030)
    

str() displays today’s date in a way that the user can understand the date and
time.

repr() prints “official” representation of a date-time object

