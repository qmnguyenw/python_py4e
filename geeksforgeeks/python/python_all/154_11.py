Python | Matrix creation of n*n



Many times while working with numbers in data science we come across the
problem in which we need to work with data science we need to transform a
number to a matrix of consecutive numbers and hence this problem has a good
application. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension**  
List comprehension can be used to accomplish this particular task by using the
range function for each list that needs to be constructed consecutively.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# matrix creation of n * n

# using list comprehension

 

# initializing N

N = 4

 

# printing dimension

print("The dimension : " + str(N))

 

# using list comprehension

# matrix creation of n * n

res = [list(range(1 + N * i, 1 + N * (i +
1)))

 for i in range(N)]

 

# print result

print("The created matrix of N * N: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The dimension : 4
    The created matrix of N*N: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    

**Method #2 : Usingnext() + itertools.count()**  
The count function can be used start the count of numbers and next function
does the task of creation of sublist consecutively. List comprehension handles
the processing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# matrix creation of n * n

# using next() + itertools.count()

import itertools

 

# initializing N

N = 4

 

# printing dimension

print("The dimension : " + str(N))

 

# using next() + itertools.count()

# matrix creation of n * n

temp = itertools.count(1) 

res = [[next(temp) for i in range(N)] for i in
range(N)]

 

# print result

print("The created matrix of N * N: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The dimension : 4
    The created matrix of N*N: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

