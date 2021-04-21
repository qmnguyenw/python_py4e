Python | Values till False element



Many a times we require to find the first occurring False number to begin the
processing with. This has mostly use case in Machine Learning domain in which
we require to process data excluding None or 0 values. Let’s discuss certain
ways in which this can be performed.

 **Method #1 : Usingnext() + enumerate()**  
The next function can be used to iterate through the list and enumerate along
with it checks for the list if the number is a False element and returns the
number of Truths before a False value i.e a zero value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Values till False element

# using next() and enumerate()

 

# initializing list 

test_list = [ 1, 5, 0, 0, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Values till False element

# using next() and enumerate()

res = next((i for i, j in enumerate(test_list) if not
j), None)

 

# printing result

print ("The values till first False value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 5, 0, 0, 6]
    The values till first False value : 2
    

**Method #2 : Usingfilter() + lamda + index()**  
Using the combination of the above functions one can easily perform this
particular task. The filter function can be used to screen out the False value
that is processed by the lambda functions and index function returns the first
occurrence of this.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Values till False element

# using filter() + lamda + index()

 

# initializing list 

test_list = [ 1, 5, 0, 0, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Values till False element

# using filter() + lamda + index()

res = test_list.index(next(filter(lambda i: i == 0,
test_list)))

 

# printing result

print ("The values till first False value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 5, 0, 0, 6]
    The values till first False value : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

