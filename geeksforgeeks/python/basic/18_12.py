Python in Competitive Programming



In 2017, when ACM allowed Python support for its prestigious competition, the
ACM ICPC, a whole new community became interested in the sport of competitive
programming. This meant more people coming back to the basics, learning
algorithms that are the building blocks of complex packages they use to build
their high level packages.  
Unfortunately, not a lot of information exists out there on how to effectively
use data structures and even the scoping rules of python which lead people to
believe that python is subpar for competitive programming.  
Today I’ll show you how python sometimes is even more powerful than C++ or
Java thanks to its amazing libraries, and how simple it actually can be.

Let me demonstrate with a simple example, look at the following snippets of
code-

 __

 __  
 __

 __

 __  
 __  
 __

alphabets= ['a', 'b', 'c']

for item in alphabets:

 len(item)   
  
---  
  
__

__

__

__  
__

__

__  
__  
__

alphabets= ['a', 'b', 'c']

fn = len

for item in alphabets:

 fn(item)  
  
---  
  
 __

 __

You might think I’ve assigned an alias to the function ‘len’ and it might not
make a difference.  
So i wrote a performance testing function as follows.

 __

 __  
 __

 __

 __  
 __  
 __

import datetime

alphabets = [str(x)for x in range(10000000)]

a = datetime.datetime.now() # store initial time

for item in alphabets:

 len(item)

b = datetime.datetime.now() # store final time

print (b-a).total_seconds() # results

a = datetime.datetime.now()

fn = len # function stored locally

for item in alphabets:

 fn(item)

b = datetime.datetime.now()

print (b-a).total_seconds()  
  
---  
  
 __

 __

I encourage you to try it on your systems.  
Here’s the output on mine on running the performance.py script.

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-
from-2018-08-13-13-13-31.png)

  

  

Almost half!

Okay, now let’s try to analyse why this happened. Reason? Lookup for a
function is a costly operation.  
In the second snippet, I stored the function directly in the scope of the
function, so it doesn’t matter how many times I call it, each time the runtime
knows exactly where it has to look for the results.

Itertools  
If you’ve been to codeforces, you know by now that the a lot of programming
challenges involve backtracking. So today I’ll tell you about a library to
generate all permutations and combinations using a inbuilt library package
which is extremely fast. Itertools. If you’re looking to solve algorithmic
challenges with python then itertools is library you must definitely explore.  
To generate all permutations –

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import permutations

perm = permutations([1, 2, 3], 2)

for i in list(perm):

 print i

 

# Answer->(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)  
  
---  
  
 __

 __

The combinations() functions behaves similarly I encourage the readers to try
it on their own.

> Python is a slow language only if your code is not leveraging the power of
> it successfully. Do not feel like you are at a disadvantage if you’re a
> python coder, it’s actually very neat and very quick!

![competitive-programming-img](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200604102100/GFG-CP-Article-2.png)

My Personal Notes _arrow_drop_up_

Save

