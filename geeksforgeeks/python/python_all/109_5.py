Python | Alternate front – rear Sum



While working with python, we usually come by many problems that we need to
solve in day-day and in development. Specially in development, small tasks of
python are desired to be performed in just one line. We discuss some ways to
compute a list consisting of elements that are alternate front-rear sum in the
list.

 **Method #1 : Using loop**  
This is brute force method in which this problem can be solved. In this, we
take two pointers and store their sum in array while increasing and decreasing
their positions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate front - rear Sum

# using loop

 

# initializing list 

test_list = [1, 4, 5, 3, 6, 7]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# Alternate front - rear Sum

# using loop

res = []

j = len(test_list) - 1

for i in range(0, len(test_list) // 2):

 res.append(test_list[i] + test_list[j])

 j = j - 1

 

# printing result

print ("The alterate front - rear Sum list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 3, 6, 7]
    The alterate front - rear Sum list is : [8, 10, 8]
    

**Method #2 : Using list comprehension**  
Naive method can be used to perform, but list comprehension provides a one
liner method to perform this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate front - rear Sum

# using list comprehension

 

# initializing list 

test_list = [1, 4, 5, 3, 6, 7]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# Alternate front - rear Sum

# using list comprehension

res = [test_list[i] + test_list[len(test_list) - (i +
1)] for i in range(len(test_list) // 2)]

 

# printing result

print ("The alterate front - rear Sum list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 3, 6, 7]
    The alterate front - rear Sum list is : [8, 10, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

