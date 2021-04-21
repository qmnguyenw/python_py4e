Python | Chuncked summation every K value



The prefix array is quite famous in the programming world. This article would
discuss a variation of this scheme. This deals with the cumulative list sum
till a K value, and again starts cumulation of sum from occurrence of K value.
Let’s discuss certain way in which this can be performed.

 **Method #1 : Using Naive Method**  
In the naive method, we just construct the new list comprising of the the sum
of prev. value of list until K and restarts the procedure once a non K value
is encountered.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Chuncked summation every K value

# using naive method 

 

# initializing list of lists

test_list = [1, 3, 4, 10, 4, 5, 10, 7,
8]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 10

 

# Chuncked summation every K value

# using naive method

for i in range(1, len(test_list)):

 if test_list[i]: 

 test_list[i] += test_list[i - 1]

 else:

 test_list[i] = 0

 

# printing result

print ("The computed modified new list : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 4, 10, 4, 5, 10, 7, 8]
    The computed modified new list : [1, 4, 8, 18, 22, 27, 37, 44, 52]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

