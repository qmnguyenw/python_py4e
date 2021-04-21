Python – Convert 2D list to 3D at K slicing



Sometimes, while working with Python lists, we can have a problem in which we
need to convert a 2D list to 3D, at every Kth list. This type of problem is
peculiar, but can have application in various data domains. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_list = [[6, 5], [2, 3], [3, 1], [4, 6], [3, 2], [1, 6]] ,
> K = 3  
>  **Output** : [[[6, 5], [2, 3], [3, 1]], [[4, 6], [3, 2], [1, 6]]]
>
>  **Input** : test_list = [[6, 5], [2, 3], [3, 1]] , K = 1  
>  **Output** : [[[6, 5]], [[2, 3]], [[3, 1]]]

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we iterate
through each element, and maintain a counter, at every Kth sublist, create a
new list and append accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert 2D list to 3D at K slicing

# Using loop

 

# initializing list

test_list = [[6, 5], [2, 3], [3, 1], [4,
6], [3, 2], [1, 6]] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# Convert 2D list to 3D at K slicing

# Using loop

res = []

subl = []

cnt = 0

for sub in test_list:

 subl.append(sub)

 cnt = cnt + 1

 if cnt >= K:

 res.append(subl)

 subl = []

 cnt = 0

 

# printing result 

print("Records after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [[6, 5], [2, 3], [3, 1], [4, 6], [3, 2], [1, 6]]
    Records after conversion : [[[6, 5], [2, 3]], [[3, 1], [4, 6]], [[3, 2], [1, 6]]]
    

