File flush() method in Python



Python allows users to manage files by using the concept of file handling. A
user can open, read, write, manipulate files and can perform many other file
handling operations to a file. One of these file handling operations is the
file flush() method in Python.

## File flush() method –

The flush() method in Python file handling clears the internal buffer of the
file. In Python, files are automatically flushed while closing them. However,
a programmer can flush a file before closing it by using the flush() method.  
 **Syntax:**

    
    
    fileObject.flush()

This method does not require any parameters and it does not return anything.

 **Example 1:**  
Now let us look at the below example which illustrates the use of flush()
method. Before going through the program a text file gfg.txt is created
having the below content.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200307121211/gfg_txt.png)

 __

 __  
 __

 __

 __  
 __  
 __

# openinng the file in read mode

fileObject = open("gfg.txt", "r")

 

# clearing the input buffer

fileObject.flush()

 

# reading the content of the file

fileContent = fileObject.read()

 

# displaying the content of the file

print(fileContent)

 

# closing the file

fileObject.close()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Geeks 4 geeks!

In the above program, the gfg.txt is opened in read mode then the
flush() method only clears the internal buffer of the file, it does not
affect the content of the file. So, the contents of the file can be read and
displayed.

 **Example 2:**  
Now let us look at another example which demonstrates the use of the flush()
method.

 __

 __  
 __

 __

 __  
 __  
 __

# program to demonstrate the use of flush()

 

# creating a file

fileObject = open("gfg.txt", "w+")

 

# writing into the file

fileObject.write("Geeks 4 geeks !")

 

# closing the file

fileObject.close()

 

 

 

# opening the file to read its content

fileObject = open("gfg.txt", "r")

 

# reading the contents before flush()

fileContent = fileObject.read()

 

# displaying the contents

print("\nBefore flush():\n", fileContent)

 

 

 

# clearing the input buffer

fileObject.flush()

 

# reading the contents after flush()

# reads nothing as the internal buffer is cleared

fileContent = fileObject.read()

 

# displaying the contents

print("\nAfter flush():\n", fileContent)

 

# closing the file

fileObject.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    Before flush():
    Geeks 4 geeks!
    
    After flush():
    

In this program initially, we create gfg.txt file and write Geeks 4 geeks!
as content in it and then we close the file. After that we read and display
the contents of the file and then the flush() method is called which clears
the input buffer of the file so the fileObject reads nothing and
fileContent remains an empty variable. Hence nothing is displayed after
flush() method.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

