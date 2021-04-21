Extracting email addresses using regular expressions in Python



Let suppose a situation in which you have to read some specific data like
phone numbers, email addresses, dates, a collection of words etc. How can you
do this in a very efficient manner?The Best way to do this by Regular
Expression.

Let take an example in which we have to find out only email from the given
input by Regular Expression.  
Examples:

    
    
    Input  : Hello shubhamg199630@gmail.com Rohit neeraj@gmail.com
    Output : shubhamg199630@gmail.com neeraj@gmail.com
    Here we have only selected email from the given input string.
    
    Input : My 2 favourite numbers are 7 and 10
    Output :2 7 10
    Here we have selected only digits.
    

**Regular Expression** –  
Regular expression is a sequence of character(s) mainly used to find and
replace patterns in a string or file.  
So we can say that the task of searching and extracting is so common that
Python has a very powerful library called regular expressions that handles
many of these tasks quite elegantly.Symbol| Usage| $| Matches the end of the
line| \s| Matches whitespace|  **\S**|  Matches any non-whitespace character|
*****|  Repeats a character zero or more times|  **\S**|  Matches any non-
whitespace character|  ***?**|  Repeats a character zero or more times (non-
greedy)|  **+**|  Repeats a character one or more times|  **+?**|  Repeats a
character one or more times (non-greedy)|  **[aeiou]**|  Matches a single
character in the listed set|  **[^XYZ]**|  Matches a single character not in
the listed set|  **[a-z0-9]**|  The set of characters can include a range|
**(**|  Indicates where string extraction is to start|  **)**|  Indicates
where string extraction is to end  
---|---  
  
 __

 __  
 __

 __

 __  
 __  
 __

# Python program to extract numeric digit

# from A string by regular expression...

 

# Importing module required for regular

# expressions

import re 

 

# Example String 

s = 'My 2 favourite numbers are 7 and 10'

 

# find all function to select all digit from 0 

# to 9 [0-9] for numeric Letter in the String

# + for repeats a character one or more times

lst = re.findall('[0-9]+', s) 

 

# Printing of List

print(lst)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['2', '7', '10']
    

__

__  
__

__

__  
__  
__

# Python program to extract emails From

# the String By Regular Expression. 

 

# Importing module required for regular 

# expressions 

import re 

 

# Example string 

s = """Hello from shubhamg199630@gmail.com

 to priya@yahoo.com about the meeting @2PM"""

 

# \S matches any non-whitespace character 

# @ for as in the Email 

# + for Repeats a character one or more times 

lst = re.findall('\S+@\S+', s) 

 

# Printing of List 

print(lst)   
  
---  
  
__

__

**Output:**

  

  

    
    
    ['shubhamg199630@gmail.com', 'priya@yahoo.com']
    

