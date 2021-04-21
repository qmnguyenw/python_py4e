Python | Percentage occurrence at index



Sometimes while dealing with statistics, we might come across this particular
problem in which we require to find the percentage of occurrence of element at
particular index in list of list. Let’s discuss certain ways in which this can
be done.

 **Method #1 : Using loop + list comprehension**  
We can perform this particular task using the loop for each list index, and
for that we can compute the percentage occurrence of element using the list
comprehension logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# index percentage calculation of element

# using loop + list comprehension

 

# initializing test list

test_list = [[3, 4, 5], [2, 4, 6], [3, 5,
4]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using loop + list comprehension

# index percentage calculation of element

res = []

for i in range(len(test_list[1])):

 res.append(len([j[i] for j in test_list if j[i]== 4
])/len(test_list))

 

# print result

print("The percentage of 4 each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 4, 5], [2, 4, 6], [3, 5, 4]]
    The percentage of 4 each index is : [0.0, 0.6666666666666666, 0.3333333333333333]
    

**Method #2 : Usingzip() + count() \+ list comprehension**  
This particular task can also be performed using the combination of above
functions. The count and zip function do the task of percentage computation
and grouping respectively.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# index percentage calculation of element

# using zip() + count() + list comprehension

 

# initializing test list

test_list = [[3, 4, 5], [2, 4, 6], [3, 5,
4]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using zip() + count() + list comprehension

# index percentage calculation of element

res = [sub.count(4)/len(sub) for sub in
zip(*test_list)]

 

# print result

print("The percentage of 4 each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 4, 5], [2, 4, 6], [3, 5, 4]]
    The percentage of 4 each index is : [0.0, 0.6666666666666666, 0.3333333333333333]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

