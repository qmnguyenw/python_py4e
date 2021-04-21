Python | Uncommon elements in Lists of List



This particular article aims at achieving the task of finding uncommon two
list, in which each element is in itself a list. This is also a useful utility
as this kind of task can come in life of programmer if he is in the world of
development. Lets discuss some ways to achieve this task.

 **Method 1 : Naive Method**  
This is the simplest method to achieve this task and uses the brute force
approach of executing a loop and to check if one list contains similar list as
of the other list, not including that.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Uncommon elements in List

# using naive method

 

# initializing lists

test_list1 = [ [1, 2], [3, 4], [5, 6] ]

test_list2 = [ [3, 4], [5, 7], [1, 2] ]

 

# printing both lists 

print ("The original list 1 : " + str(test_list1))

print ("The original list 2 : " + str(test_list2))

 

# using naive method 

# Uncommon elements in List

res_list = []

for i in test_list1:

 if i not in test_list2:

 res_list.append(i)

for i in test_list2:

 if i not in test_list1:

 res_list.append(i)

 

# printing the uncommon

print ("The uncommon of two lists is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [[1, 2], [3, 4], [5, 6]]
    The original list 2 : [[3, 4], [5, 7], [1, 2]]
    The uncommon of two lists is : [[5, 6], [5, 7]]
    

**Method 2 : Usingset() + map() and ^**  
The most efficient and recommended method to perform this task is using the
combination of set() and map() to achieve it. Firstly converting inner lists
to tuples using map, and outer lists to set, use of ^ operator can perform the
set symmetic difference and hence perform this task. Further if it is required
to get in lists of list fashion, we can convert outer and inner containers
back to list using map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Uncommon elements in Lists of List

# using map() + set() + ^

 

# initializing lists

test_list1 = [ [1, 2], [3, 4], [5, 6] ]

test_list2 = [ [3, 4], [5, 7], [1, 2] ]

 

# printing both lists 

print ("The original list 1 : " + str(test_list1))

print ("The original list 2 : " + str(test_list2))

 

# using map() + set() + ^

# Uncommon elements in Lists of List

res_set = set(map(tuple, test_list1)) ^
set(map(tuple, test_list2))

res_list = list(map(list, res_set))

 

# printing the uncommon 

print ("The uncommon of two lists is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [[1, 2], [3, 4], [5, 6]]
    The original list 2 : [[3, 4], [5, 7], [1, 2]]
    The uncommon of two lists is : [[5, 6], [5, 7]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

