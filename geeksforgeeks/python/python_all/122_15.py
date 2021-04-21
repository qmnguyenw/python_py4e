Python | Conversion to N*N tuple matrix



Sometimes, while working with data, we can have a problem in which we have
data in form of tuple Matrix with uneven length rows. In this case there’s a
requirement to complete the N*N matrix with a default value. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using loop +* operator**  
This problem can be solved using loop. This is brute force method to perform
this task. We just append the default value as many times, as the data is
missing in a row than N.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Conversion to N * N tuple matrix 

# using loop + * operator

 

# initialize tuple

test_tup = ((5, 4), (3, ), (1, 5, 6, 7),
(2, 4, 5))

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# initializing dimension

N = 4

 

# Conversion to N * N tuple matrix 

# using loop + * operator

res = []

for tup in test_tup :

 res.append( tup +(0, ) * (N - len(tup)))

 

# printing result

print("Tuple after filling values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ((5, 4), (3, ), (1, 5, 6, 7), (2, 4, 5))
    Tuple after filling values : [(5, 4, 0, 0), (3, 0, 0, 0), (1, 5, 6, 7), (2, 4, 5, 0)]
    

**Method #2 : Using tuple() \+ generator expression**  
Similar task can be performed in one line using generator expression. In this,
similar logic is applied as above just zipped as one-liner. The tuple(),
changes result to tuple.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Conversion to N * N tuple matrix 

# using tuple() + generator expression

 

# initialize tuple

test_tup = ((5, 4), (3, ), (1, 5, 6, 7),
(2, 4, 5))

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# initializing dimension

N = 4

 

# Conversion to N * N tuple matrix 

# using tuple() + generator expression

res = tuple(sub + (0, ) * (N-len(sub)) for sub
in test_tup)

 

# printing result

print("Tuple after filling values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ((5, 4), (3, ), (1, 5, 6, 7), (2, 4, 5))
    Tuple after filling values : ((5, 4, 0, 0), (3, 0, 0, 0), (1, 5, 6, 7), (2, 4, 5, 0))
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

