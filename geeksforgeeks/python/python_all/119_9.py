Python | Compare tuples



Sometimes, while working with records, we can have a problem in which we need
to check if each element of one tuple is greater/smaller than it’s
corresponding index in other tuple. This can have many possible applications.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingall() + generator expression + zip()**  
The combination of above functionalities can be used to perform this task. In
this, we just compare all elements using all(). The cross tuple access is
done by zip() and generator expression gives us the logic to compare.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Comparing tuples

# using generator expression + all() + zip()

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (13, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Comparing tuples

# using generator expression + all() + zip()

res = all(x < y for x, y in zip(test_tup1, test_tup2))

 

# printing result

print("Are all elements in second tuple greater than first ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (13, 5, 18)
    Are all elements in second tuple greater than first ? : True
    

**Method #2 : Usingall() + map() \+ lambda**  
The combination of above functionalities can be used to perform this
particular task. In this, we perform extension of logic to each element using
map() and logic generation by lambda function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Comparing tuples

# using all() + lambda + map()

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (13, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Comparing tuples

# using all() + lambda + map()

res = all(map(lambda i, j: i < j, test_tup1, test_tup2))

 

# printing result

print("Are all elements in second tuple greater than first ? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (13, 5, 18)
    Are all elements in second tuple greater than first ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

