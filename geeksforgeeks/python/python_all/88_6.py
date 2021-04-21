Python – K Summation from Two lists



Sometimes, while working with Python lists we can have a problem in which we
need to find summation of lists taking elements from two different lists. This
kind of application can come in different domains such as web development.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This task can be done using loop in a brute force manner. We run a nested loop
one for each list and when we find a match we update the result list with the
pair.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Summation from Two lists

# using loop

 

# Initializing lists

test_list1 = [3, 2, 5]

test_list2 = [4, 3, 6, 8, 7]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 9

 

# K Summation from Two lists

# using loop

res = []

for idx in test_list1:

 val_req = K - idx

 for j in test_list2:

 if j == val_req:

 x, y = j, idx

 res.append((x, y))

 

# printing result 

print ("Summation pairs among lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [3, 2, 5]
    The original list 2 is : [4, 3, 6, 8, 7]
    Summation pairs among lists : [(6, 3), (7, 2), (4, 5)]
    

**Method #2 : Using list comprehension**  
This is yet another way in which this task can be performed. In this, we
perform similar task as above. The difference is that this is one liner and we
perform task in one line.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Summation from Two lists

# using list comprehension

 

# Initializing lists

test_list1 = [3, 2, 5]

test_list2 = [4, 3, 6, 8, 7]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing K 

K = 9

 

# K Summation from Two lists

# using list comprehension

res = [(a, b) for a in test_list1 for b in test_list2
if a + b == K]

 

# printing result 

print ("Summation pairs among lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [3, 2, 5]
    The original list 2 is : [4, 3, 6, 8, 7]
    Summation pairs among lists : [(6, 3), (7, 2), (4, 5)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

