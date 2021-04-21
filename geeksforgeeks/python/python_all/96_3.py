Python | Column Average in Record List



Sometimes the data that we receive, is in the form of tuples having data from
various sources and we can usually have a use case in which we require to
process the finding average of each index of tuple for cumulation. Let’s
discuss certain ways in which this can be performed.

 **Method #1 : Using list comprehension**  
This is the most naive method to perform this particular task, in this method
we compute the average of each index of all the possible indices of the tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Column Average in Record List

# using list comprehension

 

# initializing list 

test_list = [(1, 6), (3, 4), (5, 8)]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# Column Average in Record List

# using list comprehension

temp = sum(i[0] for i in test_list), sum(i[1]
for i in test_list)

res = []

for ele in temp:

 res.append(ele / len(test_list))

 

# printing summation

print ("The position Average of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 6), (3, 4), (5, 8)]
    The position Average of tuples : [3.0, 6.0]
    

**Method #2 : Usingzip() + sum()**  
This is the most elegant and pythonic way to perform this particular task. In
this we combine all the indices of the element using zip() and the performance
of summation using sum function. And then divide the list by list length to
compute average.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Column Average in Record List

# using zip() + sum()

 

# initializing list 

test_list = [(1, 6), (3, 4), (5, 8)]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# Column Average in Record List

# using zip() + sum()

temp = [sum(i) for i in zip(*test_list)]

res = []

for ele in temp:

 res.append(ele / len(test_list))

 

# printing summation

print ("The position Average of tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 6), (3, 4), (5, 8)]
    The position Average of tuples : [3.0, 6.0]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

