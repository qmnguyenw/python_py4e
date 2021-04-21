Python | Assign value to unique number in list



We can assign all the numbers in a list a unique value that upon repetition it
retains that value retained to it. This is a very common problem that is faced
in web development when playing with id’s. Let’s discuss certain ways in which
this problem can be solved.

 **Method #1 : Usingenumerate() \+ list comprehension**  
List comprehension can be used to perform this particular task along with the
enumerate function which selects the unique numbers with the help of set and
former helping in the iteration in the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# assign unique value to list elements

# using list comprehension + enumerate

 

# initializing list

test_list = [1, 4, 6, 1, 4, 5, 6]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using list comprehension + enumerate

# assign unique value to list elements 

temp = {i: j for j, i in enumerate(set(test_list))}

res = [temp[i] for i in test_list]

 

# printing result

print ("The unique value list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 6, 1, 4, 5, 6]
    The unique value list is : [0, 1, 3, 0, 1, 2, 3]
    

  
**Method #2 : Usingsetdefault() + map() + count()**  
The combination of all the three function can also be used to perform this
particular task. Map binds all the like elements, setdefault assigns them
unique number and count function helps map to find number of total
occurrences.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# assign unique value to list elements

# using setdefault() + map() + count()

from itertools import count

 

# initializing list

test_list = [1, 4, 6, 1, 4, 5, 6]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using setdefault() + map() + count()

# assign unique value to list elements 

res = list(map({}.setdefault, test_list, count()))

 

# printing result

print ("The unique value list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 6, 1, 4, 5, 6]
    The unique value list is : [0, 1, 2, 0, 1, 5, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

