Python tempfile module



 **Tempfile** is a Python module used in a situation, where we need to read
multiple files, change or access the data in the file, and gives output files
based on the result of processed data. Each of the output files produced
during the program execution was no longer needed after the program was done.
In this case, a problem arose that many output files were created and this
cluttered the file system with unwanted files that would require deleting
every time the program ran.

In this situation, tempfiles are used to create temporary files so that next
time we don’t have to find delete when our program is done with them

## Working with temporary files

A temporary file can also be used for securing sensitive data. This module
contains many functions to create temporary files and folders, and access them
easily.

### Creating Temporary Files

Suppose your application needs a temporary file for use within the program,
i.e. it will create one file, use it to store some data, and then delete it
after use. To achieve this, we can use the TemporaryFile() function.

  * First, we have to import tempfile then the file is created using the TemporaryFile() function.
  * The file is opened in w+b (both read and write to the open file)mode by default.
  * This function creates a temporary file in the temp directory and returns a file object
  * the file’s entry in the temp folder is removed as soon as the file object is closed

 **Code:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tempfile

 

temp = tempfile.TemporaryFile()

print('temp:',temp)

print('temp.name:', temp.name)

temp.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    temp: <_io.BufferedRandom name=6>
    temp.name: 6

### Reading and writing plain text into Temporary Files

Similar to reading or writing from a file, we can use the same kind of
function calls to do this from a temporary file too!!

  * Create a temporary file and write some data to it
  * After writing, you have to rewind the file handle using seek() in order to read the data back from it.
  * Go back to the beginning and read data from the file
  * Close the file, it will be removed

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tempfile

 

temp = tempfile.TemporaryFile()

 

try:

 temp.write(b'Hello world!')

 temp.seek(0)

 

 print(temp.read())

finally:

 temp.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    b'Hello world!'

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tempfile

 

f = tempfile.TemporaryFile()

 

try:

 f.write(b'Welcome to geeksforgeeks')

 f.seek(0)

 data=f.read()

 print(data)

finally:

 f.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    b'Welcome to geeksforgeeks'

###  **Creating a named Temporary Files**

If your application spans multiple processes, or even hosts, naming the file
is the simplest way to pass it between parts of the application. The
NamedTemporaryFile() function creates a file with a name, accessed from the
name attribute.

  * First import tempfile and then the file is created using the NamedTemporaryFile() function.
  * NamedTemporaryFile returns a file-like object that can be used as temporary storage, however, contrary to TemporaryFile, a file created with NamedTemporaryFile is guaranteed to have a visible name during its lifetime.
  * TemporaryFile gets destroyed as soon as the file is closed, NamedTemporaryFile has support for the deleted flags, which defaults to True

 **Example 1:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tempfile

 

print("Creating a named temporary file..")

temp = tempfile.NamedTemporaryFile()

 

print("Created file is:", temp)

print("Name of the file is:", temp.name)

temp.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    Creating a named temporary file..
    Created file is: <tempfile._TemporaryFileWrapper object at 0x7ff135ed1710>
    Name of the file is: /tmp/tmpg8efl258

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tempfile

 

fo = tempfile.NamedTemporaryFile()

print(fo.name)

 

fo.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    /tmp/tmp6nxmoagy

### Providing Filename Suffix and Prefix

Sometimes we need to add a prefix or suffix to a temp-file’s name. It will
help us to identify all temp files created by our program

  * We can add suffix or prefix to the name of a named temporary file, by using the parameters ‘suffix’ and ‘prefix’.
  * Use the same NamedTemporaryFile function defined above. The only thing we need to add is two extra parameters while calling this function: suffix and prefix
  * So, if we will pass the two extra arguments suffix and prefix to the NamedTemporaryFile() function, it will automatically add those at the start and end of the file name

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tempfile

 

temp = tempfile.NamedTemporaryFile(prefix="demoPrefix_",

 suffix="_demoSuffix")

 

print("Created file is:", temp)

print("Name of the file is:", temp.name)

temp.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    Created file is: <tempfile._TemporaryFileWrapper object at 0x7fbf5d39b6d8>
    Name of the file is: /tmp/demoPrefix_t_inxb7v_demoSuffix

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import tempfile

 

temp=tempfile.NamedTemporaryFile(suffix='_greeks',

 prefix='forgreeks_')

print(temp.name)  
  
---  
  
 __

 __

 **Output:**

    
    
    /tmp/forgreeks_4sigabye_greeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

