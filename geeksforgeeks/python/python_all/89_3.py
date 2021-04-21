Python – Reverse Row sort in Lists of List



Sometimes, while working with data, we can have a problem in which we need to
perform the sorting of rows of matrix in descending order. This kind of
problem has its application in web development and Data Science domain. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + sort() + reverse**  
This problem can be solved using a loop to loop over each row. The sort and
reverse can be used to perform reverse sort of rows.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse Row sort in Lists of List

# using loop

 

# initializing list 

test_list = [[4, 1, 6], [7, 8], [4, 10,
8]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Reverse Row sort in Lists of List

# using loop

for ele in test_list: 

 ele.sort(reverse = True) 

 

# printing result 

print ("The reverse sorted Matrix is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
    The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
    

**Method #2 : Using list comprehension +sorted()**  
This is yet another way in which this task can be performed. In this, we
perform in similar way, just pack the logic in one line using list
comprehension to provide a compact alternative.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse Row sort in Lists of List

# using list comprehension + sorted()

 

# initializing list 

test_list = [[4, 1, 6], [7, 8], [4, 10,
8]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Reverse Row sort in Lists of List

# using list comprehension + sorted()

res = [sorted(sub, reverse = True) for sub in
test_list]

 

# printing result 

print ("The reverse sorted Matrix is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
    The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

