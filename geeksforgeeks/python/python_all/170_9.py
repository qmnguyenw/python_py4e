Python | Initializing multiple lists



In real applications, we often have to work with multiple lists and to
initialize them with empty lists hampers the readability of code. Hence a one-
liner is required to perform this task in short so as to give a clear idea of
type and number of lists declared to be used.

 **Method #1 : Using * operator**  
We can enlist all the required list comma separated and then initialize them
with an empty list and multiply that empty list using the * operator by the
number of lists specified.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to initialize multiple lists

# using * operator

 

# using * operator

# to initialize multiple lists

list1, list2, list3, list4 = ([], ) * 4

 

# printing lists

print ("The initialized lists are : ")

print ("List 1 : " + str(list1))

print ("List 2 : " + str(list2))

print ("List 3 : " + str(list3))

print ("List 4 : " + str(list4))  
  
---  
  
 __

 __

 **Output:**

    
    
    The initialized lists are : 
    List 1 : []
    List 2 : []
    List 3 : []
    List 4 : []
    

  
**Method #2 : Using loop**  
This method is similar to the method explained above but the only difference
is that we use loop instead of * operator to perform the task of multiple
assignments.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to initialize multiple lists

# using loop

 

# using loop

# to initialize multiple lists

list1, list2, list3, list4 = ([] for i in range(4))

 

# printing lists

print ("The initialized lists are : ")

print ("List 1 : " + str(list1))

print ("List 2 : " + str(list2))

print ("List 3 : " + str(list3))

print ("List 4 : " + str(list4))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The initialized lists are : 
    List 1 : []
    List 2 : []
    List 3 : []
    List 4 : []
    

