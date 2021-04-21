Python – Actual order index distance



Sometimes we have an unsorted list an we wish to find the actual position the
elements could be when they would be sorted, i.e we wish to construct the list
which could give the position distance to each element destined if the list
was sorted. This has a good application in web development and competitive
programming domain. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingsorted() + index() \+ list comprehension**  
All the above function can combine to achieve this particular task. The sorted
function returns the sorted order and the indexing is done by the index
function. List comprehension does the task of doing for whole list elements
and integrating both tasks.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Actual order index distance

# using sorted() + index() + list comprehension

 

# initializing list

test_list = [6, 3, 1, 2, 5, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using sorted() + index() + list comprehension

# Actual order index distance

temp = sorted(test_list) 

res = [abs(temp.index(ele) - idx) for idx, ele in
enumerate(test_list)]

 

# printing result

print ("The relative ordering list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [6, 3, 1, 2, 5, 4]
    The relative ordering list is : [5, 1, 2, 2, 0, 2]
    

**Method #2 : Usingmap() + enumerate() + dictionary comprehension +
sorted()**  
The dictionary comprehension is used in place of list comprehension and the
sorted list is formed and the index distance of actual ordering in sorted list
are traversed using enumerate to have key-value pair and then are get by map
for all the indices in list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Actual order index distance

# using map() + enumerate() + dictionary comprehension + sorted()

 

# initializing list

test_list = [6, 3, 1, 2, 5, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# using map() + enumerate() + dictionary comprehension + sorted()

# Actual order index distance

temp = {val: abs(key - test_list.index(val)) for key, val
in enumerate(sorted(test_list))}

res = list(map(temp.get, test_list))

 

# printing result

print ("The relative ordering list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [6, 3, 1, 2, 5, 4]
    The relative ordering list is : [5, 1, 2, 2, 0, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

