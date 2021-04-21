Python compile() Function



 **Compile():** Consider a situation where we have a piece of Python code in a
string and we want to compile it so that we can later run it when needed. The
compile method does this task. It takes sourcecode as input and returns a code
object which is ready to be executed.

 **Syntax:**

    
    
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
    

**Parameters:**

>  **Source** – It can be a normal string, a byte string, or an AST object
>
>  **Filename** -This is the file from which the code was read. If it wasn’t
> read from a file, you can give a name yourself.
>
>  
>
>
>  
>
>
>  **Mode** – Mode can be exec, eval or single.  
>  **a.** eval – If the sorce is a single expression.  
>  **b.** exec – It can take a block of a code that has Python statements,
> class and functions and so on.  
>  **c.** single – It is used if consists of a single interactive statement
>
>  **Flags** (optional) and dont_inherit (optional) – Default value=0. It
> takes care that which future statements affect the compilation of the
> source.  
>  **Optimize (optional)** – It tells optimization level of compiler. Default
> value -1.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of compile().

 

# Creating sample sourcecode to multiply two variables

# x and y.

srcCode = 'x = 10\ny = 20\nmul = x * y\nprint("mul =", mul)'

 

# Converting above source code to an executable

execCode = compile(srcCode, 'mulstring', 'exec')

 

# Running the executable code.

exec(execCode)  
  
---  
  
 __

 __

 **Output:**

    
    
    mul = 200
    

__

__  
__

__

__  
__  
__

# Another Python code to demonstrate working of compile().

x = 50

 

# Note eval is used for single statement

a = compile('x', 'test', 'single')

exec(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    50
    

**Applications:**

  1. If the Python code is in string form or is an AST object, and you want to change it to a code object, then you can use compile() method.
  2. The code object returned by the compile() method can later be called using methods like: exec() and eval() which will execute dynamically generated Python code.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

