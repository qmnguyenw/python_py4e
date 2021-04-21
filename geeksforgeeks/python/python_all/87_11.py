Python – Similar index elements Matrix



Sometimes, while working with data, we can have a problem in which we need to
perform the construction of matrix from lists element vertically than
horizontally. This kind of application can come in Data Science domains in
which we need to construct Matrix from several lists. Lets discuss certain
ways in which this task can be performed.

 **Method #1 : Usingzip() + map()**  
The combination of above functions can be used to perform this task. In this,
we pair up lists using zip() and then using map() the construction of matrix
occurs from the paired up lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Similar index elements Matrix

# using zip() + map()

 

# Initializing lists

test_list1 = [3, 4, 5]

test_list2 = [1, 2, 6]

test_list3 = [7, 9, 8]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# Similar index elements Matrix

# using zip() + map()

res = []

res += map(list, zip(test_list1, test_list2, test_list3))

 

# printing result 

print ("The matrix after cummulation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [3, 4, 5]
    The original list 2 is : [1, 2, 6]
    The original list 3 is : [7, 9, 8]
    The matrix after cummulation is : [[3, 1, 7], [4, 2, 9], [5, 6, 8]]
    

**Method #2 : Using list comprehension +zip()**  
This is yet another way in which this task can be performed. In this, we
perform the task of map() in above with the help of list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Similar index elements Matrix

# using zip() + list comprehension

 

# Initializing lists

test_list1 = [3, 4, 5]

test_list2 = [1, 2, 6]

test_list3 = [7, 9, 8]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# Similar index elements Matrix

# using zip() + list comprehension

res = [list(sub) for sub in zip(test_list1, test_list2,
test_list3)]

 

# printing result 

print ("The matrix after cummulation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [3, 4, 5]
    The original list 2 is : [1, 2, 6]
    The original list 3 is : [7, 9, 8]
    The matrix after cummulation is : [[3, 1, 7], [4, 2, 9], [5, 6, 8]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

