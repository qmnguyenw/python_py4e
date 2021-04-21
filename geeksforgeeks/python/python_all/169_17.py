Python | Get first and last elements of a list



Sometimes, there might be a need to get the range between which a number lies
in the list, for such applications we require to get the first and last
element of the list. Let’s discuss certain ways to get the first and last
element of the list.  

 **Method #1 : Using list index**  
Using the list indices inside the master list can perform this particular
task. This is most naive method to achieve this particular task one can think
of.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get first and last element of list

# using list indexing

 

# initializing list 

test_list = [1, 5, 6, 7, 4]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list indexing

# to get first and last element of list

res = [ test_list[0], test_list[-1] ] 

 

# printing result

print ("The first and last element of list are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 5, 6, 7, 4]
    The first and last element of list are : [1, 4]
    

  
**Method #2 : Using List slicing**  
One can also make use of list slicing technique to perform the particular task
of getting first and last element. We can use step of whole list to skip to
the last element after the first element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get first and last element of list

# using List slicing

 

# initializing list 

test_list = [1, 5, 6, 7, 4]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using List slicing

# to get first and last element of list

res = test_list[::len(test_list)-1] 

 

# printing result

print ("The first and last element of list are : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [1, 5, 6, 7, 4]
    The first and last element of list are : [1, 4]
    

