Python | List of tuples Minimum



Sometimes, while working with Python records, we can have a problem in which
we need to perform cross minimum of list of tuples. This kind of application
is popular in web development domain. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using list comprehension +zip() + min()**  
The combination of above functionalities can be used to perform this
particular task. In this, we iterate through the list using list comprehension
and the minimum across lists is performed with help of zip(). The minimum is
performed using min().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of tuples Minimum

# using list comprehension + zip() + min()

 

# initialize lists

test_list1 = [(2, 4), (6, 7), (5, 1)]

test_list2 = [(5, 4), (8, 10), (8, 14)]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# List of tuples Minimum

# using list comprehension + zip() + min()

res = [(min(x[0], y[0]), min(x[1], y[1])) for
x, y in zip(test_list1, test_list2)]

 

# printing result

print("The Minimum across lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [(2, 4), (6, 7), (5, 1)]
    The original list 2 : [(5, 4), (8, 10), (8, 14)]
    The Minimum across lists is : [(2, 4), (6, 7), (5, 1)]
    

**Method #2 : Usingmin() + zip() + map()**  
This is yet another way to perform this task. This is similar to above method,
the difference is that minimum is performed by inbuilt function and extending
logic to each element is done by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of tuples Minimum

# using min() + zip() + map()

 

# initialize lists

test_list1 = [(2, 4), (6, 7), (5, 1)]

test_list2 = [(5, 4), (8, 10), (8, 14)]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# List of tuples Minimum

# using min() + zip() + map()

res = [tuple(map(min, zip(a, b))) for a, b in
zip(test_list1, test_list2)]

 

# printing result

print("The Minimum across lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [(2, 4), (6, 7), (5, 1)]
    The original list 2 : [(5, 4), (8, 10), (8, 14)]
    The Minimum across lists is : [(2, 4), (6, 7), (5, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

