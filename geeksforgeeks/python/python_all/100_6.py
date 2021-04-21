Python – Suffix Product in list



Nowdays, especially in the field of competitive programming, the utility of
computing suffix product is quite popular and features in many problems.
Hence, having a one liner solution to it would possess a great help. Let’s
discuss certain way in which this problem can be solved.

 **Method : Using list comprehension + loop + list slicing**  
This problem can be solved using the combination of above two functions in
which we use list comprehension to extend logic to each element, explicit
product function to get the product along, slicing is used to get product till
the particular index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Suffix List Product 

# using list comprehension + loop + list slicing 

 

# compute prod 

def prod(test_list): 

 res = 1

 for ele in test_list: 

 res = res * ele 

 return res 

 

# initializing list 

test_list = [3, 4, 1, 7, 9, 1] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# using list comprehension + loop + list slicing 

# Suffix List Product

test_list.reverse() 

res = [prod(test_list[ : i + 1 ]) for i in
range(len(test_list))] 

 

# print result 

print("The suffix product list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [3, 4, 1, 7, 9, 1]
    The suffix product list is : [1, 9, 63, 63, 252, 756]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

