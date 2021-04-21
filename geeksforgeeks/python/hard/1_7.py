Numpy Gradient – Descent Optimizer of Neural Networks



In differential calculus, the derivative of a function tells us how much the
output changes with a small nudge in the input variable. This idea can be
extended to multivariable functions as well. This article shows the
implementation of the Gradient Descent Algorithm using NumPy. The idea is very
simple- start with an arbitrary starting point and move towards the minimum
(that is -ve of gradient value), and return a point that is as close to the
minimum.

GD() is a user-defined function employed for this purpose. It takes the
following parameters:

  *  **gradient** is a function which or it can be a python callable object which takes a vector & returns the gradient of a function which we are trying to minimize.
  *  **start** is the arbitrary starting point which we give to the function, it is a single independent variable. It can also be a list, Numpy array for multivariable.
  *  **learn_rate** controls the magnitude by which the vectors get updated.
  *  **n_iter** is the number of iterations the operation should run.
  *  **tol** is the tolerance level that specifies the minimum movement in each iteration.

Given below is the implementation to produce out required functionality.

 **Example:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

def GD(f, start, lr, n_iter=50, tol=1e-05):

 res = start

 

 for _ in range(n_iter):

 

 # graident is calculated using the np.gradient 

 # function.

 new_val = -lr * np.gradient(f)

 if np.all(np.abs(new_val) <= tol):

 break

 res += new_val

 

 # we return a vector as the gradient can be

 # multivariable function. if the function has 1

 # dependent variable then it returns a scalar value.

 return res

 

 

# Example 1

f = np.array([1, 2, 4, 7, 11, 16],
dtype=float)

print(f"The vector notation of global minima:{GD(f,10,0.01)}")

 

# Example 2

f = np.array([2, 4], dtype=float)

print(f'The vector notation of global minima: {GD(f,10,0.1)}')  
  
---  
  
 __

 __

