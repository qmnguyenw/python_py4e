Python | Adding two list elements



There can be many situations in which one requires to find index wise
summation of two different lists. This can have a possible applications in
day-day programming. Lets discuss various ways in which this task can be
performed.  

 **Method #1 : Naive Method**  
In this method, we simply run a loop and append to the new list the summation
of the both list elements at similar index till we reach end of the smaller
list. This is the basic method to achieve this task.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# addition of two list 

# naive method 

 

# initializing lists

test_list1 = [1, 3, 4, 6, 8]

test_list2 = [4, 5, 6, 2, 10]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using naive method to 

# add two list 

res_list = []

for i in range(0, len(test_list1)):

 res_list.append(test_list1[i] + test_list2[i])

 

# printing resultant list 

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list 1 : [1, 3, 4, 6, 8]
    Original list 2 : [4, 5, 6, 2, 10]
    Resultant list is : [5, 8, 10, 8, 18]
    

**Method #2 : Using List Comprehension**  
The shorthand for the above explained technique, list comprehensions are
usually quicker to type and hence must be preferred to perform these kind of
programming tasks.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# addition of two list 

# list comprehension

 

# initializing lists

test_list1 = [1, 3, 4, 6, 8]

test_list2 = [4, 5, 6, 2, 10]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using list comprehension to 

# add two list 

res_list = [test_list1[i] + test_list2[i] for i in
range(len(test_list1))]

 

# printing resultant list 

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Original list 1 : [1, 3, 4, 6, 8]
    Original list 2 : [4, 5, 6, 2, 10]
    Resultant list is : [5, 8, 10, 8, 18]
    

**Method #3 : Usingmap() + add()**  
map() can also be used, as we can input the add operation to the map()
along with the two list and map() can perform the addition of both the
techniques. This can be extended to any mathematical operation possible.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# addition of two list 

# map() + add()

from operator import add

 

# initializing lists

test_list1 = [1, 3, 4, 6, 8]

test_list2 = [4, 5, 6, 2, 10]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using map() + add() to 

# add two list 

res_list = list(map(add, test_list1, test_list2))

 

# printing resultant list 

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list 1 : [1, 3, 4, 6, 8]
    Original list 2 : [4, 5, 6, 2, 10]
    Resultant list is : [5, 8, 10, 8, 18]
    

**Method #4 : Usingzip() + sum()**  
sum() can perform the index-wise addition of the list that can be “zipped”
together using the zip(). This is quite elegant way to perform this
particular task.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# addition of two list 

# zip() + sum()

from operator import add

 

# initializing lists

test_list1 = [1, 3, 4, 6, 8]

test_list2 = [4, 5, 6, 2, 10]

 

# printing original lists

print ("Original list 1 : " + str(test_list1))

print ("Original list 2 : " + str(test_list2))

 

# using zip() + sum() to 

# add two list 

res_list = [sum(i) for i in zip(test_list1, test_list2)]

 

# printing resultant list 

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list 1 : [1, 3, 4, 6, 8]
    Original list 2 : [4, 5, 6, 2, 10]
    Resultant list is : [5, 8, 10, 8, 18]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

