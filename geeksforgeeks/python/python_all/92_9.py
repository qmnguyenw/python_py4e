python | Nested List Intersection Matrix Product



The problem of finding the common elements in list of 2 lists is quite a
common problem and can be dealt with ease and also has been discussed before
many times. But sometimes, we require to find the elements that are in common
from N lists and return their product. Let’s discuss certain ways in which
this operation can be performed.

 **Method #1 : Usingreduce() + lambda + set() + loop**  
This particular task can be achieved in just a one line using the combination
of the above functions. The reduce function can be used to operate the
function of “&” operation to all the list. The set function can be used to
convert list into a set to remove repetition. The task of performing product
is done using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Nested List Intersection Matrix Product

# using reduce() + lambda + set() + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list of lists

test_list = [[2, 3, 5, 8], [2, 6, 7, 3],
[10, 9, 2, 3]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Nested List Intersection Matrix Product

# using reduce() + lambda + set() + loop

res = prod(list(reduce(lambda i, j: i & j, (set(x) for
x in test_list))))

 

# printing result

print ("The common row elements product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
    The common row elements product is : 6
    

**Method #2 : Usingmap() + intersection() + loop**  
The map function can be used to convert each of the lists to set to be
operated by to perform the intersection, using the set.intersection function.
This is the most elegant way to perform this particular task. The task of
performing product is done using loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Nested List Intersection Matrix Product

# using map() + intersection() + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list of lists

test_list = [[2, 3, 5, 8], [2, 6, 7, 3],
[10, 9, 2, 3]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# Common Row elements Summation

# using map() + intersection() + loop

res = prod(list(set.intersection(*map(set,
test_list))))

 

# printing result

print ("The common row elements product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
    The common row elements product is : 6
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

