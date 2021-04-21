maketrans() and translate() functions in Python



In the world of programming, seldom there is a need to replace all the
words/characters at once in the whole file python offers this functionality
using functions translate() and its helper functions maketrans(). Both
functions are discussed in this article.

 **maketrans()**

maketrans() function is used to construct the transition table i.e specify the
list of characters that need to be replaced in the whole string or the
characters that need to be deleted from the string

> Syntax : **maketrans(str1, str2, str3)**
>
>  **Parameters :**  
>  **str1 :** Specifies the list of characters that need to be replaced.  
>  **str2 :** Specifies the list of characters with which the characters need
> to be replaced.  
>  **str3 :** Specifies the list of characters that needs to be deleted.
>
>  **Returns :** Returns the translation table which specifies the conversions
> that can be used by translate()
>
>  
>
>
>  
>

 **Translate using maketrans()**

To translate the characters in the string translate() is used to make the
translations. This function uses the translation mapping specified using the
maketrans().

> Syntax : **translate(table, delstr)**
>
>  **Parameters :**  
>  **table :** Translate mapping specified to perform translations.  
>  **delstr :** The delete string can be specified as optional argument is not
> mentioned in table.
>
>  **Returns :** Returns the argument string after performing the translations
> using the translation table.

  
**Code #1 :** Code to translate using translate() and maketrans().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# translations using 

# maketrans() and translate()

 

# specify to translate chars

str1 = "wy"

 

# specify to replace with

str2 = "gf"

 

# delete chars

str3 = "u"

 

# target string 

trg = "weeksyourweeks"

 

# using maketrans() to 

# construct translate

# table

table = trg.maketrans(str1, str2, str3)

 

# Printing original string 

print ("The string before translating is : ", end ="")

print (trg)

 

# using translate() to make translations.

print ("The string after translating is : ", end ="")

print (trg.translate(table))  
  
---  
  
 __

 __

Output :

    
    
    The string before translating is : weeksyourweeks
    The string after translating is : geeksforgeeks
    

  

**Translate without maketrans()**

Translation can also be achieved by specifying the translation dictionary and
passing as an object which acts as a mapping. In this case, there is no need
for maketrans() to perform translations.

  
**Code #2 :** Code to translate without maketrans().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# translations without

# maketrans() 

 

# specifying the mapping 

# using ASCII 

table = { 119 : 103, 121 : 102, 117 : None }

 

# target string 

trg = "weeksyourweeks"

 

# Printing original string 

print ("The string before translating is : ", end ="")

print (trg)

 

# using translate() to make translations.

print ("The string after translating is : ", end ="")

print (trg.translate(table))  
  
---  
  
 __

 __

Output :

    
    
    The string before translating is : weeksyourweeks
    The string after translating is : geeksforgeeks
    

  

**Application :**  
There are many are times where mistakes can occur while coding or developing,
these functions provide an easy and quick way to replace and rectify them and
would potentially save a lot of time.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

