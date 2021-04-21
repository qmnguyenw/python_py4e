Python – Remove Negative Elements in List



Sometimes, while working with Python lists, we can have a problem in which we
need to remove all the negative elements from list. This kind of problem can
have application in many domains such as school programming and web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [6, 4, 3]  
>  **Output** : [6, 4, 3]
>
>  **Input** : test_list = [-6, -4]  
>  **Output** : []

 **Method #1 : Using list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of removing negative elements by iteration in one liner
using list comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Negative Elements in List

# Using list comprehension

 

# initializing list

test_list = [5, 6, -3, -8, 9, 11, -12,
2] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove Negative Elements in List

# Using list comprehension

res = [ele for ele in test_list if ele > 0]

 

# printing result 

print("List after filtering : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [5, 6, -3, -8, 9, 11, -12, 2]
    List after filtering : [5, 6, 9, 11, 2]
    

