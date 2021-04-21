Python program to convert hex string to decimal



In Python, element conversion has been a very useful utility as it offers it
in a much simpler way that other languages. This makes Python a robust
language and hence knowledge of interconversions is always a plus for a
programmer. This article discusses the hexadecimal string to a decimal number.
Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingint()**

This function can be used to perform this particular task, adding an argument
(16) this function can convert hexadecimal string number to base sixteen and
convert it into integer at the same time.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting hexadecimal string to decimal

# Using int()

 

# initializing string 

test_string = 'A'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using int()

# converting hexadecimal string to decimal

res = int(test_string, 16)

 

# print result

print("The decimal number of hexadecimal string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : A
    The decimal number of hexadecimal string : 10
    

  

  

**Method #2 : Usingast.literal_eval()**

We can perform this particular function by using literal evaluation function
that predicts the base and converts the number string to its decimal number
format.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting hexadecimal string to decimal

# Using ast.literal_eval()

from ast import literal_eval

 

# initializing string 

test_string = '0xA'

 

# printing original string 

print("The original string : " + str(test_string))

 

# using ast.literal_eval()

# converting hexadecimal string to decimal

res = literal_eval(test_string)

 

# print result

print("The decimal number of hexadecimal string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : A
    The decimal number of hexadecimal string : 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

