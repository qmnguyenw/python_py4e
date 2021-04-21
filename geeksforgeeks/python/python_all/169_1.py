Python program to count words in a sentence



Data preprocessing is an important task in text classification. With emergence
of Python in the field of data science, it is essential to have certain
shorthands to have upper hand among others. This article discusses ways to
count words in a sentence, it starts with space separated words but also
includes ways to in presence of special characters as well. Let’s discuss
certain ways to perform this.

 **Method #1 : Usingsplit()**  
split function is quite useful and usually quite generic method to get words
out of the list, but this approach fails once we introduce special characters
in the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to count words in string 

# using split()

 

# initializing string 

test_string = "Geeksforgeeks is best Computer Science Portal"

 

# printing original string

print ("The original string is : " + test_string)

 

# using split()

# to count words in string

res = len(test_string.split())

 

# printing result

print ("The number of words in string are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Geeksforgeeks is best Computer Science Portal  
> The number of words in string are : 6

  
**Method #2 : Usingregex(findall())**

  

  

Regular expressions have to be used in case we require to handle the cases of
punctuation marks or special characters in the string. This is the most
elegant way in which this task can be performed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to count words in string 

# using regex (findall())

import re

 

# initializing string 

test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

 

# printing original string

print ("The original string is : " + test_string)

 

# using regex (findall())

# to count words in string

res = len(re.findall(r'\w+', test_string))

 

# printing result

print ("The number of words in string are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Geeksforgeeks, is best @# Computer Science
> Portal.!!!  
> The number of words in string are : 6

  
**Method #3 : Usingsum() + strip() + split()**  
This method performs this particular task without using regex. In this method
we first check all the words consisting of all the alphabets, if so they are
added to sum and then returned.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to count words in string 

# using sum() + strip() + split()

import string

 

# initializing string 

test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

 

# printing original string

print ("The original string is : " + test_string)

 

# using sum() + strip() + split()

# to count words in string

res = sum([i.strip(string.punctuation).isalpha() for i in
test_string.split()])

 

# printing result

print ("The number of words in string are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : Geeksforgeeks, is best @# Computer Science
> Portal.!!!  
> The number of words in string are : 6

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

