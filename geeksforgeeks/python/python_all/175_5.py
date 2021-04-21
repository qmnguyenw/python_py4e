Remove multiple elements from a list in Python



Given a list of numbers, write a Python program to remove multiple elements
from a list based on the given condition.

 **Example:**

    
    
     **Input:** [12, 15, 3, 10]
    **Output:** Remove = [12, 3], New_List = [15, 10]
    
    **Input:** [11, 5, 17, 18, 23, 50]
    **Output:** Remove = [1:5], New_list = [11, 50]
    

Multiple elements can be deleted from a list in Python, based on the knowledge
we have about the data. Like, we just know the values to be deleted or also
know the indexes of those values. Let’s see different examples based on
different scenario.

 **Example #1:** Let’s say we want to delete each element in the list which is
divisible by 2 or all the even numbers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove multiple

# elements from a list 

 

# creating a list

list1 = [11, 5, 17, 18, 23, 50] 

 

# Iterate each element in list

# and add them in variale total

for ele in list1:

 if ele % 2 == 0:

 list1.remove(ele)

 

# printing modified list

print("New list after removing all even numbers: ", list1)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    New list after removing all even numbers:  [11, 5, 17, 23]

  
**Example #2:** Using list comprehension

Removing all even elements in a list is as good as only including all the
elements which are not even( i.e. odd elements).

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove multiple

# elements from a list 

 

# creating a list

list1 = [11, 5, 17, 18, 23, 50] 

 

# will create a new list, 

# excluding all even numbers

list1 = [ elem for elem in list1 if elem % 2 !=
0]

 

print(*list1)  
  
---  
  
 __

 __

 **Output:**

    
    
    11 5 17 23

  
**Example #3:** Remove adjacent elements using list slicing

Below Python code remove values from index 1 to 4.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove multiple

# elements from a list 

 

# creating a list

list1 = [11, 5, 17, 18, 23, 50] 

 

# removes elements from index 1 to 4

# i.e. 5, 17, 18, 23 will be deleted

del list1[1:5]

 

print(*list1)  
  
---  
  
 __

 __

 **Output:**

    
    
    11 50

  
**Example #4:** Using list comprehension

Let’s say the elements to be deleted is known, instead of the indexes of those
elements. In this case, we can directly eliminate those elements without
caring about indexes which we will see in next example.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove multiple

# elements from a list 

 

# creating a list

list1 = [11, 5, 17, 18, 23, 50] 

 

# items to be removed

unwanted_num = {11, 5}

 

list1 = [ele for ele in list1 if ele not in
unwanted_num]

 

# printing modified list

print("New list after removing unwanted numbers: ", list1)  
  
---  
  
 __

 __

 **Output:**

    
    
    New list after removing unwanted numbers:  [17, 18, 23, 50]

**Example #5:** When index of elements is known.

Though indexes of elements in known, deleting the elements randomly will
change the values of indexes. Hence, it is always recommended to delete the
largest indices first. Using this strategy, index of smaller values will not
be changed. We can sort the list in reverse order and delete the elements of
list in descending order.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove multiple

# elements from a list 

 

# creating a list

list1 = [11, 5, 17, 18, 23, 50] 

 

# given index of elements 

# removes 11, 18, 23

unwanted = [0, 3, 4]

 

for ele in sorted(unwanted, reverse = True): 

 del list1[ele]

 

# printing modified list

print (*list1)  
  
---  
  
 __

 __

 **Output:**

    
    
    5 17 50

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

