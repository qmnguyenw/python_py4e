Currying Function in Python



In problem solving and functional programming, _currying_ is the practice of
simplifying the execution of a function that takes multiple arguments into
executing sequential single-argument functions. In simple terms, Currying is
used to transform multiple-argument function into single argument function by
evaluating incremental nesting of function arguments. Currying also mends one
argument to another forms a relative pattern while execution.

 **Mathematical Illustration of Currying:**  
In general currying of functions takes up any number of calculations and data
to single real function that returns an expected output. Here we take,

    
    
    f(x, y) = (x*x*x) + (y*y*y)
    h(x) = (x*x*x)
    h(y) = (y*y*y)
    h(x)(y) = h(x)+h(y)
    f(x, y) = h(x)(y)
    Curry f = h(x)(y)

For example, we will take chaining the composition of function.

 **a(x) = b(c(d(x)))**

 __

 __  
 __

 __

 __  
 __  
 __

def change(b, c, d):

 def a(x):

 return b(c(d(x)))

 return a  
  
---  
  
 __

 __

 **v(a, b, c, d, e) = w(x(y(z(a, b, c, d, e))))**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Currying in Python - Many to Single Argument

 def change(a):

 def w(b):

 def x(c):

 def y(d):

 def z(e):

 print(a, b, c, d, e)

 return z

 return y

 return x

 return w

 

change(10)(20)(30)(40)(50)  
  
---  
  
 __

 __

 **Output:**

    
    
    10 20 30 40 50

Here, the concept is nesting of one function to another function and hence the
result of one function gets recorded in the chain of functions. There by
simplifying one huge block of manipulation to simpler sequential blocks.

 **Code #1:** Change kilometer to meter and meter to centimeter.

 __

 __  
 __

 __

 __  
 __  
 __

# Demonstrate Currying of composition of function

def change(b, c, d):

 def a(x):

 return b(c(d(x)))

 return a

 

def kilometer2meter(dist): 

 """ Function that converts km to m. """

 return dist * 1000

 

def meter2centimeter(dist): 

 """ Function that converts m to cm. """

 return dist * 100

 

def centimeter2feet(dist):

 """ Function that converts cm to ft. """

 return dist / 30.48

 

if __name__ == '__main__':

 transform = change(centimeter2feet, meter2centimeter, kilometer2meter
)

 e = transform(565)

 print(e)

   
  
---  
  
__

__

**Output:**

    
    
    1853674.5406824148

  
**Code #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# Demonstrate Currying of composition of function

 

def change(b, c, d):

 def a(x):

 return b(c(d(x)))

 return a

 

def daystohour(time): 

 """ Function that converts days to hours. """

 return time * 24

 

def hourstominutes(time): 

 """ Function that converts hours to minutes. """

 return time * 60

 

def minutestoseconds(time):

 """ Function that converts minutes to seconds. """

 return time * 60

 

if __name__ == '__main__':

 transform = change(minutestoseconds, hourstominutes, daystohour)

 e = transform(10)

 print(e)

   
  
---  
  
__

__

**Output:**

    
    
    864000

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

