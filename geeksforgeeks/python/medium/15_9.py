Verbose in Python Regex



In this article, we will learn about **VERBOSE** flag of the **re package**
and how to use it.

 **re.VERBOSE :** This flag allows you to write regular expressions that
look nicer and are more readable by allowing you to visually separate logical
sections of the pattern and add comments.  
Whitespace within the pattern is ignored, except when in a character class, or
when preceded by an unescaped backslash, or within tokens like *?, (?: or
(?P. When a line contains a # that is not in a character class and is not
preceded by an unescaped backslash, all characters from the leftmost such #
through the end of the line are ignored.

 __

 __  
 __

 __

 __  
 __  
 __

# Without Using VERBOSE

regex_email =
re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2, 6})$',

 re.IGNORECASE)

 

# Using VERBOSE

regex_email = re.compile(r"""

 ^([a-z0-9_\.-]+) # local Part

 @ # single @ sign

 ([0-9a-z\.-]+) # Domain name

 \. # single Dot .

 ([a-z]{2,6})$ # Top level Domain 

 """,re.VERBOSE | re.IGNORECASE)   
  
---  
  
__

__

It’s passed as an argument tore.compile() i.e **re.compile(Regular
Expression, re.VERBOSE)**. re.compile() returns a _RegexObject_ which is
then matched with the given string.

Let’s consider an example where the user is asked to enter their Email ID and
we have to validate it using RegEx. The format of an email is as follow:

  * Personal details/local part like john123
  * Single @
  * Domain Name like gmail/yahoo etc
  * Single Dot(.)
  * Top Level Domain like .com/.org/.net

 **Examples:**

  

  

    
    
    **Input** : expectopatronum@gmail.com
    **Output** : Valid
    
    
    **Input** : avadakedavra@yahoo.com@
    **Output** : Invalid
    This is invalid because there is @ after the top level domain name.
    

Below is the Python implementation –

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to show the Implementation of VERBOSE in RegEX

import re

 

def validate_email(email):

 

 # RegexObject = re.compile( Regular expression, flag )

 # Compiles a regular expression pattern into 

 # a regular expression object

 regex_email=re.compile(r"""

 ^([a-z0-9_\.-]+) # local Part

 @ # single @ sign

 ([0-9a-z\.-]+) # Domain name

 \. # single Dot .

 ([a-z]{2,6})$ # Top level Domain 

 """,re.VERBOSE | re.IGNORECASE)

 

 # RegexObject is matched with the desired

 # string using fullmatch function

 # In case a match is found, search()

 # returns a MatchObject Instance

 res=regex_email.fullmatch(email)

 

 #If match is found, the string is valid

 if res:

 print("{} is Valid. Details are as follow:".format(email))

 

 #prints first part/personal detail of Email Id

 print("Local:{}".format(res.group(1)))

 

 #prints Domain Name of Email Id

 print("Domain:{}".format(res.group(2)))

 

 #prints Top Level Domain Name of Email Id

 print("Top Level domain:{}".format(res.group(3)))

 print()

 

 else:

 #If match is not found,string is invalid

 print("{} is Invalid".format(email))

 

# Driver Code

validate_email("expectopatronum@gmail.com")

validate_email("avadakedavra@yahoo.com@")

validate_email("Crucio@.com")  
  
---  
  
 __

 __

 **Output:**

    
    
    expectopatronum@gmail.com is Valid. Details are as follow:
    Local:expectopatronum
    Domain:gmail
    Top Level domain:com
    
    avadakedavra@yahoo.com@ is Invalid
    Crucio@.com is Invalid
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

