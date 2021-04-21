Python – Consecutive Pairs comma removal



Sometimes, while working amonst lists, we can have a problem in which we need
to pair up elements from two lists. In this, we can have pairs in which we
find that there is comma that is printed in tuple and we wish to avoid it
usually. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingzip() + list comprehension + replace()**  
The combination of above functionalities can be used to perform this task. In
this, we join lists using zip() and task of removal of comma and joining is
performed using replace().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Pairs Duplication Removal

# using list comprehension + zip() + replace()

 

# Initializing lists

test_list1 = [1, 2, 3, 4, 5]

test_list2 = [2, 3, 4, 5, 6]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Consecutive Pairs Duplication Removal

# using list comprehension + zip() + replace()

res = str(list(zip(test_list1, test_list2))).replace('),
(', ') (')

 

# printing result 

print ("The combined list after consecutive comma removal : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 2, 3, 4, 5]
    The original list 2 is : [2, 3, 4, 5, 6]
    The combined list after consecutive comma removal : [(1, 2) (2, 3) (3, 4) (4, 5) (5, 6)]
    

**Method #2 : Usingmap() + list comprehension + zip()**  
This is yet another way in which this task can be performed. In this we
perform the task performed using replace() with map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Pairs Duplication Removal

# using list comprehension + zip() + map()

 

# Initializing lists

test_list1 = [1, 2, 3, 4, 5]

test_list2 = [2, 3, 4, 5, 6]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Consecutive Pairs Duplication Removal

# using list comprehension + zip() + map()

res = "[" + " ".join(map(str, zip(test_list1,
test_list2))) + "]"

 

# printing result 

print ("The combined list after consecutive comma removal : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 2, 3, 4, 5]
    The original list 2 is : [2, 3, 4, 5, 6]
    The combined list after consecutive comma removal : [(1, 2) (2, 3) (3, 4) (4, 5) (5, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

