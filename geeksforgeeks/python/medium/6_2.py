How to use the NumPy sum function?



NumPy’s sum() function is extremely useful for summing all elements of a given
array in Python. In this article, we’ll be going over how to utilize this
function and how to quickly use this to advance your code’s functionality.

Let’s go over how to use these functions and the benefits of using this
function rather than iteration summation. Let’s first write the underlying
algorithm to do simple summation ourselves. This will take the form of a
function as follows:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Let's define our function

# Parameters: Input Array

def sum(array):

 

 # Set variable for our final answer

 sum = 0

 

 # Parse through our array

 for i in array:

 

 # Continuously add current element

 # to final sum

 sum += i

 

 # Return our sum

 return sum

 

 

# Create a test array

testArray = [1, 3, 34, 92, 29, 48, 20.3]

 

# Test our function

print('The sum of your numbers is ' + str(sum(testArray)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The sum of your numbers is 227.3
    

Now that we’ve seen how many lines it takes to write just this simple
summation function, let’s test out NumPy’s sum() function to see how it
compares.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import NumPy Library

import numpy as np

 

# Let's begin with an example array

# Initialize our array

array = [1, 4, 2.5, 3, 7.4, 8]

 

# Utilize the the sum() function

print('The sum of these numbers is ' + str(np.sum(array)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The sum of these numbers is 25.9
    

Let’s see some more examples for understanding the usage of this function. One
thing to note before going any further is that if the sum() function is called
with a two-dimensional array, the sum() function will return the sum of all
elements in that array.

 **Example 1:**

In this example, we’ll just do another simple summation of a one-dimensional
array, just as we have seen before. It’ll get more exciting later on though!

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import NumPy

import numpy as np

 

# Initialize our test array

array = [0.5, 1.5]

 

# Call our sum() function

print(np.sum(array))  
  
---  
  
 __

 __

 **Output:**

    
    
    2.0
    

**Example 2:**

  

  

In this example, we’ll go over summing a two-dimensional array. Still pretty
basic.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import NumPy Library

import numpy as np

 

# Initialize our array

array = [[1, 3.4, 4.5], [3.45, 5.6, 9.8], 

 [4.5, 5, 6.3]]

 

# Call our sum() function

print(np.sum(array))  
  
---  
  
 __

 __

 **Output:**

    
    
    43.55
    

**Example 3:**

Let’s try to use the optional parameters to try and manipulate our output.
Let’s try out the **axis** parameter.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import NumPy

import numpy as np

 

# Initialize our array

array = [[0, 1], [0, 5]]

 

# Let's say we want to sum each sub array

# Sums will be returned seperately in array

# format Call sum() function

print(np.sum(array, axis = 1))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1 5]
    

**Example 4:**

Let’s try using the **initial** parameter to initialize our sum value.
Essentially, the initial value gets added to the sum of the elements of the
array. This is useful in certain problems utilizing counters.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import NumPy Library

import numpy as np

 

# Initialize our array

array = [1.5, 3, 5.6]

 

# Call our sum() function

# initial = 3

print(np.sum(array, initial = 3))  
  
---  
  
 __

 __

 **Output:**

    
    
    13.1
    

**Example 5:**

If the accumulator for the sum is too small, then we get issues as far as
overflow. Though this won’t directly throw an error, we will get issues with
the results being unreliable. Let’s take a look at an example. We’ll use
NumPy’s ones() function to automatically create an array of a given length
that is filled with ones.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import NumPy Library

import numpy as np

 

# Initialize our array

array = np.ones(250, dtype=np.int8)

 

# Call our sum() function with a specified

# accumulator type

print(np.sum(array, dtype=np.int8))

 

# Expected Output: 250  
  
---  
  
 __

 __

 **Output:**

    
    
    -6
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

