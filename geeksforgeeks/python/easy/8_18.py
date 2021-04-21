Python – Call function from another file



Given a Python file, we need to call a function in it defined in any other
Python file.  
 **Example:**

> Suppose there is a file test.py which contains the definition of the
> function displayText().  
> #test.py>
>
> def displayText():  
>  print( "Geeks 4 Geeks!")
>
> 
>
> We need to call the function displayText() in any other Python file such
> that wherever we call displayText() function displays text present in it.
> This can be done using Python modules.

 **Approach:**

  

  

  1. Create a Python file containing the required functions.
  2. Create another Python file and import the previous Python file into it.
  3. Call the functions defined in the imported file.

The above approach has been used in the below examples:

 **Example 1:** A Python file test.py is created and it contains the
displayText() function.

 __

 __  
 __

 __

 __  
 __  
 __

# test.py>

 

# function

def displayText():

 print( "Geeks 4 Geeks !")  
  
---  
  
 __

 __

Now another Python file is created which calls thedisplayText() function
defined in test.py.

 __

 __  
 __

 __

 __  
 __  
 __

# importing all the

# functions defined in test.py

from test import *

 

 

# calling functions

displayText()  
  
---  
  
 __

 __

 **Output:**

    
    
    Geeks 4 Geeks!
    

In the above program, all the functions defined in test.py file is imported
then a functions is called.

 **Example 2:** A Python file calc.py is created containing addNumbers(),
subractNumbers(), multiplyNumbers(), divideNumbers() and
modulusNumbers().

 __

 __  
 __

 __

 __  
 __  
 __

# calc.py>

 

# functions

def addNumbers(a, b):

 print("Sum is ", a + b)

 

def subtractNumbers(a, b):

 print("Differnece is ", a-b)

 

def multiplyNumbers(a, b):

 print("Product is ", a * b)

 

def divideNumbers(a, b):

 print("Division is ", a / b)

 

def modulusNumbers(a, b):

 print("Remainder is ", a % b)  
  
---  
  
 __

 __

The functions defined incalc.py is called in another Python file.

 __

 __  
 __

 __

 __  
 __  
 __

# importing limited functions

# defined in calc.py

from calc import addNumbers, multiplyNumbers

 

 

# calling functions

addNumbers(2, 5)

multiplyNumbers(5, 4)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    7
    20
    

In the above program, all the functions defined in calc.py are not imported.  
To import all the functions defined in a Python file:

 **Syntax:**

    
    
    from file import *
    

To import only required functions defined in a Python file:

 **Syntax:**

    
    
    from file import func1, func2, func3
    

**Example 3:**  
The below Python files test.py and calc.py are created having various
function definitions.

 __

 __  
 __

 __

 __  
 __  
 __

# test.py>

 

# function defined in test.py

def displayText():

 print("\nGeeks 4 Geeks !")  
  
---  
  
 __

 __

 __

 __  
 __

 __

 __  
 __  
 __

# calc.py>

 

# functions defined in calc.py

def addNumbers(a, b):

 print("Sum is ", a + b)

 

def subtractNumbers(a, b):

 print("Differnece is ", a-b)

 

def multiplyNumbers(a, b):

 print("Product is ", a * b)

 

def divideNumbers(a, b):

 print("Division is ", a / b)

 

def modulusNumbers(a, b):

 print("Remainder is ", a % b)  
  
---  
  
 __

 __

Both files are imported into an another Python file namedfile.py.

 __

 __  
 __

 __

 __  
 __  
 __

# file.py> 

 

# importing all the functions

# defined in calc.py

from calc import *

 

# importing required functions

# defined in test.py

from test import displayText

 

 

# calling functions defined 

# in calc.py

addNumbers(25, 6)

subtractNumbers(25, 6)

multiplyNumbers(25, 6)

divideNumbers(25, 6)

modulusNumbers(25, 6)

 

# calling function defined

# in test.py

displayText()  
  
---  
  
 __

 __

 **Output:**

    
    
    Sum is  31
    Difference is  19
    Product is  150
    Division is  4.166666666666667
    Remainder is  1
    
    Geeks 4 Geeks!
    

In the above program, functions defined in test.py and calc.py are called
in a differnt file which is file.py.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

