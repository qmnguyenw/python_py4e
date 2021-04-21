Python | Generator Expressions



In **Python** , to create iterators, we can use both regular functions and
generators. **Generators** are written just like a normal function but we use
yield() instead of return() for returning a result. It is more powerful as
a tool to implement iterators. It is easy and more convenient to implement
because it offers the evaluation of elements on demand. Unlike regular
functions which on encountering a return statement terminates entirely,
generators use yield statement in which the state of the function is saved
from the last call and can be picked up or resumed the next time we call a
generator function. Another great advantage of the generator over a list is
that it takes much less memory.  
In addition to that, two more functions _next_() and _iter_() make the
generator function more compact and reliable. Example :

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate generator, yield() and next().

def generator(): 

 t = 1

 print ('First result is ',t) 

 yield t 

 

 t += 1

 print ('Second result is ',t) 

 yield t 

 

 t += 1

 print('Third result is ',t) 

 yield t 

 

call = generator() 

next(call) 

next(call) 

next(call)   
  
---  
  
__

__

Output :

    
    
    First result is  1
    Second result is  2
    Third result is  3
    

**Difference between Generator function and Normal function –**

  * Once the function yields, the function is paused and the control is transferred to the caller.
  * When the function terminates, StopIteration is raised automatically on further calls.
  * Local variables and their states are remembered between successive calls.
  * Generator function contains one or more yield statement instead of return statement.
  * As the methods like _next_() and _iter_() are implemented automatically, we can iterate through the items using next().

There are various other expressions that can be simply coded similar to list
comprehensions but instead of brackets we use parenthesis. These expressions
are designed for situations where the generator is used right away by an
enclosing function. Generator expression allows creating a generator without a
yield keyword. However, it doesn’t share the whole power of generator created
with a yield function. Example :

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate generator expression

generator = (num ** 2 for num in range(10)) 

for num in generator:

 print(num)  
  
---  
  
 __

 __

Output :

  

  

    
    
    0
    1
    4
    9
    16
    25
    36
    49
    64
    81
    

We can also generate a list using generator expressions :

 __

 __  
 __

 __

 __  
 __  
 __

string= 'geek'

li = list(string[i] for i in range(len(string)-1,
-1, -1))

print(li)  
  
---  
  
 __

 __

Output:

    
    
    ['k', 'e', 'e', 'g']
    

This article is contributed by **Chinmoy Lenka**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
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

