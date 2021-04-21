Create a tuple from string and list – Python



Sometimes, we can have a problem in which we need to construct a new container
with elements from different containers. This kind of problem can occur in
domains in which we use different types of data. Let’s discuss ways to convert
string and list data to tuple.

 **Method #1 : Using List conversion to tuple +tuple()**  
In this method, we convert the string to list and then append to target list
and then convert this result list to tuple using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct tuple from string and list

# using list conversion to tuple + tuple()

 

# initialize list and string 

test_list = ["gfg", "is"]

test_str = "best"

 

# printing original list and tuple

print("The original list : " + str(test_list))

print("The original string : " + test_str)

 

# Construct tuple from string and list

# using list conversion to tuple + tuple()

res = tuple(test_list + [test_str])

 

# printing result

print("The aggregated tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is']
    The original string : best
    The aggregated tuple is : ('gfg', 'is', 'best')
    

**Method #2 : Using Tuple conversion to tuple + tuple()**  
This is another way in which this task can be performed. In this, we convert
the string and list both to tuple and add them to result tuple. This method is
more efficient than the above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct tuple from string and list

# using tuple conversion to tuple + tuple()

 

# initialize list and string 

test_list = ["is", "best"]

test_str = "gfg"

 

# printing original list and tuple

print("The original list : " + str(test_list))

print("The original string : " + test_str)

 

# Construct tuple from string and list

# using tuple conversion to tuple + tuple()

res = (test_str, ) + tuple(test_list)

 

# printing result

print("The aggregated tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is']
    The original string : best
    The aggregated tuple is : ('gfg', 'is', 'best')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

