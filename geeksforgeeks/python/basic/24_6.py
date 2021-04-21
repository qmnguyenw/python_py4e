sum() function in Python



Sum of numbers in the list is required everywhere. Python provide an inbuilt
function sum() which sums up the numbers in the list.  
 **  
Syntax:**

    
    
    **sum(iterable, start)**
    **iterable :** iterable can be anything list , tuples or dictionaries ,
     but most importantly it should be numbers.
    **start** : this start is added to the sum of 
    numbers in the iterable. 
    If start is not given in the syntax , it is assumed to be 0.

 **Possible two syntaxes:**

    
    
     **sum(a)**
    a is the list , it adds up all the numbers in the 
    list a and takes start to be 0, so returning 
    only the sum of the numbers in the list.
    **sum(a, start)**
    this returns the sum of the list + start 
    

Below is the Python implementation of the sum()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# sum()

 

numbers = [1,2,3,4,5,1,4,5]

 

# start parameter is not provided

Sum = sum(numbers)

print(Sum)

 

# start = 10

Sum = sum(numbers, 10)

print(Sum)  
  
---  
  
 __

 __

Output:

    
    
    25
    35
    

**Error and Exceptions**

  

  

 **TypeError :** This error is raised in the case when there is anything other
then numbers in the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the exception of

# sum()

arr = ["a"]

 

# start parameter is not provided

Sum = sum(arr)

print(Sum)

 

# start = 10

Sum = sum(arr, 10)

print(Sum)  
  
---  
  
 __

 __

Runtime Error :

    
    
    Traceback (most recent call last):
      File "/home/23f0f6c9e022aa96d6c560a7eb4cf387.py", line 6, in 
        Sum = sum(arr)
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    

**So the list should contain numbers**

 **Practical Application:** Problems where we require sum to be calculated to
do further operations such as finding out the average of numbers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the practical application

# of sum()

 

numbers = [1,2,3,4,5,1,4,5]

 

# start = 10

Sum = sum(numbers)

average= Sum/len(numbers) 

print (average)  
  
---  
  
 __

 __

Output:

    
    
    3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

