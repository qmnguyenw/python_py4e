Python – Check if previous element is smaller in List



Sometimes, while working with Python lists, we can have a problem in which we
need to check for each element if its preceding element is smaller. This type
of problem can have its use in data preprocessing domains. Let’s discuss
certain problems in which this task can be performed.

>  **Input** : test_list = [1, 3, 5, 6, 8]  
>  **Output** : [True, True, True, True]
>
>  **Input** : test_list = [3, 1]  
>  **Output** : [False]

 **Method #1 : Using loop**  
This is one of the ways in which this task can be performed. In this, we
perform the task of checking for elements using brute for in loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if previous element is smaller in List

# Using loop

 

# initializing list

test_list = [6, 3, 7, 3, 6, 7, 8, 3] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# Check if previous element is smaller in List

# Using loop

res = []

for idx in range(1, len(test_list)):

 if test_list[idx - 1] < test_list[idx]:

 res.append(True)

 else:

 res.append(False)

 

# printing result 

print("List after filtering : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [6, 3, 7, 3, 6, 7, 8, 3]
    List after filtering : [False, True, False, True, True, True, False]
    

