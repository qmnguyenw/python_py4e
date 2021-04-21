Difference between various Implementations of Python



When we speak of Python we often mean not just the language but also the
implementation. Python is actually a specification for a language that can be
implemented in many different ways.

 **Background**  
 _Before proceeding further let us understand the difference between bytecode
and machine code(native code)._  
 **Machine Code( _aka native code_ )**  
Machine code is set of instructions that directly gets executed by the CPU.
Each instruction performs a very unique task, such as load or an logical
operation on data in CPU memory. Almost all the high level languages such as C
translate the source code into executable machine code with the help of
Compilers, loaders and linkers. Every processor or processor family has its
own machine code instruction set.  
![machine](https://media.geeksforgeeks.org/wp-content/uploads/Machine.jpg)  
 **Bytecode**  
Bytecode is also binary representation executed by virtual machine (not by CPU
directly). The virtual machine (which is written different for different
machines) converts binary instruction into a specific machine instruction. One
of the language that uses the concept of Bytecode is Java.  
![byte](https://media.geeksforgeeks.org/wp-content/uploads/byteCode.jpg)

 _Machine Code is much faster as compared to Bytecode but Bytecode is portable
and secure as compared to Machine Code._

 **Implementations of Python**  
 **Cpython**  
The default implementation of the Python programming language is Cpython. As
the name suggests Cpython is written in C language. Cpython compiles the
python source code into intermediate bytecode, which is executed by the
Cpython virtual machine. CPython is distributed with a large standard library
written in a mixture of C and Python. CPython provides the highest level of
compatibility with Python packages and C extension modules. All versions of
the Python language are implemented in C because CPython is the reference
implementation.  
Some of the implementations which are based on CPython runtime core but with
extended behavior or features in some aspects are Stackless Python, wpython,
MicroPython.  
Stackless Python – CPython with an emphasis on concurrency using tasklets and
channels (used by dspython for the Nintendo DS)

 **Other Implementations**  
There are some other implementations of the Python language too The only
implementations that are known to be compatible with a given version of the
language are **IronPython** , **Jython** and **PyPy**.

  

  

 **Jython**  
Jython is an implementation of the Python programming language that can run on
the Java platform. Jython programs use Java classes instead of Python modules
.Jython compiles into Java byte code, which can then be run by Java virtual
machine. Jython enables the use of Java class library functions from the
Python program. Jython is slow as compared to Cpython and lacks compatibility
with CPython libraries.  
![geeks](https://media.geeksforgeeks.org/wp-content/uploads/python.jpg)

 **IronPython**  
A Python implementation written in C# targeting Microsoft’s .NET framework.
Similar to Jython, it uses .Net Virtual Machine i.e Common Language Runtime.
IronPython can use the .NET Framework and Python libraries, and other .NET
languages can use Python code very efficiently. IronPython performs better in
Python programs that use threads or multiple cores, as it has a JIT, and also
because it doesn’t have the Global Interpreter Lock.

 **PyPy**  
 _“If you want your code to run faster, you should probably just use PyPy.” —
Guido van Rossum (creator of Python)_  
Python is dynamic programming language. Python is said to be slow as the
default CPython implementation compiles the python source code in bytecode
which is slow as compared to machine code(native code). Here PyPy comes in.  
PyPy is an implementation of the Python programming language written in
Python. The Interpreter is written in RPython (a subset of Python).

![flo](https://media.geeksforgeeks.org/wp-content/uploads/pythonByteCode.jpg)

PyPy uses (just-in-time compilation). In simple terms JIT uses compilation
methods to make interpreter system more efficient and fast. So basically JIT
makes it possible to compile the source code into native machine code which
makes it very fast.  
PyPy also comes with default with support for stackless mode, providing micro-
threads for massive concurrency. _Python is said to be approximately 7.5 times
faster than Cpython._

Some other Implementations of Python are **CLPython** , **Pyston** , **Psyco**
, **Cython** , **IPython**.

 **References:**

  * https://wiki.python.org/moin/PythonImplementations
  * http://pypy.org/
  * https://wiki.python.org/moin/IronPython
  * http://www.jython.org/

This article is contributed by **Saurabh Daalia**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

