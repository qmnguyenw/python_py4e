Python | Group elements at same indices in a multi-list



Flattening a 2D list to one is a common problem that is faced in many domains.
But sometimes we require to pair elements at specific indices as one, so that
elements at respective indices are together. This problem is not common but
still having a solution to it helps.

Let’s discuss certain ways to pair elements at specific indices.

 **Method #1 : Using list comprehension +zip()**  
List comprehension can be used to achieve this particular task along with zip
function which does the task of pairing the like indices together. This method
is just shorthand to the naive method.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# index list elements pairing

# using list comprehension 

 

# initializing list 

test_list = [[1, 4, 5], [4, 6, 8], [8, 3,
10]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list comprehension 

# to perform index list elements pairing

res = [list(x) for x in zip(*test_list)]

 

# printing result

print ("The index elements pairs list is " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[1, 4, 5], [4, 6, 8], [8, 3, 10]]
    The index elements pairs list is [[1, 4, 8], [4, 6, 3], [5, 8, 10]]
    

  
**Method #2 : Usingmap() + zip()**  
map function can be used to map each iteration result into a single list
while zip function performs the index element pairing. This combination can
be used to achieve the desired result.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# index list elements pairing

# using map() + zip()

 

# initializing list 

test_list = [[1, 4, 5], [4, 6, 8], [8, 3,
10]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using map() + zip() 

# to perform index list elements pairing

res = list(map(list, zip(*test_list)))

 

# printing result

print ("The index elements pairs list is " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[1, 4, 5], [4, 6, 8], [8, 3, 10]]
    The index elements pairs list is [[1, 4, 8], [4, 6, 3], [5, 8, 10]]
    

  
**Method #3 : Usingzip()**  
Using zip function alone does it all and just needs to be typecast to list
to print result in list format. It’s the most pythonic way to perform this
task and the most elegant as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# index list elements pairing

# using zip()

 

# initializing list 

test_list = [[1, 4, 5], [4, 6, 8], [8, 3,
10]]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using zip() 

# to perform index list elements pairing

res = list(zip(*test_list))

 

# printing result

print ("The index elements pairs list is " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[1, 4, 5], [4, 6, 8], [8, 3, 10]]
    The index elements pairs list is [(1, 4, 8), (4, 6, 3), (5, 8, 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

