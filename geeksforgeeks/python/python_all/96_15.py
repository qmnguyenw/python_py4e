Python | Modulo K List



While working with the python lists, we can come over a situation in which we
require to modulo the integer k to each element in the list. We possibly need
to iterate and modulo k to each element but that would increase the line of
code. Let’s discuss certain shorthands to perform this task.

 **Method #1 : Using List Comprehension**  
List comprehension is just the short way to perform the task we perform using
the naive method. This is mainly useful to save time and also is best among
others when it comes to readability of the code.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Modulo K List

# using list comprehension

 

# initializing list 

test_list = [4, 5, 6, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# using list comprehension

# Modulo K List

res = [x % K for x in test_list]

 

# printing result 

print ("The list after Modulo K to each element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list after Modulo K to each element : [0, 1, 2, 3, 1]
    

**Method #2 : Using map() \+ lambda**  
The map function can be used to pair each element with the lambda function
which performs the task of modulo K to each element in the list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Modulo K List

# using map() + lambda

 

# initializing list 

test_list = [4, 5, 6, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# initializing K

K = 4

 

# using map() + lambda

# Modulo K List

res = list(map(lambda x : x % K, test_list))

 

# printing result 

print ("The list after Modulo K to each element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6, 3, 9]
    The list after Modulo K to each element : [0, 1, 2, 3, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

