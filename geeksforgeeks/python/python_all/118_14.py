Python | Convert Tuple to integer



Sometimes, while working with records, we can have a problem in which we need
to convert the data records to integer by joining them. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingreduce() \+ lambda**  
The combination of above functions can be used to perform this task. In this,
we use lambda function to perform logic of conversion and reduce performs task
of iteration and combining result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple to integer

# Using reduce() + lambda

import functools

 

# initialize tuple

test_tuple = (1, 4, 5)

 

# printing original tuple 

print("The original tuple : " + str(test_tuple))

 

# Convert Tuple to integer

# Using reduce() + lambda

res = functools.reduce(lambda sub, ele: sub * 10 + ele,
test_tuple)

 

# printing result

print("Tuple to integer conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 4, 5)
    Tuple to integer conversion : 145
    

**Method #2 : Usingint() + join() + map()**  
The combination of these functions can also be used to perform this task. In
this, we convert each element to string using join() and iterate using map().
At last we perform integer conversion.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuple to integer

# Using int() + join() + map()

 

# initialize tuple

test_tuple = (1, 4, 5)

 

# printing original tuple 

print("The original tuple : " + str(test_tuple))

 

# Convert Tuple to integer

# Using int() + join() + map()

res = int(''.join(map(str, test_tuple)))

 

# printing result

print("Tuple to integer conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 4, 5)
    Tuple to integer conversion : 145
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

