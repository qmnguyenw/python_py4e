Python String Concatenation



In Python, Strings are arrays of bytes representing Unicode characters.
However, Python does not have a character data type, a single character is
simply a string with a length of 1. Square brackets [] can be used to access
elements of the string.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# strings

 

 

# Assign Welcome string to the variable var1

var1 = "Welcome"

 

# Assign statistics string to the variable var2

var2 = "statistics"

 

# print the result

print(var1)

print(var2)  
  
---  
  
 __

 __

 **Output:**

    
    
    Welcome
    statistics
    

## String Concatenation in Python

String Concatenation is the technique of **combining two strings**. String
Concatenation can be done using many ways.

 **We can perform string concatenation using following ways:**

  

  

  1. Using + operator
  2. Using join() method
  3. Using % operator
  4. Using format() function

#### Using + Operator

It’s very easy to use + operator for string concatenation. This operator can
be used to add multiple strings together. However, the arguments must be a
string.

 **Note:** Strings are immutable, therefore, whenever it is concatenated, it
is assigned to a new variable.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# string concatenation

 

 

# Defining strings

var1 = "Hello "

var2 = "World"

 

# + Operator is used to combine strings

var3 = var1 + var2

print(var3)  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello World
    

Here, the variable var1 stores the string “Hello ” and variable var2
stores the string “World”. The + Operator combines the string that is stored
in the var1 and var2 and stores in another variable var3.

#### Using join() Method

The join() method is a string method and returns a string in which the
elements of sequence have been joined by str separator.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# string concatenation

 

 

var1 = "Hello"

var2 = "World"

 

# join() method is used to combine the strings

print("".join([var1, var2]))

 

# join() method is used here to combine 

# the string with a separator Space(" ")

var3 = " ".join([var1, var2])

 

print(var3)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    HelloWorld
    Hello World
    

In the above example, the variable var1 stores the string “Hello” and
variable var2 stores the string “World”. The join() method combines the
string that is stored in the var1 and var2. The join method accepts only the
list as it’s argument and list size can be anything. We can store the combined
string in another variable var3 which is separated by space.

 **Note:** To know more about join() method click here.

#### Using % Operator

We can use % operator for string formatting, it can also be used for string
concatenation. It’s useful when we want to concatenate strings and perform
simple formatting.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# string concatenation

 

 

var1 = "Hello"

var2 = "World"

 

# % Operator is used here to combine the string

print("% s % s" % (var1, var2))  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello World
    

Here, the % Operator combine the string that is stored in the var1 and var2.
The %s denotes string data type. The value in both the variable is passed to
the string %s and becomes “Hello World”.

#### Using format() function

str.format() is one of the string formatting methods in Python, which allows
multiple substitutions and value formatting. This method lets us concatenate
elements within a string through positional formatting.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# string concatenation

 

 

var1 = "Hello"

var2 = "World"

 

# format function is used here to 

# combine the string

print("{} {}".format(var1, var2))

 

# store the result in another variable 

var3 = "{} {}".format(var1, var2)

 

print(var3)  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello World
    Hello World
    

Here, the format() function combines the string that is stored in the var1
and var2 and stores in another variable var3. The curly braces {} are used
to set the position of strings. The first variable stores in the first curly
braces and second variable stores in the second curly braces. Finally it
prints the value “Hello World”.

 **Note:** To know more about format() function click here.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

