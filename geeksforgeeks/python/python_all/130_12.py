Python | Shift sublist in list



Sometimes, while working with list, we can have a problem in which we need to
shift some sublist to desired index in same sublist. This problem can occur in
day-day programming. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Usinginsert() + pop() \+ loop**  
The combination of above functions can be used to perform the particular task.
The pop function can be used to remove the sublist and insert function
inserts the sublist. This happens for each element in single iteration in
loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Shift sublist in list

# Using insert() + pop() + loop

 

# function to perform the task 

def shift_sublist(test_list, strt_idx, no_ele, shft_idx):

 for ele in range(no_ele):

 test_list.insert(shft_idx + 1, test_list.pop(strt_idx))

 return test_list

 

# initializing list

test_list = [4, 5, 6, 7, 3, 8, 10, 1,
12, 15, 16]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using insert() + pop() + loop

# Shift sublist in list

res = shift_sublist(test_list, 2, 3, 6)

 

# Printing result

print("The list after shift of sublist : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [4, 5, 6, 7, 3, 8, 10, 1, 12, 15, 16]  
> The list after shift of sublist : [4, 5, 8, 10, 1, 6, 7, 3, 12, 15, 16]

  

  

**Method #2 : Using list slicing**  
This task can also be using list slicing technique in which one can just add
the different sections of list at required positions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Shift sublist in list

# Using list slicing

 

# function to perform the task 

def shift_sublist(test_list, strt_idx, no_ele, shft_idx):

 return (test_list[:strt_idx] + test_list[strt_idx + no_ele :
no_ele + shft_idx - 1]

 + test_list[strt_idx : strt_idx + no_ele] + test_list[shft_idx
+ no_ele -1:])

 

# initializing list

test_list = [4, 5, 6, 7, 3, 8, 10, 1,
12, 15, 16]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using list slicing

# Shift sublist in list

res = shift_sublist(test_list, 2, 3, 6)

 

# Printing result

print("The list after shift of sublist : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 7, 3, 8, 10, 1, 12, 15, 16]
    The list after shift of sublist : [4, 5, 8, 10, 1, 6, 7, 3, 12, 15, 16]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

