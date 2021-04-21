Python – False values Frequency



Checking a number/element by a condition is a common problem one faces and is
done in almost every program. Sometimes we also require to get the totals that
match the particular condition to have a distinguish which to not match for
further utilization like in data Science. Lets discuss certain ways in which
we can count False values.

 **Method #1 : Usingsum() \+ generator expression**  
This method uses the trick of adding 1 to the sum whenever the generator
expression returns true. By the time list gets exhausted, summation of count
of numbers matching a condition is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# False values Frequency

# using sum() + generator expression 

 

# initializing list 

test_list = [3, False, False, 6, False, 9] 

 

# printing original list 

print ("The original list is : " + str(test_list)) 

 

# using sum() + generator expression 

# False values Frequency

# checks for False

res = sum(1 for i in test_list if not i) 

 

# printing result 

print ("The number of False elements: " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [3, False, False, 6, False, 9]
    The number of False elements: 3
    

**Method #2 : Usingsum() + map()**  
map() does the task almost similar to the generator expression, difference is
just the internal data structure employed by it is different hence more
efficient.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# False values Frequency

# using sum()+ map() 

 

# initializing list 

test_list = [3, False, False, 6, False, 9] 

 

# printing original list 

print ("The original list is : " + str(test_list)) 

 

# using sum()+ map() 

# False values Frequency

# checks for False

res = sum(map(lambda i: not i, test_list)) 

 

# printing result 

print ("The number of False elements: " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [3, False, False, 6, False, 9]
    The number of False elements: 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

