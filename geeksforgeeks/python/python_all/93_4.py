Python | K Value Indices Product



Usually, we require to find the index, in which the particular value is
located. There are many method to achieve that, using index() etc. But
sometimes require to find all the indices of a particular value in case it has
multiple occurrences in list and compute their product. Lets discuss certain
ways to do so.

 **Method #1 : Naive Method**  
We can achieve this task by iterating through the list and check for that
value and just append the value index in new list and print that. This is the
basic brute force method to achieve this task. The task of performing product
is done by loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# K Value Indices Product

# using naive method 

 

# initializing list 

test_list = [1, 3, 4, 3, 6, 7, 3]

 

# printing initial list 

print ("Original list : " + str(test_list))

 

# initializing K 

K = 3

 

# using naive method

# K Value Indices Product

res = 1

for i in range(0, len(test_list)) :

 if test_list[i] == K :

 res *= i

 

# printing resultant list 

print ("K Value indices product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [1, 3, 4, 3, 6, 7, 3]
    K Value indices product is : 18
    

**Method #2 : Usingenumerate() \+ loop**  
Using enumerate() we can achieve the similar task, this is slightly faster
technique than above and hence is recommended to be used over the list
comprehension technique. The task of performing product is done by loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# K Value Indices Product

# using enumerate()

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list 

test_list = [1, 3, 4, 3, 6, 7, 3]

 

# printing initial list 

print ("Original list : " + str(test_list))

 

# initializing K 

K = 3

 

# using enumerate()

# K Value Indices Product

res = prod([i for i, value in enumerate(test_list) if value
== K])

 

# printing resultant list 

print ("K Value indices product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [1, 3, 4, 3, 6, 7, 3]
    K Value indices product is : 18
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

