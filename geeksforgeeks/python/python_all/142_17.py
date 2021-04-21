Python | Get the substring from given string using list slicing



Given a string, write a Python program to get the substring from given string
using list slicing. Let’s try to get this using different examples.

 **Code #1:**

In this example, we will see how to take a substring from the end or from
starting of string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to create a substring from a string

 

# Initialising string

ini_string = 'xbzefdgstb'

 

# printing initial string and character

print ("initial_strings : ", ini_string)

 

# creating substring from start of string

# define length upto which substring required

sstring_strt = ini_string[:2]

sstring_end = ini_string[3:]

 

# printing result

print ("print resultant substring from start", sstring_strt)

print ("print resultant substring from end", sstring_end)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_strings :  xbzefdgstb
    print resultant substring from start xb
    print resultant substring from end efdgstb
    

  
**Code #2:**

  

  

In this example, we will see how to create a string by taking characters from
the certain positional gap.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to create a substring from string

 

# Initialising string

ini_string = 'xbzefdgstb'

 

# printing initial string and character

print ("initial_strings : ", ini_string)

 

# creating substring by taking element

# after certain position gap

# define length upto which substring required

sstring_alt = ini_string[::2]

sstring_gap2 = ini_string[::3]

 

# printing result

print ("print resultant substring from start", sstring_alt)

print ("print resultant substring from end", sstring_gap2)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_strings :  xbzefdgstb
    print resultant substring from start xzfgt
    print resultant substring from end xegb
    

  
**Code #3:**

In this example, we are considering both cases of taking string from the
middle with some positional gap between characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to create a substring from string

 

# Initialising string

ini_string = 'xbzefdgstb'

 

# printing initial string and character

print ("initial_strings : ", ini_string)

 

# creating substring by taking element

# after certain position gap

# in defined length

sstring = ini_string[2:7:2]

 

# printing result

print ("print resultant substring", sstring)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_strings :  xbzefdgstb
    print resultant substring zfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

