Python – Cubes Product in list



Python being the language of magicians can be used to perform many tedious and
repetitive tasks in a easy and concise manner and having the knowledge to
utilize this tool to the fullest is always useful. One such small application
can be finding product of cubes of list in just one line. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Usingreduce() \+ lambda**  
The power of lambda functions to perform lengthy tasks in just one line,
allows it combined with reduce which is used to accumulate the subproblem, to
perform this task as well. Works with only Python 2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Cubes Product in list

# using reduce() + lambda

 

# initializing list

test_list = [3, 5, 7, 9, 11]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using reduce() + lambda

# Cubes Product in list

res = reduce(lambda i, j: i * j*j * j,
[test_list[:1][0]**3]+test_list[1:])

 

# printing result

print ("The product of cubes of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 7, 9, 11]
    The product of cubes of list is : 1123242379875
    

**Method #2 : Usingmap() \+ loop**  
The similar solution can also be obtained using the map function to integrate
and external product function to perform the product of the cubed number.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Cubes Product in list

# using loop + max()

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list

test_list = [3, 5, 7, 9, 11]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using loop + max()

# Cubes Product in list

res = prod(map(lambda i : i * i * i, test_list))

 

# printing result

print ("The product of cubes of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 5, 7, 9, 11]
    The product of cubes of list is : 1123242379875
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

