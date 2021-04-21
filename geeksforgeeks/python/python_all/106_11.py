Python | True Record



Sometimes, while working with Python, we can have a problem in which we have a
record and we need to check if it contains all valid values. This kind of
problem is common in data preprocessing steps. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usingnot + any() + map() \+ lambda**  
Combination of above functions can be used to perform this task. In this, we
check for any element using any() and extension of logic is done by map()
and lambda.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# True Record

# using any() + map() + lambda + not

 

# initialize tuple

test_tup = (True, True, True, True)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# True Record

# using any() + map() + lambda + not 

res = not any(map(lambda ele: not ele, test_tup))

 

# printing result

print("Is Tuple True ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (True, True, True, True)
    Is Tuple True ? : True
    

**Method #2 : Usingall()**  
This checks for truthness of all elements of tuple using all(), returns True
if there is no False element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# True Record

# using all()

 

# initialize tuple

test_tup = (True, True, True, True)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# True Record

# using all()

res = all(test_tup)

 

# printing result

print("Is Tuple True ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (True, True, True, True)
    Is Tuple True ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

