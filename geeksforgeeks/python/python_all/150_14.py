Python | Delete elements with frequency atmost K



There are many methods that can be employed to perform the deletion in the
list. Be it remove function, pop function and many other functions. But most
of the times, we usually don’t deal with the simple deletion, but with certain
constraints. This article discusses certain ways in which we can delete only
those elements which occurs less than K times.

 **Method #1 : Using list comprehension +count()**  
The idea applied here is to construct a new list using list comprehension and
insert only those elements which occur more than K times. The count operation
is done with the help of count function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# remove elements less than and equal K 

# using list comprehension + count()

 

# initializing list

test_list = [1, 4, 3, 2, 3, 3, 2, 2,
2, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K

K = 2

 

# using list comprehension + count()

# remove elements less than K 

res = [ i for i in test_list if test_list.count(i) > K]

 

# print result

print("The list removing elements less than and equal K : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 4, 3, 2, 3, 3, 2, 2, 2, 1]
    The list removing elements less than and equal K  : [3, 2, 3, 3, 2, 2, 2]
    

**Method #2 : UsingCounter() \+ list comprehension**  
This problem can be efficiently solved using the Counter function that
precomputes the count of each elements in list so that the decision to keep or
reject a particular element takes lesser time.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# remove elements less than and equal K 

# using Counter() + list comprehension

from collections import Counter

 

# initializing list

test_list = [1, 4, 3, 2, 3, 3, 2, 2,
2, 1]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K

K = 2

 

# using Counter() + list comprehension

# remove elements less than K 

freq = Counter(test_list)

res = [ele for ele in test_list if freq[ele] > K]

 

# print result

print("The list removing elements less than and equal K : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 4, 3, 2, 3, 3, 2, 2, 2, 1]
    The list removing elements less than and equal K  : [3, 2, 3, 3, 2, 2, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

