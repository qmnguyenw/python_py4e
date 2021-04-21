Python | Sort tuple list by Nth element of tuple



Sometimes, while working with Python list, we can come across a problem in
which we need to sort list according to any tuple element. These must be a
generic way to perform the sort by particular tuple index. This has a good
utility in web development domain. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Usingsort() + lambda**  
The combination of above functions can be used to perform this task. In this,
we just pass a lambda function to sort() with appropriate tuple element
index according to which sort has to be performed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort tuple list by Nth element of tuple

# using sort() + lambda

 

# initializing list

test_list = [(4, 5, 1), (6, 1, 5), (7, 4,
2), (6, 2, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# index according to which sort to perform

N = 1

 

# Sort tuple list by Nth element of tuple

# using sort() + lambda

test_list.sort(key = lambda x: x[N])

 

# printing result 

print("List after sorting tuple by Nth index sort : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)]
    List after sorting tuple by Nth index sort : [(6, 1, 5), (6, 2, 4), (7, 4, 2), (4, 5, 1)]
    

**Method #2 : Usingsort() + itemgetter()**  
This is similar to the above method. The difference is just that we use
itemgetter(), to perform this task that is done by lambda in above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort tuple list by Nth element of tuple

# using sort() + itemgetter()

from operator import itemgetter

 

# initializing list

test_list = [(4, 5, 1), (6, 1, 5), (7, 4,
2), (6, 2, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# index according to which sort to perform

N = 1

 

# Sort tuple list by Nth element of tuple

# using sort() + itemgetter()

test_list.sort(key = itemgetter(N))

 

# printing result 

print("List after sorting tuple by Nth index sort : " +
str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)]
    List after sorting tuple by Nth index sort : [(6, 1, 5), (6, 2, 4), (7, 4, 2), (4, 5, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

