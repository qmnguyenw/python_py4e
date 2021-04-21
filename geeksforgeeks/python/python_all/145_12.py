Python | Separate odd and even index elements



Python list are quite popular and no matter what type of field one is coding,
one has to deal with lists and its various applications. In this particular
article, we discuss ways to separate odd and even indexed elements and its
reconstruction join. Let’s discuss ways to achieve this.

 **Method #1 : Using Naive method**

Using Naive method, this task can be performed by using the loops. One can use
two containers one each to store alternate elements and later joining them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Separating odd and even index elements

# using naive method

 

# initializing list

test_list = [3, 6, 7, 8, 9, 2, 1, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# using naive method

# Separating odd and even index elements

odd_i = []

even_i = []

for i in range(0, len(test_list)):

 if i % 2:

 even_i.append(test_list[i])

 else :

 odd_i.append(test_list[i])

 

res = odd_i + even_i

 

# print result

print("Seprated odd and even index list: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 6, 7, 8, 9, 2, 1, 5]
    Seprated odd and even index list : [3, 7, 9, 1, 6, 8, 2, 5]
    

  

  

**Method #2 : Using list slicing**

This particular task can be easily performed using the list slicing method in
a more compact and efficient manner, this is a recommended method to solve
this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Separating odd and even index elements

# Using list slicing

 

# initializing list

test_list = [3, 6, 7, 8, 9, 2, 1, 5]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using list slicing

# Separating odd and even index elements

res = test_list[::2] + test_list[1::2]

 

# print result

print("Seprated odd and even index list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 6, 7, 8, 9, 2, 1, 5]
    Seprated odd and even index list : [3, 7, 9, 1, 6, 8, 2, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

