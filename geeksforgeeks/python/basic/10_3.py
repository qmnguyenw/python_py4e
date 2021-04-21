Open a File in Python



Python provides inbuilt functions for creating, writing and reading files.
There are two types of files that can be handled in Python, normal text files
and binary files (written in binary language, 0s and 1s).

  *  **Text files:** In this type of file, Each line of text is terminated with a special character called **EOL (End of Line)** , which is the new line character (‘\n’) in Python by default.
  *  **Binary files:** In this type of file, there is no terminator for a line and the data is stored after converting it into machine-understandable binary language.

> Refer the below articles to get the idea about basics of file handling.
>
>   * Basics of file handling
>   * Reading and Writing to file
>

## Opening a file

Opening a file refers to getting the file ready either for reading or for
writing. This can be done using the open() function. This function returns a
file object and takes two arguments, one that accepts the file name and
another that accepts the mode(Access Mode). Now, the question arises what is
access mode?

Access modes govern the type of operations possible in the opened file. It
refers to how the file will be used once it’s opened. These modes also define
the location of the **File Handle** in the file. **File handle** is like a
cursor, which defines from where the data has to be read or written in the
file. There are 6 access modes in python.

  *  **Read Only (‘r’):** Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exist, raises I/O error. This is also the default mode in which the file is opened.
  *  **Read and Write (‘r+’):** Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.
  *  **Write Only (‘w’):** Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
  *  **Write and Read (‘w+’):** Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
  *  **Append Only (‘a’):** Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
  *  **Append and Read (‘a+’):** Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

 **Syntax:**

  

  

    
    
    File_object = open(r"File_Name", "Access_Mode")
    

**Note:** The file should exist in the same directory as the Python script,
otherwise full address of the file should be written.

 **Example #1:** Suppose the text file looked like this

![open-file-python](https://media.geeksforgeeks.org/wp-
content/uploads/20191203192405/open-file-python.png)

We want to read the content of the file using Python.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# opening a file

 

 

# Open function to open the file "myfile.txt" 

# (same directory) in read mode and store

# it's reference in the variable file1

 

file1 = open("myfile.txt")

 

# Reading from file

print(file1.read())

 

file1.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    Welcome to GeeksForGeeks!!
    

**Example #2:** Suppose we want to write more data to the above file using
Python.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# opening a file

 

 

# Open function to open the file "myfile.txt"

# (same directory) in append mode and store

# it's reference in the variable file1

file1 = open("myfile.txt", "a")

 

# Writing to file

file1.write("\nWriting to file :)")

 

# Closing file

file1.close()  
  
---  
  
 __

 __

 **Output:**

![python-open-file](https://media.geeksforgeeks.org/wp-
content/uploads/20191203193237/python-open-file.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

