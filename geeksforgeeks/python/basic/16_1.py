Python – Ways to remove duplicates from list



This article focuses on one of the operations of getting the unique list from
a list that contains a possible duplicated. Remove duplicates from list
operation has large number of applications and hence, it’s knowledge is good
to have.  

 **Method 1 : Naive method**  
In naive method, we simply traverse the list and append the first occurrence
of the element in new list and ignore all the other occurrences of that
particular element.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# removing duplicated from list 

# using naive methods 

 

# initializing list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using naive method

# to remove duplicated 

# from list 

res = []

for i in test_list:

 if i not in res:

 res.append(i)

 

# printing list after removal 

print ("The list after removing duplicates : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    The list after removing duplicates : [1, 3, 5, 6]
    

**Method 2 : Using list comprehension**  
This method has working similar to the above method, but this is just a one-
liner shorthand of longer method done with the help of list comprehension.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# removing duplicated from list 

# using list comprehension

 

# initializing list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using list comprehension

# to remove duplicated 

# from list 

res = []

[res.append(x) for x in test_list if x not in res]

 

# printing list after removal 

print ("The list after removing duplicates : " + str(res))  
  
---  
  
 __

 __

Output :

  

  

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    The list after removing duplicates : [1, 3, 5, 6]
    

**Method 3 : Using set()**  
This is the most popular way by which the duplicated are removed from the
list. But the main and notable drawback of this approach is that the ordering
of the element is lost in this particular method.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# removing duplicated from list 

# using set()

 

# initializing list

test_list = [1, 5, 3, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using set()

# to remove duplicated 

# from list 

test_list = list(set(test_list))

 

# printing list after removal 

# distorted ordering

print ("The list after removing duplicates : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 5, 3, 6, 3, 5, 6, 1]
    The list after removing duplicates : [1, 3, 5, 6]
    

**Method 4 : Using list comprehension +enumerate()**  
list comprehension coupled with enumerate function can also achieve this task.
It basically looks for already occurred elements and skips adding them. It
preserves the list ordering.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# removing duplicated from list 

# using list comprehension + enumerate()

 

# initializing list

test_list = [1, 5, 3, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using list comprehension + enumerate()

# to remove duplicated 

# from list 

res = [i for n, i in enumerate(test_list) if i not in
test_list[:n]]

 

# printing list after removal 

print ("The list after removing duplicates : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 5, 3, 6, 3, 5, 6, 1]
    The list after removing duplicates : [1, 5, 3, 6]
    

**Method 5 : Usingcollections.OrderedDict.fromkeys()**  
This is fastest method to achieve the particular task. It first removes the
duplicates and returns a dictionary which has to be converted to list. This
works well in case of strings also.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# removing duplicated from list 

# using collections.OrderedDict.fromkeys()

from collections import OrderedDict

 

# initializing list

test_list = [1, 5, 3, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using collections.OrderedDict.fromkeys()

# to remove duplicated 

# from list 

res = list(OrderedDict.fromkeys(test_list))

 

# printing list after removal 

print ("The list after removing duplicates : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 5, 3, 6, 3, 5, 6, 1]
    The list after removing duplicates : [1, 5, 3, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

