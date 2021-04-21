Python | Integer count in Mixed List



The lists in python can handle different type of data types in it. The
manipulation of such lists is complicated. Sometimes we have a problem in
which we need to find the count of integer values in which the list can
contain string as a data type i.e heterogenous. Let’s discuss certain ways in
which this can be performed.

 **Method #1 : Using list comprehension +len() + isinstance()**  
This particular problem can be solved by filtering our search of len using the
isinstance method, we can filter out the integer value and then can use len
function to get required length value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Integer count in Mixed List

# using list comprehension + len() + isinstance()

 

# initializing list

test_list = [3, 'computer', 5, 'geeks', 6, 7]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension + len() + isinstance()

# Integer count in Mixed List

res = len(list(i for i in test_list if isinstance(i,
int)))

 

# printing result

print ("The length of integers in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 'computer', 5, 'geeks', 6, 7]
    The length of integers in list is : 4
    

**Method #2 : Using lambda + map() +len() + isinstance()**  
The above problem can also be solved using the lambda function as a map() in
the len() along with the isinstance method which performs the task of checking
for integer values.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Integer count in Mixed List

# using lambda + map() + len() + isinstance()

 

# initializing list

test_list = [3, 'computer', 5, 'geeks', 6, 7]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using lambda + map() + len() + isinstance()

# Integer count in Mixed List

temp = list(map(lambda i: isinstance(i, int),
test_list))

res = len([ele for ele in temp if ele])

 

# printing result

print ("The length of integers in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 'computer', 5, 'geeks', 6, 7]
    The length of integers in list is : 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

