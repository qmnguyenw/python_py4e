Python | Indices of numbers greater than K



Many times we might have problem in which we need to find indices rather than
the actual numbers and more often, the result is conditioned. First approach
coming to mind can be a simple index function and get indices greater than
particular number, but this approach fails in case of duplicate numbers. Let’s
discuss certain ways in which this problem can be successfully solved.

 **Method #1 : Using loop**  
This problem can easily be solved using loop with a brute force approach in
which we can just check for the index as we iterate and append it in a new
list as we proceed forward.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# index of matching element using loop

 

# initializing list 

test_list = [12, 10, 18, 15, 8, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop

# index of matching element

res = []

for idx in range(0, len(test_list)) :

 if test_list[idx] > 10:

 res.append(idx)

 

# print result

print("The list of indices greater than 10 : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [12, 10, 18, 15, 8, 18]
    The list of indices greater than 10 : [0, 2, 3, 5]
    

**Method #2 : Using list comprehension +enumerate()**  
The combination of these two function can also perform this particular task
efficiently and in one line. The enumerate function is used to get element and
its index simultaneously.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# index of matching element

# using list comprehension + enumerate()

 

# initializing list 

test_list = [12, 10, 18, 15, 8, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + enumerate()

# index of matching element

res = [idx for idx, val in enumerate(test_list) if val >
10]

 

# print result

print("The list of indices greater than 10 : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [12, 10, 18, 15, 8, 18]
    The list of indices greater than 10 : [0, 2, 3, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

