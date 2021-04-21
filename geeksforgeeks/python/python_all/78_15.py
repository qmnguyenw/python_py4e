codeop.compile_command in Python



With the help of **codeop.compile_command()** method, we can compile the
single or multiple lines of code to check for the syntax error if any by using
codeop.compile_command() method.

>  **Syntax :** codeop.compile_command(code)
>
>  **Return :** Return the object or compilation error if any.

 **Example #1 :**  
In this example we can see that by using codeop.compile_command() method, we
are able to compile the multiple lines of code by using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# import codeop

from codeop import compile_command

 

code = 'a = 5 b = 9; print(a + b)'

# Using codeop.compile_command() method

compile_command(code)   
  
---  
  
__

__

**Output :**

  

  

> a = 5 b = 9; print(a + b)  
> ^  
> SyntaxError: invalid syntax

 **Example #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import codeop

from codeop import compile_command

 

code = '-a = 5'

# Using codeop.compile_command() method

compile_command(code)   
  
---  
  
__

__

**Output :**

> SyntaxError: can’t assign to operator

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

