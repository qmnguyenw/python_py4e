Python | Tuple list cross multiplication



Sometimes, while working with Python records, we can have a problem in which
we need to perform cross multiplication of list of tuples. This kind of
application is popular in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using list comprehension +zip()**  
The combination of the above functionalities can be used to perform this
particular task. In this, we iterate through the list using list comprehension
and the multiplication across lists is performed with the help of zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple list cross multiplication

# using list comprehension + zip()

 

# initialize lists

test_list1 = [(2, 4), (6, 7), (5, 1)]

test_list2 = [(5, 4), (8, 10), (8, 14)]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Tuple list cross multiplication

# using list comprehension + zip()

res = [(x[0] * y[0], x[1] * y[1]) for x, y
in zip(test_list1, test_list2)]

 

# printing result

print("The multiplication across lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [(2, 4), (6, 7), (5, 1)]
    The original list 2 : [(5, 4), (8, 10), (8, 14)]
    The multiplication across lists is : [(10, 16), (48, 70), (40, 14)]
    

**Method #2 : Using loop + zip() + map()**  
This is yet another way to perform this task. This is similar to above method,
the difference is that multiplication is performed by explicit function and
extending logic to each element is done by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple list cross multiplication

# using max() + zip() + loop

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initialize lists

test_list1 = [(2, 4), (6, 7), (5, 1)]

test_list2 = [(5, 4), (8, 10), (8, 14)]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Tuple list cross multiplication

# using max() + zip() + loop

res = [tuple(map(prod, zip(a, b))) for a, b in
zip(test_list1, test_list2)]

 

# printing result

print("The multiplication across lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [(2, 4), (6, 7), (5, 1)]
    The original list 2 : [(5, 4), (8, 10), (8, 14)]
    The multiplication across lists is : [(10, 16), (48, 70), (40, 14)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

