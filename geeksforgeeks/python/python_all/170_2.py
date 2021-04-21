Python | Extract words from given string



We sometimes come through the situations where we require to get all the works
present in the string, this can be a tedious task done using naive method.
Hence having shorthands to perform this task is always useful. Additionally
this article also includes the cases in which punctuation marks have to be
ignored.

 **Method #1 : Usingsplit()**  
Using split function, we can split the string into a list of words and is most
generic and recommended method if one wished to accomplish this particular
task. But drawback is that it fails in the cases in string contains
punctuation marks.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to extract words from string 

# using split()

 

# initializing string 

test_string = "Geeksforgeeks is best Computer Science Portal"

 

# printing original string

print ("The original string is : " + test_string)

 

# using split()

# to extract words from string

res = test_string.split()

 

# printing result

print ("The list of words is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Geeksforgeeks is best Computer Science Portal  
> The list of words is : [‘Geeksforgeeks’, ‘is’, ‘best’, ‘Computer’,
> ‘Science’, ‘Portal’]

  
**Method #2 : Usingregex( findall() )**  
In the cases which contain all the special characters and punctuation marks,
as discussed above, the conventional method of finding words in string using
split can fail and hence requires regular expressions to perform this task.
findall function returns the list after filtering the string and extracting
words ignoring punctuation marks.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to extract words from string 

# using regex( findall() )

import re

 

# initializing string 

test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

 

# printing original string

print ("The original string is : " + test_string)

 

# using regex( findall() )

# to extract words from string

res = re.findall(r'\w+', test_string)

 

# printing result

print ("The list of words is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Geeksforgeeks, is best @# Computer Science
> Portal.!!!  
> The list of words is : [‘Geeksforgeeks’, ‘is’, ‘best’, ‘Computer’,
> ‘Science’, ‘Portal’]

  
**Method #3 : Using regex() + string.punctuation**  
This method also used regular expressions, but string function of getting all
the punctuations is used to ignore all the punctuation marks and get the
filtered result string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to extract words from string 

# using regex() + string.punctuation

import re

import string

 

# initializing string 

test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

 

# printing original string

print ("The original string is : " + test_string)

 

# using regex() + string.punctuation

# to extract words from string

res = re.sub('['+string.punctuation+']', '',
test_string).split()

 

# printing result

print ("The list of words is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Geeksforgeeks, is best @# Computer Science
> Portal.!!!  
> The list of words is : [‘Geeksforgeeks’, ‘is’, ‘best’, ‘Computer’,
> ‘Science’, ‘Portal’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

