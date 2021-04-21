Python | Summation of first N matching condition



Summation of elements in list can be performed using many inbuilt function.
Normal summation functions have many applications in various domains. This
article discusses to sum just the first N occurrences of elements matching
particular condition.

 **Method #1 : Naive Method**  
We can sum the elements that are matching condition, after N occurrences of
elements have been done and we can stop the operation. Code below demonstrates
the same.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Summation of first N matching condition

# using Naive Method 

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9, 8, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using Naive Method 

# Summation of first N matching condition

# sums first 3 odd occurrences

counter = 1

res = 0

for i in test_list:

 if counter <= 3 and (i % 2 != 0):

 res = res + i

 counter = counter + 1

 

# printing result

print ("The filtered list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9, 8, 5]
    The filtered list is : 9
    

**Method #2 : Usingsum() + list comprehension**  
This is different and elegant way to perform this particular task. It filters
out all the numbers that are less than equal N and sums according to
condition. This is one liner and preferred method to achieve this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Summation of first N matching condition

# using sum() + list comprehension

 

# initializing list

test_list = [3, 5, 1, 6, 7, 9, 8, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using sum() + list comprehension

# to sum first N elements matching condition 

# sum first 3 odd occurrences

res = sum([i for i in test_list if i % 2 !=
0][:3])

 

# printing result

print ("The filtered list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 1, 6, 7, 9, 8, 5]
    The filtered list is : 9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

