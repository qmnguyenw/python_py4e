Python | Column Product in List of lists



Sometimes, we are encountered with such problem in which we need to find the
product of each column in a matrix i.e product of each index in list of lists.
This kind of problem is quite common and useful in competitive programming.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop + list comprehension +zip()**  
The combination of above methods are required to solve this particular
problem. The explicit product function is used to get the required product
value and zip function provides the combination of like indices and then list
is created using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Column Product in List of lists

# using loop + list comprehension + zip()

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list

test_list = [[3, 7, 6], [1, 3, 5], [9, 3,
2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop + list comprehension + zip()

# Column Product in List of lists

res = [prod(idx) for idx in zip(*test_list)]

 

# print result

print("The Product of each index list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    The Product of each index list is : [27, 63, 60]
    

**Method #2 : Usingmap() + loop + zip()**  
This works in almost similar way as the above method, but the difference is
just that we use map function to build the product list rather than using list
comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Column Product in List of lists

# using map() + loop + zip()

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initializing list

test_list = [[3, 7, 6], [1, 3, 5], [9, 3,
2]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + loop + zip()

# Column Product in List of lists

res = list(map(prod, zip(*test_list)))

 

# print result

print("The Product of each index list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
    The Product of each index list is : [27, 63, 60]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

