Python – Pairs with Sum equal to K in tuple list



Sometimes, while working with data, we can have a problem in which we need to
find the sum of pairs of tuple list. And specifically the sum that is equal to
K. This kind of problem can be important in web development and competitive
programming. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This can be solved using loop. This is brute way in which this task is
performed. In this, we iterate the list for pair summation and retain whose
sum is K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pairs with Sum equal to K in tuple list

# using loop

 

# Initializing list

test_list = [(4, 5), (6, 7), (3, 6), (1,
2), (1, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 9

 

# Pairs with Sum equal to K in tuple list

# using loop

res = []

for ele in test_list:

 if ele[0] + ele[1] == K: 

 res.append(ele)

 

# printing result 

print ("List after extracting pairs equal to K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5), (6, 7), (3, 6), (1, 2), (1, 8)]
    List after extracting pairs equal to K : [(4, 5), (3, 6), (1, 8)]
    

**Method #2 : Using list comprehension**  
This is yet another way in which this task can be performed. In this, we
extract the elements in similar method as above, the difference is that we
perform this task as shorthand and in one line.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Pairs with Sum equal to K in tuple list

# using list comprehension

 

# Initializing list

test_list = [(4, 5), (6, 7), (3, 6), (1,
2), (1, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 9

 

# Pairs with Sum equal to K in tuple list

# using list comprehension

res = [(ele[0], ele[1]) for ele in test_list if
ele[0] + ele[1] == K]

 

# printing result 

print ("List after extracting pairs equal to K : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5), (6, 7), (3, 6), (1, 2), (1, 8)]
    List after extracting pairs equal to K : [(4, 5), (3, 6), (1, 8)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

