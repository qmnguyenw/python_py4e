Python | Alternate range slicing in list



List slicing is quite common utility in Python, one can easily slice certain
elements from a list, but sometimes, we need to perform that task in non-
contiguous manner and slice alternate ranges. Let’s discuss how this
particular problem can be solved.

 **Method #1 : Using list comprehension**  
List comprehension can be used to perform this particular task with ease as it
can be used to run a loop and only filter the elements that leave a remainder
more than half of target slice size _multiplied by 2_. By this way we can
extract the sliced numbers in range alternatively.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# alternate range slicing 

# using list comprehension

 

# initializing list 

test_list = [2, 4, 6, 8, 9, 10, 12, 16,
18, 20, 7, 30]

 

# printing original list

print("The original list : " + str(test_list))

 

# Select range size 

N = 3

 

# using list comprehension

# alternate range slicing

res = [test_list[i] for i in range(len(test_list)) 

 if i % (N * 2) >= N]

 

# print result

print("The alternate range sliced list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [2, 4, 6, 8, 9, 10, 12, 16, 18, 20, 7, 30]
    The alternate range sliced list : [8, 9, 10, 20, 7, 30]
    

**Method #2 : Usingenumerate() \+ list comprehension**  
The list comprehension can also be combined with the enumerate function to
perform this task. The advantage of using enumerate is that we can track of
index along with the value and it’s more efficient and has lesser run-time
than the above function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# alternate range slicing 

# using list comprehension + enumerate()

 

# initializing list 

test_list = [2, 4, 6, 8, 9, 10, 12, 16,
18, 20, 7, 30]

 

# printing original list

print("The original list : " + str(test_list))

 

# Select range size 

N = 3

 

# using list comprehension + enumerate()

# alternate range slicing

res = [val for i, val in enumerate(test_list)

 if i % (N * 2) >= N]

 

# print result

print("The alternate range sliced list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [2, 4, 6, 8, 9, 10, 12, 16, 18, 20, 7, 30]
    The alternate range sliced list : [8, 9, 10, 20, 7, 30]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

