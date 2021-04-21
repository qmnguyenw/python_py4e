Python | K Division Grouping



Sometimes, we have a problem in which we need to deal with the grouping of
elements. These groupings are comparatively easier while working with the
databases, but using languages, this can be tricky. Let’s discuss certain ways
to perform the grouping in Python by K.

 **Method #1 : Using loops**  
This is the brute force method to perform this particular task. In this we use
loops to have each number’s K’s place and add that number to designated list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Division Grouping

# using loops

 

# initializing list

test_list = [3, 12, 13, 22, 25, 30]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 7

 

# using loops

# K Division Grouping

res = []

dec = -1

for num in sorted(test_list):

 while num // K != dec:

 res.append([])

 dec += 1

 res[-1].append(num)

 

# print result

print("The list after grouping by K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 12, 13, 22, 25, 30]
    The list after grouping by K is : [[3], [12, 13], [], [22, 25], [30]]
    

**Method #2 : Using list comprehension + max() + min()**  
Another method to perform this particular task in a shortened way is by using
list comprehension. The min and max function specify the number of lists
required as inner lists and rest of the task is performed inside the list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# K Division Grouping

# using list comprehension + min() + max()

 

# initializing list

test_list = [3, 12, 13, 22, 25, 30]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 7

 

# using list comprehension + min() + max()

# K Division Grouping

temp = sorted(test_list)

res = [[ele for ele in temp if ele // K == sub]
for sub in range(min(test_list) // K, (max(test_list)
// K) + 1)]

 

# print result

print("The list after grouping by K is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 12, 13, 22, 25, 30]
    The list after grouping by K is : [[3], [12, 13], [], [22, 25], [30]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

