Python | Move element to end of the list



The manipulation of lists is quite common in day-day programming. One can come
across various issues where one wishes to perform using just one-liners. One
such problem can be of moving a list element to the rear ( end of list ).
Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingappend() + pop() + index()**  
This particular functionality can be performed in one line by combining these
functions. The append function adds the element removed by pop function using
the index provided by index function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# moving element to end 

# using append() + pop() + index()

 

# initializing list

test_list = ['3', '5', '7', '9', '11']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using append() + pop() + index()

# moving element to end 

test_list.append(test_list.pop(test_list.index(5)))

 

# printing result

print ("The modified element moved list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['3', '5', '7', '9', '11']
    The modified element moved list is : ['3', '7', '9', '11', '5']
    

**Method #2 : Usingsort() + key = (__eq__)**  
The sort method can also be used to achieve this particular task in which we
provide the key as equal to the string we wish to shift so that it is moved to
the end.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# moving element to end 

# using sort() + key = (__eq__)

 

# initializing list

test_list = ['3', '5', '7', '9', '11']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using sort() + key = (__eq__)

# moving element to end 

test_list.sort(key = '5'.__eq__)

 

# printing result

print ("The modified element moved list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['3', '5', '7', '9', '11']
    The modified element moved list is : ['3', '7', '9', '11', '5']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

