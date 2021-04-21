Python | Uneven Sized Matrix Column product



The usual list of list, unlike conventional C type Matrix, can allow the
nested list of lists with variable lengths, and when we require the product of
its columns, the uneven length of rows may lead to some elements in that
elements to be absent and if not handled correctly, may throw exception. Let’s
discuss certain ways in which this problem can be performed in error free
manner.

 **Method #1 : Using loop +filter() + map() \+ list comprehension**  
The combination of above three function combined with list comprehension can
help us perform this particular task, the external prod function helps to
perform the multiplication, filter allows us to check for the present elements
and all rows are combined using the map function. Works only with python 2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Uneven Sized Matrix Column product

# using loop + filter() + map() + list comprehension

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list of lists

test_list = [[1, 5, 3], [4], [9, 8]]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using loop + filter() + map() + list comprehension

# Uneven Sized Matrix Column product

res = [prod(filter(None, j)) for j in map(None,
*test_list)]

 

# printing result

print ("The product of columns is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[1, 5, 3], [4], [9, 8]]
    The product of columns is : [36, 40, 3]
    

**Method #2 : Using list comprehension + loop +zip_longest()**  
If one desires not to play with the None values, one can opt for this method
to resolve this particular problem. The zip_longest function helps to fill the
not present column with 1 so that it does not has to handle the void of
elements not present.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Uneven Sized Matrix Column product

# using list comprehension + loop + zip_longest()

import itertools

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list of lists

test_list = [[1, 5, 3], [4], [9, 8]]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension + loop + zip_longest()

# Uneven Sized Matrix Column product

res = [prod(i) for i in itertools.zip_longest(*test_list,
fillvalue = 1)]

 

# printing result

print ("The product of columns is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[1, 5, 3], [4], [9, 8]]
    The product of columns is : [36, 40, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

