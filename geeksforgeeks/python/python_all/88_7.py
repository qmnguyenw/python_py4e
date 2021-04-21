Python – Matrix Custom Multiplier



Sometimes, while working with data, we can have a problem in which we need to
multiply each row of matrix with a different multiplier. This kind of
application is important in data science domain. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop +zip()**  
The combination of above functions can be used to perform this task. In this,
we iterate through each row and perform the task of multiplication using
zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix Custom Multiplier

# using loop + zip()

 

# Initializing list

test_list1 = [[1, 3], [5, 6], [8, 9]]

test_list2 = [4, 3, 6]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Matrix Custom Multiplier

# using loop + zip()

res = []

for mul, sub in zip(test_list2, test_list1):

 temp = []

 for ele in sub:

 temp.append(mul * ele)

 res.append(temp)

 

# printing result 

print ("Matrix after custom multiplication : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [[1, 3], [5, 6], [8, 9]]
    The original list 2 is : [4, 3, 6]
    Matrix after custom multiplication : [[4, 12], [15, 18], [48, 54]]
    

**Method #2 : Using list comprehension +zip()**  
The combination of above methods can be used to solve this problem. In this,
we just iterate through the list and perform the task of multiplication in one
liner.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Matrix Custom Multiplier

# using list comprehension + zip()

 

# Initializing list

test_list1 = [[1, 3], [5, 6], [8, 9]]

test_list2 = [4, 3, 6]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Matrix Custom Multiplier

# using list comprehension + zip()

res = [[mul * ele for ele in sub] for mul, sub in
zip(test_list2, test_list1)]

 

# printing result 

print ("Matrix after custom multiplication : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [[1, 3], [5, 6], [8, 9]]
    The original list 2 is : [4, 3, 6]
    Matrix after custom multiplication : [[4, 12], [15, 18], [48, 54]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

