Python | Check if a variable is string



While working with different datatypes, we might come across a time, where we
need to test the datatype for its nature. This article gives ways to test a
variable against the data type it is. Let’s discuss certain ways in which this
task can be done.

 **Method #1 : Usingisinstance(x, str)**

This method can be used to test whether any variable is a particular datatype.
By giving the second argument as “str”, we can check if the variable we pass
is a string or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check if variable is string 

# using isinstance()

 

# initializing string 

test_string = "GFG"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using isinstance()

# Check if variable is string 

res = isinstance(test_string, str)

 

# print result

print("Is variable a string ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    Is variable a string ? : True
    

  

  

**Method #2 : Usingtype()**

This task can also be achieved using the type function in which we just need
to pass the variable and equate with a particular type.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check if variable is string 

# using type()

 

# initializing string 

test_string = "GFG"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using type()

# Check if variable is string 

res = type(test_string) == str

 

# print result

print("Is variable a string ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    Is variable a string ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

