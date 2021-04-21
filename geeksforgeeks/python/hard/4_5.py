Concatenate two strings using Operator Overloading in Python



 **Operator Overloading** refers to using the same operator to perform
different tasks by passing different types of data as arguments. To understand
how ‘+’ operator works in two different ways in python let us take the
following example

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# taking two numbers

a = 2

b = 3

 

# using '+' operator add them

c = a+b

 

# printing the result

print("The sum of these two numbers is ", c)  
  
---  
  
 __

 __

 **Output:**

    
    
    The sum of these two numbers is  5
    

In this example we used ‘+’ operator to add numbers, now let us take one more
example to understand how ‘+’ operator is used to concatenate strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# taking two strings from the user

a = 'abc'

b = 'def'

 

# using '+' operator concatenate them

c = a+b

 

# printing the result

print("After Concatenation the string becomes", c)  
  
---  
  
 __

 __

 **Output:**

    
    
    After Concatenation the string becomes abcdef
    

For a better understanding of operator overloading, here is an example where a
**common method** is used for both purposes.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# let us define a class with add method

class operatoroverloading:

 

 def add(self, a, b):

 self.c = a+b

 return self.c

 

 

# creating an object of class

obj = operatoroverloading()

 

# using add method by passing integers

# as argument

result = obj.add(23, 9)

print("sum is", result)

 

# using same add method by passing strings

# as argument

result = obj.add("23", "9")

print("Concatenated string is", result)  
  
---  
  
 __

 __

 **Output:**

    
    
    sum is 32
    Concatenated string is 239
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

