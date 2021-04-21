format() function in Python



With Python 3.0, the format() method has been introduced for handling complex
string formatting more efficiently. This method of the built-in string class
provides

functionality for complex variable substitutions and value formatting. This
new formatting technique is regarded as more elegant. The general syntax of
format()

method is: string.format(var1, var2,…)  

**Using a Single Formatter :**

Formatters work by putting in one or more replacement fields and placeholders
defined by a pair of curly braces **{ }** into a string and calling the
str.format(). The value we wish to put into the placeholders and concatenate
with the string passed as parameters into the format function.  

  

  

> **Syntax :** **{ } .format(value)**  
>  **Parameters :**  
>  **(value) :** Can be an integer, floating point numeric constant, string,
> characters or even variables.  
>  **Returntype :** Returns a formatted string with the value passed as
> parameter in the placeholder position.  
>

**Code #1 :** Simple demonstration of format().  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstarte

# the str.format() method

# using format option in a simple string

print ("{}, A computer science portal for geeks."

 .format("GeeksforGeeks"))

# using format option for a

# value stored in a variable

str = "This article is written in {}"

print (str.format("Python"))

# formatting a string using a numeric constant

print ("Hello, I am {} years old !".format(18))  
  
---  
  
 __

 __

 **Output :**  

    
    
    GeeksforGeeks, A computer science portal for geeks.
    This article is written in Python
    Hello, I am  18 years old!

#### Using Multiple Formatters :

Multiple pairs of curly braces can be used while formatting the string. Let’s
say if another variable substitution is needed in the sentence, can be done by
adding a second pair of curly braces and passing a second value into the
method. Python will replace the placeholders with values in **order.**  

> **Syntax :** { } { } .format(value1, value2)  
>  **Parameters :**  
> **(value1, value2) :** Can be integers, floating point numeric constants,
> strings, characters and even variables. Only difference is, the number of
> values passed as parameters in format() method must be equal to the number
> of placeholders created in the string.  
>  **Errors and Exceptions :**  
> **IndexError :** Occurs when string has an extra placeholder, and we didn’t
> pass any value for it in the format() method. Python usually assigns the
> placeholders with default index in order like _0, 1, 2, 3…._ to acces the
> values passed as parameters. So when it encounters a placeholder whose index
> doesn’t have any value passed inside as parameter, it throws IndexError.  
>

**Code #2 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program demonstrating Index error

# Number of placeholders are four but

# there are only three values passed

# parameters in format function.

my_string = "{}, is a {} {} science portal for {}"

print (my_string.format("GeeksforGeeks", "computer",
"geeks"))  
  
---  
  
 __

 __

 **Output :**  

  

  

    
    
    Traceback (most recent call last):
      File "/home/949ca7b5b7e26575871639f03193d1b3.py", line 2, in 
        print (my_string.format("GeeksforGeeks", "computer", "geeks"))
    IndexError: tuple index out of range

  
**Code #3:** Formatters with multiple placeholders.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program using multiple place

# holders to demonstrate str.format() method

# Multiple placeholders in format() function

my_string = "{}, is a {} science portal for {}"

print (my_string.format("GeeksforGeeks", "computer",
"geeks"))

# different datatypes can be used in formatting

print ("Hi ! My name is {} and I am {} years old"

 .format("User", 19))

# The values passed as parameters

# are replaced in order of their entry

print ("This is {} {} {} {}"

 .format("one", "two", "three", "four"))  
  
---  
  
 __

 __

 **Output :**  

    
    
    GeeksforGeeks, is a computer science portal for geeks
    Hi! My name is User and I am 19 years old
    This is one two three four

 **Formatting Strings using Escape Sequences:**

You can use two or more specially designated characters within a string to
format a string or perform a command. These characters are called escape
sequences. An

Escape sequence in Python starts with a backslash (\\). For example, \n is an
escape sequence in which the common meaning of the letter n is literally
escaped and given an alternative meaning – a new line.Escape sequence|
Description |  Example | \n| Breaks the string into a new line| print(‘I
designed this rhyme to explain in due time\nAll I know’)| \t| Adds a
horizontal tab| print(‘Time is a \tvaluable thing’)| \\\| Prints a backslash|
print(‘Watch it fly by\\\as the pendulum swings’)| \’ | Prints a single quote|
print(‘It doesn\’t even matter how hard you try’)| \” |  Prints a double
quote| print(‘It is so\”unreal\”‘)| \a| makes a sound like a bell| print(‘\a’)  
---|---|---  
  
#### Formatters with Positional and Keyword Arguments :

When placeholders **{ }** are empty, Python will replace the values passed
through str.format() in order.  
The values that exist within the str.format() method are essentially **tuple
data types** and each individual value contained in the tuple can be called by
its index number, which starts with the index number 0. These index numbers
can be passed into the curly braces that serve as the placeholders in the
original string.  

> **Syntax :** {0} {1}.format(positional_argument, keyword_argument)  
>  **Parameters :** (positional_argument, keyword_argument)  
>  **Positional_argument** can be integers, floating point numeric constants,
> strings, characters and even variables.  
> **Keyword_argument** is essentially a variable storing some value, which is
> passed as parameter.

 **Code #4 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# To demonstrate the use of formatters

# with positional key arguments.

# Positional arguments

# are placed in order

print("{0} love {1}!!".format("GeeksforGeeks",

 "Geeks"))

# Reverse the index numbers with the

# parameters of the placeholders

print("{1} love {0}!!".format("GeeksforGeeks",

 "Geeks"))

print("Every {} should know the use of {} {} programming and {}"

 .format("programmer", "Open", "Source", "Operating
Systems"))

# Use the index numbers of the

# values to change the order that

# they appear in the string

print("Every {3} should know the use of {2} {1} programming and {0}"

 .format("programmer", "Open", "Source", "Operating
Systems"))

# Keyword arguments are called

# by their keyword name

print("{gfg} is a {0} science portal for {1}"

.format("computer", "geeks", gfg ="GeeksforGeeks"))  
  
---  
  
 __

 __

 **Output :**  

    
    
    GeeksforGeeks love Geeks!!
    Geeks love GeeksforGeeks!!
    Every programmer should know the use of Open Source programming and Operating Systems
    Every Operating Systems should know the use of Source Open programming and programmer
    GeeksforGeeks is a computer science portal for geeks

#### Type Specifying :

More parameters can be included within the curly braces of our syntax. Use the
format code syntax **{field_name:conversion}** , where field_name specifies
the index number of the argument to the str.format() method, and conversion
refers to the conversion code of the data type.  

> **%s** – string conversion via str() prior to formatting
>
> example:
>
> 1)print(“%20s” % (‘geeksforgeeks’, ))
>
> output- geeksforgeeks
>
> 2)print(“%-20s” % (‘Interngeeks’, ))
>
> output- Interngeeks
>
> 3)print(“%.5s” % (‘Interngeeks’, ))
>
> output- Inter
>
>  **%c** – character
>
> example:
>
> type=’bug’
>
> result=’troubling’
>
> print(‘I wondered why the program was %s me. Then it dawned on me it was a
> %s .’ %(result, type ))
>
> output-I wondered why the program was me troubling me. Then it dawned on me
> it was a bug.
>
>  **%i** – signed decimal integer
>
>  **%d** – signed decimal integer(base-10)
>
> example-
>
> match=12000
>
> site=’amazon’
>
> print(“%s is so useful. I tried to look up mobile and they had a nice one
> that cost %d rupees.” % (site, match))
>
> output- amazon is so useful. I tried to look up mobiles and they had a nice
> one that cost 12000 rupees”)
>
>  **%u** unsigned decimal integer  
> **%o** octal integer  
> **f** – floating point display  
> **b** – binary  
> **o** – octal  
> **%x** – hexadecimal with lowercase letters after 9  
> **%X** – hexadecimal with uppercase letters after 9  
> **e** – exponent notation
>
> You can also specify formatting symbols. Only change is using colon (:)
> instead of %. For example, instead of %s use {:s} and instead of %d use (:d}

> **Syntax :**  
> String {field_name:conversion} Example.format(value)  
>  **Errors and Exceptions :**  
> **ValueError :** Error occurs during type conversion in this method.

**Code #5 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Demonstrate ValueError while

# doing forced type-conversions

# When explicitly converted floating-point

# values to decimal with base-10 by 'd'

# type conversion we encounter Value-Error.

print("The temperature today is {0:d} degrees outside !"

 .format(35.567))

# Instead write this to avoid value-errors

''' print("The temperature today is {0:.0f} degrees outside !"

 .format(35.567))'''  
  
---  
  
 __

 __

 **Output :**  

    
    
    Traceback (most recent call last):
      File "/home/9daca03d1c7a94e7fb5fb326dcb6d242.py", line 5, in 
        print("The temperature today is {0:d} degrees outside!".format(35.567))
    ValueError: Unknown format code 'd' for object of type 'float'

  
**Code #6 :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Convert base-10 decimal integers

# to floating point numeric constants

print ("This site is {0:f}% securely {1}!!".

 format(100, "encrypted"))

# To limit the precision

print ("My average of this {0} was {1:.2f}%"

 .format("semester", 78.234876))

# For no decimal places

print ("My average of this {0} was {1:.0f}%"

 .format("semester", 78.234876))

# Convert an integer to its binary or

# with other different converted bases.

print("The {0} of 100 is {1:b}"

 .format("binary", 100))

 

print("The {0} of 100 is {1:o}"

 .format("octal", 100))  
  
---  
  
 __

 __

 **Output :**  

    
    
    This site is 100.000000% securely encrypted!!
    My average of this semester was 78.23%
    My average of this semester was 78%
    The binary of 100 is 1100100
    The octal of 100 is 144

  

#### Padding Substitutions or Generating Spaces :

 **Code #7 :**  
By default, strings are left-justified within the field, and numbers are
right-justified. We can modify this by placing an alignment code just
following the colon.  

    
    
    **<**   :  left-align text in the field
    **^**   :  center text in the field
    **>**   :  right-align text in the field

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# To demonstrate spacing when

# strings are passed as parameters

print("{0:4}, is the computer science portal for {1:8}!"

 .format("GeeksforGeeks", "geeks"))

# To demonstrate spacing when numeric

# constants are passed as parameters.

print("It is {0:5} degrees outside !"

 .format(40))

# To demonstrate both string and numeric

# constants passed as parameters

print("{0:4} was founded in {1:16}!"

 .format("GeeksforGeeks", 2009))

# To demonstrate aligning of spaces

print("{0:^16} was founded in {1:<4}!"

 .format("GeeksforGeeks", 2009))

print("{:*^20s}".format("Geeks"))  
  
---  
  
 __

 __

 **Output :**  

    
    
    GeeksforGeeks, is the computer science portal for geeks   !
    It is    40 degrees outside!
    GeeksforGeeks was founded in             2009!
     GeeksforGeeks   was founded in 2009 !
    *******Geeks********

  

### Applications :

Formatters are generally used to Organize Data. Formatters can be seen in
their best light when they are being used to organize a lot of data in a
visual way. If we are showing databases to users, using formaters to increase
field size and modify alignment can make the output more readable.  

**Code #8:** To demonstrate organization of large data  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# which prints out i, i ^ 2, i ^ 3,

# i ^ 4 in the given range

# Function prints out values

# in an unorganized manner

def unorganized(a, b):

 for i in range (a, b):

 print ( i, i**2, i**3, i**4 )

# Function prints the organized set of values

def organized(a, b):

 for i in range (a, b):

 # Using formatters to give 6

 # spaces to each set of values

 print("{:6d} {:6d} {:6d} {:6d}"

 .format(i, i ** 2, i ** 3, i ** 4))

# Driver Code

n1 = int(input("Enter lower range :-\n"))

n2 = int(input("Enter upper range :-\n"))

print("------Before Using Formatters-------")

# Calling function without formatters

unorganized(n1, n2)

print()

print("-------After Using Formatters---------")

print()

# Calling function that contains

# formatters to organize the data

organized(n1, n2)  
  
---  
  
 __

 __

 **Output :**  

    
    
    Enter lower range :-
    3
    Enter upper range :-
    10
    ------Before Using Formatters-------
    3 9 27 81
    4 16 64 256
    5 25 125 625
    6 36 216 1296
    7 49 343 2401
    8 64 512 4096
    9 81 729 6561
    
    -------After Using Formatters---------
    
         3      9     27     81
         4     16     64    256
         5     25    125    625
         6     36    216   1296
         7     49    343   2401
         8     64    512   4096
         9     81    729   6561

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

