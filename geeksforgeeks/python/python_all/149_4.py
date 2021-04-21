Python | Custom Multiplication in list of lists



Sometimes, when we are fed with the list of list, we need to multiply each of
its element list with a particular element fed by the order in the other list.
This particular problem is very specific but knowledge of it can be useful in
such cases. Let’s discuss certain ways in which this can be done.

 **Method #1 : Using loops**

This is the Naive and brute force method perform this particular task in which
we run a loop to get all the elements and it’s nested components and multiply
accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom Multiplication in list of lists

# Using loops

 

# initializing list

test_list = [[5, 6, 8], [7, 4, 3], [8,
10, 12]]

 

# initializing multiply list 

mult_list = [10, 20, 30]

 

# printing original list

print("The original list : " + str(test_list))

 

# printing multiply list

print("The original multiply list : " + str(mult_list))

 

# using loops

# Custom Multiplication in list of lists

res = [[] for idx in range(len(test_list))]

for i in range(len(test_list)):

 for j in range(len(mult_list)):

 res[i] += [mult_list[i] * test_list[i][j]]

 

# print result

print("The list after multiply : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[5, 6, 8], [7, 4, 3], [8, 10, 12]]
    The original multiply list : [10, 20, 30]
    The list after multiply : [[50, 60, 80], [140, 80, 60], [240, 300, 360]]
    

  

  

**Method #2 : Using list comprehension +enumerate()**

This problem can also be solved in a shorter way using the power of enumerate
function to get the indices and value of the container at one time. This is
one-liner approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Custom Multiplication in list of lists

# Using list comprehension + enumerate()

 

# initializing list

test_list = [[5, 6, 8], [7, 4, 3], [8,
10, 12]]

 

# initializing multiply list 

mult_list = [10, 20, 30]

 

# printing original list

print("The original list : " + str(test_list))

 

# printing multiply list

print("The original multiply list : " + str(mult_list))

 

# using list comprehension + enumerate()

# Custom Multiplication in list of lists

res = [[mult_list[i] * j for j in sub] 

 for i, sub in enumerate(test_list)]

 

# print result

print("The list after multiply : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[5, 6, 8], [7, 4, 3], [8, 10, 12]]
    The original multiply list : [10, 20, 30]
    The list after multiply : [[50, 60, 80], [140, 80, 60], [240, 300, 360]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

