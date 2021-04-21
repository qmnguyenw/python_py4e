How to generate byte code file in python ?



Whenever the Python script compiles, it automatically generates a compiled
code called as byte code. The byte-code is not actually interpreted to machine
code, unless there is some exotic implementation such as PyPy.

The byte-code is loaded into the Python run-time and interpreted by a virtual
machine, which is a piece of code that reads each instruction in the byte-code
and executes whatever operation is indicated.

Byte Code is automatically created in the same directory as .py file, when a
_module_ of python is imported for the first time, or when the source is more
recent than the current compiled file. Next time, when the program is run,
python interpretator use this file to skip the compilation step.

Running a script is not considered an **import** and no .pyc file will be
created. For instance, let’s write a script file **abc.py** that imports
another module **xyz.py**. Now run **abc.py** file, **xyz.pyc** will be
created since xyz is imported, but no **abc.pyc** file will be created since
**abc.py** isn’t being imported.

But there exist an inbuilt **py_compile** and **compileall** modules and
commands which facilitate the creation of .pyc file.

  

  

  1. Using **py_compile.compile** function: The _py_compile_ module can manually compile any module. One way is to use the py_compile.compile function in that module interactively:
    
    
    >>> import py_compile
    >>> py_compile.compile('abc.py')
    

This will write the .pyc to the same location as abc.py.

  2. Using **py_compile.main()** function: It compiles several files at a time.
    
    
    >>> import py_compile
    >>> py_compile.main(['File1.py','File2.py','File3.py'])
    

  3. Using **compileall.compile_dir()** function: It compiles every single python file present in the directory supplied.
    
    
    >>> import compileall
    >>> compileall.compile_dir(directoryname)
    

  4. Using **py_compile** in Terminal:
    
    
    $ python -m py_compile File1.py File2.py File3.py ...
    

Or, for Interactive Compilation of files

    
    
    $ python -m py_compile -
      File1.py
      File2.py
      File3.py
       .
       .
       .
    

  5. Using **compileall** in Terminal: This command will automatically go recursively into sub directories and make .pyc files for all the python files it finds.
    
    
    $ python -m compileall 
    

**Note** : The **compileall** and **py_compile** module is part of the python
standard library, so there is no need to install anything extra to use it.

 **References:**  
1\. https://docs.python.org/3/library/py_compile.html  
2\. https://docs.python.org/2/library/compileall.html  
3\. Effbot

This article is contributed by Shubham Bansal. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

