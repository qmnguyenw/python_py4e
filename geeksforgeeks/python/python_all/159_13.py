Python | Strings length summation



Sometimes we receive data in the container that we need to process to handle
it further for some essential utility. The magnitude of amount of data
sometimes becomes important and needs to be known. This article discusses the
total length of list of strings. Let’s discuss certain ways in which this can
be done.

 **Method #1 : Usingsum() \+ list comprehension**  
The combination of these two functions can be used to perform this particular
function. The sum function is used to find the summation of each string of
list and list comprehension does the task of iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# string lengths summation 

# using sum() + list comprehension

 

# initializing list of tuples

test_list = ['Geeks', 'for', 'Geeks']

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using sum() + list comprehension

# string lengths summation 

res = sum(len(i) for i in test_list)

 

# printing result

print ("The summation of strings is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['Geeks', 'for', 'Geeks']
    The summation of strings is : 13
    

  
**Method #2 : Usingjoin() + len()**  
The inbuilt functions of python can help to perform this particular task. The
join function can be used to join all the strings together and len function
takes their cumulative sum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# string lengths summation 

# using sum() + list comprehension

 

# initializing list of tuples

test_list = ['Geeks', 'for', 'Geeks']

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using sum() + list comprehension

# string lengths summation 

res = len(''.join(test_list))

 

# printing result

print ("The summation of strings is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['Geeks', 'for', 'Geeks']
    The summation of strings is : 13
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

