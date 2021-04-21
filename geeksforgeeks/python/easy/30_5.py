Python Input Methods for Competitive Programming



Python is an amazingly user-friendly language with the only flaw of being
slow. In comparison to C, C++, and Java, it is quite slower. Online coding
platforms, if C/C++ limit provided is **X**. Usually, in Java time provided is
**2X** and Python, it’s **5X**.  
To improve the speed of code execution for input/output intensive problems,
languages have various input and output procedures.  

**An Example Problem :**  
Consider a question of finding the sum of **N** numbers inputted from the
user.  
Input a number **N**.  
Input **N** numbers separated by a single space in a line.  

**Examples:**

    
    
    Input : 
    5
    1 2 3 4 5
    Output :
    15
    
    
    
    
    

**Different Python solutions for the above Problem :**

**Normal Method Python: (Python 2.7)**  
1\. **raw_input()** takes an optional prompt argument. It also strips the
trailing newline character from the string it returns.  
2\. **print** is just a thin wrapper that formats the inputs (space between
args and newline at the end) and calls the write function of a given object.  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# basic method of input output

# input N

n = int(raw_input())

# input the array

arr = [int(x) for x in raw_input().split()]

# initialize variable

summation = 0

# calculate sum

for x in arr:

 summation += x

 

# print answer

print(summation)  
  
---  
  
 __

 __

 **A bit faster method using inbuilt stdin, stdout: (Python 2.7)**  
1\. **sys.stdin** on the other hand is a **File Object**. It is like creating
any other file object one could create to read input from the file. In this
case, the file will be standard input buffer.  
2\. **stdout.write(‘D\n’)** is faster than **print ‘D’**.  
3\. Even faster is to write all once by **stdout.write(“”.join(list-
comprehension))** but this makes memory usage dependent on size of input.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# import inbuilt standard input output

from sys import stdin, stdout

# suppose a function called main() and

# all the operations are performed

def main():

 # input via readline method

 n = stdin.readline()

 # array input similar method

 arr = [int(x) for x in stdin.readline().split()]

 #initialize variable

 summation = 0

 

 # calculate sum

 for x in arr:

 summation += x

 # could use inbuilt summation = sum(arr)

 # print answer via write

 # write method writes only

 # string operations

 # so we need to convert any

 # data into string for input

 stdout.write(str(summation))

# call the main method

if __name__ == "__main__":

 main()   
  
---  
  
__

__

**Difference in time:**  

> Timing summary (100k lines each)  
> ——————————–  
> Print : 6.040 s  
> Write to file : 0.122 s  
> Print with Stdout : 0.121 s  
>

As we have seen till now that taking input from the standard system and giving
output to the standard system is always a good idea to improve the efficiency
of the code which is always a need in Competitive programming. But wait! would
you like to write these long lines every time when you need them? Then, what’s
the benefit of using Python.  
Let’s discuss the solution to this problem. What we can do is let’s create
separate functions for taking inputs of various types and just call them
whenever you need them.  

### When you want to take input of particular integers of integers given in a
single line

Suppose the input is of the following form  

    
    
    5 7 19 20
    
    
    
    
    

and we want separate variables to reference them. what we want is:  

    
    
    a = 5
    b = 7
    c = 19
    d = 20
    
    
    
    
    

so, we can create a function named as **get_ints()** as follows:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sys

def get_ints(): return map(int,
sys.stdin.readline().strip().split())

a,b,c,d = get_ints()  
  
---  
  
 __

 __

Now you don’t have to write this line again and again. You just have to call
the **get_ints()** function in order to take input in this form. In the
function _get_ints_ we are using the _map_ function.

  

  

### When you want to take input of list of integers given in a single line

Suppose the input is of the following form  

    
    
    1 2 3 4 5 6 7 8
    
    
    
    
    

and we want that a single variable will hold the whole list of integers. What
we want is :  

    
    
    Arr = [1, 2, 3, 4, 5, 6, 7, 8]
    
    
    
    
    

So, here we will create a function named as **get_list()** as follows:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sys

def get_ints(): return list(map(int,
sys.stdin.readline().strip().split()))

Arr = get_ints()  
  
---  
  
 __

 __

Now you don’t have to write this line again and again. You just have to call
the **get_ints()** function in order to take input in this form  

### When you want to take input of string

Suppose the input is of the following form  

    
    
    GeeksforGeeks is the best platform to practice Coding.
    
    
    
    
    

and we want that a single reference variable will hold this string. What we
want is :  

    
    
    string = "GeeksforGeeks if the best platform to practice coding."
    
    
    
    
    

So, here we will create a function named as **get_string()** as follows:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import sys

def get_string(): return sys.stdin.readline().strip()

string = get_string()  
  
---  
  
 __

 __

Now you don’t have to write this line again and again. You just have to call
the **get_string()** function in order to take input in this form  
 **Adding a buffered pipe io: (Python 2.7)**  
1\. Simply, **adding the buffered IO** code before your submission code to
make the output faster.  
2\. The benefit of **io.BytesIO** objects is that they implement a common
interface (commonly known as a ‘file-like’ object). **BytesIO** objects have
an internal pointer and for every call to read(n) the pointer advances.  
3\. The **atexit** module provides a simple interface to register functions to
be called when a program closes down normally. The **sys** module also
provides a hook, sys.exitfunc, but only one function can be registered there.
The **atexit registry** can be used by multiple modules and libraries
simultaneously.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# template begins

#####################################

# import libraries for input/ output handling

# on generic level

import atexit, io, sys

# A stream implementation using an in-memory bytes

# buffer. It inherits BufferedIOBase.

buffer = io.BytesIO()

sys.stdout = buffer

# print via here

@atexit.register

def write():

 sys.__stdout__.write(buffer.getvalue())

#####################################

# template ends

# normal method followed

# input N

n = int(raw_input())

# input the array

arr = [int(x) for x in raw_input().split()]

# initialize variable

summation = 0

# calculate sum

for x in arr:

 summation += x

# print answer

print(summation)  
  
---  
  
 __

 __

While handling a large amount of data usually, the normal method fails to
execute within the time limit. Method 2 helps in maintaining a large amount of
I/O data. Method 3 is the fastest. Usually, handling of input data files
greater than 2 or 3 MBs is helped via method 2 and 3.  
 **Note :** above mention codes are in Python 2.7, to use in Python 3.X
versions. Simply replace the **raw_input()** with Python 3.X’s input() syntax.
Rest should work fine.  
 **References:**  
1.More About Input in Python 2.7  
2.Output via sys library and other commands.  
3.Input via sys library and other commands.  
4\. Python atexit Module docs.  
This article is contributed by **Shubham Saxena**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

![competitive-programming-img](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200604102100/GFG-CP-Article-2.png)

My Personal Notes _arrow_drop_up_

Save

