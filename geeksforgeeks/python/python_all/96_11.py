Python | Triple List Summation



There can be an application requirement to append elements of 2-3 lists to one
list and perform summation. This kind of application has a potential to come
into the domain of Machine Learning or sometimes in web development as well.
Let’s discuss certain ways in which this particular task can be performed.

 **Method #1 : Using + operator + sum()**  
This can be easily done using the plus operator as it does the element
addition at the back of list. Similar logic is extended in case of multiple
lists. The summation is performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Triple List Summation

# using + operator + sum()

 

# initializing lists

test_list1 = [1, 3, 5, 5, 4]

test_list2 = [4, 6, 2, 8, 10]

test_list3 = [7, 5, 2, 9, 11]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

print ("The original list 3 is : " + str(test_list3))

 

# using + operator + sum()

# Triple List Summation

test_list1 = sum(test_list1 + test_list2 + test_list3)

 

# printing result 

print ("The summed and modified list is : " + str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 5, 5, 4]
    The original list 2 is : [4, 6, 2, 8, 10]
    The original list 3 is : [7, 5, 2, 9, 11]
    The summed and modified list is : 82
    

**Method #2 : Usingitertools.chain() + sum()**  
The chain function can also be employed to perform this particular tasks as it
uses the iterator to perform this and hence offers a better performance over
the above method. The summation is performed using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Triple List Summation

# using itertools.chain() + sum()

from itertools import chain

 

# initializing lists

test_list1 = [1, 3, 5, 5, 4]

test_list2 = [4, 6, 2, 8, 10]

test_list3 = [7, 5, 2, 9, 11]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

print ("The original list 3 is : " + str(test_list3))

 

# using itertools.chain() + sum()

# Triple List Summation

test_list1 = sum(list(chain(test_list1, test_list2, test_list3)))

 

# printing result 

print ("The summed and modified list is : " + str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 5, 5, 4]
    The original list 2 is : [4, 6, 2, 8, 10]
    The original list 3 is : [7, 5, 2, 9, 11]
    The summed and modified list is : 82
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

