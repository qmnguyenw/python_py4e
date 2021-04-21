Python – sys.settrace()



Python sys module provides some of the powerful functions but they are
complex to understand. One of which is the sys.settrace() which is used for
implementing debuggers, profilers and coverage tools. This is thread-specific
and must register the trace using threading.settrace().

Knowing how the function works internally is really important in case you are
planning to create your own debugger.

On a higher level, sys.settrace() registers the traceback to the Python
interpreter. A traceback is basically the information that is returned when an
event happens in the code. You might have seen traceback when your code has
some error or an exception is raised.

The registered traceback is invoked when one of the following four events
occur :

  1. Function is called
  2. Function returns
  3. Execution of a line
  4. Exception is raised

>  **Syntax:** sys.settrace(frame, event, arg.frame)
>
>  
>
>
>  
>
>
>  **Parameters:**  
>  **frame:** frame is the current stack frame  
>  **event:** A string which be either 'call', 'line', 'return', 'exception'
> or 'opcode'  
>  **arg:** Depends on the event type
>
>  **Returns:** Reference to the local trace function which then returns
> reference to itself.

 **Example:**

Let’s create our own local trace function with line, function and call
events. These events are highlighted in the below given code.

 __

 __  
 __

 __

 __  
 __  
 __

# program to display the functioning of

# settrace()

from sys import settrace

 

 

# local trace function which returns itself

def my_tracer(frame, event, arg = None):

 # extracts frame code

 code = frame.f_code

 

 # extracts calling function name

 func_name = code.co_name

 

 # extracts the line number

 line_no = frame.f_lineno

 

 print(f"A {event} encountered in \

 {func_name}() at line number {line_no} ")

 

 return my_tracer

 

 

# global trace function is invoked here and

# local trace function is set for fun()

def fun():

 return "GFG"

 

 

# global trace function is invoked here and

# local trace function is set for check()

def check():

 return fun()

 

 

# returns reference to local

# trace function (my_tracer)

settrace(my_tracer)

 

check()  
  
---  
  
 __

 __

 **Output:**

    
    
    A call encountered in check() at line number 30 
    A line encountered in check() at line number 31 
    A call encountered in fun() at line number 24 
    A line encountered in fun() at line number 25 
    A return encountered in fun() at line number 25 
    A return encountered in check() at line number 31 
    

You might be wondering why does the local function my_code returns itself?  
The reason is hidden in the functioning of sys.settrace(). What
sys.settrace does is that it first registers a global trace which is called
whenever a frame is created which returns our local trace function my_trace
whenever any one of the above mentioned event occurs. For better understanding
look at the image shown below:

![Working-of-settrace-python](https://media.geeksforgeeks.org/wp-
content/uploads/20200402234220/functionality11.png)

If we don’t want our scope to be traced then None should be returned but if
that is not the case we might want to do the same with our local trace
function then it should return None else if there is an error then
settrace(None) is automatically called.

 **Note :** There is a function named gettrace available in sys module to
get the trace set by sys.settrace()

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

