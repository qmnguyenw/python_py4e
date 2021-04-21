Difference between str.capitalize() VS str.title()



Both **title()** and **capitalize()** have similar functionality of
capitalizing first characters. Let us see the difference between the two of
them.

### title()

 **title()** function in Python is the Python String Method which is used to
convert the first character in each word to Uppercase and remaining characters
to Lowercase in the string and returns a new string.

>  **Syntax:** str.title()
>
>  **Parameters:** None
>
>  **Returns:** This function returns a string which has first letter in each
> word is uppercase and all remaining letters are lowercase.
>
>  
>
>
>  
>

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python Title() Method Example

 

str1 = 'geeKs foR geEks'

str2 = str1.title() 

print ('First Output after Title() method is = ', str2) 

 

# observe the original string 

print ('Converted String is = ', str1.title()) 

print ('Original String is = ', str1 )

 

# Performing title() function directly 

str3 = 'ASIPU pawan kuMAr'.title() 

print ('Second Output after Title() method is = ', str3) 

 

str4 = 'stutya kUMari sHAW'.title() 

print ('Third Output after Title() method is = ', str4) 

 

str5 = '6041'.title() 

print ('Fourth Output after Title() method is = ', str5)  
  
---  
  
 __

 __

 **Output:**

    
    
    First Output after Title() method is =  Geeks For Geeks
    Converted String is =  Geeks For Geeks
    Original String is =  geeKs foR geEks
    Second Output after Title() method is =  Asipu Pawan Kumar
    Third Output after Title() method is =  Stutya Kumari Shaw
    Fourth Output after Title() method is =  6041
    

### capitalize()

In Python, the **capitalize()** method converts the first character of a
string to a capital **(uppercase)** letter. If the string has its first
character as capital, then it returns the original string.

>  **Syntax:** str.title()
>
>  **Parameters:** None
>
>  **Returns:** This function returns a string which has the first letter in
> uppercase and all remaining letters in lowercase.

**Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the

# use of capitalize() function 

 

# capitalize() first letter of 

# string. 

name = "geeks for geeks"

 

print(name.capitalize()) 

 

# demonstration of individual words 

# capitalization to generate camel case 

name1 = "geeks"

name2 = "for"

name3 = "geeks"

print(name1.capitalize() + name2.capitalize() 

 + name3.capitalize())  
  
---  
  
 __

 __

 **Output:**

    
    
    Geeks for geeks
    GeeksForGeeks
    

### Difference Between title() and capitalize()

The difference between them is that Python string method title() returns a
copy of the string in which the first characters of all the words are
capitalized whereas the string method capitalize() returns a copy of the
string in which just the first word of the entire string is capitalized.

 **Example:**

    
    
    str = "geeks for geeks"
    str.title() will return Geeks For Geeks
    str.capitalize() will return Geeks for geeks
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

str1= "my name is xyz"

str2 = "geeks for geeks"

 

# using title()

print(str1.title())

print(str2.title())

 

# usng capitalize()

print(str1.capitalize())

print(str2.capitalize())  
  
---  
  
 __

 __

 **Output:**

    
    
    My Name Is Xyz
    Geeks For Geeks
    My name is xyz
    Geeks for geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

