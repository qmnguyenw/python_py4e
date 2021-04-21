Python | Compiled or Interpreted ?



In various books of python programming, it is mentioned that python language
is interpreted. But that is half correct the python program is first compiled
and then interpreted. The compilation part is hidden from the programmer thus,
many programmers believe that it is an interpreted language. The compilation
part is done first when we execute our code and this will generate byte code
and internally this byte code gets converted by the python virtual
machine(p.v.m) according to the underlying platform(machine+operating system).  
Now the question is – if there is any proof that python first compiles the
program internally and then run the code via interpreter?  
The answer is yes! and note this compiled part is get deleted by the python(as
soon as you execute your code) just it does not want programmers to get into
complexity.

 **Code : Sample Python code**

 __

 __  
 __

 __

 __  
 __  
 __

print("i am learning python")

print("i am enjoying it")  
  
---  
  
 __

 __

now if you run this code using command prompt just save this above code in
notepad and save with the extension “.py”  
 **syntax:** python (name of the program.py) and press enter.  
 **Note:** If you are writing code in the notepad just save the code with
extension “py” inlet suppose you have created a folder named python_prog in d
drive.

![](https://media.geeksforgeeks.org/wp-content/uploads/20190620133534/u2.png)

as you press enter the byte code will get generated. A folder created and this
will contain the byte code of your program. This folder is in the python_prog
folder where you will save your python codes.  
![](https://media.geeksforgeeks.org/wp-content/uploads/20190620134350/u31.png)

  

  

now to run the compiled byte code just type the following command in the
command prompt:-  
![](https://media.geeksforgeeks.org/wp-content/uploads/20190620134637/u13.png)  
the extension .pyc is python compiler..

Thus, it is proven that python programs are both compiled as well as
interpreted!! but the compilation part is hidden from the programmer.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

