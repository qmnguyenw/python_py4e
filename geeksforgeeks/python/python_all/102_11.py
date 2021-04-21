Python – Reverse Sort a String



Sorting has always been quite popular utility with lots of applications
everywhere, where Python language has opted. Python in its language offers a
sort function to perform this task. But due to fact that not all the
containers in Python mutable, such as string, sort function doesn’t work as it
inplace tries to sort and immutability stops this. Let’s discuss certain ways
in which a string can be sorted in reverse way.

 **Method #1 :join() + sorted() + reverse key**  
The combination of above functions can potentially solve this particular
problem. This task is performed in 2 steps in which in first step we get the
reverse sorted list of characters and then we join the result to get the
resultant sorted string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Reverse Sort a String

# using join() + sorted() + reverse

 

# initializing string 

test_string = "geekforgeeks"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using join() + sorted() + reverse

# Sorting a string 

res = ''.join(sorted(test_string, reverse = True))

 

# print result

print("String after reverse sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : geekforgeeks
    String after reverse sorting : srokkggfeeee
    

**Method #2 : Usingsorted() + reduce() + lambda**  
This particular task can also be performed using the combination of above 3
functions. Here we join the resultant reverse sorted list of characters using
the lambda function joined by the reduce function. Works only for Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Reverse Sort a String

# using sorted() + reduce() + lambda

 

# initializing string 

test_string = "geekforgeeks"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using sorted() + reduce() + lambda

# Reverse Sort a String

res = reduce(lambda x, y: x + y, sorted(test_string,
reverse = True))

 

# print result

print("String after reverse sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : geekforgeeks
    String after reverse sorting : srokkggfeeee
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

