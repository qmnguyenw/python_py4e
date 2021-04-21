Python – Multiply Consecutive elements in list



While working with python, we usually come by many problems that we need to
solve in day-day and in development. Specially in development, small tasks of
python are desired to be performed in just one line. We discuss some ways to
compute a list consisting of elements that are successive product in the list.

 **Method #1 : Using list comprehension**  
Naive method can be used to perform, but as this article discusses the one
liner solutions to this particular problem, we start with the list
comprehension as a method to perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Product list

# using list comprehension

 

# initializing list 

test_list = [1, 4, 5, 3, 6]

 

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension

# Consecutive Product list

res = [test_list[i] * test_list[i + 1] for i in
range(len(test_list)-1)]

 

# printing result

print ("The computed successive product list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 3, 6]
    The computed successive product list is : [4, 20, 15, 18]
    

**Method #2 : Usingzip()**  
zip() can also be used to perform the similar task and uses the power of
negative indices to zip() the index element with its next element and hence
compute the product.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive Product list

# using zip()

 

# initializing list 

test_list = [1, 4, 5, 3, 6]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using zip()

# Consecutive Product list

res = [i * j for i, j in zip(test_list[: -1],
test_list[1 :])]

 

# printing result

print ("The computed successive product list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 3, 6]
    The computed successive product list is : [4, 20, 15, 18]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

