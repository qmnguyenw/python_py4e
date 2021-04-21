Python | Record Index Product



Sometimes, while working with records, we can have a problem in which we need
to multiply all the columns of a container of lists which are tuples. This
kind of application is common in web development domain. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop + list comprehension +zip()**  
This task can be performed using combination of above functions. In this, we
cummulate the like index elements, i.e columns using zip(), and then iterate
through them using list comprehension and perform product using explicit
function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Record Index Product

# using list comprehension + loop + zip()

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Record Index Product

# using list comprehension + loop + zip()

res = [prod(ele) for ele in zip(*test_list)]

 

# printing result

print("The Cummulative column product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column product is : [6, 84, 144]
    

**Method #2 : Using zip() + map() + loop**  
This method is similar to the above method. In this, the task performed by
list comprehension is performed by map(), which extends the product of columns
to zipped elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Record Index Product

# using zip() + map() + loop

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Record Index Product

# using zip() + map() + loop

res = list(map(prod, zip(*test_list)))

 

# printing result

print("The Cummulative column product is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column product is : [6, 84, 144]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

