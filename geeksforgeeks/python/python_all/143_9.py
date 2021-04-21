Python program to sort a string



Sorting has always been quite popular utility with lots of applications
everywhere, where Python languages is opted. Python in its language offer a
sort function to perform this task. But due to fact that not all the
containers in Python mutable, such as string, sort function doesn’t work as it
inplace tries to sort and immutability stops this. Let’s discuss certain ways
in which a string can be sorted.

 **Method #1 :join() + sorted()**  
The combination of above functions can potentially solve this particular
problem. This task is performed in 2 steps in which in first step we get the
sorted list of characters and then we join the result to get the resultant
sorted string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sorting a string 

# using join() + sorted()

 

# initializing string 

test_string = "geekforgeeks"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using join() + sorted()

# Sorting a string 

res = ''.join(sorted(test_string))

 

# print result

print("String after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : geekforgeeks
    String after sorting : eeeefggkkors
    

**Method #2 : Usingsorted() + reduce() + lambda**  
This particular task can also be performed using the combination of above 3
functions. Here we join the resultant sorted list of characters using the
lambda function joined by the reduce function. Works only for Python2

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Sorting a string 

# using sorted() + reduce() + lambda

 

# initializing string 

test_string = "geekforgeeks"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using sorted() + reduce() + lambda

# Sorting a string 

res = reduce(lambda x, y: x + y, sorted(test_string))

 

# print result

print("String after sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : geekforgeeks
    String after sorting : eeeefggkkors
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

