Python – Every Kth index Maximum in List



We generally wish to employ a particular function to all the elements in a
list. But sometimes, according to requirement we would wish to employ a
particular functionality to certain elements of the list, basically to every
Kth element in list. Let’s discuss certain ways in which maximum of these
elements can be performed.

 **Method #1 : Using list comprehension +enumerate() + max()**  
The functionality of getting every Kth number of list can be done with the
help of list comprehension and enumerate function helps in the iteration of
the whole list. The max() helps to find max.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Every Kth index Maximum in List

# using list comprehension + enumerate() + max()

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using list comprehension + enumerate() + max()

# Every Kth index Maximum in List

# max of every 3rd element

res = max([i for j, i in enumerate(test_list) if j %
K == 0 ])

 

# printing result

print ("The max of every kth element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The max of every kth element : 9
    

**Method #2 : Using list comprehension + list slicing**  
Above mentioned functions can help to perform these tasks. The list
comprehension does the task of iteration in list and list slicing does the
extraction of every Kth element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# The max() helps to find max.

# using list comprehension + list slicing + max()

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using list comprehension + list slicing + max()

# Edit every Kth element in list 

# max of every 3rd element

res = max(test_list[0::3])

 

# printing result

print ("The max of every kth element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The max of every kth element : 9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

