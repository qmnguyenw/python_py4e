Python Keywords and Identifiers



The keywords are some predefined and reserved words in python that have
special meaning. Keywords are used to define the syntax of the coding. The
keyword cannot be used as an identifier, function, and variable name. All the
keywords in python are written in lower case expect True and False. There are
33 keywords in Python 3.7 let’s go through all of them one by one.

##  **Total Python keywords**

No. | Keywords |  Description| 1|  **and**|  This is a logical operator it
returns true if both the operands are true else return false.| 2|  **Or**|
This is also a logical operator it returns true if anyone operand is true else
return false.| 3|  **not**|  This is again a logical operator it returns True
if the operand is false else return false.| 4|  **if**|  This is used to make
a conditional statement.| 5|  **elif**|  Elif is a condition statement used
with if statement the elif statement is executed if the previous conditions
were not true| 6|  **else**|  Else is used with if and elif conditional
statement the else block is executed if the given condition is not true.| 7|
**for**|  This is created for a loop.| 8|  **while**|  This keyword is used to
create a while loop.| 9|  **break**|  This is used to terminate the loop.| 10|
**as**|  This is used to create an alternative.| 11|  **def**|  It helps us to
define functions.| 12|  **lambda**|  It used to define the anonymous
function.| 13|  **pass**|  This is a null statement that means it will do
nothing.| 14|  **return**|  It will return a value and exit the function.| 15|
**True**|  This is a boolean value.| 16|  **False**|  This is also a boolean
value.| 17|  **try**|  It makes a try-except statement.| 18|  **with**|  The
with keyword is used to simplify exception handling.| 19|  **assert**|  This
function is used for debugging purposes. Usually used to check the correctness
of code| 20|  **class**|  It helps us to define a class.| 21|  **continue**|
It continues to the next iteration of a loop| 22|  **del**|  It deletes a
reference to an object.| 23|  **except**|  Used with exceptions, what to do
when an exception occurs| 24|  **finally**|  Finally is use with exceptions, a
block of code that will be executed no matter if there is an exception or
not.| 25|  **from**|  The form is used to import specific parts of any
module.| 26|  **global**|  This declares a global variable.| 27|  **import**|
This is used to import a module.| 28|  **in**|  It’s used to check if a value
is present in a list, tuple, etc, or not.| 29|  **is**|  This is used to check
if the two variables are equal or not.| 30|  **None**|  This is a special
constant used to denote a null value or avoid. It’s important to remember, 0,
any empty container(e.g empty list) do not compute to None| 31|  **nonlocal**|
It’s declared a non-local variable.| 32|  **raise**|  This raises an
exception| 33|  **yield**|  It’s ends a function and returns a generator.  
---|---|---  
  
 **Identifiers:** The identifier is a name used to identify a variable,
function, class, module, etc. The identifier is a combination of character
digits and underscore. The identifier should start with a character or
Underscore then use digit. The characters are A-Z or a-z,a UnderScore ( _ )
and digit (0-9). we should not use special characters ( #, @, $, %, ! ) in
identifiers.

 **Examples of valid identifiers:**

  1. var1
  2. _var1
  3. _1_var
  4. var_1

 **Examples of invalid identifiers**

  1. !var1
  2. 1var
  3. 1_var
  4. var#1

 **Example 1:** Example of and, or, not, True, False keywords.

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

print("example of True, False, and, or not keywords")

# compare two operands using and operator

print(True and True)

# compare two operands using or operator

print(True or False)

# use of not operator

print(not False)  
  
---  
  
 __

 __

 **Output:**

    
    
    example of True, False, and, or not keywords
    True
    True
    True

 **Example 2:** Example of a break, continue.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# execute for loop

for i in range(1, 11):

 

 # print the value of i

 print(i)

 

 # check the value of i is less then 5

 # if i lessthen 5 then continue loop

 if i < 5: 

 continue

 

 # if i greather then 5 then break loop

 else: 

 break  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    2
    3
    4
    5

 **Example 3:** example of for, in, if, elif and else keyword.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# run for loop

for t in range(1, 5):

 # print one of t ==1

 if t == 1:

 print('One')

 # print two if t ==2

 elif t == 2:

 print('Two')

 else:

 print('else block execute')  
  
---  
  
 __

 __

 **Output:**

    
    
    One
    Two
    else block execute
    else block execute

 **Example 4:** Example of def, if and else keywords.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# define GFG() function using def keyword

def GFG():

 i=20

 # check i is odd or not

 # using if and else keyword

 if(i % 2 == 0):

 print("given number is even")

 else:

 print("given number is odd") 

 

# call GFG() function 

GFG()  
  
---  
  
 __

 __

 **Output:**

    
    
    given number is even

 **Example 5:** example try, except, raise.

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

def fun(num):

 try:

 r = 1/num

 except:

 print('Exception raies')

 return

 return r

print(fun(10))

print(fun(0))  
  
---  
  
 __

 __

 **Output:**

    
    
    0.1
    Exception raies
    None

 **Example 6:** Example of a lambda keyword.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# define a anonymous using lambda keyword

# this labda function increment the value of b

a = lambda b: b+1

# run a for loop

for i in range(1, 6):

 print(a(i))  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    3
    4
    5
    6

 **Example 7:** use of return keyword.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# define a function

def fun():

 # declare a variable

 a = 5

 # return the value of a

 return a

# call fun method and store

# it's return value in a variable 

t = fun()

# print the value of t

print(t)  
  
---  
  
 __

 __

 **Output:**

    
    
    5

 **Example 8:** use of a del keyword.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# create a list

l = ['a', 'b', 'c', 'd', 'e']

# print list before using del keyword

print(l)

del l[2]

# print list after using del keyword

print(l)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['a', 'b', 'c', 'd', 'e']
    ['a', 'b', 'd', 'e']

 **Example 9** : use of global keyword.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# declare a variable

gvar = 10

# create a function

def fun1():

 # print the value of gvar

 print(gvar)

# declare fun2()

def fun2():

 # declare global value gvar

 global gvar

 gvar = 100

# call fun1()

fun1()

# call fun2()

fun2()  
  
---  
  
 __

 __

 **Output:**

    
    
    10

 **Example 10:** example of yield keyword.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

def Generator():

 for i in range(6):

 yield i+1

t = Generator()

for i in t:

 print(i)  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    2
    3
    4
    5
    6

 **Example 10:** example of assert keyword.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def sumOfMoney(money):

 assert len(money) != 0,"List is empty."

 return sum(money)

money = []

print("sum of money:",sumOfMoney(money))  
  
---  
  
 __

 __

 **Output:**

    
    
    AssertionError: List is empty.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

