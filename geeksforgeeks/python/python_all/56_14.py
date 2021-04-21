Python – Rear Kth elements



Given a list, the task is to extract all Kth elements from rear end.

>  **Input** : test_list = [3, 4, 5, 2, 1], K = 2  
>  **Output** : [1, 5, 3]  
>  **Explanation** : Every 2nd elements are extracted from rear starting from
> 1.
>
>  **Input** : test_list = [3, 4, 5], K = 1  
>  **Output** : [5, 4, 3]  
>  **Explanation** : Every elements are extracted from rear starting from 1.

 **Method #1 : Using loop**  
The is brute method to solve this problem. In this, we reverse and then
perform iteration to get each Kth multiple element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear Kth elements

# Using loop

 

# initializing list

test_list = [3, 5, 7, 9, 10, 2, 8, 6] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# Rear Kth elements

res = []

test_list.reverse()

for idx, ele in enumerate(test_list):

 

 # Extracting elements divisible by K

 if idx % K == 0:

 res.append(ele)

 

# printing result 

print("Rear Kth elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [3, 5, 7, 9, 10, 2, 8, 6]
    Rear Kth elements : [6, 10, 5]
    

