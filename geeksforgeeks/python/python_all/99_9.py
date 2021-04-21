Python | Above K elements summation



Many times we might have problem in which we need to find summation rather
than the actual numbers and more often, the result is conditioned.. Let’s
discuss certain ways in which this problem can be successfully solved.

 **Method #1 : Using loop**  
This problem can easily be solved using loop with a brute force approach in
which we can just check for the sum as we iterate and append it in a new list
as we proceed forward.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Above K elements summation

# using loop

 

# initializing list 

test_list = [12, 10, 18, 15, 8, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop

# Above K elements summation

res = 0

for idx in range(0, len(test_list)) :

 if test_list[idx] > 10:

 res += test_list[idx]

 

# print result

print("The summation of elements greater than 10 : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [12, 10, 18, 15, 8, 18]
    The summation of elements greater than 10 : 63
    

**Method #2 : Using list comprehension +sum()**  
The combination of these two function can also perform this particular task
efficiently and in one line. The sum function is used to perform summation of
elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Above K elements summation

# using list comprehension + sum()

 

# initializing list 

test_list = [12, 10, 18, 15, 8, 18]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + sum()

# index of matching element

res = sum(ele for ele in test_list if ele > 10)

 

# print result

print("The summation of elements greater than 10 : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [12, 10, 18, 15, 8, 18]
    The summation of elements greater than 10 : 63
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

