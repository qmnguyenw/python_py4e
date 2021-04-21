Python | Consecutive elements pairing in list



Sometimes, while working with lists, we need to pair up the like elements in
the list and then store them as lists of lists. This particular task has its
utility in many domains, be it web development or day-day programming. Let’s
discuss certain ways in which this can be achieved.

 **Method #1 : Using list comprehension**  
The list comprehension can be easily used to perform this particular task, but
consecutively making the pairs of i’th and (i+1)th element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# consecutive element pairing 

# using list comprehension

 

# initializing list

test_list = [5, 4, 1, 3, 2]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension

# consecutive element pairing 

res = [[test_list[i], test_list[i + 1]]

 for i in range(len(test_list) - 1)]

 

# print result

print("The consecutive element paired list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
        
    The original list : [5, 4, 1, 3, 2]
    The consecutive element paired list is : [[5, 4], [4, 1], [1, 3], [3, 2]]
    

**Method # 2: Usingzip()**  
This task can also be achieved using only the zip function which performs the
task for all the elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# consecutive element pairing 

# using zip()

 

# initializing list

test_list = [5, 4, 1, 3, 2]

 

# printing original list

print("The original list : " + str(test_list))

 

# using zip()

# consecutive element pairing 

res = list(zip(test_list, test_list[1:]))

 

# print result

print("The consecutive element paired list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
        
    The original list : [5, 4, 1, 3, 2]
    The consecutive element paired list is : [[5, 4], [4, 1], [1, 3], [3, 2]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

