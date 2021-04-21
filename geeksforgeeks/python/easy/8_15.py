Python – Reading last N lines of a file



 **Prerequisite:** Read a file line-by-line in Python

Given a text file _fname_ , a number _N_ , the task is to read the last N
lines of the file.

As we know, Python provides multiple in-built features and modules for
handling files. Let’s discuss different ways to read last N lines of a file
using Python.

 ** _File:_**  
![Image of content of a file](https://media.geeksforgeeks.org/wp-
content/uploads/20200312012317/Screenshot-4691.png)

 **Method 1: Naive approach**  
In this approach, the idea is to use a negative iterator with the
readlines() function to read all the lines requested by the user from the
end of file.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation to

# read last N lines of a file

 

# Function to read

# last N lines of the file 

def LastNlines(fname, N):

 # opening file using with() method

 # so that file get closed

 # after completing work

 with open(fname) as file:

 

 # loop to read iterate 

 # last n lines and print it

 for line in (file.readlines() [-N:]):

 print(line, end ='')

 

 

# Driver Code: 

if __name__ == '__main__':

 fname = 'File1.txt'

 N = 3

 try:

 LastNlines(fname, N)

 except:

 print('File not found'  
  
---  
  
 __

 __

 **Output:**

    
    
    Eighth line
    Ninth line
    Tenth line
    

**Method 2: Using OS module and buffering policy**  
In this approach, the idea is to work on the buffering policy in the python. A
buffer stores a part of data received from a file stream of the operating
system for a time period it is used and then more data comes in.

The buffer size determines the size of the data that can be stored at a time
until it is used. We have the option to pass an integer to buffering in order
to set buffering policy and if we do not specify any policy then the size of
the buffer depends upon the device’s block size. Usually, the buffer is 4096
or 8192 bytes long. In this approach size of the buffer is 8192 bytes.

Moreover, the **st_size** attribute of os.stat() method in the OS module is
used to represent the size of the file in bytes.

Below is the implementation of the above approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation to

# read last N lines of a file

# Using OS module and buffering policy

 

# importing os module

import os

 

# Function to read

# last N lines of the file

def LastNlines(fname, N):

 # taking buffer size of 8192 bytes

 bufsize = 8192

 

 # calculating size of

 # file in bytes

 fsize = os.stat(fname).st_size

 

 iter = 0

 

 # opening file using with() method

 # so that file get closed

 # after completing work

 with open(fname) as f:

 if bufsize > fsize:

 

 # adjusting buffer size

 # according to size

 # of file

 bufsize = fsize-1

 

 # list to store 

 # last N lines

 fetched_lines = []

 

 # while loop to

 # fetch last N lines

 while True:

 iter += 1

 

 # moving cursor to

 # the last Nth line

 # of file

 f.seek(fsize-bufsize * iter)

 

 # storing each line

 # in list upto

 # end of file

 fetched_lines.extend(f.readlines())

 

 # halting the program

 # when size of list

 # is equal or greater to

 # the number of lines requested or

 # when we reach end of file

 if len(fetched_lines) >= N or f.tell() == 0:

 print(''.join(fetched_lines[-N:]))

 break

 

# Driver Code: 

if __name__ == '__main__':

 

 fname = 'File1.txt'

 N = 3

 

 try:

 LastNlines(fname, N)

 except:

 print('File not found')  
  
---  
  
 __

 __

 **Output:**

    
    
    Eighth line
    Ninth line
    Tenth line
    

  
**Method 3: Through Exponential search**

  

  

In this method, the idea is to use Exponential Search algorithm which is
generally used for searching sorted, unbounded or infinite lists. To get
information about exponential search click here.

This approach uses assert statement which acts as a debugging tool to checks a
condition. The program will continue to execute if the given statement is true
otherwise, it generates an **AssertionError exception**. To get more details
of assert statements click here.

Click here to get familiar with different kinds of use of seek() method.

Below is the implementation of the above approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python implementation to

# read last N lines of a file

# through Exponential search

 

# Function to read

# last N lines of the file

def LastNlines(fname, N):

 

 # assert statement check

 # a condition

 assert N >= 0

 

 # declaring variable

 # to implement 

 # exponential search

 pos = N + 1

 

 # list to store

 # last N lines

 lines = []

 

 # opening file using with() method

 # so that file get closed

 # after completing work

 with open(fname) as f:

 

 # loop which runs

 # until size of list

 # becomes equal to N

 while len(lines) <= N:

 

 # try block

 try:

 # moving cursor from

 # left side to

 # pos line from end

 f.seek(-pos, 2)

 

 # exception block 

 # to hadle any run 

 # time error

 except IOError:

 f.seek(0)

 break

 

 # finally block 

 # to add lines 

 # to list after

 # each iteration

 finally:

 lines = list(f)

 

 # increasing value

 # of variable

 # exponentially

 pos *= 2

 

 # returning the

 # whole list

 # which stores last

 # N lines

 return lines[-N:]

 

# Driver Code: 

if __name__ == '__main__':

 fname = 'File1.txt'

 N = 3

 try:

 lines = LastNlines(fname, N)

 for line in lines:

 print (line, end ='')

 except:

 print('File not found')  
  
---  
  
 __

 __

 **Output:**

    
    
    Eighth line
    Ninth line
    Tenth line
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

