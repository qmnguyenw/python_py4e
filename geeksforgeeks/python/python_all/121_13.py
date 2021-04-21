Python | Check if two list of tuples are identical



Sometimes, while working with tuples, we can have a problem in which we have
list of tuples and we need to test if they are exactly identical. This is a
very basic problem and can occur in any domain. Let’s discuss certain ways in
which this task can be done.

 **Method #1 : Using == operator**  
This is the simplest and elegant way to perform this task. It also checks for
equality of tuple indices with one other.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if two list of tuples are identical

# using == operator

 

# initialize list of tuples 

test_list1 = [(10, 4), (2, 5)]

test_list2 = [(10, 4), (2, 5)]

 

# printing original tuples lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Check if two list of tuples are identical

# using == operator

res = test_list1 == test_list2

 

# printing result

print("Are tuple lists identical ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [(10, 4), (2, 5)]
    The original list 2 : [(10, 4), (2, 5)]
    Are tuple lists identical ? : True
    

**Method #2 : Usingcmp()**  
This inbuilt function, computes the difference of values of tuples. If they
are computed out to be 0, then it means that tuples are identical. Works only
with Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Check if two list of tuples are identical

# using cmp()

 

# initialize list of tuples 

test_list1 = [(10, 4), (2, 5)]

test_list2 = [(10, 4), (2, 5)]

 

# printing original tuples lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Check if two list of tuples are identical

# using cmp()

res = not cmp(test_list1, test_list2)

 

# printing result

print("Are tuple lists identical ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [(10, 4), (2, 5)]
    The original list 2 : [(10, 4), (2, 5)]
    Are tuple lists identical ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

