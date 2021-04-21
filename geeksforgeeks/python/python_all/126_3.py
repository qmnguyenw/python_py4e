Python | Scope resolution when a function is called or defined



Python resolves the scope of the parameters of a function in two ways:

  * When the function is defined
  * When the function is called

 **When the function is defined**  
Consider this sample program which has a function adder(a, b) which adds an
element a to the list b and returns the list b. The default value of b is [1,
8, 11].  
 **  
Code :**

 __

 __  
 __

 __

 __  
 __  
 __

def adder(a, b = [1, 8, 11]):

 b.append(a)

 return b

 

print(adder(1))

print(adder(2))

print(adder(9))

print(adder(2, [3, 6]))  
  
---  
  
 __

 __

    
    
    **Expected Output :** 
    
    [1, 8, 11, 1]
    [1, 8, 11, 2]
    [1, 8, 11, 9]
    [3, 6, 2]
    
    
    
    **Actual Output :** 
    
    [1, 8, 11, 1]
    [1, 8, 11, 1, 2]
    [1, 8, 11, 1, 2, 9]
    [3, 6, 2]
    

Observe that even though we don’t pass a parameter in the 2nd and 3rd call,
the default value of b no longer remains [1, 8, 11]. It is because of the fact
that **Python resolves the reference to name of a default parameter in the
scope of a function only once, when it is defined and not every time it is
called.** Even if a and b were to be any other mutable type like _dict and
set_ , the program would have worked in the same way.  
What do we do if we want the default value of b to always be [1, 8, 11] ?
Inside the function, we can check if b was passed while calling the function
or not. If it was not, then we reassign the value of b to [1, 8, 11].  
  
**When the function is called**  
Now, consider this program which **tries** to store lambda function objects
(to calculate the square of numbers between 0 and 4) inside a list and call
them one by one.  
 **Code :**

 __

 __  
 __

 __

 __  
 __  
 __

l= []

for i in range(5):

 l.append(lambda : i**2)

for j in range(5):

 print(l[j]())  
  
---  
  
 __

 __

    
    
    **Expected Output :** 
    
    0
    1
    4
    9
    16
    
    
    
    **Actual Output :** 
    
    16
    16
    16
    16
    16
    

However, the result is not what was expected from the program. It is because
**_Python resolves the reference to names of non-default parameters in the
scope of a function when it is called and not when it is defined._** Here the
parameter is _i_. When the loop terminates, the value of _i_ is 4 and when we
call any of the lambda functions stored in l, 4**2 = 16 is returned.  
What do we do to make the program work the way we expected? Just make _i_ a
default parameter for the lambda function and let python’s scope resolution
behaviour do that for you.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

