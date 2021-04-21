Python | First occurrence of True number



Many times we require to find the first occurring non-zero number to begin the
processing with. This has mostly use case in Machine Learning domain in which
we require to process data excluding _None_ or _0 values_. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Usingnext() + enumerate()**  
The next function can be used to iterate through the list and enumerate along
with it checks for the list if the number is a non zero element and returns
the number of 0s before a True value i.e a non zero value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# finding first True value 

# using next() and enumerate()

 

# initializing list 

test_list = [ 0, 0, 5, 6, 0]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# finding first True value

# using next() and enumerate()

res = next((i for i, j in enumerate(test_list) if j),
None)

 

# printing result

print ("The values till first True value : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [0, 0, 5, 6, 0]
    The values till first True value : 2
    

  
**Method #2 : Usingfilter() + lamda + index()**  
Using the combination of the above functions, one can easily perform this
particular task. The filter function can be used to screen out the True
value that is processed by the lambda functions and index function returns the
first occurrence of this.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# finding first True value 

# using filter() + lamda + index()

 

# initializing list 

test_list = [ 0, 0, 5, 6, 0]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# finding first True value

# using filter() + lamda + index()

res = test_list.index(next(filter(lambda i: i != 0,
test_list)))

 

# printing result

print ("The values till first True value : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [0, 0, 5, 6, 0]
    The values till first True value : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

