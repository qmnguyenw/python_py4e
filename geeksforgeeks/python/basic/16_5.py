Python | How to get the last element of list



List, being an essential python container is used in day-day programming and
also in web-development. Knowledge of its operations is necessary.

Let’s see all the different ways of accessing the last element of a list.

 **Method #1 : Naive Method**

There can be 2-naive methods to get the last element of the list.

  * Iterating the whole list and getting, the second last element.
  * Reversing the list and printing the first element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# accessing last element of list

# using naive method 

 

# initializing list 

test_list = [1, 4, 5, 6, 3, 5]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# First naive method

# using loop method to print last element 

for i in range(0, len(test_list)):

 

 if i == (len(test_list)-1):

 print ("The last element of list using loop : "

 + str(test_list[i]))

 

# Second naive method 

# using reverse method to print last element

test_list.reverse()

print("The last element of list using reverse : "

 + str(test_list[0]))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [1, 4, 5, 6, 3, 5]
    The last element of list using loop : 5
    The last element of list using reverse : 5
    

  
**Method #2 : Using [] operator**

The last element can be assessed easily if no. of elements in list are already
known. There are 2 index in Python that point to last element in list.

  *  **list[ len - 1 ] :** Points to last element by definition.
  *  **list[-1] :** In python, negative indexing starts from end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# accessing last element of list

# using [] operator

 

# initializing list 

test_list = [1, 4, 5, 6, 3, 5]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using len - 1 index to print last list element

print ("The last element using [ len -1 ] is : "

 + str(test_list[len(test_list) -1]))

 

# using -1 index to print last list element

print ("The last element using [ -1 ] is : "

 + str(test_list[-1]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 3, 5]
    The last element using [ len -1 ] is : 5
    The last element using [ -1 ] is : 5
    

  
**Method #3 : Usinglist.pop()**

The list.pop() method is used to access the last element of the list. The
drawback of this approach is that it also deletes the list last element, hence
is only encouraged to use when list is not to be reused.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# accessing last element of list

# using list.pop()

 

# initializing list 

test_list = [1, 4, 5, 6, 3, 5]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using pop() to print last list element

print ("The last element using pop() is : "

 + str(test_list.pop()))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 3, 5]
    The last element using pop() is : 5
    

  
**Method #4 : Usingreversed() \+ next()**

reversed() coupled with next() can easily be used to get the last element,
as like one of the naive method, reversed method returns the reversed ordering
of list as an iterator, and next() method prints the next element, in this
case last element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# accessing last element of list

# using reversed() + next()

 

# initializing list 

test_list = [1, 4, 5, 6, 3, 5]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using reversed() + next() to print last element

print ("The last element using reversed() + next() is : "

 + str(next(reversed(test_list))))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 3, 5]
    The last element using reversed() + next() is : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

