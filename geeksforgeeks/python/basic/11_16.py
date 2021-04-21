Single and Double Quotes | Python



Python string functions are very popular. There are two ways to represent
strings in python. String is enclosed either with single quotes or double
quotes. Both the ways (single or double quotes) are correct depending upon the
requirement. Sometimes we have to use quotes (single or double quotes)
together in the same string, in such cases, we use single and double quotes
alternatively so that they can be distinguished.

 **Example #1:**  
Check below example and analyze the error –

    
    
    #Gives Error
    print('It's python')
    
    

**Explanation –**  
It gives an invalid syntax error. Because single quote after “it” is
considered as the end of the string and rest part is not the part of a string.

It can be corrected as:

 __

 __  
 __

 __

 __  
 __  
 __

print("It's Python !")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    It's Python!
    

**Example #2:**  
If you want to print _‘WithQuotes’_ in python, this can’t be done with only
single (or double) quotes alone, it requires simultaneous use of both.

 __

 __  
 __

 __

 __  
 __  
 __

# this code prints the output within quotes.

# print WithQuotes within single quotes

print("'WithQuotes'")

print("Hello 'Python'")

 

# print WithQuotes within single quotes

print('"WithQuotes"')

print('Hello "Python"')  
  
---  
  
 __

 __

 **Output –**

    
    
    'WithQuotes'
    Hello 'Python'
    "WithQuotes"
    Hello "Python"
    

**Conclusion –**  
The choice between both the types (single quotes and double quotes) depends on
the programmer’s choice. Generally, double quotes are used for string
representation and single quotes are used for regular expressions, dict keys
or SQL. Hence both single quote and double quotes depict string in python but
it’s sometimes our need to use one type over the other.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

