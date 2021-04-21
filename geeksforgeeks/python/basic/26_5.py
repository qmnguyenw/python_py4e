Program to print its own name as output



Ever thought about writing a script which prints its own name when you execute
it. It’s pretty simple. You must have noticed programs in which the main
function is written like this

    
    
    int main(int argc, char** argv)

and you must have wondered what these 2 arguments mean.

  * Well the first one _argc_ is the number of arguments passed in to your program.
  * The second one _argv_ is the array which holds the names of all the arguments passed into your program.
  * Along with those arguments there is an extra piece of information stored in the array first cell of that array i.e. argv[0] which is the full path of the file containing the code.

To print the name of the program all we need to do is to slice the filename
out of that path.

 **Implementation**

Below is the python implementation of the idea discussed above. Let’s suppose
the name of the script is print_my_name.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to prints it own name upon execution

import sys

 

def main():

 program = sys.argv[0] # argv[0] contains the full path of the
file

 

 # rfind() finds the last index of backslash

 # since in a file path the filename comes after the last '\'

 index = program.rfind("\\") + 1

 

 # slicing the filename out of the file path

 program = program[index:]

 print("Program Name: % s" % program)

 

# executes main

if __name__ == "__main__":

 main()  
  
---  
  
 __

 __

    
    
     **Output:** print_my_name.py

 **Note:** The output will vary when you run it on GeeksforGeeks online
compiler.

This article is contributed by Palash Nigam . If you like GeeksforGeeks and
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

