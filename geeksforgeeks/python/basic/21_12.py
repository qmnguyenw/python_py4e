Python | Multiply all numbers in the list (4 different ways)



Given a list, print the value obtained after multiplying all numbers in a
list.  
Examples:  

    
    
    Input :  list1 = [1, 2, 3] 
    Output : 6 
    Explanation: 1*2*3=6 
    
    Input : list1 = [3, 2, 4] 
    Output : 24 
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

**Method 1: Traversal**

Initialize the value of the product to 1(not 0 as 0 multiplied with anything
returns zero). Traverse till the end of the list, multiply every number with
the product. The value stored in the product at the end will give you your
final answer.  
Below is the Python implementation of the above approach:  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to multiply all values in the

# list using traversal

def multiplyList(myList) :

 

 # Multiply elements one by one

 result = 1

 for x in myList:

 result = result * x

 return result

 

# Driver code

list1 = [1, 2, 3]

list2 = [3, 2, 4]

print(multiplyList(list1))

print(multiplyList(list2))  
  
---  
  
 __

 __

 **Output:**  

    
    
    6
    24 
    
    
    
    

**Method 2: Using numpy.prod()**

We can use numpy.prod() from import numpy to get the multiplication of all the
numbers in the list. It returns an integer or a float value depending on the
multiplication result.  
Below is the Python3 implementation of the above approach:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to multiply all values in the

# list using numpy.prod()

import numpy

list1 = [1, 2, 3]

list2 = [3, 2, 4]

# using numpy.prod() to get the multiplications

result1 = numpy.prod(list1)

result2 = numpy.prod(list2)

print(result1)

print(result2)  
  
---  
  
 __

 __

 **Output:**  

    
    
    6
    24 
    

**Method 3 Using lambda function: Using numpy.array**

Lambda’s definition does not include a **“return”** statement, it always
contains an expression that is returned. We can also put a lambda definition
anywhere a function is expected, and we don’t have to assign it to a variable
at all. This is the simplicity of lambda functions. The **reduce()** function
in Python takes in a function and a list as an argument. The function is
called with a lambda function and a list and a n **ew reduced result is
returned**. This performs a repetitive operation over the pairs of the list.  
Below is the Python3 implementation of the above approach:  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to multiply all values in the

# list using lambda function and reduce()

from functools import reduce

list1 = [1, 2, 3]

list2 = [3, 2, 4]

result1 = reduce((lambda x, y: x * y), list1)

result2 = reduce((lambda x, y: x * y), list2)

print(result1)

print(result2)  
  
---  
  
 __

 __

 **Output:**  

    
    
    6
    24 
    

**Method 4 Using prod function of math library: Using math.prod**

Starting Python 3.8, a prod function has been included in the math module in
the standard library, thus no need to install external libraries.  
Below is the Python3 implementation of the above approach:  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to multiply all values in the

# list using math.prod

import math

list1 = [1, 2, 3]

list2 = [3, 2, 4]

result1 = math.prod(list1)

result2 = math.prod(list2)

print(result1)

print(result2)  
  
---  
  
 __

 __

 **Output:**  

    
    
    6
    24 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

