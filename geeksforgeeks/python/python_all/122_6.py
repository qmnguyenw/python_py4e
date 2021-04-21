Python | Find overlapping tuples from list



Sometimes, while working with tuple data, we can have a problem in which we
may need to get the tuples which overlap a certain tuple. This kind of problem
can occur in Mathematics domain while working with Geometry. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using loop**  
In this method, we extract the pairs with overlap using conditional statements
and append the suitable match into list keeping records.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Find overlapping tuples from list

# using loop 

 

# initialize list

test_list = [(4, 6), (3, 7), (7, 10), (5,
6)]

 

# initialize test tuple 

test_tup = (1, 5)

 

# printing original list

print("The original list : " + str(test_list))

 

# Find overlapping tuples from list

# using loop 

res = []

for tup in test_list:

 if(tup[1]>= test_tup[0] and tup[0]<=
test_tup[1]):

 res.append(tup)

 

# printing result

print("The tuple elements that overlap the argument tuple is : "

 + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(4, 6), (3, 7), (7, 10), (5, 6)]  
> The tuple elements that overlap the argument tuple is : [(4, 6), (3, 7), (5,
> 6)]

  

  

**Method #2 : Using list comprehension**  
This task can also be achieved using list comprehension functionality. This
method is similar to the above one, just packed in one-liner for use as a
shorthand.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Find overlapping tuples from list

# Using list comprehension

 

# initialize list

test_list = [(4, 6), (3, 7), (7, 10), (5,
6)]

 

# initialize test tuple 

test_tup = (1, 5)

 

# printing original list

print("The original list : " + str(test_list))

 

# Find overlapping tuples from list

# Using list comprehension

res = [(idx[0], idx[1]) for idx in test_list\

 if idx[0] >= test_tup[0] and idx[0] <=
test_tup[1]\

 or idx[1] >= test_tup[0] and idx[1] <=
test_tup[1]]

 

# printing result

print("The tuple elements that overlap the argument tuple is : "

 + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(4, 6), (3, 7), (7, 10), (5, 6)]  
> The tuple elements that overlap the argument tuple is : [(4, 6), (3, 7), (5,
> 6)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

