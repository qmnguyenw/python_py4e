Python List Comprehensions vs Generator Expressions



 **What is List Comprehension?**  
It is an elegant way of defining and creating a list. List Comprehension
allows us to create a list using for loop with lesser code. What normally
takes 3-4 lines of code, can be compressed into just a single line.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# initializing the list

list = []

 

for i in range(11):

 if i % 2 == 0:

 list.append(i)

 

# print elements

print(list)  
  
---  
  
 __

 __

 **Output:**

    
    
     0 2 4 6 8 10

Now, the same output can be derived from just a single line of code.

 __

 __  
 __

 __

 __  
 __  
 __

list = [i for i in range(11) if i % 2 ==
0]

print(list)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
     0 2 4 6 8 10

 **What are Generator Expressions?**  
Generator Expressions are somewhat similar to list comprehensions, but the
former doesn’t construct list object. Instead of creating a list and keeping
the whole sequence in the memory, the generator generates the next element in
demand.  
When a normal function with a return statement is called, it terminates
whenever it gets a return statement. But a function with a yield statement
saves the state of the function and can be picked up from the same state, next
time the function is called.  
The Generator Expression allows us to create a generator without the yield
keyword.

 **Syntax Difference:** Parenthesis are used in place of square brackets.

 __

 __  
 __

 __

 __  
 __  
 __

# List Comprehension

list_comprehension = [i for i in range(11) if i %
2 == 0]

 

print(list_comprehension)  
  
---  
  
 __

 __

 **Output:**

    
    
     0 2 4 6 8 10

 __

 __  
 __

 __

 __  
 __  
 __

# Generator Expression

generator_expression = (i for i in range(11) if i %
2 == 0)

 

print(generator_expression)  
  
---  
  
 __

 __

 **Output:**

    
    
    <generator object  at 0x000001452B1EEC50>
    

In the above example, if we want to print the output for generator
expressions, we can simply iterate it over generator object.

 __

 __  
 __

 __

 __  
 __  
 __

for i in generator_expression:

 print(i, end=" ")  
  
---  
  
 __

 __

 **Output:**

    
    
    0 2 4 6 8 10

 **So what’s the difference between Generator Expressions and List
Comprehensions?**  
The generator yields one item at a time and generates item only when in
demand. Whereas, in a list comprehension, Python reserves memory for the whole
list. Thus we can say that the generator expressions are memory efficient than
the lists.  
We can see this in the example below.

 __

 __  
 __

 __

 __  
 __  
 __

# import getsizeof from sys module

from sys import getsizeof

 

comp = [i for i in range(10000)]

gen = (i for i in range(10000))

 

#gives size for list comprehension

x = getsizeof(comp) 

print("x = ", x)

 

#gives size for generator expression

y = getsizeof(gen) 

print("y = ", y)  
  
---  
  
 __

 __

 **Output:**

    
    
    x =  87624
    y =  88
    

We just saw that generator expression are memory efficient. But, are they time
efficient too? Let’s check this with an example.

 __

 __  
 __

 __

 __  
 __  
 __

#List Comprehension:

import timeit

 

print(timeit.timeit('''list_com = [i for i in range(100) if i % 2 ==
0]''', number=1000000))  
  
---  
  
 __

 __

 **Output:**

    
    
    8.118047142050102

 __

 __  
 __

 __

 __  
 __  
 __

#Generator Expression:

import timeit

 

print(timeit.timeit('''gen_exp = (i for i in range(100) if i % 2 ==
0)''', number=1000000))  
  
---  
  
 __

 __

 **Output:**

    
    
    0.7548244756850693

There is a remarkable difference in the execution time. Thus, generator
expressions are faster than list comprehension and hence time efficient.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

