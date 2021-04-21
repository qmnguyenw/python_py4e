Python – Suffix List Sum



Nowdays, especially in the field of competitive programming, the utility of
computing suffix sum is quite popular and features in many problems. Hence,
having a one liner solution to it would possess a great help. Let’s discuss
certain way in which this problem can be solved.

 **Method : Using list comprehension +sum() \+ list slicing**  
This problem can be solved using the combination of above two functions in
which we use list comprehension to extend logic to each element, sum function
to get the sum along, slicing is used to get sum till the particular index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Suffix List Sum 

# using list comprehension + sum() + list slicing 

 

# initializing list

test_list = [3, 4, 1, 7, 9, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + sum() + list slicing

# Suffix List Sum 

test_list.reverse()

res = [sum(test_list[ : i + 1 ]) for i in
range(len(test_list))]

 

# print result

print("The suffix sum list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 1]
    The suffix sum list is : [1, 10, 17, 18, 22, 25]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

