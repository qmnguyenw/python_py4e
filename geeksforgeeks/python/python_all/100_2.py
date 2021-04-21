Python – Non-None elements indices



Many times while working in data science domain we need to get the list of all
the indices which are Non None, so that they can be easily be prepossessed.
This is quite a popular problem and solution to it comes quite handy. Let’s
discuss certain ways in which this can be done.

 **Method #1 : Using list comprehension +range()**  
In this method we just check for each index using the range function and store
the index if we find that index is Not None.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Non-None elements indices

# using list comprehension + enumerate

 

# initializing list 

test_list = [1, None, 4, None, None, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + enumerate

# Non-None elements indices 

res = [i for i in range(len(test_list)) if test_list[i]
!= None]

 

# print result

print("The Non None indices list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, None, 4, None, None, 5]
    The Non None indices list is : [0, 2, 5]
    

**Method #2 : Using list comprehension +enumerate()**  
The enumerate function can be used to iterate together the key and value pair
and list comprehension can be used to bind all this logic in one line.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Non-None elements indices 

# using list comprehension + enumerate

 

# initializing list 

test_list = [1, None, 4, None, None, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + enumerate

# Non-None elements indices

res = [i for i, val in enumerate(test_list) if val !=
None]

 

# print result

print("The Non None indices list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, None, 4, None, None, 5]
    The Non None indices list is : [0, 2, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

