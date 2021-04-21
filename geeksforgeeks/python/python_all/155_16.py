Python | Get match indices



Sometimes, while working with lists we need to handle two lists and search for
the matches, and return just the indices of the match. Querying the whole list
for this process is not feasible when the size of master list is very large,
hence having just the match indices helps in this cause. Let’s discuss certain
ways in which this can be achieved.

 **Method #1 : Using list comprehension +index()**  
This problem can potentially be solved using the index function of python to
get the wanted indices and list comprehension can be used to extend this to
the whole string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get match indices

# using list comprehension and index()

 

# initializing lists

test_list1 = [5, 4, 1, 3, 2]

test_list2 = [1, 2]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using list comprehension and index()

# Get match indices

res = [test_list1.index(i) for i in test_list2]

 

# print result

print("The Match indices list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [5, 4, 1, 3, 2]
    The original list 2 : [1, 2]
    The Match indices list is : [2, 4]
    

**Method #2 : Usingenumerate() \+ list comprehension**  
The enumerate function can be used to produce the key value pair for the list
being it’s index and value and we can store them using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get match indices

# using list comprehension and enumerate()

 

# initializing lists

test_list1 = [5, 4, 1, 3, 2]

test_list2 = [1, 2]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using list comprehension and enumerate()

# Get match indices

res = [key for key, val in enumerate(test_list1)

 if val in set(test_list2)]

 

# print result

print("The Match indices list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [5, 4, 1, 3, 2]
    The original list 2 : [1, 2]
    The Match indices list is : [2, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

