Global keyword in Python



Global keyword is a keyword that allows a user to modify a variable outside of
the current scope. It is used to create global variables from a non-global
scope i.e inside a function. Global keyword is used inside a function only
when we want to do assignments or when we want to change a variable. Global is
not needed for printing and accessing.

 **Rules of global keyword:**

  * If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
  * Variables that are only referenced inside a function are implicitly global.
  * We Use global keyword to use a global variable inside a function.
  * There is no need to use global keyword outside a function.

 **Use of global keyword:**  
To access a global variable inside a function there is no need to use global
keyword.  
 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing no need to

# use global keyword for accessing

# a global value

 

# global variable

a = 15

b = 10

 

# function to perform addition

def add():

 c = a + b

 print(c)

 

# calling a function

add()  
  
---  
  
 __

 __

 **Output:**

    
    
     
    25
    

If we need to assign a new value to a global variable then we can do that by
declaring the variable as global.  
 **Code 2:** Without global keyword

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing to modify

# a global value without using global

# keyword

 

a = 15

 

# function to change a global value

def change():

 

 # increment value of a by 5

 a = a + 5

 print(a)

 

change()  
  
---  
  
 __

 __

 **Output:**

    
    
    UnboundLocalError: local variable 'a' referenced before assignment
    

This output is an error because we are trying to assign a value to a variable
in an outer scope. This can be done with the use of **global** variable.  
 **Code 3 :** With global keyword

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to modify a global

# value inside a function

 

x = 15

def change():

 

 # using a global keyword

 global x

 

 # increment value of a by 5

 x = x + 5

 print("Value of x inside a function :", x)

change()

print("Value of x outside a function :", x)  
  
---  
  
 __

 __

 **Output:**

    
    
    Value of x inside a function : 20
    Value of x outside a function : 20
    

In the above example, we first define x as global keyword inside the function
change(). The value of x is then incremented by 5, ie. x=x+5 and hence we
get the output as 20.  
As we can see by changing the value inside the function change(), the change
is also reflected in the value outside the global variable.  
  
**Global variables across python modules :**  
The best way to share global variables across different modules within the
same program is to create a special module (often named config or cfg). Import
the config module in all modules of your application; the module then becomes
available as a global name. There is only one instance of each module and so
any changes made to the module object get reflected everywhere. For Example,
sharing global variables across modules  
 **Code 1:** Create a config.py file to store global variables:

 __

 __  
 __

 __

 __  
 __  
 __

x= 0

y = 0

z ="none"  
  
---  
  
 __

 __

 **Code 2:** Create a modify.py file to modify global variables:

 __

 __  
 __

 __

 __  
 __  
 __

import config

config.x = 1

config.y = 2

config.z ="geeksforgeeks"  
  
---  
  
 __

 __

Here we have modified the value of x, y, and z. These variables were defined
in the moduleconfig.py, hence we have to import config module and we can
use config.variable_name to access these variables.  
 **Code 3:** Create a main.py file to modify global variables:

 __

 __  
 __

 __

 __  
 __  
 __

import config

import modify

print(config.x)

print(config.y)

print(config.z)  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    2
    geeksforgeeks
    

**Global in Nested functions**  
In order to use global inside a nested functions, we have to declare a
variable with global keyword inside a nested function

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing a use of

# global in nested function

 

def add():

 x = 15

 

 def change():

 global x

 x = 20

 print("Before making changing: ", x)

 print("Making change")

 change()

 print("After making change: ", x)

 

add()

print("value of x",x)  
  
---  
  
 __

 __

 **Output:**

    
    
    Before making changing:  15
    Making change
    After making change:  15
    value of x 20
    

In the above example Before and after making change(), the variable x takes
the value of local variable i.e x = 15. Outside of the add() function, the
variable x will take value defined in the change() function i.e x = 20.
because we have used global keyword in x to create global variable inside
the change() function (local scope).

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

