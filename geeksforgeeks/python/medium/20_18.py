Python | Unzip a list of tuples



The zipping techniques, that is assigning a key-value or pairing from two
different lists has been covered in many articles before, sometimes we have
specific utility to perform the reverse task. This task can be achieved by
various methods.

Let’s discuss some of the methods to unzip a list of tuples.

 **Method #1 :** Using List Comprehension

Using list comprehension is the most naive approach to perform this task of
unzipping and usually not used to perform this task, but good method to start
with.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Unzip a list of tuples

# using list comprehension

 

# initializing list of tuples

test_list = [('Akshat', 1), ('Bro', 2), ('is',
3), ('Placed', 4)]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using list comprehension to

# perform Unzipping

res = [[ i for i, j in test_list ],

 [ j for i, j in test_list ]]

 

# Printing modified list 

print ("Modified list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Original list is : [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
    Modified list is : [['Akshat', 'Bro', 'is', 'Placed'], [1, 2, 3, 4]]
    

**Method #2 :** Using zip() and * operator

Mostly used method to perform unzip and most Pythonic and recommended as well.
This method is generally used to perform this task by programmers all over. *
operator unzips the tuples into independent lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Unzip a list of tuples

# using zip() and * operator

 

# initializing list of tuples

test_list = [('Akshat', 1), ('Bro', 2), ('is',
3), ('Placed', 4)]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using zip() and * operator to

# perform Unzipping

res = list(zip(*test_list))

 

# Printing modified list 

print ("Modified list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
    Modified list is : [('Akshat', 'Bro', 'is', 'Placed'), (1, 2, 3, 4)]
    

  
**Method #3 :** Using map()  
This is yet another way that can be employed to perform this task of unzipping
which is less known but indeed a method to achieve this task. This also uses
the * operator to perform the basic unpacking of the list. This function is
deprecated in Python >= 3 versions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Unzip a list of tuples

# using map()

 

# initializing list of tuples

test_list = [('Akshat', 1), ('Bro', 2), ('is',
3), ('Placed', 4)]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using map() to

# perform Unzipping

res = map(None, *test_list)

 

# Printing modified list 

print ("Modified list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
    Modified list is : [('Akshat', 'Bro', 'is', 'Placed'), (1, 2, 3, 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

