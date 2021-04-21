Python | Selective Merge list every Nth position



Sometimes, while working with Python list, we can come into a problem in which
we need to perform merging in list. A simple merge of list is easier to
perform. But sometimes, we need to handle variations in merge. One such can be
merge one list with other at every Nth element. This particular problem can be
faced in day-day programming and competitive programming. Let’s discuss
certain way in which this task can be performed.

 **Method : Using loop +extend() + iter() + next()**  
In this method, we use a brute force approach to tackle this problem. In this
we convert a larger list into an iterator and then access it’s element using
next(). The whole idea behind this is faster access of elements. Smaller list
is checked for every N element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective Merge list every Nth position

# using loop + extend() + iter() + next()

 

# initialize lists

test_list1 = [1, 4, 9, 10, 19, 65, 78,
23, 78]

test_list2 = [8, 14, 50]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Selective Merge list every Nth position

# using loop + extend() + iter() + next()

N = 3

temp_iter = iter(test_list1)

res = []

for ele in test_list2:

 res.extend([next(temp_iter) for _ in range(N - 1)])

 res.append(ele)

res.extend(temp_iter)

 

# printing result

print("The List after merge is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 4, 9, 10, 19, 65, 78, 23, 78]
    The original list 2 is : [8, 14, 50]
    The List after merge is : [1, 4, 8, 9, 10, 14, 19, 65, 50, 78, 23, 78]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

