Python – Substitute K for first occurrence of elements



Sometimes, while working with Python data, we can have a problem in which, we
need to perform substitution to the first occurrence of each element in list.
This type of problem can have application in various domains such as web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [4, 3, 3], K = 10  
>  **Output** : [10, 10, 3]
>
>  **Input** : test_list = [4, 3, 7], K = 8  
>  **Output** : [8, 8, 8]

 **Method #1 : Using loop**  
This is brute way to solve this problem. In this, we run a loop for each
element in list and store already occurred element for lookup, and accordingly
assign K.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substitute K for first occurrence of elements

# Using loop

 

# initializing list

test_list = [4, 3, 3, 7, 8, 7, 4, 6,
3] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 10

 

# Substitute K for first occurrence of elements

# Using loop

lookp = set()

res = []

for ele in test_list:

 if ele not in lookp:

 lookp.add(ele)

 res.append(K)

 else:

 res.append(ele)

 

# printing result 

print("List after Substitution : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [4, 3, 3, 7, 8, 7, 4, 6, 3]
    List after Substitution : [10, 10, 3, 10, 10, 7, 4, 10, 3]
    

