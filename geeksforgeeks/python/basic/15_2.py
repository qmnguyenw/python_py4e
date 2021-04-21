Absolute and Relative Imports in Python



 **Working ofimport in python :**

Import in Python is similar to #include header_file in C/C++. Python modules
can get access to code from another module by importing the file/function
using import. The import statement is the most common way of invoking the
import machinery, but it is not the only way. Import statement consists of the
import keyword along with the name of the module.

The import statement involves two operations, it searches for a module and it
binds the result of the search to name in local scope. When a module is
imported, Python runs all of the code in the module file and made available to
the importer file.

When a module is imported then interpreter first searches it in sys.modules
, which is the cache of all modules which have been previously imported. If it
is not found then it searches in all built-in modules with that name, if it is
found then interpreter runs all of the code and made available to file. If the
module is not found then it searches for a file with the same name in the list
of directories given by the variable sys.path.  
sys.path is a variable containing a list of paths that contains python
libraries, packages, and a directory containing the input script. For example
a module named math is imported then interpreter search it in a built-in
modules, if it is not found then it searches for a file named math.py in
list of directories given by sys.path.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program importing

# math module

 

import math

print(math.pi)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    3.141592653589793
    

  
**Syntax of import statements :**  
User can import both packages and modules. (Note that importing a package
essentially imports the package’s __init__.py file as a module.) User can
also import specific objects from a package or module.  
There are generally two types of import syntax. When you use the first one,
you import the resource directly.

    
    
    import gfg
    

gfg can be a package or a module.

When user uses the second syntax, then user import the resource from another
package or module.

    
    
    from gfg import geek
    

_geek_ can be a module, subpackage, or object, such as a class or function.  
  
**Styling of import statements :**  
PEP8, the official style guide for python, has set of rules for how to
formulate the python code to maximize its readability. For writing import
statements there are some points to follow:

  1. Imports should always be written at the top of the file, just after any module comments and docstrings.
  2. Imports should usually be separated by a blank space.
  3. Imports should be grouped in the following order.
    * Standard library imports (Python’s built-in modules)
    * Related third party imports.
    * Local application/library specific imports

It is also good to order import statements alphabetically within each import
group.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# how to style import statements

 

import math

import os

 

# Third party imports

from flask import Flask

from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

 

# Local application imports

from local_module import local_class

from local_package import local_function  
  
---  
  
 __

 __

### Absolute imports :

Absolute import involves full path i.e., from the project’s root folder to the
desired module. An absolute import state that the resource to be imported
using its full path from the project’s root folder.

 **Syntax and Practical Examples :**  
Let’s see we have the following directory structure:  
![](https://media.geeksforgeeks.org/wp-content/uploads/absolute-import-
updated.jpg)  
Here a directory named project, under which two subdirectories namely pkg1,
pkg2. pkg1 has two modules, module1 and module2.  
pkg2 contains three modules, module3, module4, __init__.py and one
subpackage name subpkg1 which contains module5.py. Let’s assume the following:

  

  

  * pkg1 / module1.py contain a function, fun1
  * pkg2 / module3.py contain a function, fun2
  * pkg2 / subpkg1 / module5.py contain a function fun3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# practical example of

# absolute imports

 

# importing a fun1 from pkg1/module1

from pkg1.import module1 import fun1

 

from pkg1 import module2

 

# importing a fun2 from pkg2/module3

from pkg2 import module3 import fun2

 

# importing a fun3 from pkg2/subpkg1/module5

from pkg2.subpkg1.module5 import fun3  
  
---  
  
 __

 __

In this example, we are importing the modules by writing full path from its
root folder.  
  
**Pros and Cons of Absolute imports :**  
 **Pros:**

  * Absolute imports are very useful because they are clear and straight to the point.
  * Absolute import is easy to tell exactly from where the imported resource is, just by looking at the statement.
  * Absolute import remain valid even if the current location of the import statement changes.

 **Cons:**  
If the directory structure is very big then usage of absolute imports is not
meaningful. In such case using relative imports works well.

    
    
    from pkg1.subpkg2.subpkg3.subpkg4.module5 import fun6
    

### Relative imports :

Relative import specifies object or module imported from its current location,
that is the location where import statement resides. There two types of
relative imports :

  * Implicit relative imports :

Implicit relative import have been disapproved in Python(3.x).

  * Explicit relative imports :

Explicit relative import have been approved in Python(3.x).

 **Syntax and Practical Examples :**  
The syntax of relative import depends on current location as well as a
location of module or object to be imported. Relative imports use dot(.)
notation to specify a location. Single dot specifies that the module is in the
current directory, two dots indicate that module is in its parent directory of
the current location and three dots indicate that it is in grandparent
directory and so on.  
Let’s see we have the following directory structure:  
![](https://media.geeksforgeeks.org/wp-content/uploads/absolute-import-
updated.jpg)  
Let’s assume the following:

  * pkg1 / module1.py contain a function, fun1
  * pkg2 / module3.py contain a function, fun2
  * pkg2 / subpkg1 / module5.py contain a function fun3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# practical example of

# relative imports

 

# importing fun1 into pkg1/module1.py

from .module1 import fun1

 

# importing fun2 and fun3 into pkg2/module3.py 

from .module3 import fun2

from .subpackage1.module5 import fun3  
  
---  
  
 __

 __

 **Pros and Cons of Relative imports :**  
 **Pros:**

  * Working with relative imports is concise and clear.
  * Based on current location it reduces the complexity of an import statement . **Cons:**
      * Relative imports is not so readable as absolute ones.
      * Using relative imports it is not easy because it is very hard to tell the location of a module.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

