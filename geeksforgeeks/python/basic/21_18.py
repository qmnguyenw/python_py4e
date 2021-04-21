Python String | count()



 **count()** function in an inbuilt function in python programming language
that returns the number of occurrences of a substring in the given string.

 **Syntax:**

> string.count(substring, start=…, end=…)

 **Parameters:**

> The count() function has one compulsory and two optional parameters.  
>  **Mandatory parameter:**  
>  1)substring – string whose count is to be found.
>
>  
>
>
>  
>
>
>  **Optional Parameters:**  
>  1) _start (Optional)_ – starting index within the string where search
> starts.  
> 2) _end (Optional)_ – ending index within the string where search ends.

 **Return Value:**  
count() method returns an integer that denotes **number of times** a substring
occurs in a given string.

Below is the Python implementation of the count() method **without optional
parameters:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the use of

# count() method without optional parameters 

 

# string in which occurrence will be checked

string = "geeks for geeks"

 

# counts the number of times substring occurs in 

# the given string and returns an integer

print(string.count("geeks"))  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Below is the Python implementation of the count() method **using optional
parameters.**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the use of

# count() method using optional parameters

 

# string in which occurrence will be checked

string = "geeks for geeks"

 

# counts the number of times substring occurs in 

# the given string between index 0 and 5 and returns 

# an integer

print(string.count("geeks", 0, 5))

 

print(string.count("geeks", 0, 15))  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

