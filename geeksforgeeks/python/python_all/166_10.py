Python | Concatenate two lists element-wise



Sometimes we come across this type of problem in which we require to leave
each element of one list with the other. This type of problems usually occurs
in developments in which we have the combined information, like names and
surnames in different lists. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Using list comprehension +zip()**  
List comprehension does the task of concatenating the similar index elements.
The task of zip function is concatenating the resultant string into a single
list and return list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# interlist element concatenation

# using list comprehension + zip()

 

# initializing lists 

test_list1 = ["Geeksfor", "i", "be"]

test_list2 = ['Geeks', 's', 'st']

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using list comprehension + zip()

# interlist element concatenation

res = [i + j for i, j in zip(test_list1, test_list2)]

 

# printing result 

print ("The list after element concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : ['Geeksfor', 'i', 'be']
    The original list 2 is : ['Geeks', 's', 'st']
    The list after element concatenation is : ['GeeksforGeeks', 'is', 'best']
    

  
**Method #2 : Usingmap() + lambda + zip()**  
The task of mapping each index element with each other is performed by map
function in this method and the functionality of addition is performed by
lambda function. This method works only in Python2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# interlist element concatenation

# using map() + lambda + zip()

 

# initializing lists 

test_list1 = ["Geeksfor", "i", "be"]

test_list2 = ['Geeks', 's', 'st']

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using map() + lambda + zip()

# interlist element concatenation

res = list(map(lambda(i, j): i + j, zip(test_list1,
test_list2)))

 

# printing result 

print ("The list after element concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : ['Geeksfor', 'i', 'be']
    The original list 2 is : ['Geeks', 's', 'st']
    The list after element concatenation is : ['GeeksforGeeks', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

