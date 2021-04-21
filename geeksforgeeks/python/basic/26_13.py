Unicodedata – Unicode Database in Python



 **Unicode Character Database (UCD)** is defined by Unicode Standard Annex #44
which defines the character properties for all unicode characters. This module
provides access to UCD and uses the same symbols and names as defined by the
Unicode Character Database.

 **Functions defined by the module :**

  *  **unicodedata.lookup(name)**  
This function looks up for the character by name. If a character with the
given name is found in the database, then, the corresponding character is
returned otherwise Keyerror is raised.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

import unicodedata

 

print (unicodedata.lookup('LEFT CURLY BRACKET'))

print (unicodedata.lookup('RIGHT CURLY BRACKET'))

print (unicodedata.lookup('ASTERISK'))

 

# gives error as there is 

# no symbol called ASTER

# print (unicodedata.lookup('ASTER'))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    {
    }
    *
    

  * **unicodedata.name(chr[, default])**  
This function returns the name assigned to the given character as a string. If
no name is defined, default is returned by the function otherwise ValueError
is raised if name is not given.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

import unicodedata

 

print (unicodedata.name(u'/'))

print (unicodedata.name(u'|'))

print (unicodedata.name(u':'))  
  
---  
  
 __

 __

 **Output :**

    
    
    SOLIDUS
    VERTICAL LINE
    COLON
    

  * **unicodedata.decimal(chr[, default])**  
This function returns the decimal value assigned to the given character as
integer. If no value is defined, default is returned by the function otherwise
ValueError is raised if value is not given.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

import unicodedata

 

print (unicodedata.decimal(u'9'))

print (unicodedata.decimal(u'a'))  
  
---  
  
 __

 __

 **Output :**

    
    
    9
    Traceback (most recent call last):
      File "7e736755dd176cd0169eeea6f5d32057.py", line 4, in 
        print unicodedata.decimal(u'a')
    ValueError: not a decimal
    

  * **unicodedata.digit(chr[, default])**  
This function returns the digit value assigned to the given character as
integer. If no value is defined, default is returned by the function otherwise
ValueError is raised if value is not given.

 **Example :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import unicodedata

 

print (unicodedata.decimal(u'9'))

print (unicodedata.decimal(u'143'))  
  
---  
  
 __

 __

 **Output :**

    
    
    9
    Traceback (most recent call last):
      File "ad47ae996380a777426cc1431ec4a8cd.py", line 4, in 
        print unicodedata.decimal(u'143')
    TypeError: need a single Unicode character as parameter
    

  * **unicodedata.numeric(chr[, default])**  
This function returns the numeric value assigned to the given character as
integer. If no value is defined, default is returned by the function otherwise
ValueError is raised if value is not given.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

import unicodedata

 

print (unicodedata.decimal(u'9'))

print (unicodedata.decimal(u'143'))  
  
---  
  
 __

 __

 **Output :**

    
    
    9
    Traceback (most recent call last):
      File "ad47ae996380a777426cc1431ec4a8cd.py", line 4, in 
        print unicodedata.decimal(u'143')
    TypeError: need a single Unicode character as parameter
    

  * **unicodedata.category(chr)**  
This function returns the general category assigned to the given character as
string. For example, it returns ‘L’ for letter and ‘u’ for uppercase.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

import unicodedata

 

print (unicodedata.category(u'A'))

print (unicodedata.category(u'b'))  
  
---  
  
 __

 __

 **Output :**

    
    
    Lu
    Ll
    

  * **unicodedata.bidirectional(chr)**  
This function returns the bidirectional class assigned to the given character
as string. For example, it returns ‘A’ for arabic and ‘N’ for number. An empty
string is returned by this function if no such value is defined.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

import unicodedata

 

print (unicodedata.bidirectional(u'\u0660'))  
  
---  
  
 __

 __

 **Output :**

    
    
    AN
    

  * **unicodedata.normalize(form, unistr)**  
This function returns the normal form for the Unicode string unistr. Valid
values for form are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

from unicodedata import normalize

 

print ('%r' % normalize('NFD', u'\u00C7'))

print ('%r' % normalize('NFC', u'C\u0327'))

print ('%r' % normalize('NFKD', u'\u2460'))  
  
---  
  
 __

 __

 **Output :**

    
    
    u'C\u0327'
    u'\xc7'
    u'1'
    

This article is contributed by **Aditi Gupta**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

