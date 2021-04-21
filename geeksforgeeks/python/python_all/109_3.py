Python – Match Kth number digit in list elements



Sometimes we may face a problem in which we need to find for a list if it
contains numbers at Kth index with the same digits. This particular utility
has an application in day-day programming. Let’s discuss certain ways in which
this task can be achieved.

 **Method #1 : Using list comprehension +map()**  
We can approach this problem by converting the elements to the strings and
then testing the Kth element of string and if they are equal we can return
true and then convert to set and test for size of result to be one. The
conversion is done by map, set function converts to set and list comprehension
checks for Kth element of string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Kth Number digit match

# using list comprehension + map()

 

# initializing list 

test_list = [467, 565, 2645, 8668]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 1

 

# using list comprehension + map()

# Kth Number digit match

res = len(set(sub[K] for sub in map(str, test_list)))
== 1

 

# print result

print("Does each element of index K have same digit ? " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [467, 565, 2645, 8668]
    Does each element of index K have same digit ? True
    

**Method #2 : Usingall() \+ list comprehension**  
This is yet another approach in which this problem can be solved. In this we
use all function to check for all elements and return a Boolean result and
list comprehension does the part of conversion of string by str function and
checking for all elements with the Kth digit of Kth element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Kth Number digit match

# using list comprehension + all()

 

# initializing list 

test_list = [467, 565, 2645, 8668]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 1

 

# using list comprehension + all()

# Kth Number digit match

res = all(str(i)[K] == str(test_list[K])[K] for i in
test_list)

 

# print result

print("Does each element of index K have same digit ? " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [467, 565, 2645, 8668]
    Does each element of index K have same digit ? True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

