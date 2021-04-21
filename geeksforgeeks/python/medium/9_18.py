Deconstructing Interpreter: Understanding Behind the Python Bytecode



When the CPython interpreter executes your program, it first translates onto a
sequence of bytecode instructions. Bytecode is an intermediate language for
the Python virtual machine that’s used as a performance optimization.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200423221016/python4.jpg)

Instead of directly executing the human-readable source code, compact numeric
codes, constants, and references are used that represent the result of
compiler parsing and semantic analysis. This saves time and memory for
repeated executions of programs or part of programs. For example, the bytecode
resulting from this compilation step is cached on disk in .pyc and .pyo files
so that executing the same Python file is faster the second time around. All
of this is completely transparent to the programmer. You don’t have to be
aware that this intermediate translation step happens, or how the Python
virtual machine deals with the bytecode. In fact, the bytecode format is
deemed an implementation detail and not guaranteed to remain stable or
compatible between Python versions. And yet, one may find it very enlightening
to see how the sausage is made and to peek behind the abstractions provided by
the CPython interpreter. Understanding at least some of the inner workings can
help you write more performant code.

 **Example:** Let’s take this simple **showMeByte()** function as a lab sample
and Understand’s Python’s bytecode:

 __

 __  
 __

 __

 __  
 __  
 __

def showMeByte(name):

 return "hello "+name+" !!!"

 

 

print(showMeByte("amit kumra"))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    hello amit kumra !!!

CPython first translates our source code into an intermediate language before
it runs it. We can see the results of this compilation step. Each function has
a __code__ attribute(in Python 3) that we can use to get at the virtual
machine instructions, constants, and variables used by our showMeByte
function:

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

def showMeByte(name):

 return "hello "+name+" !!!"

 

 

print(showMeByte.__code__.co_code)

 

print(showMeByte.__code__.co_consts)

 

print(showMeByte.__code__.co_stacksize)

 

print(showMeByte.__code__.co_varnames)

 

print(showMeByte.__code__.co_flags)

 

print(showMeByte.__code__.co_name)

 

print(showMeByte.__code__.co_names)  
  
---  
  
 __

 __

 **Output:**

    
    
    b'd\x01|\x00\x17\x00d\x02\x17\x00S\x00'
    (None, 'hello ', ' !!!')
    2
    ('name',)
    67
    showMeByte
    ()

You can see co_consts contains parts of the greeting string our function
assembles. Constants and code are kept separate to save memory space. So
instead of repeating the actual constant values in the co_code instruction
stream, Python stores constants separately in a lookup table. The instruction
stream can then refer to a constant with an index into the lookup table. The
same is true for variables stored in the co_varnames field. CPython developers
gave us another tool called a disassembler to make inspecting the bytecode
easier. Python’s bytecode disassembler lives in the dis module that’s part of
the standard library. So we can just import it and call dis.dis() on our
greet function to get a slightly easier-to-read representation of its
bytecode:

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import dis

 

 

def showMeByte(name):

 return "hello "+name+" !!!"

 

dis.dis(showMeByte)

bytecode = dis.code_info(showMeByte)

print(bytecode)

 

bytecode = dis.Bytecode(showMeByte)

print(bytecode)

 

for i in bytecode:

 print(i)  
  
---  
  
 __

 __

 **Output:**

![python-bytecode](https://media.geeksforgeeks.org/wp-
content/uploads/20200424214728/python-bytecode.png)

The executable instructions or simple instructions tell the processor what to
do. Each instruction consists of an operation code (opcode). Each executable
instruction generates one machine language instruction. The main thing
disassembling did was split up the instruction stream and give each opcode in
it a human-readable name like LOAD_CONST. You can also see how constant and
variable references are now interleaved with the bytecode and printed in full
to spare us the mental gymnastics of a co_const and co_varnames table lookup.

  

  

It first retrieves the constant at index 1(‘Hello’) and puts it on the stack.
It then loads the contents of the name variable and also puts them on the
stack. The stack is the data structure used as internal working storage for
the virtual machine. There are different classes of virtual machines and one
of them is called a stack machine. CPython’s virtual machine is an
implementation of such a stack machine. CPython’s virtual machine is an
implementation of such a stack machine. Let’s assume the stack starts out
empty. After the first two opcodes have been executed, this is what contents
of the VM look like(0 is the topmost element):

    
    
    0: ’amit kumra’(contents of “name”)
    1: ‘hello ‘

The **BINARY_ADD** instruction pops the two string values off the stack,
concatenation them, and then pushes the result on the stack again:

    
    
    0: ‘hello amit kumra’

Then there’s another LOAD_CONST to get the exclamation mark string on the
stack:

    
    
    0 : ‘ !!!’
    1:’Hello amit kumra’

The next BINARY_ADD opcode again combines the two to generate the final
greeting string:

    
    
    0: ‘hello amit kumra !!!’

The last bytecode instruction is **RETURN_VALUE** which tells the virtual
machine that what’s currently on top of the stack is the return value for this
function so it can be passed on to the caller. So, finally, we traced back how
our showMeCode() function gets executed internally by the CPython virtual
machine.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

