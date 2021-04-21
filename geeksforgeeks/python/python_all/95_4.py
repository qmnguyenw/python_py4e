Python | Check for Descending Sorted List



The sorted operation of list is essential operation in many application. But
it takes best of O(nlogn) time complexity, hence one hopes to avoid this. So,
to check if this is required or not, knowing if list is by default reverse
sorted or not, one can check if list is sorted or not. Lets discuss various
ways this can be achieved.

 **Method #1 : Naive method**  
The simplest way to check this is run a loop for first element and check if we
could find any larger element than it after that element, if yes, the list is
not reverse sorted.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check for Descending Sorted List

# using naive method 

 

# initializing list

test_list = [10, 8, 4, 3, 1]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using naive method to 

# Check for Descending Sorted List

flag = 0

i = 1

while i < len(test_list):

 if(test_list[i] > test_list[i - 1]):

 flag = 1

 i += 1

 

# printing result

if (not flag) :

 print ("Yes, List is reverse sorted.")

else :

 print ("No, List is not reverse sorted.")  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [10, 8, 4, 3, 1]
    Yes, List is reverse sorted.
    

**Method #2 : Usingsort() \+ reverse**  
The new list can be made as a copy of the original list, sorting the new list
and comparing with the old list will give us the result if sorting was
required to get reverse sorted list or not.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check for Descending Sorted List

# using sort() + reverse

 

# initializing list

test_list = [10, 5, 4, 3, 1]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using sort() + reverse to 

# Check for Descending Sorted List

flag = 0

test_list1 = test_list[:]

test_list1.sort(reverse = True)

if (test_list1 == test_list):

 flag = 1

 

# printing result

if (flag) :

 print ("Yes, List is reverse sorted.")

else :

 print ("No, List is not reverse sorted.")  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [10, 8, 4, 3, 1]
    Yes, List is reverse sorted.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

