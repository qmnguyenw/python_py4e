NumPy – Arithmetic operations with array containing string elements



Numpy is a library of Python for array processing written in C and Python.
Computations in numpy are much faster than that of traditional data structures
in Python like lists, tuples, dictionaries etc. due to vectorized universal
functions. Sometimes while dealing with data, we need to perform arithmetic
operations but we are unable to do so because of the presence of unwanted
strings in our data. So it is necessary to remove them. Here we are going to
create a universal function to replace unwanted strings to NaN.

 **Explanation:**  
Given a numpy array containing some unwanted string. In a user-defined
function, unwanted strings are replaced with NaN using conditional statements.
_numpy.frompyfunc()_ is used to convert the user-defined function into
universal function. The numpy array is then passed to that function, but
still, the data type of the array is an object. Therefore we need to convert
its datatype to float using _array.astype()_. It should be noted that NaN
values cannot be converted to any other datatype than float. Now we can
perform arithmetic operations on it using NaN safe version of inbuilt
universal functions.

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

# Importing numpy library

import numpy as gfg

 

# Creating array

a =
gfg.array([1,2,3,'geeks','for','geeks',4,5])

print(f"Actual array: {a}")

 

# Creating universal function to remove unwanted 

# strings from actual array

def m(a):

 if a == 'geeks'or a=='for':

 return gfg.nan

 else:

 return float(a)

 

# Converting user-defined function to universal function 

b = gfg.frompyfunc(m,1,1)

 

# Calling function

a = b(a)

 

# Changing datatype of array

a = a.astype(float)

print(f"Array after changes: {a}")

 

# Calculating mean of the array

m = gfg.nanmean(a)

print(f"Mean of the array: {m}")

 

# Calculating sum of the array

s = gfg.nansum(a)

print(f"Sum of the array: {s}")

 

# Calculating product of the array

p = gfg.nanprod(a)

print(f"Product of the array: {p}")  
  
---  
  
 __

 __

 **Output:**

    
    
    Actual array: ['1' '2' '3' 'geeks' 'for' 'geeks' '4' '5']
    Array after changes: [ 1.  2.  3. nan nan nan  4.  5.]
    Mean of the array: 3.0
    Sum of the array: 15.0
    Product of the array: 120.0

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

