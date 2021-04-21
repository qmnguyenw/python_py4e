String Formatting in Python using %



In Python a string of required formatting can be achieved by different
methods.  
Some of them are ;  
1) Using %  
2) Using {}  
3) Using Template Strings

In this article the formatting using % is discussed.

The formatting using % is similar to that of ‘printf’ in C programming
language.  
%d – integer  
%f – float  
%s – string  
%x – hexadecimal  
%o – octal

The below example describes the use of formatting using % in Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate the use of formatting using %

 

# Initialize variable as a string 

variable = '15'

string = "Variable as string = %s" %(variable) 

print (string )

 

# Printing as raw data 

# Thanks to Himanshu Pant for this 

print ("Variable as raw data = %r" %(variable))

 

# Convert the variable to integer 

# And perform check other formatting options 

 

variable = int(variable) # Without this the below statement 

 # will give error. 

string = "Variable as integer = %d" %(variable) 

print (string) 

print ("Variable as float = %f" %(variable)) 

 

# printing as any string or char after a mark 

# here i use mayank as a string 

print ("Variable as printing with special char = %cmayank"
%(variable)) 

 

print ("Variable as hexadecimal = %x" %(variable))

print ("Variable as octal = %o" %(variable))   
  
---  
  
__

__

**Output :**

  

  

    
    
    Variable as string = 15
    Variable as raw data = '15'
    Variable as integer = 15
    Variable as float = 15.000000
    Variable as printing with special char = mayank
    Variable as hexadecimal = f
    Variable as octal = 17
    

This article is contributed by **Nikhil Kumar Singh (nickzuck_007)**

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

