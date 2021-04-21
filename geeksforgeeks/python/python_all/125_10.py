Python | Sort lists in tuple



Sometimes, while working with Python tuples, we can have a problem in which we
need to sort the tuples which constitutes of lists and we need to sort each of
them. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingtuple() + sorted() \+ generator expression**  
This task can be performed using the combination of above functions. In this,
we iterate through each list using generator expression and perform the sort
operation using sorted().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort lists in tuple

# Using tuple() + sorted() + generator expression

 

# Initializing tuple

test_tup = ([7, 5, 4], [8, 2, 4], [0, 7,
5])

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# Sort lists in tuple

# Using tuple() + sorted() + generator expression

res = tuple((sorted(sub) for sub in test_tup))

 

# printing result

print("The tuple after sorting lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ([7, 5, 4], [8, 2, 4], [0, 7, 5])
    The tuple after sorting lists : ([4, 5, 7], [2, 4, 8], [0, 5, 7])
    

**Method #2 : Usingmap() + sorted()**  
This method performs the similar task as the above method, but it uses map()
to extend the logic to each element of tuple, the task performed by list
comprehension in above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort lists in tuple

# Using map() + sorted()

 

# Initializing tuple

test_tup = ([7, 5, 4], [8, 2, 4], [0, 7,
5])

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# Sort lists in tuple

# Using map() + sorted()

res = tuple(map(sorted, test_tup))

 

# printing result

print("The tuple after sorting lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ([7, 5, 4], [8, 2, 4], [0, 7, 5])
    The tuple after sorting lists : ([4, 5, 7], [2, 4, 8], [0, 5, 7])
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

