Python | Remove duplicates from nested list



The task of removing duplicates many times in recent past, but sometimes when
we deal with the complex data structure, in those cases we need different
techniques to handle this type of problem. Let’s discuss certain ways in which
this task can be achieved.

 **Method #1 : Usingsorted() + set()**  
This particular problem can be solved using the above functions. The idea here
is to sort the sublist and then removing the like elements using the set
operations which removes duplicates.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing duplicate sublist 

# using set() + sorted()

 

# initializing list

test_list = [[1, 0, -1], [-1, 0, 1],
[-1, 0, 1],

 [1, 2, 3], [3, 4, 1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using set() + sorted()

# removing duplicate sublist

res = list(set(tuple(sorted(sub)) for sub in
test_list))

 

# print result

print("The list after duplicate removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [[1, 0, -1], [-1, 0, 1], [-1, 0, 1], [1, 2, 3], [3, 4, 1]]
    The list after duplicate removal : [(-1, 0, 1), (1, 3, 4), (1, 2, 3)]
    

**Method #2 : Usingset() + map() + sorted()**  
The task performed by the list comprehension in the above method can be
modified using the map function using lambda functions to extend the logic to
each and every sublist.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing duplicate sublist 

# using set() + map() + sorted()

 

# initializing list

test_list = [[1, 0, -1], [-1, 0, 1],
[-1, 0, 1],

 [1, 2, 3], [3, 4, 1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using set() + map() + sorted()

# removing duplicate sublist

res = list(set(map(lambda i: tuple(sorted(i)),
test_list)))

 

# print result

print("The list after duplicate removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[1, 0, -1], [-1, 0, 1], [-1, 0, 1], [1, 2, 3], [3, 4, 1]]
    The list after duplicate removal : [(-1, 0, 1), (1, 3, 4), (1, 2, 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

