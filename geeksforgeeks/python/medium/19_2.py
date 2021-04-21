Overuse of lambda expressions in Python



 **What are lambda expressions?**  
A lambda expression is a special syntax to create functions without names.
These functions are called lambda functions. These lambda functions can have
any number of arguments but only one expression along with an implicit return
statement. Lambda expressions return function objects. For Example consider
the lambda expression:

    
    
    **lambda (arguments) : (expression)**
    

This lambda expression defines an **unnamed function** , which accepts two
arguments and returns the sum of the two arguments. But how do we call an
unnamed function? The above defined unnamed **lambda function** can be called
as:

    
    
    (lambda x, y: x + y)(1, 2)
    

**Code 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing a use

# lambda function

 

# performing a addition of three number

x1 = (lambda x, y, z: (x + y) * z)(1, 2, 3)

print(x1)

 

# function using a lambda fumction 

x2 = (lambda x, y, z: (x + y) if (z == 0) else (x
* y))(1, 2, 3)

print(x2)   
  
---  
  
__

__

**Output:**

    
    
    9
    2
    

Though it is not encouraged, the function object returned by a lambda
expression can be assigned to a variable. See the example below in which a
variable sum is assigned a function object returned by a lambda expression.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# variable is storing lambda

# expression

 

# assingned to a variable

sum = lambda x, y: x + y

print(type(sum))

 

x1 = sum(4, 7)

print(x1)  
  
---  
  
 __

 __

 **Output:**

    
    
    11
    

  
**Common uses of lambda expressions :**

  * Since lambda functions are anonymous and do not require a name to be assigned, they are usually **used to call functions(or classes) which require a function object as an argument**. Defining separate functions for such function arguments is of no use because, the function definition is usually short and they are required only once or twice in the code. For example, the **key** argument of the inbuilt function, sorted().

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# using of normal function

def Key(x):

 return x%2

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8,
9]

sort = sorted(nums, key = Key)

print(sort)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    

__

__  
__

__

__  
__  
__

# Python program showing use

# of lambda function

 

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8,
9]

sort_lambda = sorted(nums, key = lambda x: x%2)

print(sort_lambda)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    

  * Lambda functions are inline functions and hence they are **used whenever there is a need of repetitive function calls** to reduce execution time. Some of the examples of such scenarios are the functions: map(), filter() and sorted(). For example,

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing a use

# of lambda function

 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,
0]

 

# using map() function

squares = map(lambda x: x * x, nums)

print(list(squares))

 

# using filter() function

evens = filter(lambda x: True if (x % 2 == 0)

 else False, nums)

print(list(evens))  
  
---  
  
 __

 __

  
**Pros and Cons of lambda functions :**  
 **Pros of lambda functions:**

  * Being anonymous, lambda functions can be easily passed without being assigned to a variable.
  * Lambda functions are inline functions and thus execute comparatively faster.
  * Many times lambda functions make code much more readable by avoiding the logical jumps caused by function calls. For example, read the following blocks of code.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program performing

# operation using def()

def fun(x, y, z):

 return x*y+z

a = 1

b = 2

c = 3

 

# logical jump

d = fun(a, b, c)

print(d)   
  
---  
  
__

__

**Output:**

    
    
    5
    

__

__  
__

__

__  
__  
__

# Python program performing

# operation using lambda

 

d = (lambda x, y, z: x*y+z)(1, 2, 3)

print(d)  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

**Cons on lambda functions:**

  

  

  * Lambda functions can have only one expression.
  * Lambda functions cannot have a docstring.
  * Many times lambda functions make code difficult to read. For example, see the blocks of code given below.

 __

 __  
 __

 __

 __  
 __  
 __

def func(x):

 if x == 1:

 return "one"

 elif x == 2:

 return "two"

 elif x == 3:

 return "three"

 else:

 return "ten"

num = func(3)

print(num)  
  
---  
  
 __

 __

 **Output:**

    
    
    three
    

__

__  
__

__

__  
__  
__

# Python program showing use

# of lambda function

num = (lambda x: "one" if x == 1 else( "two" if
x == 2

 else ("three" if x == 3 else "ten")))(3)

print(num)  
  
---  
  
 __

 __

 **Output:**

    
    
    three
    

  
**Misuse of Lambda expressions :**

  *  **Assignment of lambda expressions :** The official python style guide PEP8, strongy discourages the assignment of lambda expressions as shown in the example below.
    
    
    func = lambda x, y, z: x*y + z
    

Instead, it is recommended to write a one-liner function as,

    
    
    def func(x, y, z): return x*y + z 
    

While the second method encourages the fact that lambda functions are
anonymous, it is also useful for tracebacks during debugging. Run the code
below to see how **def** makes tracebacks much useful.

 __

 __  
 __

 __

 __  
 __  
 __

func= lambda x, y, z: x * y + z

print(func)

def func(x, y, z): return x * y + z

print(func)  
  
---  
  
 __

 __

  *  **Wrapping lambda expressions around functions :** Many times, lambda expressions are needlessly wrapped around functions as shown below.
    
    
    nums = [-2, -1, 0, 1, 2]
    sort = sorted(nums, key=lambda x: abs(x))
    

While the above syntax is absolutely correct, programmers must understand that
all functions in python can be passed as function objects. Hence the same code
can(and should) be written as,

    
    
    sort = sorted(nums, key=abs)
    

  * **Passing functions unnecessarily :** Many times, programmers pass functions which perform only a single operation. See the following code.
    
    
    nums = [1, 2, 3, 4, 5]
    summation = reduce(lambda x, y: x + y, nums)
    

The lambda function passed above performs only a single operation, adding the
two arguments. The same result can be obtained by the using the built-in
function **sum** , as shown below.

    
    
    nums = [1, 2, 3, 4, 5]
    summation = sum(nums)
    

Programmers should avoid using lambda expressions for common operations,
because it is highly probable to have a built-in function providing the same
results.

  
**Overuse of lambda expressions :**

*  **Using lambda for non-trivial functions :** Sometimes, simple functions can be non-trivial. See the code below.

 __

 __  
 __

 __

 __  
 __  
 __

details= [{'p':100, 'r':0.01, 'n':2,
't':4},

 {'p':150, 'r':0.04, 'n':1, 't':5},

 {'p':120, 'r':0.05, 'n':5, 't':2}] 

sorted_details = sorted(details, 

 key=lambda x: x['p']*((1 + x['r']/

 x['n'])**(x['n']*x['t'])))

print(sorted_details)  
  
---  
  
 __

 __

 **Output:**

> [{‘n’: 2, ‘r’: 0.01, ‘t’: 4, ‘p’: 100}, {‘n’: 5, ‘r’: 0.05, ‘t’: 2, ‘p’:
> 120}, {‘n’: 1, ‘r’: 0.04, ‘t’: 5, ‘p’: 150}]

Here, we are sorting the dictionaries on the basis of the compound interest.
Now, see the code written below, which uses **def**.

 __

 __  
 __

 __

 __  
 __  
 __

details= [{'p':100, 'r':0.01, 'n':2,
't':4},

 {'p':150, 'r':0.04, 'n':1, 't':5},

 {'p':120, 'r':0.05, 'n':5, 't':2}] 

def CI(det):

 '''sort key: coumpound interest, P(1 + r/n)^(nt)'''

 return det['p']*((1 +
det['r']/det['n'])**(det['n']*det['t']))

sorted_details = sorted(details, key=CI)

print(sorted_details)  
  
---  
  
 __

 __

 **Output:**

> [{‘n’: 2, ‘r’: 0.01, ‘t’: 4, ‘p’: 100}, {‘n’: 5, ‘r’: 0.05, ‘t’: 2, ‘p’:
> 120}, {‘n’: 1, ‘r’: 0.04, ‘t’: 5, ‘p’: 150}]

Though both codes do the same thing, the second one which uses **def** is much
more readable. The expression written here under the lambda might be simple,
but it has a meaning(formula for compound interest). Hence, the expression is
non-trivial and deserves a name. Using lambda expressions for non-trivial
functions reduces the readability of the code.

*  **Using lambdas when multiple lines would help :** If using a multiple line function makes the code more readable, using lambda expressions to reduce some lines of code is not worth it. For example, see the code below.  

> people = [(‘sam’, ‘M’, 18), (‘susan’, ‘F’, 22), (‘joy’, ‘M’, 21), (‘lucy’,
> ‘F’, 12)]  
> sorted_people = sorted(people, key=lambda x: x[1])

Also see the following code which uses **def**.

    
    
    def Key(person):
        name, sex, age = person
        return sex
    sorted_people = sorted(people, key=Key)
    

See how tuple unpacking in the second block of code makes it much more
readable and logical. Readibility of the code should the be utmost priority of
a programmer, working in a collaborative environment.

*  **Using lambda expressions for map and filter :** Lambdas are very commonly used with map() and filter() as shown.

 __

 __  
 __

 __

 __  
 __  
 __

nums= [0, 1, 2, 3, 4, 5]

mapped = map(lambda x: x * x, nums)

filtered = filter(lambda x: x % 2, nums)

print(list(mapped))

print(list(filtered))  
  
---  
  
 __

 __

Following is another block of code which usesgenerator expressions to achieve
similar results.

 __

 __  
 __

 __

 __  
 __  
 __

nums= [0, 1, 2, 3, 4, 5]

mapped = (x * x for x in nums)

filtered = (x for x in nums if x % 2 == 1)

print(list(mapped))

print(list(filtered))  
  
---  
  
 __

 __

Unlike map() and filter(), generator expressions are general purpose features
of python language. Thus generators enhance the readability of the code.
While, map() and filter() require prior knowledge of these functions.

*  **Use of higher order functions :** The functions which accept other function objects as arguments are called higher order functions (i.e. map() and filter()), which are common in functional programming. As stated above, lambda expressions are commonly used as the function arguments of higher order functions. Compare the two code blocks shown below.  
Using high order function reduce()

    
    
    nums = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x*y, nums, 1)
    

Without using high order function

    
    
    nums = [1, 2, 3, 4, 5]
    def multiply(nums):
        prod = 1
        for number in nums:
            prod *= number
        return prod
    product = multiply(nums)
    

While the first block uses fewer lines of code and is not that difficult to
understand, programmers with no background of functional programming will find
the second block of code much readable. Unless practicing proper functional
programming paradigm, passing one function to another function is not
appreciated, as it can reduce readability.

