Python | Slice String from Tuple ranges



Sometimes, while working with data, we can have a problem in which we need to
perform the removal from strings depending on specified substring ranges.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + list slicing**  
This is the brute force task to perform this task. In this we remake the
String by carefully omitting the slice ranges using list slicing. The
iteration of tuples is done by loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Slice String from Tuple ranges

# using loop + list slicing

 

# initialize list and string 

test_list = [(2, 4), (5, 9), (13, 17), (24,
27)]

 

test_str = "geeksforgeeks is best for geeks and programming"

 

# printing original list and string

print("The original list : " + str(test_list))

print("The original string : " + str(test_str))

 

# Slice String from Tuple ranges

# using loop + list slicing

for front, rear in reversed(test_list):

 test_str = test_str[ : front] + test_str[rear + 1:]

 

# printing result

print("The String after slicing is : " + str(test_str))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (5, 9), (13, 17), (24, 27)]
    The original string : geeksforgeeks is best for geeks and programming
    The String after slicing is : geeksest foeks and programming
    

**Method #2 : Using join() + any() \+ generator expression**  
The combination of these functionalities can also be used to perform this
task. In this, we perform the task of slicing using generator expression and
exclusion is handled by any(). The creation of modified string is done by
join().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Slice String from Tuple ranges

# using join() + any() + generator expression

 

# initialize list and string 

test_list = [(2, 4), (5, 9), (13, 17), (24,
27)]

 

test_str = "geeksforgeeks is best for geeks and programming"

 

# printing original list and string

print("The original list : " + str(test_list))

print("The original string : " + str(test_str))

 

# Slice String from Tuple ranges

# using join() + any() + generator expression

res = "".join(test_str[idx] for idx in
range(len(test_str))\

 if not any(front <= idx <= rear for front, rear in
test_list))

 

 

# printing result

print("The String after slicing is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (5, 9), (13, 17), (24, 27)]
    The original string : geeksforgeeks is best for geeks and programming
    The String after slicing is : geeksest foeks and programming
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

