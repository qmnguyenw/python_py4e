Python – Retain all K elements Rows



Sometimes, while working with Python lists, we can have a problem in which we
need to retain rows which have only K as elements. This kind of application
can occur in data domains which take Matrix as input. Let’s discuss certain
ways in which this task can be performed.

>  **Input** : test_list = [[7, 6], [4, 4], [1, 2], [4]], K = 4  
>  **Output** : [[4, 4], [4]]
>
>  **Input** : test_list = [[7, 6], [7, 4], [1, 2], [9]], K = 4  
>  **Output** : []

 **Method #1 : Using list comprehension +any()**  
The combination of above functions provide a way in which this task can be
performed. In this, we perform the task of filtering out rows which have any
element other than K using any().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain all K elements Rows

# Using list comprehension + any()

 

# initializing list

test_list = [[2, 4, 6], [2, 2, 2], [2,
3], [2, 2]]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K 

K = 2

 

# Retain all K elements Rows

# Using list comprehension + any()

res = [ele for ele in test_list if not any(el != K
for el in ele)]

 

# printing result 

print("Matrix after filtering : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [[2, 4, 6], [2, 2, 2], [2, 3], [2, 2]]
    Matrix after filtering : [[2, 2, 2], [2, 2]]
    

