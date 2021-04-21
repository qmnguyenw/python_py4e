Iterate over words of a String in Python



Given a String comprising of many words separated by space, write a Python
program to iterate over these words of the string.

 **Examples:**

>  **Input:** str = “GeeksforGeeks is a computer science portal for Geeks”  
>  **Output:**  
>  GeeksforGeeks  
> is  
> a  
> computer  
> science  
> portal  
> for  
> Geeks
>
>  **Input:** str = “Geeks for Geeks”  
>  **Output:**  
>  Geeks  
> for  
> Geeks

 **Method 1:** Using split()

  

  

Using split() function, we can split the string into a list of words and is
the most generic and recommended method if one wished to accomplish this
particular task. But the drawback is that it fails in the cases in string
contains punctuation marks.

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

test_string = "GeeksforGeeks is a computer science portal for Geeks"

 

# printing original string 

print ("The original string is : " + test_string) 

 

# using split() 

# to extract words from string 

res = test_string.split() 

 

# printing result 

print ("\nThe words of string are")

for i in res:

 print(i)  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : GeeksforGeeks is a computer science portal for Geeks
    
    The words of string are
    GeeksforGeeks
    is
    a
    computer
    science
    portal
    for
    Geeks
    

**Method 2:** Using re.findall()

In the cases which contain all the special characters and punctuation marks,
as discussed above, the conventional method of finding words in a string using
split can fail and hence requires regular expressions to perform this task.
findall() function returns the list after filtering the string and
extracting words ignoring punctuation marks.

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

test_string = "GeeksforGeeks is a computer science portal for Geeks !!!"

 

# printing original string 

print ("The original string is : " + test_string) 

 

# using regex( findall() ) 

# to extract words from string 

res = re.findall(r'\w+', test_string) 

 

# printing result 

print ("\nThe words of string are")

for i in res:

 print(i)  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : GeeksforGeeks is a computer science portal for Geeks!!!
    
    The words of string are
    GeeksforGeeks
    is
    a
    computer
    science
    portal
    for
    Geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

