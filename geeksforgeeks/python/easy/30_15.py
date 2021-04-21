Command Line Interface Programming in Python



This article discusses how you can create a CLI for your python programs using
an example in which we make a basic “text file manager”.  
Let us discuss some basics first.

 **What is a Command Line Interface(CLI)?**

A command-line interface or command language interpreter (CLI), also known as
command-line user interface, console user interface, and character user
interface (CUI), is a means of interacting with a computer program where the
user (or client) issues commands to the program in the form of successive
lines of text (command lines).(Wiki)

 **Advantages of CLI:**

  * Requires fewer resources
  * Concise and powerful
  * Expert-friendly
  * Easier to automate via scripting

 **Why to use CLI in your python program?**

  

  

  * Having even just a very basic command-line interface (CLI) for your program can make everyone’s life easier for modifying parameters, including programmers, but also non-programmers.
  * A CLI for your program can also make it easier to automate running and modifying variables within your program, for when you want to run your program with a cronjob or maybe an os.system call.

Now, let us start making our “Text file manager”. Here, we will be using a
built-in python library called **Argparse**.

 **About Argparse:**

  * It makes it easy to write user-friendly command-line interfaces.
  * The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv.
  * The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

Ok let’s start with a really basic program to get a feel of what argparse
does.

 __

 __  
 __

 __

 __  
 __  
 __

# importing required modules

import argparse

 

# create a parser object

parser = argparse.ArgumentParser(description = "An addition
program")

 

# add argument

parser.add_argument("add", nargs = '*', metavar = "num",
type = int, 

 help = "All the numbers separated by spaces will be added.")

 

# parse the arguments from standard input

args = parser.parse_args()

 

# check if add argument has any input data.

# If it has, then print sum of the given numbers

if len(args.add) != 0:

 print(sum(args.add))  
  
---  
  
 __

 __

Let us go through some important points related to above program:

  * First of all, we imported the argparse module.
  * Then, created a **ArgumentParser** object and also provided a description of our program.
  * Now, we can fill up our parser object with information by adding arguments. In this example, we created an argument **add.** A lot of arguments can be passed to the **add_argument** function. Here I explain the ones I have used in above example:  
 **argument 1:** (“add”) It is nothing but the name of the argument. We will
use this name to access the **add** arguments by typing **args.add**.  
 **argument 2:** (nargs = ‘*’) The number of command-line arguments that
should be consumed. Specifying it to ‘*’ means it can be any no. of arguments
i.e, from 0 to anything.  
 **argument 3:** (metavar = ‘num’) A name for the argument in usage messages.  
 **argument 4:** (type = int) The type to which the command-line argument
should be converted. It is str by default.  
 **argument 5:** (help) A brief description of what the argument does.

  * Once we have specified all the arguments, it is the time to parse the arguments from the standard command line input stream. For this, we use parse_args() function.
  * Now, one can simply check if the input has invoked a specific argument. Here, we check the length of args.add to check if there is any data received from input. Note that values of an argument are obtained as a **list.**
  * There are two types of arguments: Positional and Optional.  
Positional ones are those which do not need any specification to be invoked.
Whereas, optional arguments need to be specified by their name first (which
starts with ‘–‘ sign, ‘-‘ is also a shorthand.)

  * One can always use –help or -h optional argument to see the help message.  
Here is an example (The python script has been saved as add.py):  
![2](https://indianpythonista.files.wordpress.com/2016/12/2.png)

  * Now, let us have a look at another example where our positional argument **add** is invoked.  
![3](https://indianpythonista.files.wordpress.com/2016/12/3.png)

  * One more special feature worth mentioning is how argparse issues errors when users give the program invalid arguments.  
![4](https://indianpythonista.files.wordpress.com/2016/12/4.png)

So, this was a basic example so that you can get comfortable with argparse and
CLI concept. Now, let us move on to our **“Text file manager”** program.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the required modules

import os

import argparse

 

# error messages

INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt
file."

INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not
exist."

 

 

def validate_file(file_name):

 '''

 validate file name and path.

 '''

 if not valid_path(file_name):

 print(INVALID_PATH_MSG%(file_name))

 quit()

 elif not valid_filetype(file_name):

 print(INVALID_FILETYPE_MSG%(file_name))

 quit()

 return

 

def valid_filetype(file_name):

 # validate file type

 return file_name.endswith('.txt')

 

def valid_path(path):

 # validate file path

 return os.path.exists(path)

 

 

 

def read(args):

 # get the file name/path

 file_name = args.read[0]

 

 # validate the file name/path

 validate_file(file_name)

 

 # read and print the file content

 with open(file_name, 'r') as f:

 print(f.read())

 

 

def show(args):

 # get path to directory

 dir_path = args.show[0]

 

 # validate path

 if not valid_path(dir_path):

 print("Error: No such directory found.")

 exit()

 

 # get text files in directory

 files = [f for f in os.listdir(dir_path) if
valid_filetype(f)]

 print("{} text files found.".format(len(files)))

 print('\n'.join(f for f in files))

 

 

def delete(args):

 # get the file name/path

 file_name = args.delete[0]

 

 # validate the file name/path

 validate_file(file_name)

 

 # delete the file

 os.remove(file_name)

 print("Successfully deleted {}.".format(file_name))

 

 

def copy(args):

 # file to be copied

 file1 = args.copy[0]

 # file to copy upon

 file2 = args.copy[1]

 

 # validate the file to be copied

 validate_file(file1)

 

 # validate the type of file 2

 if not valid_filetype(file2):

 print(INVALID_FILETYPE_MSG%(file2))

 exit()

 

 # copy file1 to file2

 with open(file1, 'r') as f1:

 with open(file2, 'w') as f2:

 f2.write(f1.read())

 print("Successfully copied {} to {}.".format(file1, file2))

 

 

def rename(args):

 # old file name

 old_filename = args.rename[0]

 # new file name

 new_filename = args.rename[1]

 

 # validate the file to be renamed

 validate_file(old_filename)

 

 # validate the type of new file name

 if not valid_filetype(new_filename):

 print(INVALID_FILETYPE_MSG%(new_filename))

 exit()

 

 # renaming

 os.rename(old_filename, new_filename)

 print("Successfully renamed {} to {}.".format(old_filename,
new_filename))

def main():

 # create parser object

 parser = argparse.ArgumentParser(description = "A text file
manager!")

 

 # defining arguments for parser object

 parser.add_argument("-r", "--read", type = str, nargs =
1,

 metavar = "file_name", default = None,

 help = "Opens and reads the specified text file.")

 

 parser.add_argument("-s", "--show", type = str, nargs =
1,

 metavar = "path", default = None,

 help = "Shows all the text files on specified directory path.\

 Type '.' for current directory.")

 

 parser.add_argument("-d", "--delete", type = str, nargs
= 1,

 metavar = "file_name", default = None,

 help = "Deletes the specified text file.")

 

 parser.add_argument("-c", "--copy", type = str, nargs =
2,

 metavar = ('file1','file2'), help = "Copy file1 contents
to \

 file2 Warning: file2 will get overwritten.")

 

 parser.add_argument("--rename", type = str, nargs = 2,

 metavar = ('old_name','new_name'),

 help = "Renames the specified file to a new name.")

 

 # parse the arguments from standard input

 args = parser.parse_args()

 

 # calling functions depending on type of argument

 if args.read != None:

 read(args)

 elif args.show != None:

 show(args)

 elif args.delete !=None:

 delete(args)

 elif args.copy != None:

 copy(args)

 elif args.rename != None:

 rename(args)

 

 

if __name__ == "__main__":

 # calling the main function

 main()  
  
---  
  
 __

 __

After the previous example, the above code seems self explanatory.  
All we did was to add a set of arguments for our file manager program. Note
that all these arguments are optional arguments. So, we use some if-elif
statements to match the command line input with correct argument type function
so that query could be processed.  
Here are a few screenshots which describe the usage of above program:

  * Help message (The python script has been saved as tfmanager.py):  
![5](https://indianpythonista.files.wordpress.com/2016/12/5.png)

  * Here are examples of operations using the text file manager:  
![9](https://indianpythonista.files.wordpress.com/2016/12/9.png)

So, this was an example of a simple CLI python program which we made. Many
complex CLIs could be easily created by the Argparse module. I hope that these
examples will give you a head start in this area.

This article is contributed by **Nikhil Kumar**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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

