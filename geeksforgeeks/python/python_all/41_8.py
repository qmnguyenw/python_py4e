Python – Check if all tuples have element difference less than K



Given a Tuple list, check if each tuple has difference less than K.

>  **Input** : test_list = [(3, 4), (1, 2), (7, 8), (9, 13)], K = 2  
>  **Output** : False  
>  **Explanation** : 13 – 9 = 4 > 2.
>
>  **Input** : test_list = [(3, 4), (1, 2), (7, 8)], K = 2  
>  **Output** : True  
>  **Explanation** : All have abs. diff 1 < 2.

 **Method #1 : Using loop**

In this, we keep a boolean variable and check if any element is greater than
or equal to K, then mark it False and break.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if all tuples have element difference less than K

# Using loop

 

# initializing list

test_list = [(3, 4), (1, 2), (7, 8), (9,
8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

res = True

for ele1, ele2 in test_list:

 

 # using abs() to compute absolute difference

 if abs(ele1 - ele2) >= K:

 res = False

 

# printing result 

print("Are all elements difference less than K ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 4), (1, 2), (7, 8), (9, 8)]
    Are all elements difference less than K ? : True
    

**Method #2 : Using all()**

In this, we use all() to check if all the tuples have difference within K.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if all tuples have element difference less than K

# Using all()

 

# initializing list

test_list = [(3, 4), (1, 2), (7, 8), (9,
8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# shorthand to solve this problem

res = all(abs(sub1 - sub2) < K for sub1, sub2 in
test_list)

 

# printing result 

print("Are all elements difference less than K ? : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(3, 4), (1, 2), (7, 8), (9, 8)]
    Are all elements difference less than K ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

