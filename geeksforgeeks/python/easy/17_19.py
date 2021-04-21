Python | Perform append at beginning of list



The usual append operation of Python list adds the new element at the end of
the list. But in certain situations, we need to append each element we add in
front of list. If we perform brute force techniques, we need to perform
unnecessary shifts of elements and hence, having shorthands for it is useful.

Let’s discuss certain ways to perform append at beginning of the list.

 **Method #1 : Usinginsert()**

This method generally inserts the element at any position in the list and also
performs the necessary shifts required internally and hence can also be used
to perform this very task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to add element at beginning

# using insert()

 

# initializing list 

test_list = [1, 3, 4, 5, 7]

 

# printing initial list 

print ("Original list : " + str(test_list))

 

# using insert() to append

# at beginning. append 6

test_list.insert(0, 6)

 

# printing resultant list 

print ("Resultant list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Original list : [1, 3, 4, 5, 7]
    Resultant list is : [6, 1, 3, 4, 5, 7]
    

