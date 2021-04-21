Python | Element indices Summation



Usually, we require to find the sum of index, in which the particular value is
located. There are many method to achieve that, using index() etc. But
sometimes require to find all the indices of a particular value in case it has
multiple occurrences in list. Lets discuss certain ways to do so.

 **Method #1 : Naive Method + sum()**  
We can achieve this task by iterating through the list and check for that
value and just append the value index in new list and print that. This is the
basic brute force method to achieve this task. The sum() is used to perform
sum of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Element indices Summation

# using naive method + sum()

 

# initializing list 

test_list = [1, 3, 4, 3, 6, 7]

 

# printing initial list 

print ("Original list : " + str(test_list))

 

# using naive method

# Element indices Summation

# to find indices for 3

res_list = []

for i in range(0, len(test_list)) :

 if test_list[i] == 3 :

 res_list.append(i)

res = sum(res_list)

 

# printing resultant list 

print ("New indices summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [1, 3, 4, 3, 6, 7]
    New indices summation : 4
    

**Method #2 : Using list comprehension +sum()**  
List comprehension is just the shorthand technique to achieve the brute force
task, just uses lesser lines of codes to achieve the task and hence saves
programmers time. The sum() is used to perform sum of list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Element indices Summation

# using list comprehension + sum()

 

# initializing list 

test_list = [1, 3, 4, 3, 6, 7]

 

# printing initial list 

print ("Original list : " + str(test_list))

 

# using list comprehension + sum()

# Element indices Summation

# to find indices for 3

res_list = [i for i in range(len(test_list)) if
test_list[i] == 3]

res = sum(res_list)

 

# printing resultant list 

print ("New indices summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [1, 3, 4, 3, 6, 7]
    New indices summation : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

