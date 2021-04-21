Python – Consecutive Triple element pairing



Sometimes, while working with lists, we need to triple pair up the like
elements in list and then store them as lists of list. This particular task
has it’s utility in many domains, be it web development or day-day
programming. Let’s discuss certain ways in which this can be achieved.

 **Method #1 : Using list comprehension**  
The list comprehension can be easily used to perform this particular task, but
consecutively making the pairs of i’th, (i+1)th and (i+2)th element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Triple element pairing

# using list comprehension

 

# initializing list

test_list = [5, 4, 1, 3, 2]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension

# Consecutive Triple element pairing

res = [[test_list[i], test_list[i + 1], test_list[i + 2]]
for i in range(len(test_list) - 2)]

 

# print result

print("The consecutive element triple paired list is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [5, 4, 1, 3, 2]
    The consecutive element triple paired list is : [[5, 4, 1], [4, 1, 3], [1, 3, 2]]
    

**Method #2 : Usingzip() + map()**  
This task can also be achieved using the zip function which performs the task
for all the elements and map function does the task of pairing of consecutive
elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Triple element pairing

# using zip() + map()

 

# initializing list

test_list = [5, 4, 1, 3, 2]

 

# printing original list

print("The original list : " + str(test_list))

 

# using zip() + map()

# Consecutive Triple element pairing

res = list(map(list, zip(test_list, test_list[1:],
test_list[2:])))

 

# print result

print("The consecutive element triple paired list is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [5, 4, 1, 3, 2]
    The consecutive element triple paired list is : [[5, 4, 1], [4, 1, 3], [1, 3, 2]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

