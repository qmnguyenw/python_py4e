Powerful One-Liner Python codes



Python is a widely-used general-purpose, high-level programming language.
Python programs generally are smaller than other programming languages like
Java. Programmers have to type relatively less and indentation requirements of
the language makes them readable all the time. However, Python programs can be
made more concise using some one-liner codes. These can save time by having
less code to type.

> Refer to the below articles to know more about Python.
>
>   * Python basics
>

## One-Liners in Python

 **One-Liner #1:** To input space separated integers in a list:

Suppose you want to take space separated input from the console and you want
to convert it into List. To do this map() function can be used that takes
int() method and input().split() methods as parameter. Here the int()
method is used for conversion of input to int type and input().split()
methods are used to take input from the console and split the input by spaces.
Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

lis= list(map(int, input().split()))  
  
---  
  
 __

 __

 **Note:** To know more about Python map() function click here.

  

  

 **One-Liner #2:** To input a 2-D matrix(When the entries are given row-wise):

The most naive method that comes in mind while taking a input for 2-D matrix
is given below.

 __

 __  
 __

 __

 __  
 __  
 __

# Input for row and column

R = int(input()) 

C = int(input()) 

 

matrix = [] 

 

# for loop for row entries 

for i in range(R): 

 a =[] 

 

 # for loop for column entries 

 for j in range(C):

 a.append(int(input())) 

 matrix.append(a)   
  
---  
  
__

__

The above code can be written in one-line that is way more concise and saves
time especially for competitive programmers.

 __

 __  
 __

 __

 __  
 __  
 __

# Input for row and column

R = int(input())

C = int(input())

 

# Using list comprehension for input

matrix = [[int(input()) for x in range (C)] for y
in range(R)]   
  
---  
  
__

__

**One-Liner #3:** We know this fact, but sometimes we tend to ignore it while
translating from other languages. It is swapping of two numbers. The most
naive way of doing this is:

 __

 __  
 __

 __

 __  
 __  
 __

temp= a

a = b

b = temp  
  
---  
  
 __

 __

However, Python provides one-liner for this also. The Pythonic way is:

 __

 __  
 __

 __

 __  
 __  
 __

# to swap two numbers a and b

a, b = b, a  
  
---  
  
 __

 __

 **One-Liner #4** **Lambda Functions(Anonymous Functions)** – Lambda functions
are python one liner functions and are often used when an expression is to be
evaluated.

For example, let’s suppose we want to create a function that returns the
square of the number passed as argument. The normal way of doing this is:

 __

 __  
 __

 __

 __  
 __  
 __

def sqr(x):

 return x * x

 

print(sqr(5))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    25
    

Lambda function replaces a function wherever a single expression is to be
evaluated.

 __

 __  
 __

 __

 __  
 __  
 __

sqr= lambda x: x * x

print(sqr(5))  
  
---  
  
 __

 __

 **Output:**

    
    
    25
    

**One-Liner #5** **List comprehensions** – This is a concise way to create
lists. Instead of doing it the usual way, we can make use of list
comprehensions.

For example, we want to create a list of even numbers till 11. The normal way
of doing this is:

 __

 __  
 __

 __

 __  
 __  
 __

evenNumbers=[]

for x in range(11):

 if x % 2 == 0:

 evenNumbers.append(x)

 

print(evenNumbers)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 2, 4, 6, 8, 10]
    

The pythonic way:

 __

 __  
 __

 __

 __  
 __  
 __

evenNumbers=[x for x in range(11) if x % 2 ==
0]

print(evenNumbers)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 2, 4, 6, 8, 10]
    

**One-Liner #6:** This trick may help while using if-else or while loop.
Instead of doing this –

 __

 __  
 __

 __

 __  
 __  
 __

if m == 1 or m == 2 or m == 3:

 pass  
  
---  
  
 __

 __

We can code it as:

 __

 __  
 __

 __

 __  
 __  
 __

if m in [1, 2, 3]:

 pass  
  
---  
  
 __

 __

 **One-Liner #7:** There are various ways to reverse a list in python.  
Pythonic ways to reverse a list:

  *  **Using the slicing technique-** This technique creates the copy of the list while reversing. It takes up more memory.

 __

 __  
 __

 __

 __  
 __  
 __

lis= [1, 2, 3]

reversed_list = lis[::-1]

 

print(reversed_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 2, 1]
    

  * Using the reverse function- It reverse the contents of the list object in-place.

 __

 __  
 __

 __

 __  
 __  
 __

lis= [1, 2, 3]

lis.reverse()

 

print(lis)  
  
---  
  
 __

 __

 **Output:**

    
    
    [3, 2, 1]
    

**One-Liner #8:** You can take this as a challenge. Making one-liner python
patterns.

For example, Make the following code concise to one line.

 __

 __  
 __

 __

 __  
 __  
 __

for i in range(0, 5): 

 

 for j in range(0, i + 1): 

 # printing stars 

 print("* ", end ="") 

 

 # ending line after each row 

 print("\r")  
  
---  
  
 __

 __

 **Output:**

    
    
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    

Concise all this in one line is fun.

 __

 __  
 __

 __

 __  
 __  
 __

n= 5

 

# one liner code for half pyramid pattern

print('\n'.join('* ' * i for i in range(1, n +
1)))  
  
---  
  
 __

 __

 **Output:**

    
    
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
    

**One-Liner #9** Finding the factorial. The normal way of finding a factorial
is iterating till that number and multiplying the number in each iteration.

 __

 __  
 __

 __

 __  
 __  
 __

n= 5

fact = 1

 

for i in range(1, n + 1): 

 fact = fact * i 

print (fact)   
  
---  
  
__

__

**Output:**

    
    
    120
    

We can use math.factorial(x)– It returns the factorial of x. But it raises
Value error if number is negative or non-integral.

 __

 __  
 __

 __

 __  
 __  
 __

import math

 

 

n = 5

print(math.factorial(n))  
  
---  
  
 __

 __

 **Output:**

    
    
    120
    

One more way to do find the factorial concisely is by using reduce() and
lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

import functools

 

 

n = 5

print(functools.reduce(lambda x, y: x * y, range(1, n
+ 1)))  
  
---  
  
 __

 __

 **Output:**

    
    
    120
    

**One-Liner #10:** Finding all subsets of a set in one line.  
Usual way takes a lot of hard work and can be seen here. It can be be done in
a much simpler way using itertools.combinations()

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import combinations

 

 

# list of all subsets of 

# length r (r = 2 in this example) 

print(list(combinations([1, 2, 3, 4], 2)))  
  
---  
  
 __

 __

 **Output:**

    
    
    [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    

**One-Liner #11:** Read file in python and input it to a list.

 __

 __  
 __

 __

 __  
 __  
 __

file = open('gfg.txt', 'r') 

lis =[]

 

for each in file:

 

 # removing '\n' from the end of the string

 a = each[:-1] 

 lis.append(a)

 

file.close()  
  
---  
  
 __

 __

One liner code is:

 __

 __  
 __

 __

 __  
 __  
 __

lis= [line.strip() for line in open('gfg.txt', 'r')]  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

