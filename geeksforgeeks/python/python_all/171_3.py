Python | List consisting of all the alternate elements



Some of the list operations are quite general and having shorthands without
needing to formulate a multiline code is always required. Wanting to construct
the list consisting of all the alternate elements of the original list is a
problem that one developer faces in day-day applications.

Let’s discuss certain ways to print all the alternate elements of the given
list.

 **Method #1 : Usinglist comprehension**

Shorthand to the naive method, list comprehension provides a faster way to
perform this particular task. In this method, all the indices which are not
multiple of 2, hence odd are inserted in the new list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to construct alternate element list

# using list comprehension 

 

# initializing list 

test_list = [1, 4, 6, 7, 9, 3, 5]

 

# printing original list 

print ("The original list : " + str(test_list))

 

# using list comprehension

# to construct alternate element list

res = [test_list[i] for i in range(len(test_list)) if i
% 2 != 0]

 

# printing result 

print ("The alternate element list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list : [1, 4, 6, 7, 9, 3, 5]
    The alternate element list is : [4, 7, 3]
    

