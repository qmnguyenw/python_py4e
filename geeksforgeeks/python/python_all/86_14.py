Python – First Even Number in List



Sometimes, while working with lists, we can have a problem in which we need to
extract certain numbers occurring first time. This can also be even number.
This kind of problem is common in day-day and competitive programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we loop
through the list and when 1st time even number occurs, we store and break the
loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# First Even Number in List

# using loop

 

# Initializing list

test_list = [43, 9, 6, 72, 8, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# First Even Number in List

# using loop

res = None

for ele in test_list:

 if not ele % 2 :

 res = ele

 break

 

# printing result 

print ("The first even element in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [43, 9, 6, 72, 8, 11]
    The first even element in list is : 6
    

**Method #2 : Using binary search (Sorted list)**  
The binary search can also be employed on list when we have sorted list. In
this, we keep looking for smaller even term when we find one and move to rear
end in case we don’t find one.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# First Even Number in List

# using binary search

 

# Initializing list

test_list = [3, 7, 8, 9, 10, 15]

 

# printing original list

print("The original list is : " + str(test_list))

 

# First Even Number in List

# using binary search

res = len(test_list)

low = 0

high = len(test_list) - 1

while low <= high:

 mid = (low + high) // 2

 if test_list[mid] % 2:

 low = mid + 1

 else:

 res = test_list[mid]

 high = mid - 1

 

# printing result 

print ("The first even element in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 7, 8, 9, 10, 15]
    The first even element in list is : 8
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

