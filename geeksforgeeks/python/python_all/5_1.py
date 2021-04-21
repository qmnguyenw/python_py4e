Python Program to find the cube of each list element



Given a list, the task is to write a python program to cube all the list
elements.

>  **Input:** [1, 2, 3, 4]
>
>  **Output** : [1, 8, 27, 64]
>
>  **Explanation:** Cubing all the list elements
>
>  **Input:** [2, 4, 6]
>
>  
>
>
>  
>
>
>  **Output:** [8, 64, 216]

 **Method 1 :** _Using loop_

This is the brute force way. In this, we just multiply the same element two
times to itself.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Initializing list

l = [1, 2, 3, 4]

 

# Cube List using loop

res = []

for i in l:

 res.append(i*i*i)

 

# printing result

print(res)  
  
---  
  
 __

 __

 **Output:**

> [1, 8, 27, 64]

 **Method 2 :** _Using pow() function_

This is also the brute force way. In this, we use in-built pow() function

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Initializing list

l = [1, 2, 3, 4]

 

# Cube List using loop

res = []

for i in l:

 res.append(pow(i, 3))

 

# printing result

print(res)  
  
---  
  
 __

 __

 **Output:**

  

  

> [1, 8, 27, 64]

 **Method 3 :** _Using list comprehension_

This task can also be performed using list comprehension. This is similar to
above function. Just the difference is that its compact and one liner.

 **Example** :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Initializing list

l = [1, 2, 3, 4]

 

# Cube List using list comprehension

res = [pow(i, 3) for i in l]

 

# printing result

print(res)  
  
---  
  
 __

 __

 **Output:**

> [1, 8, 27, 64]

 **Method 4:** _Using lambda_

This can also be achieved using lambda function

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Initializing list

l = [1, 2, 3, 4]

 

res = list(map(lambda x: x ** 3, l))

print(res)  
  
---  
  
 __

 __

 **Output:**

> [1, 8, 27, 64]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

