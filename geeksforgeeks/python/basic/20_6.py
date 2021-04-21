How to clear screen in python?



Most of the time, while working with python interactive shell/terminal (not a
console), we end up with a messy output and want to clear the screen for some
reason.  
In an interactive shell/terminal, we can simply use

    
    
    ctrl+l

But, what if we want to clear the screen while running a python script.  
Unfortunately, there’s no built-in keyword or function/method to clear the
screen. So, we do it on our own.

We can use ANSI escape sequence but these are not portable and might not
produce desired output.

    
    
    print(chr(27)+'[2j')  
    print('\033c')  
    print('\x1bc')

So, here’s what we’re going to do in our script:

>   1. From os import system.
>   2. Define a function.
>   3. Make a system call with ‘clear’ in Linux and ‘cls’ in Windows as an
> argument.
>   4. Store the returned value in an underscore or whatever variable you want
> (an underscore is used because python shell always stores its last output in
> an underscore).
>   5. Call the function we defined.
>

 __

 __  
 __

 __

 __  
 __  
 __

# import only system from os

from os import system, name

 

# import sleep to show output for some time period

from time import sleep

 

# define our clear function

def clear():

 

 # for windows

 if name == 'nt':

 _ = system('cls')

 

 # for mac and linux(here, os.name is 'posix')

 else:

 _ = system('clear')

 

# print out some text

print('hello geeks\n'*10)

 

# sleep for 2 seconds after printing output

sleep(2)

 

# now call function we defined above

clear()  
  
---  
  
 __

 __

NOTE: You can also only “import os” instead of “from os import system” but
with that, you have to change system(‘clear’) to os.system(‘clear’).

  

  

Another way to accomplish this is using subprocess module.

 __

 __  
 __

 __

 __  
 __  
 __

# import call method from subprocess module

from subprocess import call

 

# import sleep to show output for some time period

from time import sleep

 

# define clear function

def clear():

 # check and make call for specific operating system

 _ = call('clear' if os.name =='posix' else 'cls')

 

print('hello geeks\n'*10)

 

# sleep for 2 seconds after printing output

sleep(2)

 

# now call function we defined above

clear()  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

