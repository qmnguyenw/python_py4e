Python – Values Frequency Index List



Sometimes, while working with Python tuples, we can have a problem in which we
need to extract the frequency of each value in tuple. This has been solved
earlier. We can have a modification in which we need to create list in which
index represents the key and value of it represents the frequency of that
index number. This kind of problem can have applications in competitive
programming domain. Let’s discuss certain ways in which we need to solve this
problem.

>  **Input** : test_list = [(‘Gfg’, 1), (‘is’, 1), (‘best’, 1), (‘for’, 1),
> (‘geeks’, 1)]  
>  **Output** : [0, 5, 0, 0, 0, 0]
>
>  **Input** : test_list = [(‘Gfg’, 5), (‘is’, 5)]  
>  **Output** : [0, 0, 0, 0, 0, 2]

 **Method #1 : Using loop**  
This is brute force approach by which this task can be performed. In this, we
perform the task of assigning frequency by iterating and assigning pre-
initialized list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values Frequency Index List

# Using loop

 

# initializing list

test_list = [('Gfg', 3), ('is', 3), ('best', 1),
('for', 5), ('geeks', 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Values Frequency Index List

# Using loop

res = [0 for _ in range(6)]

for ele in test_list:

 res[ele[1]] = res[ele[1]] + 1

 

# printing result 

print("The Frequency list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [('Gfg', 3), ('is', 3), ('best', 1), ('for', 5), ('geeks', 1)]
    The Frequency list : [0, 2, 0, 2, 0, 1]
    

