numpy.savetxt()



 **numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n',
header='', footer='', comments='# ', encoding=None)** : This method is used
to save an array to a text file.

>  _ **Parameters:**  
>  **fname :** If the filename ends in .gz, the file is automatically saved
> in compressed gzip format. loadtxt understands gzipped files transparently.  
>  **X** : [1D or 2D array_like] Data to be saved to a text file.  
>  **fmt** : A single format (%10.5f), a sequence of formats, or a multi-
> format string, e.g. ‘Iteration %d – %10.5f’, in which case delimiter is
> ignored.  
>  **delimiter** : String or character separating columns.  
>  **newline** : String or character separating lines.  
>  **header** : String that will be written at the beginning of the file.  
>  **footer** : String that will be written at the end of the file.  
>  **comments** : String that will be prepended to the header and footer
> strings, to mark them as comments. Default: ‘# ‘, as expected by e.g.
> numpy.loadtxt.  
>  **encoding** : Encoding used to encode the output file. Does not apply to
> output streams. If the encoding is something other than ‘bytes’ or ‘latin1’
> you will not be able to load the file in NumPy versions < 1.14. Default is
> ‘latin1’.
>
> _

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# savetxt() function

import numpy as geek

 

x = geek.arange(0, 10, 1)

print("x is:")

print(x)

 

# X is an array

c = geek.savetxt('geekfile.txt', x, delimiter =', ') 

a = open("geekfile.txt", 'r')# open file in read mode

 

print("the file contains:")

print(a.read())  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    x is:
    [0 1 2 3 4 5 6 7 8 9]
    the file contains:
    0.000000000000000000e+00
    1.000000000000000000e+00
    2.000000000000000000e+00
    3.000000000000000000e+00
    4.000000000000000000e+00
    5.000000000000000000e+00
    6.000000000000000000e+00
    7.000000000000000000e+00
    8.000000000000000000e+00
    9.000000000000000000e+00
    
    

  
**Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# savetxt() function

 

import numpy as geek

 

x = geek.arange(0, 10, 1)

y = geek.arange(10, 20, 1)

z = geek.arange(20, 30, 1)

print("x is:")

print(x)

 

print("y is:")

print(y)

 

print("z is:")

print(z)

 

# x, y, z are 3 numpy arrays with same dimension 

c = geek.savetxt('geekfile.txt', (x, y, z)) 

a = open("geekfile.txt", 'r')# open file in read mode

 

print("the file contains:")

print(a.read())  
  
---  
  
 __

 __

 **Output :**

> x is:  
> [0 1 2 3 4 5 6 7 8 9]  
> y is:  
> [10 11 12 13 14 15 16 17 18 19]  
> z is:  
> [20 21 22 23 24 25 26 27 28 29]
>
> the file contains:  
> 0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00
> 3.000000000000000000e+00 4.000000000000000000e+00 5.000000000000000000e+00
> 6.000000000000000000e+00 7.000000000000000000e+00 8.000000000000000000e+00
> 9.000000000000000000e+00  
> 1.000000000000000000e+01 1.100000000000000000e+01 1.200000000000000000e+01
> 1.300000000000000000e+01 1.400000000000000000e+01 1.500000000000000000e+01
> 1.600000000000000000e+01 1.700000000000000000e+01 1.800000000000000000e+01
> 1.900000000000000000e+01  
> 2.000000000000000000e+01 2.100000000000000000e+01 2.200000000000000000e+01
> 2.300000000000000000e+01 2.400000000000000000e+01 2.500000000000000000e+01
> 2.600000000000000000e+01 2.700000000000000000e+01 2.800000000000000000e+01
> 2.900000000000000000e+01

  
**Code #3:** TypeError

 __

 __  
 __

 __

 __  
 __  
 __

# Python program explaining

# savetxt() function

 

import numpy as geek

 

x = geek.arange(0, 10, 1)

y = geek.arange(0, 20, 1)

z = geek.arange(0, 30, 1)

print("x is:")

print(x)

 

print("y is:")

print(y)

 

print("z is:")

print(z)

 

# x, y, z are 3 numpy arrays without having same dimension 

c = geek.savetxt('geekfile.txt', (x, y, z))   
  
---  
  
__

__

**Output:**

> fh.write(asbytes(format % tuple(row) + newline))  
> TypeError: only length-1 arrays can be converted to Python scalars
>
> During handling of the above exception, another exception occurred:
>
> % (str(X.dtype), format))  
> TypeError: Mismatch between array dtype (‘object’) and format specifier
> (‘%.18e’)

Note that if the numpy arrays are not of equal dimension error occurs.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

