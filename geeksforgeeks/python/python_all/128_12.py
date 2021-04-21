Python | Get Kth Column of Matrix



Sometimes, while working with Python Matrix, one can have a problem in which
one needs to find the Kth column of Matrix. This is a very popular problem in
Machine Learning Domain and having solution to this is useful. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension**  
This problem can be solved using list comprehension in which we can iterate
through all the rows and selectively gather all the elements occurring at Kth
index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get Kth Column of Matrix

# using list comprehension

 

# initialize list

test_list = [[4, 5, 6], [8, 1, 10], [7,
12, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K

K = 2

 

# Get Kth Column of Matrix

# using list comprehension

res = [sub[K] for sub in test_list]

 

# printing result

print("The Kth column of matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
    The Kth column of matrix is : [6, 10, 5]
    

**Method #2 : Usingzip()**  
This task can also be performed using zip(). This does the similar task of
gathering elements like is done by above list comprehension and offers compact
but slower execution. Works with Python2 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Get Kth Column of Matrix

# using zip()

 

# initialize list

test_list = [[4, 5, 6], [8, 1, 10], [7,
12, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K

K = 2

 

# Get Kth Column of Matrix

# using zip()

res = list(zip(*test_list)[K])

 

# printing result

print("The Kth column of matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
    The Kth column of matrix is : [6, 10, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

