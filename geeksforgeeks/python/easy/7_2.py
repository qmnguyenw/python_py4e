Python infinity



As ironic as it may seem infinity is defined as an undefined number that can
either be a positive or negative value. All arithmetic operations performed on
an infinite value always lead to an infinite number, say it be sum,
subtraction, multiplication, or any other operation.

In the world of computer science, infinity is generally used to measure
performance and optimize algorithms that perform computations on a large scale
application.

 **Representing infinity as an Integer in python**

The concept of representing infinity as an integer violates the definition of
infinity itself. As of 2020, there is no such way to represent infinity as an
integer in any programming language so far. But in python, as it is a dynamic
language, float values can be used to represent an infinite integer. One can
use **float('inf')** as an integer to represent it as infinity.Below is the
list of ways one can represent infinity in Python.

 **1\. Using float(‘inf’) and float(‘-inf’):**

  

  

As infinity can be both positive and negative they can be represented as a
float(‘inf’) and float(‘-inf’) respectively. The below code shows the
implementation of the above-discussed content:

 __

 __  
 __

 __

 __  
 __  
 __

# Defining a positive infinite integer

positive_infnity = float('inf')

print('Positive Infinity: ', positive_infnity)

 

# Defining a negative infinite integer

negative_infnity = float('-inf')

print('Negative Infinity: ', negative_infnity)  
  
---  
  
 __

 __

 **Output:**

    
    
    Positive Infinity:  inf
    Negative Infinity:  -inf

 **2\. using Python’s math module:**

Python’s math module can also be used for representating infinite integers.
The below code shows how it is done:

 __

 __  
 __

 __

 __  
 __  
 __

import math

 

# Defining a positive infinite integer

positive_infnity = math.inf

print('Positive Infinity: ', positive_infnity)

 

# Defining a negative infinite integer

negative_infinity = -math.inf

print('Negative Infinity: ', negative_infinity)  
  
---  
  
 __

 __

 **Output:**

    
    
    Positive Infinity:  inf
    Negative Infinity:  -inf

 **3\. using Python’s decimal module:**

Python’s decimal module can also be used for representating infinite float
values.  
It is used as **Decimal('Infinity')** for positve and
**Decimal('-Infinity')** for negative infinite value.  
The below code shows its implementation:

 __

 __  
 __

 __

 __  
 __  
 __

from decimal import Decimal

 

# Defining a positive infinite integer

positive_infnity = Decimal('Infinity')

print('Positive Infinity: ', positive_infnity)

 

# Defining a negative infinite integer

negative_infinity = Decimal('-Infinity')

print('Negative Infinity: ', negative_infinity)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Positive Infinity:  Infinity
    Negative Infinity:  -Infinity

 **4\. using Python’s Numpy library:**

Python’s Numpy module can also be used for representating infinite values.It
is used as **np.inf** for positve and **-np.inf** for negative infinite
value. The use of Numpy library for representating an infinite value is shown
in the code below:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

# Defining a positive infinite integer

positive_infnity = np.inf

print('Positive Infinity: ', positive_infnity)

 

# Defining a negative infinite integer

negative_infinity = -np.inf

print('Negative Infinity: ', negative_infinity)  
  
---  
  
 __

 __

 **Output:**

    
    
    Positive Infinity:  inf
    Negative Infinity:  -inf

 **Checking If a Number Is Infinite in Python**

To check if a given number is infinite or not, one can use **isinf()**
method of the math library which returns a boolean value.The below code shows
the use of isinf() method:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import math

 

# Defining a positive infinite integer

a = np.inf

 

# Defining a negative infinite integer

b = -np.inf

 

# Define a finite integer

c = 300

 

# chech if a in infinite

print(math.isinf(a))

 

# chech if b in infinite

print(math.isinf(b))

 

# chech if c in infinite

print(math.isinf(c))  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    True
    False

 **Comparing infinite values to finite values in python**  
The concept of comparing an infinite value to finite values is as simple as it
gets. As positive infinity is always bigger than every natural number and
negative infinity is always smaller than the negative numbers. For better
understanding look into the code below:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

# Defining a positive infinite integer

a = np.inf

 

# Defining a negative infinite integer

b = -np.inf

 

# Define a finite + ve integer

c = 300

 

 

# Define a finite -ve integer

d = -300

 

# helper function to make comparisions

def compare(x, y):

 if x>y:

 print("True")

 else:

 print("False")

 

compare(a, b)

compare(a, c)

compare(a, d)

compare(b, c)

compare(b, d)  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    True
    True
    False
    False

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

