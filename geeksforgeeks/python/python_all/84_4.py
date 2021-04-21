Python | Prefix extraction depending on size



Sometimes, while working with Python, we can have a problem in which we need
to extract prefix from a string. This can be conditional sometimes, and we
just need to extract specific length substring if size of string is larger
than some N. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way to perform this task, in which we extract the string
according to size using a loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix extraction depending on size

# using loop

 

# Initializing list

test_list = ['geeksforgeeks', 'is', 'best', 'for',
'geeks']

 

# Initializing K 

K = 2

 

# Initializing N 

N = 4

 

# printing original list

print("The original list is : " + str(test_list))

 

# Prefix extraction depending on size

# using loop

res = []

for idx in test_list:

 if len(idx) >= N:

 res.append(idx[:K])

 

# printing result 

print ("List after prefix extraction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    List after prefix extraction : ['ge', 'be', 'ge']
    

**Method #2 : Usingfilter() \+ lambda**  
This task can also be performed using combination of above functions. In this,
we perform the task of checking using filter(), and extraction is done in
shorter way using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Prefix extraction depending on size

# using filter() + lambda

 

# Initializing list

test_list = ['geeksforgeeks', 'is', 'best', 'for',
'geeks']

 

# Initializing K 

K = 2

 

# Initializing N 

N = 4

 

# printing original list

print("The original list is : " + str(test_list))

 

# Prefix extraction depending on size

# using filter() + lambda

res = [sub[:K] for sub in filter(lambda ele : len(ele)
>= N, test_list)]

 

# printing result 

print ("List after prefix extraction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    List after prefix extraction : ['ge', 'be', 'ge']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

