Timeit in Python with Examples



This article will introduce you to a method of measuring the execution time of
your python code snippets.  
We will be using an in-built python library timeit.

This module provides a simple way to find the execution time of small bits of
Python code.

 **Why timeit?**

  * Well, how about using a simple time module? Just save the time before and after the execution of code and subtract them! But this method is not precise as there might be a background process momentarily running which disrupts the code execution and you will get significant variations in the running time of small code snippets.
  * timeit runs your snippet of code millions of times (default value is 1000000) so that you get the statistically most relevant measurement of code execution time!
  * timeit is pretty simple to use and has a command-line interface as well as a callable one.

So now, let’s start exploring this handy library!

The module function **timeit.timeit(stmt, setup, timer, number)** accepts four
arguments:

  

  

  *  **stmt** which is the statement you want to measure; it defaults to ‘pass’.
  *  **setup** which is the code that you run before running the **stmt** ; it defaults to ‘pass’.  
We generally use this to import the required modules for our code.

  *  **timer** which is a **timeit.Timer** object; it usually has a sensible default value so you don’t have to worry about it.
  *  **number** which is the number of executions you’d like to run the **stmt**.

Where the **timeit.timeit()** function returns the number of seconds it took
to execute the code.

 **Example 1**

Let us see a basic example first.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the required module

import timeit 

 

# code snippet to be executed only once 

mysetup = "from math import sqrt"

 

# code snippet whose execution time is to be measured 

mycode = ''' 

def example(): 

 mylist = [] 

 for x in range(100): 

 mylist.append(sqrt(x)) 

'''

 

# timeit statement 

print (timeit.timeit(setup = mysetup,

 stmt = mycode,

 number = 10000))   
  
---  
  
__

__

  * The output of above program will be the execution time(in seconds) for 10000 iterations of the code snippet passed to **timeit.timeit()** function.

 **Note:** _Pay attention to the fact that the output is the execution time of
**number** times iteration of the code snippet, not the single iteration. For
a single iteration exec. time, divide the output time by **number**._

  * The program is pretty straight-forward. All we need to do is to pass the code as a string to the **timeit.timeit()** function.
  * It is advisable to keep the import statements and other static pieces of code in setup argument.

 **Example 2**

Let’s see another practical example in which we will compare two searching
techniques, namely, **Binary search** and **Linear search**.  
Also, here I demonstrate two more features, **timeit.repeat** function and
calling the functions already defined in our program.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the required modules

import timeit

 

# binary search function

def binary_search(mylist, find):

 while len(mylist) > 0:

 mid = (len(mylist))//2

 if mylist[mid] == find:

 return True

 elif mylist[mid] < find:

 mylist = mylist[:mid]

 else:

 mylist = mylist[mid + 1:]

 return False

 

 

# linear search function

def linear_search(mylist, find):

 for x in mylist:

 if x == find:

 return True

 return False

 

 

# compute binary search time

def binary_time():

 SETUP_CODE = '''

from __main__ import binary_search

from random import randint'''

 

 TEST_CODE = '''

mylist = [x for x in range(10000)]

find = randint(0, len(mylist))

binary_search(mylist, find)'''

 

 # timeit.repeat statement

 times = timeit.repeat(setup = SETUP_CODE,

 stmt = TEST_CODE,

 repeat = 3,

 number = 10000)

 

 # priniting minimum exec. time

 print('Binary search time: {}'.format(min(times))) 

 

 

# compute linear search time

def linear_time():

 SETUP_CODE = '''

from __main__ import linear_search

from random import randint'''

 

 TEST_CODE = '''

mylist = [x for x in range(10000)]

find = randint(0, len(mylist))

linear_search(mylist, find)

 '''

 # timeit.repeat statement

 times = timeit.repeat(setup = SETUP_CODE,

 stmt = TEST_CODE,

 repeat = 3,

 number = 10000)

 

 # priniting minimum exec. time

 print('Linear search time: {}'.format(min(times))) 

 

if __name__ == "__main__":

 linear_time()

 binary_time()  
  
---  
  
 __

 __

  * The output of above program will be the minimum value in the list **times**.  
This is how a sample output looks like:  
![1](https://indianpythonista.files.wordpress.com/2017/01/1.png)

  *  **timeit.repeat()** function accepts one extra argument, **repeat**. The output will be a list of the execution times of all code runs repeated a specified no. of times.
  * In setup argument, we passed:
    
        from __main__ import binary_search
    from random import randint

This will import the definition of function **binary_search** , already
defined in the program and **random** library function **randint**.

  * As expected, we notice that execution time of binary search is significantly lower than linear search!

 **Example 3**  
Finally, I demonstrate below how you can utilize the command line interface of
**timeit** module:

![3](https://indianpythonista.files.wordpress.com/2017/01/31.png)

Here I explain each term individually:  
![2](https://indianpythonista.files.wordpress.com/2017/01/2.png)

So, this was a brief yet concise introduction to **timeit** module and its
practical applications.  
Its a pretty handy tool for python programmers when they need a quick glance
of the execution time of their code snippets.

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

