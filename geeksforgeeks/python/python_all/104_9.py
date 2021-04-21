Python program to input a comma separated string



Given an input string that is comma-separated instead of space. The task is to
store this input string in a list or variables. This can be achieved in Python
using two ways:

  *  **Using List comprehension andsplit()**
  *  **Usingmap() and split()**

 **Method 1:** Using List comprehension and split()

split() function helps in getting multiple inputs from the user. It breaks
the given input by the specified separator. If the separator is not provided
then any white space is used as a separator. Generally, users use a split()
method to split a Python string but one can also use it in taking multiple
inputs.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to take a comma

# separated string as input

 

 

# Taking input when the numbers 

# of input are known and storing

# in different variables

 

# Taking 2 inputs

a, b = [int(x) for x in input("Enter two
values\n").split(', ')]

print("\nThe value of a is {} and b is {}".format(a, b))

 

# Taking 3 inputs

a, b, c = [int(x) for x in input("Enter three
values\n").split(', ')]

print("\nThe value of a is {}, b is {} and c is {}".format(a, b,
c))

 

# Taking multiple inputs

L = [int(x) for x in input("Enter multiple
values\n").split(', ')]

print("\nThe values of input are", L)   
  
---  
  
__

__

**Output:**

  

  

    
    
    Enter two values
    1, 2
    
    The value of a is 1 and b is 2
    Enter three values
    1, 2, 3
    
    The value of a is 1, b is 2 and c is 3
    Enter multiple values
    1, 22, 34, 6, 88, 2
    
    The values of input are [1, 22, 34, 6, 88, 2]
    

**Method 2:** Using map() and split()

map() function returns a list of the results after applying the given
function to each item of a given iterable (list, tuple etc.)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to take a comma

# separated string as input

 

 

# Taking input when the numbers 

# of input are known and storing

# in different variables

 

# Taking 2 inputs

a, b = map(int, input("Enter two values\n").split(',
'))

print("\nThe value of a is {} and b is {}".format(a, b))

 

# Taking 3 inputs

a, b, c = map(int, input("Enter three values\n").split(',
'))

print("\nThe value of a is {}, b is {} and c is {}".format(a, b,
c))

 

# Taking multiple inputs

L = list(map(int, input("Enter multiple
values\n").split(', ')))

print("\nThe values of input are", L)  
  
---  
  
 __

 __

 **Output:**

    
    
    Enter two values
    1, 2
    
    The value of a is 1 and b is 2
    Enter three values
    1, 2, 3
    
    The value of a is 1, b is 2 and c is 3
    Enter multiple values
    1, 2, 3, 4
    
    The values of input are [1, 2, 3, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

