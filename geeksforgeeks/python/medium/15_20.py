Python | Execute and parse Linux commands



 **Prerequisite:** Introduction to Linux Shell and Shell Scripting  

 **Linux** is one of the most popular operating systems and is a common choice
for developers. It is popular because it is open source, it’s free and
customizable, it is very robust and adaptable.

An operating system mainly consists of two parts: The kernel and the Shell.
The kernel basically handles communication between the software and the
hardware. The shell takes inputs or commands from the user and produces an
output. Most Linux distributions nowadays use the BASH shell (Bourne again
shell). Shell commands and scripts are very powerful and are used commonly by
developers.

In this article, we shall look at executing and parsing Linux commands using
python.

### Subprocess –

Subprocess is a module in Python that allows us to start new applications or
processes in Python. This module intends to replace several older modules in
python. We can use this module to run other programs or execute Linux
commands.

  

  

### Starting a process –

A new process can be spawned by using the Popen function defined in the
subprocess module. It is a constructor for the Popen class that takes
arguments to set up the new process. The underlying process creation and
management in this module is handled by the Popen class.

 **Arguments:**

>   1. The first parameter is a list that contains the commands and their
> options if any.  
> ex: ['ls', '-l']  
> the above example is equivalent to typing ‘ls -l’ in the terminal
>

* The second parameter is the stdout value. it specifies the standard output.  
ex: stdout = subprocess.PIPE  
This indicates that a new pipe or redirection should be created. The default
value is  
“None”, which means that no redirection will occur.

