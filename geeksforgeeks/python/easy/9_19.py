Is Python call by reference or call by value



Python utilizes a system, which is known as “Call by Object Reference” or
“Call by assignment”. In the event that you pass arguments like whole numbers,
strings or tuples to a function, the passing is like call-by-value because you
can not change the value of the immutable objects being passed to the
function. Whereas passing mutable objects can be considered as call by
reference because when their values are changed inside the function, then it
will also be reflected outside the function.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# call by value

 

 

string = "Geeks"

 

 

def test(string):

 

 string = "GeeksforGeeks"

 print("Inside Function:", string)

 

# Driver's code

test(string)

print("Outside Function:", string)  
  
---  
  
 __

 __

 **Output**

    
    
    Inside Function: GeeksforGeeks
    Outside Function: Geeks
    

**Example 2**

 __

 __  
 __

 __

 __  
 __  
 __



# Python code to demonstrate 

# call by reference

 

 

def add_more(list):

 list.append(50)

 print("Inside Function", list)

 

# Driver's code

mylist = [10,20,30,40]

 

add_more(mylist)

print("Outside Function:", mylist)  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Inside Function [10, 20, 30, 40, 50]
    Outside Function: [10, 20, 30, 40, 50]
    

#### Binding Names to Objects

In python, each variable to which we assign a value/container is treated as an
object. When we are assigning a value to a variable, we are actually
**binding** a name to an **object**.

 __

 __  
 __

 __

 __  
 __  
 __

a= "first"

b = "first"

 

 

# Returns the actual location 

# where the variable is stored

print(id(a))

 

# Returns the actual location 

# where the variable is stored

print(id(b))

 

# Returns true if both the variables

# are stored in same location

print(a is b)  
  
---  
  
 __

 __

 **Output**

    
    
    110001234557894
    110001234557894
    True
    

Now, let’s try and understand this better with another example.

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

a= [10, 20, 30]

b = [10, 20, 30]

 

# return the location

# where the variable 

# is stored

print(id(a))

 

# return the location

# where the variable 

# is stored

print(id(b))

 

# returns false if the

# location is not same

print(a is b)  
  
---  
  
 __

 __

 **Output**

    
    
    541190289536222
    541190288737777
    False
    

The output of the above two examples are different because the list is
**mutable** and the string is **immutable**. An **immutable** variable cannot
be changed once created. If we wish to change an **immutable** variable, such
as a string, we must create a new instance and bind the variable to the new
instance. Whereas, **mutable** variable can be changed in place.

 **Example 3:**

 __

 __  
 __

 __

 __  
 __  
 __

def foo(a):

 

 # A new vriable is assigned

 # for the new string

 a = "new value"

 print("Inside Function:", a)

 

 

# Driver's code

string = "old value"

foo(string)

 

print("Outside Function:", string)  
  
---  
  
 __

 __

 **Output:**

    
    
    Inside Function: new value
    Outside Function: old value
    

In the above example, a string which is an **immutable** type of object is
passed as argument to the function foo. Within the scope of the given
function foo, a= "new value" has been bounded to the same object that
string has been bound outside. Within the scope of the function foo, we
modify “old value” to “new value”. Once we leave the scope of function foo
, a="new value" is no longer in the name space, and the value that string
refers to was never changed.

 **Example 4:** Now, let us look at how **mutable variable** is passed into
the function.

 __

 __  
 __

 __

 __  
 __  
 __

def foo(a):

 a[0] = "Nothing"

 

# Driver' code

bar = ['Hi', 'how', 'are', 'you', 'doing']

foo(bar)

print(bar)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['Nothing, 'how', 'are', 'you', 'doing']
    

When we pass a mutable variable into the function foo and modify it to
some other name the function foo still points to that object and continue to
point to that object during its execution.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

