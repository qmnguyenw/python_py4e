Python return statement



A return statement is used to end the execution of the function call and
“returns” the result (value of the expression following the return keyword)
to the caller. The statements after the return statements are not executed. If
the return statement is without any expression, then the special value None
is returned.

 **Note:** Return statement can not be used outside the function.

 **Syntax:**

    
    
    def fun():
        statements
        .
        .
        return [expression]
    

**Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate return statement 

 

def add(a, b):

 

 # returning sum of a and b

 return a + b

 

def is_true(a):

 

 # returning boolean of a

 return bool(a)

 

# calling function

res = add(2, 3)

print("Result of add function is {}".format(res))

 

res = is_true(2<5)

print("\nResult of is_true function is {}".format(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Result of add function is 5
    
    Result of is_true function is True
    

## Returning Multiple Values

In Python, we can return multiple values from a function. Following are
different ways.

  *  **Using Object:** This is similar to C/C++ and Java, we can create a class (in C, struct) to hold multiple values and return an object of the class.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using class 

class Test: 

 def __init__(self): 

 self.str = "geeksforgeeks"

 self.x = 20

 

# This function returns an object of Test 

def fun(): 

 return Test() 

 

# Driver code to test above method 

t = fun() 

print(t.str) 

print(t.x)  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks
    20
    

  * **Using Tuple:** A Tuple is a comma separated sequence of items. It is created with or without (). Tuples are immutable. See this for details of tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using tuple 

 

# This function returns a tuple 

def fun(): 

 str = "geeksforgeeks"

 x = 20

 return str, x; # Return tuple, we could also 

 # write (str, x) 

 

# Driver code to test above method 

str, x = fun() # Assign returned tuple 

print(str) 

print(x)   
  
---  
  
__

__

**Output:**

    
    
    geeksforgeeks
    20
    

  * **Using a list:** A list is like an array of items created using square brackets. They are different from arrays as they can contain items of different types. Lists are different from tuples as they are mutable. See this for details of list.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using list 

 

# This function returns a list 

def fun(): 

 str = "geeksforgeeks"

 x = 20

 return [str, x]; 

 

# Driver code to test above method 

list = fun() 

print(list)   
  
---  
  
__

__

**Output:**

    
    
    ['geeksforgeeks', 20]
    

  * **Using a Dictionary:** A Dictionary is similar to hash or map in other languages. See this for details of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to return multiple

# values from a method using dictionary 

 

# This function returns a dictionary 

def fun(): 

 d = dict(); 

 d['str'] = "GeeksforGeeks"

 d['x'] = 20

 return d 

 

# Driver code to test above method 

d = fun() 

print(d)   
  
---  
  
__

__

**Output:**

    
    
    {'x': 20, 'str': 'GeeksforGeeks'}
    

## Function returning another function

In Python, functions are objects so, we can return a function from another
function. This is possible because funcitons are treated as first class
objects in Python. To know more about first class objects click here.  
In the below example, the create_adder function returns adder function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate functions

# can return another function 

 

def create_adder(x): 

 def adder(y): 

 return x + y 

 

 return adder 

 

add_15 = create_adder(15) 

 

print("The result is", add_15(10)) 

 

# Returning different function

def outer(x):

 return x * 10

 

def my_func():

 

 # returning different function

 return outer

 

# storing the function in res

res = my_func()

 

print("\nThe result is:", res(10))  
  
---  
  
 __

 __

 **Output:**

    
    
    The result is 25
    
    The result is: 100
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

