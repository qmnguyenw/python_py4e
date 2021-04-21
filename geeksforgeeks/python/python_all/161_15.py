Python | Column deletion from list of lists



The problem of removing a row from a list is quite simple and we just need to
pop a list out of list of lists. But there can be a utility where we need to
delete a column i.e particular index element of each of the list. This is
problem that can occur if we store any database data into containers. Let’s
discuss certain ways in which this can be performed.

 **Method #1 : Usingdel + loop**  
In this strategy, we just delete the column element one by one using a loop to
iterate the row number at each of the iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# deleting columns of list of lists

# using del + loop

 

# initializing list 

test_list = [[4, 5, 6, 8],

 [2, 7, 10, 9],

 [12, 16, 18, 20]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using del + loop

# deleting column element of row

for j in test_list:

 del j[1]

 

# printing result 

print ("The modified mesh after column deletion : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [[4, 5, 6, 8], [2, 7, 10, 9], [12, 16, 18, 20]]  
> The modified mesh after column deletion : [[4, 6, 8], [2, 10, 9], [12, 18,
> 20]]

  

  

**Method #2 : Usingpop() + list comprehension**  
We can do this particular task in an easier and shorter way using the list
comprehension technique and using the pop function which can be used to remove
the list element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# deleting columns of list of lists

# using pop() + list comprehension

 

# initializing list 

test_list = [[4, 5, 6, 8],

 [2, 7, 10, 9],

 [12, 16, 18, 20]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using pop() + list comprehension

# deleting column element of row

[j.pop(1) for j in test_list]

 

# printing result 

print ("The modified mesh after column deletion : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [[4, 5, 6, 8], [2, 7, 10, 9], [12, 16, 18, 20]]  
> The modified mesh after column deletion : [[4, 6, 8], [2, 10, 9], [12, 18,
> 20]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

