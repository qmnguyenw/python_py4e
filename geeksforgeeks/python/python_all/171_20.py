Python subprocess module to execute programs written in different languages



The subprocess module present in Python(both 2.x and 3.x) is used to run new
applications or programs through Python code by creating new processes. It
also helps to obtain the input/output/error pipes as well as the exit codes of
various commands.

To execute different programs using Python two functions of the subprocess
module are used:

>  **1.subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None,
> shell=False)**  
>  **Parameters:**  
>  args=The command to be executed.Several commands can be passed as a string
> by separated by “;”.  
> stdin=Value of standard input stream to be passed as (os.pipe()).  
> stdout=Value of output obtained from standard output stream.  
> stderr=Value of error obtained(if any) from standard error stream.  
> shell=Boolean parameter.If True the commands get executed through a new
> shell environment.  
>  **Return Value:**  
>  The function returns the return code of the command.If the retrun code is
> zero, the function simply returns(command executed successfully) otherwise
> CalledProcessError is being raised.
>
>  **2.subprocess.check_output(args, *, stdin=None, stderr=None, shell=False,
> universal_newlines=False)**  
>  **Parameters:**  
>  args=The command to be executed. Several commands can be passed as a string
> by separated by “;”.  
> stdin=Value of standard input stream to be passed as pipe(os.pipe()).  
> stdout=Value of output obtained from standard output stream.  
> stderr=Value of error obtained(if any) from standard error stream.  
> shell=boolean parameter.If True the commands get executed through a new
> shell environment.  
> universal_newlines=Boolean parameter.If true files containing stdout and
> stderr are opened in universal newline mode.  
>  **Return Value:**  
>  The function returns the return code of the command.If the retrun code is
> zero, the function simply returns the output as a byte string(command
> executed successfully) otherwise CalledProcessError is being raised.

Let us consider the following examples:

  

  

 **C program:**

 __

 __  
 __

 __

 __  
 __  
 __

#include<stdio.h>

int main()

{

 printf("Hello World from C");

 

 // returning with any other non zero value

 // would result in an exception

 // when called from python

 return 0;

}  
  
---  
  
 __

 __

 **C++ program:**

 __

 __  
 __

 __

 __  
 __  
 __

#include<iostream>

using namespace std;

int main()

{

 int a, b;

 cin >> a >> b;

 cout << "Hello World from C++.Values are:" << a << " " << b;

 return 0;

}  
  
---  
  
 __

 __

 **Java Program:**

 __

 __  
 __

 __

 __  
 __  
 __

class HelloWorld {

 public static void main(String args[])

 {

 System.out.print("Hello World from Java.");

 }

}  
  
---  
  
 __

 __

 **Python 3 code to execute the above programs:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to demonstrate subprocess

# module

 

import subprocess

import os

 

def excuteC():

 

 # store the return code of the c program(return 0)

 # and display the output

 s = subprocess.check_call("gcc HelloWorld.c -o out1;./out1", shell
= True)

 print(", return code", s)

 

def executeCpp():

 

 # create a pipe to a child process

 data, temp = os.pipe()

 

 # write to STDIN as a byte object(convert string

 # to bytes with encoding utf8)

 os.write(temp, bytes("5 10\n", "utf-8"));

 os.close(temp)

 

 # store output of the program as a byte string in s

 s = subprocess.check_output("g++ HelloWorld.cpp -o out2;./out2",
stdin = data, shell = True)

 

 # decode s to a normal string

 print(s.decode("utf-8"))

 

def executeJava():

 

 # store the output of

 # the java program

 s = subprocess.check_output("javac HelloWorld.java;java
HelloWorld", shell = True)

 print(s.decode("utf-8"))

 

 

# Driver function

if __name__=="__main__":

 excuteC() 

 executeCpp()

 executeJava()  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello World from C, return code 0
    Hello World from C++. Values are:5 10
    Hello World from Java.
    

**Note:** Although subprocess module is OS independent these commands must
only be executed in Linux environments. Also according to Python documentation
passing shell=True can be a security hazard if combined with untrusted input.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

